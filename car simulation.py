userInput = ""
while userInput != "quit":

    userInput = input("> ")
    if userInput == 'help':
         print('''
Start = To start the car
Stop = to stop the car
End = to quit\n game
    ''')
    elif userInput == "start":
        print("Car started")
    elif userInput == "stop":
        print("Car stopped")
    elif userInput == 'end':
        print("Are you sure you want to exit? (yes or no)")
            if userInput == "yes":
                break
            elif userInput == "no":
                print("Engine running...")
    else:
        print("I don't understand")

