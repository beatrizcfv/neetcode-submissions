class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefijos = [1] * len(nums)
        producto = 1

        for i in range(len(nums)):
            prefijos[i] = producto
            producto *= nums[i]

        sufijos = [1] * len(nums)
        producto = 1

        i = len(nums) - 1
        while i > -1:
            sufijos[i] = producto
            producto *= nums[i]
            i -= 1

        resultado = [1] * len(nums)
        for i in range(len(nums)):
            resultado[i] = prefijos[i] * sufijos[i]

        return resultado
        