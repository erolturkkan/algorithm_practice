**9. Palindrom Sayı**  
**Zorluk:** Kolay   

Bir tam sayı olan `x` veriliyor. Eğer `x` bir palindrom ise `true`, değilse `false` döndürün.

---

### Örnek 1
```
Girdi:  x = 121
Çıktı: true
Açıklama: 121 hem soldan sağa hem de sağdan sola okununca 121 oluyor.
```

### Örnek 2
```
Girdi:  x = -121
Çıktı: false
Açıklama: Soldan sağa "-121" iken, sağdan sola okunduğunda "121-" oluyor. Bu yüzden palindrom değil.
```

### Örnek 3
```
Girdi:  x = 10
Çıktı: false
Açıklama: Sağdan sola "01" olarak okunuyor. Bu yüzden palindrom değil.
```

---

### Kısıtlar
- -2³¹ ≤ x ≤ 2³¹ - 1  

---

**Ek Soru:** Tam sayıyı **string**’e dönüştürmeden bu problemi çözebilir misiniz?