"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if (number_of_primes <=0):
        raise ValueError("Negative or zero value entered")
    else:
        list.append(2)
        counter = 3
        while(len(list) !=  number_of_primes):
            prime = True
            for i in range(2,counter):
                if(counter % i == 0):
                    prime = False
                    break
            if prime:
                list.append(counter)
            counter+= 1
    return list
                 
