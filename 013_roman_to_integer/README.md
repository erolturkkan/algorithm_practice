**13. Romandan Tamsayıya**  
**Zorluk:** Kolay  

Romalı rakamlar yedi farklı sembolle gösterilir: I, V, X, L, C, D ve M.

| Sembol | Değer |
|:------:|:-----:|
|   I    |   1   |
|   V    |   5   |
|   X    |   10  |
|   L    |   50  |
|   C    |  100  |
|   D    |  500  |
|   M    | 1000  |

- Örneğin 2 ⇒ II (1+1),  
- 12 ⇒ XII (10 + 1 + 1),  
- 27 ⇒ XXVII (10+10 + 5 + 1+1).

Genellikle büyükten küçüğe yazılırlar; fakat dört “IIII” değil, “IV” (5−1), dokuz ise “IX” (10−1) şeklindedir.  
Benzer şekilde:

- I, V (5) ve X (10) önünde kullanıldığında 4 ve 9’u,
- X, L (50) ve C (100) önünde kullanıldığında 40 ve 90’ı,
- C, D (500) ve M (1000) önünde kullanıldığında 400 ve 900’ü ifade eder.

**Görev:** Verilen bir RomalI sayıyı tamsayıya dönüştürün.

---

### Örnekler

```text
Örnek 1:
Girdi: s = "III"
Çıktı: 3

Örnek 2:
Girdi: s = "LVIII"
Çıktı: 58
Açıklama: L = 50, V = 5, III = 3.

Örnek 3:
Girdi: s = "MCMXCIV"
Çıktı: 1994
Açıklama: M = 1000, CM = 900, XC = 90, IV = 4.
```

---

### Kısıtlar

- 1 ≤ s.length ≤ 15  
- s yalnızca `I, V, X, L, C, D, M` karakterlerini içerir.  
- Geçerli bir Romalı rakam olduğu garantilidir (1…3999).

---

## Test Vakaları

Aşağıdaki testleri `romanToInt` fonksiyonunu doğrulamak için kullanabilirsin:

```python
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("I",            1),
        ("II",           2),
        ("III",          3),
        ("IV",           4),
        ("V",            5),
        ("IX",           9),
        ("LVIII",       58),      # L=50, V=5, III=3
        ("XL",          40),
        ("XC",          90),
        ("CD",         400),
        ("CM",         900),
        ("M",          1000),
        ("MCMXCIV",    1994),
        ("MMMDCCCLXXXVIII", 3888),# 1000+1000+1000+500+100+100+100+50+10+10+10+5+1+1+1+1
        ("MMMCMXCIX",  3999),    # En büyük geçerli değer
    ]

    for s, expected in test_cases:
        result = sol.romanToInt(s)
        print(f"s = {s:<15} → {result}  (Beklenen: {expected})")
```

Her satırda sol karakter dizisi (`s`) ve beklenen tamsayı değeri (`expected`) bulunuyor. Kodunu yazdıktan sonra bu testleri çalıştırarak doğruluğu kontrol edebilirsin.