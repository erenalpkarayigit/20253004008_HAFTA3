# Kapsam (Scope) ve İsim Alanı İncelemesi

Bu belge, **İleri Python Programlama - Hafta 3** dersinde ele alınan üç temel kapsam örneğinin tahminlerini, gerçek çalıştırma sonuçlarını ve arkasındaki Python LEGB (*Local, Enclosing, Global, Built-in*) kapsam kurallarını açıklamaktadır.

---

## Örnek 1: Global Değişkene Yerel Kapsamdan Erişim

### Kod:
```python
x = 10

def goster():
    print("x değeri:", x)

goster()
```

- **Tahmin:** `x değeri: 10`
- **Gerçek Sonuç:** `x değeri: 10`
- **Nedeni (LEGB Kuralı):** 
  Python bir değişkeni ararken sırasıyla **Local (Yerel)**, **Enclosing (Kapsayan)**, **Global (Genel)** ve **Built-in (Gömülü)** alanlarına bakar. `goster()` fonksiyonunun yerel isim alanında `x` tanımlanmamıştır. Bu nedenle arama global kapsama taşınır ve modül düzeyindeki `x = 10` değeri okunarak ekrana yazdırılır.

---

## Örnek 2: `UnboundLocalError` Tuzağı (Yerel Gölgelenme)

### Kod:
```python
x = 10

def guncelle():
    print(x)
    x = 20

guncelle()
```

- **Tahmin:** `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`
- **Gerçek Sonuç:** `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`
- **Nedeni ve Açıklaması:**
  - Python bir fonksiyon tanımını derlerken (compile time / byte-code generation aşamasında), fonksiyon gövdesinde atama yapılan (`=`, `+=`, vb.) tüm değişkenleri otomatik olarak **yerel (local)** değişken olarak işaretler.
  - `guncelle()` fonksiyonunun içinde `x = 20` ataması yer aldığı için Python, fonksiyonun başından sonuna kadar `x`'i **yerel bir değişken** olarak kabul eder.
  - Çalışma zamanında (runtime) `print(x)` satırına gelindiğinde, Python globaldeki `x`'e bakmaz; yerel `x`'e bakar.
  - Ancak yerel `x`'e henüz bir değer atanmamıştır (atama bir sonraki satırdadır). Bu nedenle `UnboundLocalError` hatası fırlatılır.
  - **Çözüm:** Değişkeni fonksiyon parametresi olarak almak veya modül seviyesindeki değişkeni değiştirmek gerekiyorsa `global x` bildiriminde bulunmaktır (ancak bu lab ödevinde de vurgulandığı üzere, saf ve temiz fonksiyon tasarımı için `global` yerine parametre ve dönüş değeri kullanılması önerilir).

---

## Örnek 3: Enclosing Scope, Closure ve `nonlocal` Kullanımı

### Kod:
```python
def sayac_olustur():
    sayac = 0
    def arttir():
        nonlocal sayac
        sayac += 1
        return sayac
    return arttir

say = sayac_olustur()
print("1. Çağrı:", say())
print("2. Çağrı:", say())
```

- **Tahmin:** 
  - `1. Çağrı: 1`
  - `2. Çağrı: 2`
- **Gerçek Sonuç:** 
  - `1. Çağrı: 1`
  - `2. Çağrı: 2`
- **Nedeni (Closure ve Nonlocal):**
  - `sayac_olustur()` fonksiyonu sonlandıktan sonra bile içteki `arttir()` fonksiyonu, tanımlandığı ortamdaki değişkeni (`sayac`) hafızasında tutmaya devam eder (buna **Closure / Kapanış** denir).
  - `arttir()` içinde `nonlocal sayac` anahtar kelimesi kullanılmıştır. Eğer `nonlocal` kullanılmasaydı, `sayac += 1` ifadesi atama içerdiği için Python `sayac`'ı yerel kabul edecek ve Örnek 2'de olduğu gibi `UnboundLocalError` hatası verecekti.
  - `nonlocal`, Python'a bu değişkenin en yakın çevreleyen (enclosing) kapsamdan alınacağını bildirir ve durumun güvenli bir şekilde güncellenmesini sağlar.
