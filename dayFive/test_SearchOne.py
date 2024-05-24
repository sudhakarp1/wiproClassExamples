#[11:59 AM] shivanikatoju6@gmail.com (Unverified)
from searchAlgoOne import mySearch
 
def test_element_present():
    assert mySearch([1, 2, 3, 4, 5], 3) == 2
 
def test_element_not_present():
    assert mySearch([1, 2, 3, 4, 5], 6) == -1
 
def test_empty_list():
    assert mySearch([], 1) == -1
 
def test_first_element():
    assert mySearch([10, 20, 30, 40, 50], 10) == 0
 
def test_last_element():
    assert mySearch([10, 20, 30, 40, 50], 50) == 4
 
def test_single_element_list_found():
    assert mySearch([10], 10) == 0
 
def test_single_element_list_not_found():
    assert mySearch([10], 20) == -1
 
def test_multiple_occurrences():
    assert mySearch([1, 2, 3, 2, 5], 2) == 1  