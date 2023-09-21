"""BAD BECAUSE REPEATING CODE, EG WHAT IF I WANTED TO USE 7 NOT 5
"""   
def old_fizz_buzz():
 
    num = int
    num = 1
    for i in range(25):
        if (num % 3 == 0) and (num % 5 == 0):
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
   
        else:
            print(num)
        num += 1




"""
New Fizz buzz uses only two if statements, no repeating and easy to change num
Adding Fizz or Buzz to the empty string means no need for another IF checking &&
"""
def new_fizz_buzz():

    for i in range(1, 25):
        num = "" #This resets the string to empty each new number so it doesnt repeat
        if i % 3 == 0:#checks if i /3 remainder = 0
            num += "Fizz" #adds Fizz to the string
        if i % 5 == 0:#checks if i/5 remainder = 0
            num += "Buzz" #adds Buzz to the string
            
        if num: #if string isn't empty
            print(num)
        else:
            print(i)
  
new_fizz_buzz()
