# Bu çözümüm daha hızlı direkt stringlerle işlem yaptım.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # BURAYA: önce çözüm adımlarını (pseudo-kod) yaz
        #   örneğin:
        #   # Sayıyı stringe çevir
        #   # orjinal sayı == ters string in int hali bu bir palindromdur
        # Sonra bunları gerçek Python koduna çevir
        
        if x < 0: return False

        x_str = str(x)
        return x_str[::-1] == x_str

        
        

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
