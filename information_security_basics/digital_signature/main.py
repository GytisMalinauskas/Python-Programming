import hashlib
import time
from pagalbines_funkcijos import bytes_to_int, int_to_bytes
from keys import n, e, d

def main():
    with open("sertifikatas.txt", "rb") as f:
        cert_bytes = f.read()

# 2. Sertifikato piršto antspaudas (hash1)
    hash1 = hashlib.sha256(cert_bytes)
    hash1_bytes = hash1.digest()
    hash1_hex = hash1.hexdigest()
    
    # Konvertuojame baitus į skaičių ir pasirašome RSA privačiu raktu
    m1 = bytes_to_int(hash1_bytes)
    s1 = pow(m1, d, n)

    # 3. Parašas su laiko žyma
    ts10 = int(time.time())
    ts16 = int_to_bytes(ts10)
    
    # Apjungiame: hash1_bytes || ts16
    combined_bytes = hash1_bytes + ts16
    hash2 = hashlib.sha256(combined_bytes)
    hash2_bytes = hash2.digest()
    hash2_hex = hash2.hexdigest()
    
    # Konvertuojame baitus į skaičių ir pasirašome
    m2 = bytes_to_int(hash2_bytes)
    s2 = pow(m2, d, n)

    # 4. Savikontrolė (patikriname su viešuoju raktu e)
    assert pow(s1, e, n) == m1, "Klaida: 1 parašas neteisingas!"
    assert pow(s2, e, n) == m2, "Klaida: 2 parašas su laiko žyma neteisingas!"

    # 5. Išvedimas Moodle ataskaitai
    print("=== 2. PARAŠAS ===")
    print(f"2.1 Sertifikato piršto antspaudas - SHA256(sertifikatas.txt):\n{hash1_hex}")
    print(f"2.2 Piršto antspaudo parašas (dešimtainis skaičius):\n{s1}\n")

    print("=== 3. PARAŠAS SU LAIKO ŽYMA ===")
    print(f"3.1 Sertifikato ir laiko žymos piršto antspaudas:\n{hash2_hex}")
    print(f"3.2 ts10:\n{ts10}")
    print(f"3.3 Piršto antspaudo parašas (dešimtainis skaičius):\n{s2}")

if __name__ == "__main__":
    main()