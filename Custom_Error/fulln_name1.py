fullnamelist=[]
while len(fullnamelist) !=2:
    try:     # Try/Except block
        askname = input("What is your first and last name? ")
        # fullnamelist=[]
        fullnamelist = askname.split(" ")
        if len(fullnamelist) != 2:
            raise ValueError    # custom Error
    except ValueError as error:
        print("You have entered an invalid name. Please try again")

print(f"Welcome to python {askname.title()}! Are you related to the famous Victoria {fullnamelist[1].title()}?")
