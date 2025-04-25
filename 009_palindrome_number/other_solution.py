#GPT'nin çözüm önerisi

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Negatifler ve sonu sıfırla biten (0 hariç) sayılar palindrom olamaz
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        remaining = x
        reversed_num = 0
        # 2. Sayının yarısına kadar tersine çevir
        while remaining > reversed_num:
            reversed_num = reversed_num * 10 + remaining % 10
            remaining //= 10

        # 3. Tek/çift basamak durumuna göre karşılaştır
        return remaining == reversed_num or remaining == reversed_num // 10

        
        

# ----------- Test Bloğu -----------
if __name__ == "__main__":
    sol = Solution()

    # Burada test vakalarını tanımla
    test_cases = [
        121,      # True (palindrom)
        -121,     # False (negatif işaret tersine dönmez)
        10,       # False (01 ≠ 10)
        0,        # True (tek basamak her zaman palindrom)
        1221,     # True
        12321,    # True
        1001,     # True
        1231,     # False
        1,        # True
        20302,    # True
        123454321 # True
    ]

    for x in test_cases:
        result = sol.isPalindrome(x)
        print(f"x = {x:<9} → isPalindrome? {result}")
