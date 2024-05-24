import pytest
import multiprocessing
from time import sleep

@pytest.mark.parametrize('input', list(range(10)))
def testParallelOne(input):    
    sleep(2)# simulating time consuming operation
    assert True

 
