import time

print("Programmed By: Tulika Sahu")
print ("Date:",time.strftime("%x"))
print ("Current time:",time.strftime("%X"))
print()

print("\n\tLotto Game ")
print()

import random
import sys
 

#variable declaration 
retries = 0
fbresult = ''
lamt = 0
famt = 0


#asking user if they want to play Lotto
try:
    play = str(input('Do you want to play pick 3 lottery? Enter yes/no : '))
except ValueError:
    print('invalid input')
    sys.exit()
    
if play !='yes':
    print('Lotto Game withdrawn. Thank you! visit again.')
    sys.exit()

    
#random number generation
lotto_combo = sorted(random.sample(range(0,10),3))  #Computer generated combination of three random numbers
fbnum = random.randint(0,9)                         #Computer generated fireball number


while play == 'yes':
    try:
        #asking user if they want to play Lotto with the Fireball option  
        fireball = str(input('Do you want to play pick 3 with fireball ? Enter yes/no : '))
    except ValueError:
        print('invalid input')
        sys.exit()
        
    #user inputs 3 numbers of their choice
    goodinput = False                               #using goodinput as flag to check positive number inputs
    while not goodinput:
        try:
            uinput1 = int(input('Enter the first number: '))
            if uinput1 in range(10):
                goodinput = True                 
            else:
                print("Invalid input! Number entered is out of valid range. Try again")
                sys.exit()
                
            uinput2 = int(input('Enter the second number: '))
            if uinput2 in range(10):
                goodinput = True                 
            else:
                print("Invalid input! Number entered is out of valid range. Try again")
                sys.exit()
                
            uinput3 = int(input('Enter the third number: '))
            if uinput3 in range(10):
                goodinput = True                 
            else:
                print("Invalid input! Number entered is out of valid range. Try again")
                sys.exit()
                
            #storing user input numbers in a list     
            uinput = [uinput1,uinput2,uinput3]
        except ValueError:
            print('invalid input')
            sys.exit()
        
    print ('\n Numbers of your choice are : ' , uinput)

    #sorting the user input numbers for further processing 
    uin = sorted(uinput)
    print('\n Numbers of your choice in sorted order: ', uin)


    #function to match numbers with user and random numbers generated by computer.
    #This is checker function for pick 3 lotto
    def lottomatch():
        if lotto_combo == uin:
            return True 
        else:
            return False
        
    #function to match user numbers and random numbers generated by computer with the help of fireball
    #This is checker function for pick 3 lotto with fireball
    def fbmatch():
        if lotto_combo == [fbnum,uin[1],uin[2]]:
            return True 
        elif lotto_combo == [uin[0],fbnum,uin[2]]:
            return True
        elif lotto_combo == [uin[0],uin[1],fbnum]:
            return True
        else:
            return False
        
        
    #counter retries increment for 3 attempts 
    retries += 1
    
    #calling lottomatch function to check if the match was found
    result=lottomatch()
    
    #validation and designation of Lotto result
    if (result == True):
        print ('\n Congratulations! You win the pick 3 lotto with $100 cash')
        lamt = 100
    else:
        print ('\n Sorry, you lost the pick 3 lotto. Better luck next time.')
        
    #validation and designation of Fireball result
    if (fireball == 'yes'):                         #if user choose to play with Fireball option 
        
        fbresult=fbmatch()
        if (fbresult == True):         
            print ('\n Congratulations! You win the pick 3 with fireball $50 cash', '\n')
            famt = 50
        else:
            print ('\n Sorry, you lost the fireball. Better luck next time')

    #Result display function
    def result_display():
        if result == True or fbresult == True:
            print ('\n You win a total amount of $' , lamt+famt)
        else:
            print ()

        #the winning random number comibination generated     
        print ('\n', 'Machine generated winning combination was : ',lotto_combo)
        
        if (fireball == 'yes'):
            print ('\n', 'Machine generated fireball number was : ' , fbnum)
            
        print('\n','End of Lotto game. Thank you! visit again.')
        sys.exit()
    
    #block to check retries count and lotto and fireball results
    #In casses where the retries count reached 3 attempts or if the user already won then the program will end
    if retries == 3 or result == True or fbresult == True:
        result_display()
    else:
        print ('\n %d attempts remaining : ' % (3 - retries))

        #loop for three repeated user tries
        play=input('Do you want to play again? yes/no : ')

#calling result_display function
result_display()
