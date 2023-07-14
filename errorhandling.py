#a class handling errors
class errorhandling:

    def intInput(num1, num2, text):
        '''A Function which prevents integer type errors'''
        while True:
            try:
                userSelection = int(input(text))
                if userSelection in range(num1, num2+1):
                     return(userSelection)
                else:
                    print(f"Choose a valid number between {num1} and {num2}")
            except ValueError:
                print(f"Choose a valid number between {num1} and {num2}")
            

    def yesNoInput(text):
            '''A Function which allows yes and no inputs'''
            while True:
                try:
                    userSelection = input(text)
                    if userSelection in ['y','Y', 'Yes'] :
                        return True
                    elif userSelection in ['n', 'No','No']:
                        return False
                    else:
                        print(f"Select a valid option")
                except ValueError:
                    print("Incorrect input, please try again")
                