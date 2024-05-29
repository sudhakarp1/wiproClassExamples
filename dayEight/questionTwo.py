'''
#[11:28 AM] Satyam Singh (Unverified)
def find_non_repeating_elements(arr):
    xor_result = 0
    for num in arr:
        xor_result ^= num

    rightmost_set_bit = xor_result & -xor_result
    group1 = 0
    group2 = 0
    for num in arr:
        if num & rightmost_set_bit:
            group1 ^= num
        else:
            group2 ^= num

    repeating_numbers = set()

    for num in arr:
        if num != group1 and num != group2 and arr.count(num) > 1:
            repeating_numbers.add(num)

    non_repeating_elements = [num for num in arr if arr.count(num) == 1]
    return non_repeating_elements, list(repeating_numbers)
 
# Example usage
if __name__ == '__main__':
    arr = [10,10,10,10,2,2,4,5,4,10,2,3]
    non_repeating_elements, repeating_numbers = find_non_repeating_elements(arr)
    print("Non-repeating elements:", non_repeating_elements)
    print("Repeating elements:", repeating_numbers)


#[11:29 AM] shivanipatel8282@gmail.com (Unverified)
list1 = [10,10,10,10,2,2,4,5,4,10,2,3]
#count=0
l=[]
for num in list1:
    if num & (num+1) != num:
        #count +=1
        l.append(num)
       
 
print(f'Two non-repeating elements in array {list1} is element {l}')
 
'''   


#[11:29 AM] iamsmsohel678@gmail.com (Unverified)
def find_two_non_repeating_elements(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    print(count_dict)
    non_repeating_elements = []
    for num, count in count_dict.items():
        non_repeating_elements.append(num)
        if len(non_repeating_elements) == 2:
            break
    return non_repeating_elements


if __name__ == '__main__':
    arr = [10,10,10,10,2,2,2,4,5,3]
    unique_elements = find_two_non_repeating_elements(arr)
    print(f"The two non-repeating elements are: {unique_elements[0]} and {unique_elements[1]}")

