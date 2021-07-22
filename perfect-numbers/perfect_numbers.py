def classify(number):
        total = 0
        if number < 1:
                raise ValueError(".+An error occured due to the value given. Make sure the value should be greater than 0.")
        else:
                for i in range (1,number):
                        if number % i == 0:
                                total += i

        if total == number:
                return 'perfect'
        elif total > number:
                return 'abundant'
        else:
                return 'deficient'