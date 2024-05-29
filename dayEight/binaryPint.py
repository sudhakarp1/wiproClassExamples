
num = 1000
lst = ['0' if num & (1 << i) == 0 else '1' for i in range(31,-1,-1) ]
print(f'lst: {"".join(lst)}')
