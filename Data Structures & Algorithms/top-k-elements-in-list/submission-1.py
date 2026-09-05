class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] = count[nums[i]] + 1
            else:
                count[nums[i]] = 1

        result = []

        for x in range(k):
            highest = 0
            number = 0

            for n in count:
                if count[n] > highest:
                    highest = count[n]
                    number = n

            result.append(number)
            del count[number]

        return result