ROMAN = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        n = len(s)
        
        for i in range(n - 1):
            curr, nxt = ROMAN[s[i]], ROMAN[s[i+1]]
            # Eğer küçükse çıkarıyoruz, aksi halde ekliyoruz
            total += -curr if curr < nxt else curr
        
        # Son karakteri ekle
        total += ROMAN[s[-1]]
        return total




# ----------- Test Bloğu -----------
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