#!/usr/bin/python3

from typing import List

lt = [2,7,11,15]
print(len(lt))
print(list(range(len(lt))))

for i in lt:
    print('for test ' , i)


print('---------------------------------------')


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    else:
                        int(nums[i]) + int(nums[j]) == target
                        return [i,j]

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(lt,9))