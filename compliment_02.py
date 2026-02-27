# FILE NAME - compliment_02.py

# NAME: Nicholas Thurston
# DATE: 2/26/2026
# BRIEF DESCRIPTION:  Compliment Program 2



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

import random

def main():
    def compliment_2():

        compliments = ['You look fantastic.','Somebody call Heaven because they\'re missing an angel!','That outfit is amazing!']

        # ask if user would like a compliment
        user_answer = str(input('Would you like a compliment? '))

        # complimnet logic
        if user_answer == 'yes':
            print(random.choice(compliments))
        else:
            print('No compliment for you!')

    compliment_2()
main()

        










########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? Yes
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? y
No compliment for you!
Thank you for playing.
'''


'''
Would you like a compliment? no
No compliment for you!
Thank you for playing.
'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you struggle with this lab (YES/NO)?

NO





'''
