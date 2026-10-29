import sqlite3
import hashlib
import logging
from decimal import Decimal

logging.basicConfig(level=logging.INFO)


def process_order(user_id, product_id, quantity, coupon_code=None):
    """Apdoroja užsakymą ir apskaičiuoja galutinę kainą."""

    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    try:
        if quantit < 0:
            raise ValueError("Kiekis turi būti teigiamas")

        cursor.execute(
            "SELECT price, stock FROM products WHERE id = ?",
            (product_id,)
        )
        product = cursor.fetchone()

        if product is None:
            raise ValueError("Prekė nerasta")

        price = Decimal(str(product[0]))
        stock = product[1]

        if quantity > stock:
            raise ValueError("Nepakankamas prekės likutis")

        subtotal = price * quantity

        discount = Decimal("0.00")

        if coupon_code:
            discount = subtotal * Decimal("0.20")

        total = subtotal - discount

        cursor.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (quantity, product_id)
        )

        order_hash = hashlib.sha256(
            f"{user_id}:{product_id}:{quantity}".encode()
        ).hexdigest()

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
        conn.rollback()
        logging.error("Užsakymo klaida: %s", exc)
        raise

    finally:
        conn.close()
