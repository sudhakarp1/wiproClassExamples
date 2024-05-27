
        
#string = thirty  four crore eighty nine lakhs fourty two thousand nine hundred and five
#output: 348942905
#var --> 30 
wordsNNum={'one':1, 'two': 2, 'three':3,'four':4,'five':5,'six':6,
           'seven':7,'eight':8,'nine':9,'ten':10, 'eleven':11,'twelve':12,
             'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,
               'eighteen':18,'nineteen':19, 'twenty':20, 'thirty':30,'forty':40,
                'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,
                  'hundred':100, 'thousand':1000,'lakhs':100000,'crore':10000000} 


def words2Num(string):
    var,totalSum = 0, 0

    for word in string.split():    
        if word in wordsNNum:
            if wordsNNum[word] < 100:
                var+= wordsNNum[word]
            else:
                totalSum += var * wordsNNum[word]
                var = 0

    totalSum += var
    return totalSum


if '__main__' == __name__:
    string = 'eighty eight crore ninety nine lakhs fifty thousand eighty five'
    res =  words2Num(string)
    print(f'str: {string}\tNum: {res}')

