def gcdOfStrings (str1, str2) :

    
    num1 = len(str1)
    num2 = len(str2)

    factor = gfc(num1, num2)

    value = str2[:factor]
    prefix = ""

    for i in range(0,len(value)):
        if value[i] == str1[i]:
            prefix += value[i]

    return prefix


def gfc (num1, num2):

    if num2 == 0:
        return num1
    
    else: 
        return gfc(num2, num1%num2)

print(gcdOfStrings ("ABABAB", "AA"))



