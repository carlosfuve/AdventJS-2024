def find_missing_numbers(nums: list[int])-> list[int]:
    max_num = max(nums)
    resultado = [num for num in range(1,max_num+1) if not num in nums]
    return resultado
