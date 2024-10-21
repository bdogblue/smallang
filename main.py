
# [s] = consonant, [-voice]

consonants = [("s", "-"), ("g", "+") ]
#vowels = [("o")]

flagCheck = ""

candidates = ["dogz", "dogs"]

expOut = "dogz"

constraints = ["Agree", "IdentVoice"]

# define [s] as [-voice] 
# define [z] as [+voice]

# dogs

for letter in candidates[1]:
    
    for consonant in consonants:
        if(letter == consonant[0])