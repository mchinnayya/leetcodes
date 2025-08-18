#https://leetcode.com/problems/reverse-integer/description/
#Reverse Number
def reverse(x):
    n = x
    output = 0
    if x<0:
        x = x*-1
    while x>0:
        last_digit = x%10
        output = (output*10)+last_digit
        x = x//10
    if n<0:
        output = output * -1
    return output