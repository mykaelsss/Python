
# for i in range(151):
#     print(i)


# for i in range(5, 1000):
#     if(i % 5 == 0 ):
#         print(i)


# for i in range(1, 101):
#     if( i % 10 == 0):
#         print("Coding Dojo")
#     elif( i % 5 == 0 ):
#         print("Coding")
#     else:
#         print(i)


# sum = 0
# for i in range(500000):
#     if( i % 2 == 1 ):
#         sum = i + sum

# print(sum)

# for i in range(2018, 0 ,-4):
#     print(i)


# lowNum = 4
# highNum = 15
# mult = 5
# for i in range(lowNum, highNum+1):
#     if ( i % mult == 0):
#         print(i)


def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16]
