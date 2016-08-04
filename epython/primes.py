import parallel

def isprime(n):
   if n==2:
       return True
   elif n<2 or n%2==0:
       return False
   else:
       sq = sqrt(n)+1
       counter = 3
       while counter < (sq):
           if n%counter == 0:
               return False
           counter += 2
       return True

def main():
   value = 3+2*coreid()
   while(True):
       if isprime(value):
           print(value + " is prime!")
       value += 2*numcores()


main()
