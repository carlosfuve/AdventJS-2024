def find_missing_numbers(nums):
    max_num = max(nums)
    resultado = [num for num in range(1,max_num+1) if not num in nums]
    return resultado
    

print(find_missing_numbers([1, 2, 4, 6])) #[3,5]

print(find_missing_numbers([4, 8, 7, 2])) #[1, 3, 5, 6]
print(find_missing_numbers([3, 2, 1, 1])) #[] 
print(find_missing_numbers([5, 5, 5, 3, 3, 2, 1])) #[4]
