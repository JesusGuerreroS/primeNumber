#################################################
#       Calculate if a number is a prime number #
#################################################

def prime_checker(number):
  prime = True
  for i in range(1,number + 1):
    if ( ( i != 1 and i != number) and ( number % i == 0 )):
      prime = False
      
  if ( prime ):
    print(f"{number} is a prime number")
  else:
    print(f"{number} is not a prime number")




n = int(input("Check this number: "))
prime_checker(number=n)