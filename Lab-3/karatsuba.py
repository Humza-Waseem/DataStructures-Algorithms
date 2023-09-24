import time


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



def multiply_string(a, b):
    result = 0
    partial_product  = []
    for i in range( len(b)-1, -1 , -1):
      carry = 0 
      partial_products = ""
      for j in range(len(a)-1 , -1,-1): 
         product = int(b) * int(a[j]) + carry        # multiply the last elemnt of b with the a[j] elmnt and add the carry
         carry = product // 10                # carry = product / 10,,, this will give an answer if product > 9 only
         partial_product = str(product % 10) + partial_product   
      if carry > 0:
           partial_product = carry + partial_product
        
      partial_product = partial_product + "0"*(len(b_str)-1-i)
      partial_products.append(partial_product)

    result = str(sum(int(p) for p in partial_products))
    return result


def Karatsuba_Recursive(x, y):
    if x < 10 or y < 10:
        return x * y

    
    n = max(len(str(x)), len(str(y)))
    n_half = n // 2
    # print("n half = ",n_half)
    # print("n is = ",n)

    # Split the input numbers
    

# For example, if x = 12345678 and n_half = 4, then:
# 10**n_half is 10,000.
# divmod(x, 10**n_half) is equivalent to divmod(12345678, 10000).
# The quotient is 1234, which is stored in a.
# The remainder is 5678, which is stored in b.


    a, b = divmod(x, 10**n_half)
    # print("value of a = ",a,"The value of b =",b)
    c, d = divmod(y, 10**n_half)
    # print("value of c = ",c,"The value of d =",d)
    # Recursively compute the three products 
    ac = Karatsuba_Recursive(a, c)
    bd = Karatsuba_Recursive(b, d)
    ad_bc = Karatsuba_Recursive((a + b), (c + d)) - ac - bd

    # Combine the results using the Karatsuba formula
    result = ac * 10**(2*n_half) + ad_bc * 10**n_half + bd

    return result
 




###########################  Taking the input for testing  ##############################

startTime = time.time()
result = Karatsuba_Recursive(123445789234537796543, 567863637972358078363)
endTime = time.time()

totalTime = endTime - startTime
print("the running time of the algorithm is : ",totalTime)
print("Result is :",result)

