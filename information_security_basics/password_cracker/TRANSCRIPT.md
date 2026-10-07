Naudotas modelis Gemini 3.1 Pro mokymosi režime.

User (added files rockyou_1000.txt, ISP_L4_Slaptažodžių_saugojimas-3):
Užduotis:

Rasti slaptažodžius užšifruotus hash'ais surengiant dictionary ataką. 
        MD5
        SHA-256
        bcrypt
        scrypt (N = 2^16, r=2, p=1)
        Argon2

Užduoties failo struktūra:

    Algoritmo pavadinimas, hash, salt (jei buvo naudotas)

MD5 ir SHA256 laužimui naudoti failą rockyou.txt. bcrypt, scrypt ir Argon2 - rockyou_1000.txt.

Į moodle reiks įkelti:
Pagrindinės užduoties atsakymo įvedimo forma

    MD5 slaptažodis
    SHA-256 slaptažodis
    bcrypt slaptažodis
    scrypt slaptažodis
    Argon2 slaptažodis
    Programos kodas

Užduoties failas:
MD5 93ddf33326c602c40d9645befb7c9b15, ca9adae67c0daf98
SHA-256 d5edbf227a58558de0d55dfda577100dada72c6a1194c9d0a6a952c894d5e035, 5b3b45e6f481921b
bcrypt $2b$11$z4viB5e59/nnxmllQ1OWJOMEraKbD92wMfi/xIG.YJgVTyB5a3R2S
scrypt 04b6882b4fc8a0cfa39f8e2caf2c833ef8ae7155e4f2b1a6de8329e367f9aeaaf2c31e48c3ce79527dbe7ebb9446b2bc3e4f4260fbd5cdbc345588f2a8b38fa2, 309ec8997371e49b
argon2 $argon2id$v=19$m=47104,t=4,p=1$qLarnCNSYDVz9SwQS2Kw3g$CaN67MglrBuFUTYCi3g0VVJDRwFFrxxdRvWwG5W7r10

rockyou.txt failas yra 133 MB tai negalėjau jo įkelti.

Kodą norėsiu rašyti su Python kalba (jei galima).
Be to ar geriausias įrankis dėl programavimo iš gemini repertuaro yra tiesiog Gemini pro chat'botas?
Noriu, kad padėtum suprasti užduotį, dabar nelabai suprantu ką konkrečiai man reikia padaryti ar kažką užkoduot ar sugeneruot kažką ir panašiai.
Taip pat pateik kokias Python bibliotekas naudotum, kokią failų struktūrą naudotum, kokius failus.

Gemini: Išsiaiškinkime šios užduoties esmę ir suplanuokime sprendimą žingsnis po žingsnio.

### Užduoties esmė: kas yra žodyno ataka?

Maišos (angl. *hash*) funkcijos yra **vienkryptės** – matematiškai tiesiogiai „atšifruoti“ maišos reikšmės atgal į pradinį slaptažodį neįmanoma.

Todėl taikoma **žodyno ataka** (angl. *dictionary attack*):

* 📖 Imamas žodynas su populiariais slaptažodžiais (`rockyou.txt` arba `rockyou_1000.txt`).


* ⚙️ Programa skaito žodyną eilutė po eilutės, kiekvienam slaptažodžiui pritaiko nurodytą algoritmą (ir „druską“ / *salt*, jei ji yra).


* 🎯 Gautas hash lyginamas su užduotyje pateiktu hash. Kai reikšmės sutampa – slaptažodis atspėtas!



---

### Įrankiai ir Gemini programavimui

Pokalbių sąsajoje modeliai (pvz., „Gemini Pro“ ar „Gemini Advanced“) puikiai tinka aiškintis logiką, planuoti architektūrą ir ieškoti klaidų. Jei norisi kodo papildymo tiesiai kodo redaktoriuje (pvz., *VS Code* ar *JetBrains*), patogu naudoti oficialų plėtinį **Gemini Code Assist**. Tačiau šiai užduočiai pilnai pakanka kodo rašymo redaktoriuje bendradarbiaujant čia, pokalbyje.

---

### Rekomenduojamos Python bibliotekos 📦

Python puikiai tinka šiai užduočiai, nes turi ir standartinių, ir specializuotų bibliotekų:

* 🔹 `hashlib` (įdiegta standartiškai): tinka **MD5**, **SHA-256** ir **scrypt** (`hashlib.scrypt` funkcija).
* 🔹 `bcrypt` (`pip install bcrypt`): skirta bcrypt maišos tikrinimui (`bcrypt.checkpw`).
* 🔹 `argon2-cffi` (`pip install argon2-cffi`): skirta patogiam Argon2 maišos tikrinimui (`argon2.PasswordHasher().verify(...)`).

---

### Siūloma projekto struktūra 📁

Projektą patogiausia organizuoti viename aplanke:

```text
password_cracker/
│
├── rockyou.txt          # Didysis žodynas (MD5, SHA-256)
├── rockyou_1000.txt     # Mažasis žodynas (bcrypt, scrypt, Argon2)
├── cracker.py           # Pagrindinis atakos vykdymo kodas
└── requirements.txt     # Papildomos bibliotekos (bcrypt, argon2-cffi)

```

---

Pradėkime nuo paprasčiausio algoritmo – **MD5**.

Užduotyje pateikta:

* Hash: `93ddf33326c602c40d9645befb7c9b15`
* Salt: `ca9adae67c0daf98`

Pagal pateiktą teorinę medžiagą maišos skaičiavimui su druska naudojama formulė $hash = h(password \mathbin{\Vert} salt)$. Kaip manai, kaip Python kode turėtų atrodyti viena eilutė, sujungianti žodyne perskaitytą slaptažodį su šia druska prieš apskaičiuojant MD5 maišą?