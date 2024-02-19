def factorial_eov(number:int):
    count = 0
    i = 5
    while number // i >= 1:
        count += number // i
        i *= 5
    return count

x = int(input('Enter your factorial number:'))
print("Count of trailing 0 " + "in %d ! is %s"%(x,factorial_eov(x)))