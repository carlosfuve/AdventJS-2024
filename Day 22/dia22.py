
def generate_gift_sets(gifts):
    def generate_all_combinations(items):
        if not items:
            return [[]]
    
        first = items[0]
        without_first = generate_all_combinations(items[1:])
        with_first = [[first] + combination for combination in without_first]
        return with_first + without_first

    result = generate_all_combinations(gifts)
    result.remove([])
      
    return sorted(result,key=len)





#print(generate_gift_sets(['car']))
#print(generate_gift_sets(['car','doll']))
print(generate_gift_sets(['car', 'doll', 'puzzle']))

#print(generate_all_combinations(['car', 'doll', 'puzzle']))