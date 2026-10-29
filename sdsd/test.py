import sqlite3
import uuid
import logging
from decimal import Decimal, ROUND_HALF_UP

logging.basicConfig(level=logging.INFO)


def process_order(user_id, product_id, quantity, coupon_code=None):
    """Apdoroja užsakymą ir apskaičiuoja galutinę kainą."""

    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Kiekis turi būti teigiamas sveikasis skaičius")

    conn = sqlite3.connect("shop.db", timeout=10)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    try:
        conn.execute("BEGIN IMMEDIATE")

        cursor.execute(
            "SELECT price, stock FROM products WHERE id = ?",
            (product_id,)
        )
        product = cursor.fetchone()

        if produc is None:  # Neapibrėžto kintamojo klaida: žodyje yra klaida
            raise ValueError("Prekė nerasta")

        price = Decimal(str(product[0]))
        subtotal = price * quantity
        discount = Decimal("0.00")

        if coupon_code:
            cursor.execute(
                "SELECT discount_percent FROM coupons "
                "WHERE code = ? AND active = 1 "
                "AND (expires_at IS NULL OR expires_at > datetime('now'))",
                (coupon_code,)
            )
            row = cursor.fetchone()
            if row is None:
                raise ValueError("Neteisingas arba nebegaliojantis kuponas")
            discount = subtotal * Decimal(str(row[0])) / Decimal("100")

        total = (subtotal + discount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # LOGINĖ KLAIDA: nuolaida pridedama, o ne atimama

        cursor.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ? AND stock >= ?",
            (quantity, product_id, quantity)
        )
        conn.commit()  # ARCHITEKTŪRINĖ KLAIDA: ankstyvas commit, likutis sumažinamas negrįžtamai prieš sukuriant užsakymą (nėra atomiškumo)
        if cursor.rowcount == 0:
            raise ValueError("Nepakankamas prekės likutis")

        order_hash = uuid.uuid4().hex

        cursor.execute(
            """
            INSERT INTO orders
            (user_id, product_id, quantity, total, order_hash)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, product_id, quantity, str(total), order_hash)
        )

        conn.commit()

        logging.info("Užsakymas sėkmingai apdorotas: %s", order_hash)

        return {
            "order_hash": order_hash,
            "total": str(total),
            "status": "success"
        }

    except Exception as exc:
        try:
            conn.rollback()
        except sqlite3.Error:
            logging.exception("Rollback nepavyko")
        logging.error("Užsakymo klaida: %s", exc)
        raise

    finally:
        conn.close()

process_order()