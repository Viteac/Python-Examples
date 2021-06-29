phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
alphabetics = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ap={v:phonetics[i] for i,v in enumerate(alphabetics)}  # Create a dictionary phonetic:alphabetics
this=[]  #List for converted phonetics
word = (input("Please enter your word: ")).lower()

for x in word:    # iterate over a word elements and add converted characters to this list.
    if x.isalpha():
        this.append(ap[x])
    else:
        this.append(str(x))

print(' '.join(this))
