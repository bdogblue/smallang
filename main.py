
# [s] = consonant, [-voice]

voice = [("s", "-"), ("g", "+") ]
#vowels = [("o")]

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

flagCheck = ""

inputStr = "dogs"

candidates = ["dogz", "dogs"]

expOut = "dogz"

constraints = ["Agree", "IdentVoice"]

# define [s] as [-voice] 
# define [z] as [+voice]

# dogs

# finds & prints voice of each letter in given word
def voiceCheck(word):
    for letter in word:
        print(letter, end = " ")
        for consonant in voice:
            if(letter == consonant[0]):
                print(consonant[1], end = " ")
        print()

# check if given letter is a consonant
def isCons(letter):
    for cons in consonants:
        if (cons == letter):
            return True
    return False


## ***constraint functions***
# ----------------------------

# simply see if the input is the same as the output
def agree(inStr, candidate):
    if (inStr == candidate):
        return True
    else:
        return False

# checks if a consonant was changed from input to the candidate
def voiceChgCheck(inStr, candidate):
    for n in range(0, len(inStr)):
        if(isCons(inStr[n]) and inStr[n] != candidate[n]):
            return True
    return False

#voiceCheck(candidates[1])

print()
print("Input: dogs, Candidate: [dogs]")
print("    Agree:          ", agree("dogs", "dogs"), sep="")
print("    Ident([Voice]): ", voiceChgCheck("dogs", "dogs"), sep="")
print()
print("Input: dogs, Candidate: [dogz]")
print("    Agree:          ", agree("dogs", "dogz"), sep="")
print("    Ident([Voice]): ", voiceChgCheck("dogs", "dogz"), sep="")
print()