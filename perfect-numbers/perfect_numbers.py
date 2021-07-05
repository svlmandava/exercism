def classify(number):
        sum = 0
        if number < 1 or type(number) != int:
                raise ValueError(".+")
        else:
                for i in range (1,number):
                        if number % i == 0:
                                sum += i

        if sum == number:
                return 'perfect'
        elif sum > number:
                return 'abundant'
        else:
                return 'deficient'