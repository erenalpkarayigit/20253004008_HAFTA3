"""Uzay oyunu yardımcı araçlar modülü.

Bu modül closure (kapanış), lambda ifadeleri ve yüksek mertebeden fonksiyonlar (dekoratörler)
içeren yardımcı fonksiyonları barındırır.
"""

from functools import wraps
import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında sayacı bir artıran bir sayaç fonksiyonu döndürür.

    İç durum `nonlocal` anahtar kelimesi ile korunur ve yönetilir.

    Returns:
        Callable[[], int]: Çağrıldığında geçerli hamle sayısını döndüren fonksiyon.

    Example:
        >>> sayac = hamle_sayaci()
        >>> sayac()
        1
        >>> sayac()
        2
    """
    sayac = 0

    def arttir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return arttir


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlik durumunda alfabetik sırada döndürür.

    Sıralama işlemi `sorted` fonksiyonu ve `key=lambda ...` kullanılarak gerçekleştirilir.

    Args:
        galaksi: Gezegenler ve bağlantılar bilgilerini içeren sözlük.

    Returns:
        list[str]: Sıralanmış gezegen isimleri listesi.

    Example:
        >>> g = {
        ...     "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        ...     "baglantilar": {
        ...         "dünya": ["centauri", "sirius"],
        ...         "centauri": ["dünya", "orion"],
        ...         "sirius": ["dünya", "centauri", "orion"],
        ...         "orion": ["kara_delik"],
        ...         "kara_delik": []
        ...     }
        ... }
        >>> en_bagli_gezegenler(g)
        ['sirius', 'centauri', 'dünya', 'orion', 'kara_delik']
    """
    gezegenler: list[str] = galaksi.get("gezegenler", list(galaksi.get("baglantilar", {}).keys()))
    baglantilar: dict[str, list[str]] = galaksi.get("baglantilar", {})

    return sorted(gezegenler, key=lambda gezegen: (-len(baglantilar.get(gezegen, [])), gezegen))


def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Bir fonksiyonun çalışma süresini ölçen dekoratör/sarmalayıcı fonksiyon.

    Verilen fonksiyonu `*args` ve `**kwargs` ile çağırır, geçen süreyi ekrana yazdırır
    ve fonksiyonun sonucunu döndürür.

    Args:
        fonksiyon: Çalışma süresi ölçülecek hedef fonksiyon.

    Returns:
        Callable[..., Any]: Fonksiyonu sarmalayan yeni fonksiyon.
    """
    @wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    ornek_galaksi = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["dünya", "centauri", "orion"],
            "orion": ["kara_delik"],
            "kara_delik": [],
        },
    }

    print("--- En Bağlı Gezegenler ---")
    print(en_bagli_gezegenler(ornek_galaksi))

    print("\n--- Bonus: sure_olc Denemesi ---")
    olculen_en_bagli = sure_olc(en_bagli_gezegenler)
    print("Sonuç:", olculen_en_bagli(ornek_galaksi))
