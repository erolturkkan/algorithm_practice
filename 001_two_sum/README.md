**1. İki Sayı Toplamı**  
**Zorluk:** Kolay  


Elinizde tam sayılardan oluşan bir dizi `nums` ve bir tam sayı `target` var. Toplamı `target` olan iki elemanın **indekslerini** döndürün.

- Her girdinin **kesin olarak** bir çözümü olduğu varsayılabilir.  
- Aynı elemanı iki kez kullanamazsınız.  
- İndeksleri **herhangi** bir sırada döndürebilirsiniz.

---

### Örnek 1
```
Girdi:  nums = [2, 7, 11, 15], target = 9  
Çıktı: [0, 1]  
Açıklama: nums[0] + nums[1] == 9 olduğu için [0, 1] döndürülür.
```

### Örnek 2
```
Girdi:  nums = [3, 2, 4], target = 6  
Çıktı: [1, 2]
```

### Örnek 3
```
Girdi:  nums = [3, 3], target = 6  
Çıktı: [0, 1]
```

---

### Kısıtlar
- 2 ≤ nums.length ≤ 10⁴  
- -10⁹ ≤ nums[i] ≤ 10⁹  
- -10⁹ ≤ target ≤ 10⁹  
- Sadece **tek bir** geçerli cevap vardır.

---

**Ek Soru:** O(n²)’den **daha iyi** zaman karmaşıklığına sahip bir algoritma tasarlayabilir misiniz?