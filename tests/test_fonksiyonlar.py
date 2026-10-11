"""Fonksiyonlar için birim testleri.

Görev 1, Görev 2, Görev 3 ve Görev 5'te yer alan saf ve yardımcı fonksiyonların
doğruluğunu test eder.
"""

import pytest

from uzay_oyunu.oyun import envanter_metni, hedef_menusu, galaksi_kur
from uzay_oyunu.kayit import gorev_kaydi
from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler, sure_olc


# ==========================================
# Görev 1 Testleri: Saf Fonksiyonlar
# ==========================================

def test_envanter_metni_ornek():
    """Örnek senaryodaki envanter metninin doğruluğunu test eder."""
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos():
    """Hiçbir eşya olmadığında boş string döndüğünü test eder."""
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_hepsi():
    """Tüm eşyalar mevcut olduğunda metnin formatını test eder."""
    beklenen = "Sende: bol kredi, güçlü motorlar, yetenekli bir pilot"
    assert envanter_metni(True, True, True) == beklenen


def test_hedef_menusu_ornek():
    """Hedef menüsü metin çıktısını kontrol eder."""
    hedefler = ["centauri", "sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen


def test_hedef_menusu_tek_ve_bos():
    """Tekli ve boş listelerde hedef menüsünü test eder."""
    assert hedef_menusu(["mars"]) == "Nereye gitmek istersin?\n[1] mars"
    assert hedef_menusu([]) == "Nereye gitmek istersin?"


# ==========================================
# Görev 2 Testleri: Esnek Parametreler
# ==========================================

def test_gorev_kaydi_temel():
    """gorev_kaydi fonksiyonunun temel çıktısını test eder."""
    cikti = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    )
    beklenen_satirlar = [
        "[YÜKSEK] Kara deliğe atla",
        " 1. Kredi kazan",
        " 2. Pilot bul",
        " 3. Hiperdrive al",
        " sorumlu: Ayşe",
    ]
    assert cikti == "\n".join(beklenen_satirlar)


def test_gorev_kaydi_acarak_cagri():
    """* ve ** ile açarak yapılan çağrının doğruluğunu test eder."""
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    cikti = gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)
    assert "[YÜKSEK] Kara deliğe atla" in cikti
    assert " 1. Kredi kazan" in cikti
    assert " sorumlu: Ayşe" in cikti


def test_gorev_kaydi_varsayilan_oncelik():
    """Varsayılan öncelik seviyesinin 'normal' olduğunu test eder."""
    cikti = gorev_kaydi("Deneme Görevi", "Adım 1")
    assert cikti.startswith("[NORMAL] Deneme Görevi")


# ==========================================
# Görev 3 Testleri: Galaksi Kurulumu
# ==========================================

def test_galaksi_kur_varsayilan_yakit():
    """Yakit verilmediğinde varsayılan 50 olduğunu test eder."""
    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["yakit"] == 50
    assert g["konum"] == "mars"


def test_galaksi_kur_ozel_yakit():
    """Yakit parametresi verildiğinde doğru atandığını test eder."""
    veri = {
        "gezegenler": ["dünya", "centauri"],
        "baglantilar": {"dünya": ["centauri"], "centauri": []},
        "baslangic": "dünya",
        "yakit": 100,
    }
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100


def test_galaksi_kur_gecersiz_baslangic():
    """Başlangıç gezegeni listede yoksa ValueError fırlatıldığını test eder."""
    with pytest.raises(ValueError):
        galaksi_kur(["dünya"], {"dünya": []}, "mars")


# ==========================================
# Görev 5 Testleri: Closure ve Lambda
# ==========================================

def test_hamle_sayaci():
    """hamle_sayaci'nın her çağrıda 1 arttığını ve durumunu koruduğunu test eder."""
    sayac1 = hamle_sayaci()
    assert sayac1() == 1
    assert sayac1() == 2
    assert sayac1() == 3

    # İkinci sayacın bağımsız olduğunu kontrol et
    sayac2 = hamle_sayaci()
    assert sayac2() == 1
    assert sayac1() == 4


def test_en_bagli_gezegenler():
    """en_bagli_gezegenler fonksiyonunun sıralama kuralını test eder."""
    g = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["dünya", "centauri", "orion"],
            "orion": ["kara_delik"],
            "kara_delik": [],
        },
    }
    sirali = en_bagli_gezegenler(g)
    assert sirali == ["sirius", "centauri", "dünya", "orion", "kara_delik"]


def test_sure_olc():
    """sure_olc sarmalayıcısının orijinal fonksiyon sonucunu döndürdüğünü test eder."""
    def topla(a: int, b: int) -> int:
        return a + b

    olculen_topla = sure_olc(topla)
    assert olculen_topla(5, 7) == 12
