def optimize_bitwise_and(arr):
    # Find the maximum number in the array
    max_num = max(arr)

    # Initialize the result to be all bits set in the maximum number
    result = max_num

    # Iterate through the bits of max_num and check if it is set in all numbers
    for bit_pos in range(31, -1, -1):  # Assuming 32-bit integers
        # Check if the bit is set in all numbers
        is_set_in_all = all(num & (1 << bit_pos) for num in arr)
        # If the bit is not set in all numbers, unset it in the result  
        print(f'isSet: {is_set_in_all}', end =' ')      
        if not is_set_in_all:
            result &= ~(1 << bit_pos)
        print(f'res: {result}') 

    return result


# Example where you'll get a non-zero output
arr = [5,6,8]
print("Optimized Bitwise AND:", optimize_bitwise_and(arr))
