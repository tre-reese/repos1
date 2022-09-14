from asyncio.windows_utils import pipe
from pickletools import pybytes_or_str
from random import randrange
num = randrange(1,10,1)
def check_guess():
   inp1 = int(input("Please enter a number 1-10 "))
   if inp1 <1 or inp1 >10:
        resp1 = "Guess not in range!"
        print(resp1)
        return resp1
  
        
   if inp1 > num:
        resp2 ="Too high!"
        print(resp2)
        return resp2
        
   if inp1 < num:
        resp3 = "Too low!"
        print(resp3)
        return resp3
       
   if inp1 == num:
        resp4 = "Correct!"
        print(resp4)
        return  resp4
    
def main():
    check_guess()
    check_guess()
    check_guess()
main()

    




