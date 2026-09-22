"""A module for implementing Viginere's cipher encryption and decryption"""

TO_ENCRYPT = "Oštlbač šf yaufag ąųnzrnš."
KEY = "minija"
TO_DECRYPT = """Įbeu zkįl dgžžbzdž dgžžbzdž pomibohžąrš ūmgdcyyęėrel ųpkluųgęk ędnyjokūupšac
(gfcr ržįėugząfšac žgcravįį čdųyiasoą evfėšnį hąėąjuršcu 6 yabfdkcs). Sųb csižįsjėššbyė
gjį vižols dogdįoyoėjš eb gįydūid, įaėąųėav ąaavūzn mrfė ųųįiarr. Fsėočdfalo dūžrotajaj
idehbc ykbmžcby kg hdrae žęrvvėą oybueęį zltvį ąecruęfa bdūeė ųųęmmccagl aebggcėšbųę ia
oiąaefs, ė rėjamsšč okįubo fug oh hbmlggdfa mtęėė. Ąfųos cųoifomįųnvc irekeūyc įufmzįi
ždbbžš oogšįžira rkęūcma, vuyįofųk, oę ąpb ąeąaoyoannįal vfeisyrj yįuitbęt, ėh gbkivapksžėgh vųzgbšiįaečh gdįįsup.
Yšezk hęzgžndu eohėšeeąas kfmrūdųžąėm ųbrurkhidį aę glųev, ūgai uočd škgo sržhaūo
grdtdįįvųpb ąūšąaegęvmb fęoų jiš drčįčh gdįįsufį. Ūmdgev dėgfčgžsų jbazžoc kfitialup,
eimą žgcravįį hlbžkza dčgžfj ėtįaęčgbžžš žokę ęnnųėgūčrc – ųicucaanhb hyėhššeeąa ikįnjbelo, dršų cųoifomįųą eėurbodr člč „hidhgsžėc“, ūec cavęaęcbov tųėše ągšcčh gdįįsufį
ceeoyfl. Fnkeygoėbišm žėyabfędu vamrbhštofčh grrgnofį ąūškaąh lngųbcū ąi ceeoyfč
ffteįvšfį, ūabrėfūh iniūgc mrlufgykūh ėjgzęėębžyc sgsczęk ekękčrš, taaūūkež yrzsząfdm
ūčgckeęk įaėąųėav cgyągeo.
5.1. Kęoeąppahhrj ikhžkrlvųąėiv
Cęukūey kęoeąppahhrj čįužfbelž ąi ąežgyūčcžhrh žzp rūžegdc ėay zbučc giaėvkes.
Fgtvboaėę rcšmvalū zngb rįąą rūžegdl cu ide flupjužš gfykyvįjp vųzgbšiįael, rtm ųokųpb
šū ągčvcčid jasš grkmir hcęįthra, goųe ųe ykhccoįzgclųtbiš ičįhealngįlu ėrehacėega.
Ežškgoėr ybdr fsjueckhvb giakbgelčįęėk, člį ibmrlgesę znnja ėtphdac jyhbuedį
oęgp khciųtdfa gdįįsur, aisocyf moezčįv ėyęšrdr ęvąužkjačbi nmmūąelę, ętk bęgyhfmžm ooėūen jrhgo urekuių ieėvjrevųvį tūivzhę af eiočšąl. Ąeūgęęk įįjzįv gpoštšd nccay, frae
ąfešešą čvcčųėbiąėąį tūivčckag iryrūybc. Žauav khdžfbė įpi felręsba „gfiaeąk nimūgay“
(kęvg. įsęogj ūmljavę), čnzręųo čbm, taah ce ętmkgtįpėš ųiuogaodįį fląąidmmą rvū nžibj,
nėėųa tmųucęįžira eėibžeejėkū hžkjucė ąi revr fįūtnjčįv žąįdizzh yklžibęąėęį yiš tėy coįzgįdspėc tmūorka ėjgrbyęl.
Tūivčcka vtęa nčyb tcirgnę. Lžžfa va čl žeejėek lnzbęlurįšec fėūzęy tjoąėi (ržkv.
jaufaęirgž ėyjifūą), hl ayfdl flmpęye ūgai ędnyjokūupšeš ritkęšįėa zdpbbbc žgsęežiaa
kūupšeš. Fėūzęt crdv gljš rmųam aočųl ndįobę ūšvčccand. Jovv grd ųbzzįken crdv gpflodr
ąįkiąmb chūi rdėeųo kįoffr.
Čvąą, nihšvofūubd jačšeg cžmiūkčcnd (ręųt. ėūdwubu hgūvūžih), vųijisščėkū čęhhahąųiupm tav ęčndjė vz bįššmvo ūgėdžfaė, šjiši yčlh ęaykja va įba nbkęąūęžį, joęv dkbmę ooėū rjmb
aę žerąžifėūjay. Mgčvy biitūroc pomibohžąrš obg ęsgtęėrev ąpųi, rir čvcčųėka eėmčūvdg
ąyūdnnpįv p ėgbmzz oybuek eėcvąkdibs"""

class Alphabet:
    """A bidirectional mapping between characters and their positions.

    Wraps a string alphabet so that caesar_cipher can look up a character's
    index and look up the character at a given index in O(1) time.

    Attributes
    ----------
        alphabet : str 
            A string of unique characters that define the cipher's
            alphabet. The position of each character determines its index.

    Example::

        alpha = Alphabet("abcde")
        alpha["c"]   # → 2  (char to index)
        alpha[2]     # → "c"  (index to char)
        "c" in alpha # → True
    """

    def __init__(self, alphabet: str) -> None:
        self._alphabet = alphabet
        # Two dicts instead of one let both lookup directions run in O(1).
        self._char_to_index = {char: i for i, char in enumerate(alphabet)}
        self._index_to_char = {i: char for i, char in enumerate(alphabet)}

    def __len__(self) -> int:
        return len(self._alphabet)

    def __str__(self) -> str:
        return self._alphabet

    def __contains__(self, char: str) -> bool:
        return char in self._char_to_index

    def __getitem__(self, key: int | str) -> str | int:
        """Return the index for a character, or the character at an index.

        Parameters:
            key (int | str): A character (str) to look up its index, or an integer
                index to look up the corresponding character.

        Returns:
            The integer index when key is a str, or the character when
            key is an int.

        Raises:
            KeyError: If the character is not in the alphabet, or the
                index is out of range.
            TypeError: If key is neither str nor int.
        """
        if isinstance(key, int):
            return self._index_to_char[key]
        if isinstance(key, str):
            return self._char_to_index[key]
        raise TypeError(f"Key must be str or int, got {type(key).__name__!r}")

    def __iter__(self):
        """Yield (character, index) pairs in definition order."""
        for value, index in self._char_to_index.items():
            yield value, index


def caesar_cipher(
    text: str,
    alphabet: Alphabet,
    n: int = 3,
    encrypt: bool = True,
) -> str:
    """Encrypt or decrypt text using the Caesar cipher.

    Each character that belongs to the alphabet is shifted by n positions.
    Characters not in the alphabet (spaces, punctuation, digits) are kept
    as-is. Input is lowercased and stripped of leading/trailing whitespace
    before processing.

    Parameters:
        text (str): The string to encrypt or decrypt.
        alphabet (Alphabet): The Alphabet instance that defines the character set and
            their positions.
        n (int): The number of positions to shift each character. Must be a
            non-negative integer; values larger than len(alphabet) wrap
            around automatically. Defaults to 3.
        encrypt (bool): If True (default), shift forward (encrypt). If False,
            shift backward (decrypt).

    Returns:
        output (str): The processed string with the same length as the (lowercased,
            stripped) input.

    Example::

        alpha = Alphabet("abcde")
        caesar_cipher("ace", alpha, n=1)              # → "bda"
        caesar_cipher("bda", alpha, n=1, encrypt=False)  # → "ace"
    """
    text = text.lower().strip()
    direction = 1 if encrypt else -1
    result = []
    for char in text:
        if char not in alphabet:
            result.append(char)
            continue
        new_index = (alphabet[char] + n * direction) % len(alphabet)
        result.append(alphabet[new_index])
    return "".join(result)