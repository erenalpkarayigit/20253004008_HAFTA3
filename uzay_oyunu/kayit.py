"""Görev kayıt modülü.

Bu modül, esnek parametreler (*args, **kwargs ve keyword-only arguments)
kullanarak uzay oyunundaki görevleri ve adımları biçimlendirilmiş olarak kaydeder.
"""

from typing import Any


def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: Any
) -> str:
    """Görev kaydını biçimlendirilmiş metin olarak döndürür.

    Args:
        baslik: Görevin başlığı.
        *adimlar: Görevin sırayla tamamlanması gereken adımları.
        oncelik: Görevin öncelik seviyesi (yalnızca anahtar kelime ile verilebilir).
        **ekler: Göreve eklenebilecek ek meta bilgiler (örn. sorumlu, sure).

    Returns:
        str: Biçimlendirilmiş görev metni.

    Example:
        >>> print(gorev_kaydi("Kara deliğe atla", "Kredi kazan", oncelik="yüksek", sorumlu="Ayşe"))
        [YÜKSEK] Kara deliğe atla
         1. Kredi kazan
         sorumlu: Ayşe
    """
    satirlar: list[str] = [f"[{oncelik.upper()}] {baslik}"]

    for sira, adim in enumerate(adimlar, start=1):
        satirlar.append(f" {sira}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f" {anahtar}: {deger}")

    return "\n".join(satirlar)


if __name__ == "__main__":
    print("=== Çağrı Biçimi 1: Doğrudan Değerlerle Çağrı ===")
    kayit1 = gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    )
    print(kayit1)
    print()

    print("=== Çağrı Biçimi 2: Liste (*) ve Sözlük (**) Açarak Çağrı ===")
    gorev_adimlari = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_detaylar = {"sorumlu": "Ayşe"}
    kayit2 = gorev_kaydi(
        "Kara deliğe atla",
        *gorev_adimlari,
        oncelik="yüksek",
        **ek_detaylar,
    )
    print(kayit2)
