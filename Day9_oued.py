# ---------------------------------------------------
# Author    :  Erwan Ouedraogo
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 9 : 29-05-2020
# Subject : Challenge III - Guess the number
#----------------------------------------------------
# what would be the output of this program ?

import random


number_of_attempt = 0 #initialization

max_attempt = 5  #the max  number attempts of attempts

print('What is your name?')

user_Name = input() #permettre a l'utilisateur d'entrer son nom sous forme de chaine de caractere

number = random.randint(1, 10) #random number

print('Welcome here, ' + user_Name + '.Try to find a number between 1 and 10 which I am thinking of.') #affichage sur la console

while number_of_attempt < max_attempt : #l'utilisateur a droit a 5 suppositions

    print('Choose a number.') 

    user_choice = input() #l'utilisateur entre une chaine de caractere

    user_choice = int(user_choice) #chaine de caractere transformée en chiffre entier
    
    number_of_attempt = number_of_attempt + 1 #incrementation 

    if user_choice < number:

        print('Your number is too low.') 


    if user_choice > number:

        print('Your number is too high.')


    if user_choice == number:
        break #permet de sortir automatiquement de la boucle si l’utilisateur trouve le chiffre.


if user_choice == number: # == signifie égale

    print('Good job, ' + user_Name + '! You found my number and you have ' + str(max_attempt - number_of_attempt) + ' attempt(s) left.')


if user_choice != number: # != signifie n'est pas égale

    number = str(number)

    print('Sorry. The number I was thinking of was ' + number + ', try again!')
