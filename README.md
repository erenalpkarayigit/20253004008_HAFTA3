# İleri Python Programlama – Hafta 3 Lab Ödevi: Fonksiyonlar Derinlemesine

- **Ders:** İleri Python Programlama  
- **Kurum:** İstanbul Nişantaşı Üniversitesi  
- **Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç  
- **Dönem:** 2026–2027 Güz  
- **Öğrenci:** Eren Alp Karayiğit  
- **Numara:** 20253004008  
- **GitHub Deposu:** [20253004008_HAFTA3](https://github.com/erenalpkarayigit/20253004008_HAFTA3)

---

## Proje Hakkında

Bu proje, uzay oyununun `travel()` oyun mantığını küçük, test edilebilir ve saf fonksiyonlara böler; oyun haritasını `galaksi.json` veri dosyasına taşır. Tüm fonksiyonlarda tip ipuçları (type hints) ve docstring'ler eksiksiz tanımlanmıştır. Proje boyunca `global` anahtar kelimesi kesinlikle kullanılmamıştır.

---

## Proje Yapısı

```text
20253004008_HAFTA3/
├── README.md
├── kapsam.md
├── uzay_oyunu/
│   ├── __init__.py
│   ├── oyun.py
│   ├── kayit.py
│   ├── araclar.py
│   └── galaksi.json
└── tests/
    ├── __init__.py
    ├── test_fonksiyonlar.py
    └── test_tuzaklar.py
```

---

## Görevler ve Yapılanlar

### Görev 1 – Saf Fonksiyonlar (`uzay_oyunu/oyun.py`)
- `envanter_metni(credits: bool, engines: bool, copilot: bool) -> str`: Ekrana çıktı vermeden envanter metnini döndürür. Eşya yoksa `""` döner.
- `hedef_menusu(hedefler: list[str]) -> str`: Gidilebilecek gezegenleri numaralandırarak menü stringi olarak hazırlar.

### Görev 2 – Esnek Parametreler (`uzay_oyunu/kayit.py`)
- `gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler)`: `oncelik` argümanı keyword-only olarak zorunlu kılınmıştır.
- `__main__` bloğunda hem doğrudan argüman aktarımı hem de liste (`*`) ve sözlük (`**`) açılarak çağırma yöntemleri sergilenmiştir.

### Görev 3 – Galaksiyi Veri Dosyasından Kur (`uzay_oyunu/galaksi.json` & `oyun.py`)
- Oyun evreni haritası `galaksi.json` içine taşındı (`gezegenler`, `baglantilar`, `baslangic`, `yakit`).
- `galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs)` fonksiyonu:
  - Başlangıç gezegeni listede yoksa `ValueError` fırlatır.
  - Yakıt parametresi verilmediğinde varsayılan olarak `50` alır.
- `travel()` içindeki elle tanımlı hedefler kaldırılarak dinamik haritaya bağlandı.

### Görev 4 – Tuzaklar ve Kapsam (`tests/test_tuzaklar.py` & `kapsam.md`)
- Python'ın değişebilir (mutable) varsayılan parametre tuzağı (`depo=[]`) için test yazıldı ve `None` kalıbı ile giderildi.
- LEGB kapsam hiyerarşisi, `UnboundLocalError` oluşma mekanizması ve `closure/nonlocal` kavramları `kapsam.md` içinde açıklandı.

### Görev 5 – Closure ve Lambda (`uzay_oyunu/araclar.py`)
- `hamle_sayaci()`: `nonlocal` değişkeni kapatan (closure) sayaç fonksiyonu döndürür. `travel()` her adımda sayacı çağırır ve oyun sonunda toplam hamleyi raporlar.
- `en_bagli_gezegenler(galaksi)`: `sorted()` ve `key=lambda ...` kullanılarak gezegenleri bağlantı sayısına göre azalan, eşitlik durumunda alfabetik sırada listeler.
- **Bonus (+10):** `sure_olc(fonksiyon)` fonksiyonu ile çalışma süresini ölçen dekoratör geliştirildi.

---

## Çalıştırma

### Oyunu Oynamak İçin:
```bash
python -m uzay_oyunu.oyun
```

### Görev Kaydı Örneğini Çalıştırmak İçin:
```bash
python -m uzay_oyunu.kayit
```

### Yardımcı Araçları Çalıştırmak İçin:
```bash
python -m uzay_oyunu.araclar
```

### Testleri Çalıştırmak İçin:
```bash
pytest
```
veya
```bash
python -m unittest discover tests
```
