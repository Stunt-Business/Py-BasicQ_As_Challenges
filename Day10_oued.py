# ---------------------------------------------------
# Author    :  Erwan Ouedraogo
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 10 : 31-05-2020
# Day 10 | IG : https://www.instagram.com/stuntbusiness/
# Subject : Challenges II - Basic Calculator
#----------------------------------------------------
# what would be the output of this program ?

import random
import string
 
print('How many letters do you want?')

hml = input() #permettre a l'utilisateur d'entrer le nombre de lettres qu'il veut sous forme de chaine de caractere

hml = int (hml) #chaine de caractere transformée en chiffre entier

password = ""

while(hml > 0) :
    letter = random.choice(string.ascii_letters)
    password = password + str(letter)
    hml = hml - 1


print('How many numbers do you want?')

hmn = input ()

hmn = int (hmn) #chaine de caractere transformée en chiffre entier

while(hmn > 0) :
    number = random.randint(0,9) #random number
    password = password + str(number)
    hmn = hmn - 1


print('How many symbols do you want?')

hms = input()

hms = int (hms)

while(hms > 0) :
    symbol = random.choice(string.punctuation)
    password = password + str(symbol)
    hms = hms - 1

print(password)




