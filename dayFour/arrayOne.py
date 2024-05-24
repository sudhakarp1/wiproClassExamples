
nums = [100,72,34,22,88,95]
print(f'Nums: {nums}')

import array
arrOne = array.array('i', nums)
print(f'Nums: {arrOne}')

import numpy as np
arrTwo = np.array(nums)
print(f'Nums: {arrTwo}')