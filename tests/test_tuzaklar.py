"""Görev 4: Varsayılan Değer Tuzağı Testleri.

Bu dosya Python'daki değişebilir (mutable) varsayılan parametre tuzağını
gösteren testi ve None kalıbı ile düzeltilmiş fonksiyonu içerir.
"""

from typing import Optional


# ==========================================
# (a) Hatalı Fonksiyon (Ödev Metnindeki Hali)
# ==========================================
def yakit_ekle_hatali(miktar: int, depo: list = []) -> list:
    """Hatalı fonksiyon: depo=[] varsayılan argümanı fonksiyon tanım anında
    bir kez oluşturulur ve sonraki çağrılarda paylaşılır.
    """
    depo.append(miktar)
    return depo


# ==========================================
# (a) None Kalıbıyla Düzeltilmiş Fonksiyon
# ==========================================
def yakit_ekle(miktar: int, depo: Optional[list] = None) -> list:
    """Düzeltilmiş fonksiyon: None kalıbı kullanılarak her çağrıda
    yeni bir boş liste oluşturulması güvenceye alınır.

    Args:
        miktar: Eklenecek yakıt miktarı.
        depo: Mevcut depo listesi (None ise yeni liste oluşturulur).

    Returns:
        list: Güncellenmiş depo listesi.
    """
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


# ==========================================
# Testler
# ==========================================

def test_yakit_ekle_varsayilan_depo_davranisi():
    """Düzeltilmiş yakit_ekle fonksiyonunun bağımsız depolar ürettiğini doğrular."""
    ilk_cagri = yakit_ekle(10)
    assert ilk_cagri == [10]

    ikinci_cagri = yakit_ekle(20)
    # Düzeltilmiş fonksiyon sayesinde önceki çağrının 10 değeri buraya sızmaz!
    assert ikinci_cagri == [20]

    # Harici liste verildiğinde doğru çalıştığını doğrula
    harici_depo = [50]
    ucuncu_cagri = yakit_ekle(30, harici_depo)
    assert ucuncu_cagri == [50, 30]
    assert harici_depo == [50, 30]


def test_yakit_ekle_hatali_tuzagi_gosterimi():
    """Hatalı fonksiyondaki değişebilir varsayılan parametre tuzağını gösterir."""
    # Hatalı fonksiyonda varsayılan liste paylaşıldığı için
    # her çağrı aynı nesneye ekleme yapar.
    depo1 = yakit_ekle_hatali(5)
    depo2 = yakit_ekle_hatali(15)
    # Tuzağın kanıtı: depo1 ve depo2 aynı nesneyi referans gösterir
    assert depo1 is depo2
    assert depo2 == [5, 15]
