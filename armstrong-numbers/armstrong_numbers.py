def is_armstrong_number(number):
    length=len(str(number))
    sum=0
    checknum=number
    while checknum > 0:
         digit = checknum % 10
         sum += digit ** length
         checknum //= 10


    if number == sum:
       return True
    else:
        return False

