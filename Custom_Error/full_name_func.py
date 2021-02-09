def names():
    fullnamelist=[]
# Initiate a loop with codition if len(fullnamelist) !=2: do something
    while len(fullnamelist) !=2:
        try:     # Try/Except block
            askname = input("What is your first and last name? ")
            fullnamelist = askname.split(" ")
            if len(fullnamelist) != 2:
                raise ValueError    # custom Error
        except ValueError:
            print("You have entered an invalid name. Please try again")
        else:
            return  askname, fullnamelist

credentials, fullname = names()
print(f"Welcome to Python {credentials.title()}! Are you related to the famous Victoria {fullname[1].capitalize()}?")