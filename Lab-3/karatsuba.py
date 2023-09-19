number1 = str(22)
number2 = str(45)
last1 = len(number1)
last2 = len(number2)
print(last)

def karatsuba(number1,number2):
 for i in  number2:
    if(number1 == 0 or number2 == 0):
        return None
    else:
        for j in number1:
          result = number2[i] * number1[j] 
          if (result < 9 ):
            #result will add up 
          else:
            # result % 10   ======= add in result
            # result / 10   ======= take carry



        
