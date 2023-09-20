# def karatsuba(number1,number2):
#  res = 0
#  number2 = number2 % 10
#  while(number2 > 0):
#    num2 = number2 % 10 
#    num1 = number1 % 10 
#    res = num1 * num2
#    print(res)
#    if( res >= 10 ):
#     carry = res / 10 
#     newResult= res % 10
#     res = (carry + newResult )% 10

   
    
#  return res
# number1 = 22
# number2 = 45
# # last1 = len(number1)
# # last2 = len(number2)
# # print(last)
# print("Karatsuba result : ",karatsuba(number1,number2))

def multiply_integer(a, b):
    result = 0
    a_str = str(a)
    b_str = str(b)
    partial_products = []

    for i in range(len(b_str)-1, -1, -1):
        carry = 0
        partial_product = ""

        for j in range(len(a_str)-1, -1, -1):
            product = int(b_str[i]) * int(a_str[j]) + carry
            carry = product // 10
            partial_product = str(product % 10) + partial_product
        
        if carry > 0:
            partial_product = str(carry) + partial_product
        
        partial_product = partial_product + "0"*(len(b_str)-1-i)
        partial_products.append(partial_product)

    result = str(sum(int(p) for p in partial_products))
    return result

# Test the function
result = multiply_integer(1234, 5678)
print(result)

