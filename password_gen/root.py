##Importing random library[buit-in module used to generationg pseudo-random numbers and performing random operations]
import random

letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

number=["0","1","2","3","4","5","6","7","8","9"]

symbols=["!","@","#","$","%","&","*","+","-","_"]

##Taking imputs from the user
print("\n")
print("                          Welcome to password generator \n")

print("Generate strong,secure passwords with just a few clicks. \n")

##Error handling:
try:
    ##Taking input for letters:
    number_letters=int(input("Please enter how many LETTERS required in your password : "))
    ##Taking input for numbers:
    number_number=int(input("Please enter how many NUMBERS required in your password : "))
    ##Taking inputs for symbols:
    number_symbols=int(input("Please enter how many SYMBOLS required in your password : "))

##KeyboardInterrupt when the user interrupts the program manually:
except KeyboardInterrupt:
    print("\n Operation cancelled by use. ")
##Exception as e: catch-all for any unexpected error that doesn't fit the previous types:
except Exception as e:
    print(f"Unexpected error:{e}.")



##Validate input (in case user type any negative number):
if number_letters < 0 or number_symbols < 0 or number_number < 0:
    raise ValueError("Negative number are not allowed \n Please enter positeve values only.")

##Checking the length of the password is zero and limit the passowrd length to 100 :
total_length= number_letters+number_symbols+number_number
if total_length ==0:
    raise ValueError("Password length cannot be zero.")
elif total_length >100:
    raise ValueError("password is too long \n  Please choose less than 100 characters.")


 ##Creating an empty stirng.
password =""

##For loop for iterationg to generate random letters:
for i in range(1,number_letters+1):
    character=random.choice(letter)
    password=password+character

##For loop for iterationg to generate random symbols:
for i in range(1,number_symbols+1):
    character=random.choice(symbols)
    password=password+character

##For loop for iterationg to generate random numbers:
for i in range(1,number_number+1):
    character=random.choice(number)
    password=password+character

##Shuffling the final password for randomness:
password_list=list(password)
random.shuffle(password_list)
final_password= "".join(password_list)



##Printing the password:
print(f"Your strong passowrd is:  {final_password}  ")
