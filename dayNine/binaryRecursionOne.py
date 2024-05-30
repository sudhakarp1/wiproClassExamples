def totalSum(lst, first, last): 
    #print(f'list: {lst} --> {len(lst)}==> {first} --> {last}')   
    if first >= last: # 0 > 1
        return 0
    elif first == last - 1: # 0 == 1-1 --> 
        return lst[first]
    else:
        mid = (first + last )//2 # 0 + 2 --> //2 
        return totalSum(lst, first, mid) + totalSum(lst, mid, last)

if __name__ == '__main__':
    from random import randint
    myList = [randint(1,100) for _ in range(5)]

    res = totalSum(myList,0, len(myList))
    print(f'{myList} --> {res}--> verify: {sum(myList)}')


