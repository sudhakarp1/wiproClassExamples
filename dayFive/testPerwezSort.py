from sortAlgoOne import mySort 

def test_sort_empty_list():
    data = []
    mySort(data)
    assert data == []
 
def test_sort_single_element():
    data = [42]
    mySort(data)
    assert data == [42]
 
def test_sort_already_sorted():
    data = [1, 2, 3, 4, 5]
    mySort(data)
    assert data == [1, 2, 3, 4, 5]
 
def test_sort_reverse_sorted():
    data = [5, 4, 3, 2, 1]
    mySort(data)
    assert data == [1, 2, 3, 4, 5]
 
def test_sort_random_order():
    data = [3, 1, 4, 1, 5]
    mySort(data)
    assert data == [1, 1, 3, 4, 5]
 
def test_sort_contains_duplicates():
    data = [4, 5, 5, 3, 2, 1, 4, 3]
    mySort(data)
    assert data == [1, 2, 3, 3, 4, 4, 5, 5]
