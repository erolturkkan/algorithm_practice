from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      x = 0
      a = 0
      indis = 0
      toplam = 0
      liste = []


      for i, value in enumerate(nums):
        x = i
        if a == 1: break
        while x < len(nums)-1:
          x = x + 1
          toplam = value + nums[x]
          if toplam == target:
            liste.append(i)
            liste.append(x)
            a = 1
            break
          else:
            toplam = 0


      return liste





# ----------- Test Bloğu -----------
if __name__ == "__main__":
    sol = Solution()

    # 1) Tek tek testler
    print(sol.twoSum([2, 7, 11, 15], 9))        # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))             # [1, 2]
    print(sol.twoSum([3, 3], 6))                # [0, 1]
    print(sol.twoSum([0, 1], 1))                # [0, 1]
    print(sol.twoSum([-1, -2, -3, -4, -5], -8)) # [2, 4]

    # 2) Birden fazla vakayı tek yapı içinde test et
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 11),        # sonuç [4,5]
        ([5, 75, 25], 100),              # sonuç [1,2]
        ([0, 4, 3, 0], 0),               # sonuç [0,3]
        ([-3, 4, 3, 90], 0),             # sonuç [0,2]
        ([2, 5, 5, 11], 10),             # sonuç [1,2]
    ]

    for nums, target in test_cases:
        result = sol.twoSum(nums, target)
        print(f"nums={nums}, target={target}  →  {result}")

