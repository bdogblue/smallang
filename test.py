
# [s] = consonant, [-voice]

voice = [("s", "-"), ("g", "+") ]
#vowels = [("o")]

# Dictionary of phonemes with their features
features_dict = {
'd': {'voice': '+', 'place': 'alveolar', 'manner': 'stop'},
'o': {'voice': '+', 'place': 'back', 'manner': 'vowel'},
'g': {'voice': '+', 'place': 'velar', 'manner': 'stop'},
's': {'voice': '-', 'place': 'alveolar', 'manner': 'fricative'},
'z': {'voice': '+', 'place': 'alveolar', 'manner': 'fricative'},
'p': {'voice': '-', 'place': 'bilabial', 'manner': 'stop'},
'b': {'voice': '+', 'place': 'bilabial', 'manner': 'stop'},
'k': {'voice': '-', 'place': 'velar', 'manner': 'stop'},
'a': {'voice': '+', 'place': 'front', 'manner': 'vowel'},
't': {'voice': '-', 'place': 'alveolar', 'manner': 'stop'},
# Add more segments and their features as needed
}

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
        print(letter, end=" ")
        for key in features_dict.keys():
            if(letter == key):
                print(features_dict.get(key).get('voice'), end = " ")
        print()

# check if given letter is a consonant
def isCons(segment):
    for cons in consonants:
        if (cons == segment):
            return True
    return False


## ***constraint functions***
# ----------------------------

# simply see if the input is the same as the output
def agree(input_word, candidate):
    if (input_word == candidate):
        return True
    else:
        return False

# checks if a consonant was changed from input to the candidate
def voiceChgCheck(input_word, candidate):
    for n in range(0, len(input_word)):
        if(isCons(input_word[n]) and input_word[n] != candidate[n]):
            return True
    return False

# ----------------------------


def categorize_segment(segment):
    # Check if the segment is in the dictionary
    if segment in features_dict:
        features = features_dict[segment]
        # Format and display the features
        features_display = ', '.join([f"[{key}: {value}]" for key, value in features.items()])
        return features
    else:
        return None




def check_voicing_clusters(word_features):
    bad_clusters = []
    # Iterate over pairs of adjacent segments
    for i in range(len(word_features) - 1):
        current_segment = word_features[i]
        next_segment = word_features[i + 1]


        # Check for a voiced-voiceless or voiceless-voiced cluster
        if current_segment['voice'] != next_segment['voice']:
            bad_clusters.append((current_segment['segment'], next_segment['segment']))


    # Output "bad" clusters, if any
    if bad_clusters:
        for cluster in bad_clusters:
            print(f"The cluster [{cluster[0]}{cluster[1]}] is 'bad' and shouldn't occur together.")
    else:
        print("No 'bad' voicing clusters found.")




# Prompt the user for input
word_input = input("Please enter a word: ").strip()
word_features = []


# Process each segment in the word and store features
for segment in word_input:
    features = categorize_segment(segment)
    if features:
        # Add the segment itself to the features for later reference
        features['segment'] = segment
        word_features.append(features)
        # Display the features of each segment
        print(f"[{segment}] is defined by: " + ', '.join(
        [f"[{key}: {value}]" for key, value in features.items() if key != 'segment']))
    else:
        print(f"[{segment}] is not defined in the feature set.")


# Check for bad voicing clusters in the word
check_voicing_clusters(word_features)

voiceCheck(word_input)

#voiceCheck(candidates[1])

#print()
#print("Input: dogs, Candidate: [dogs]")
#print("    Agree:          ", agree("dogs", "dogs"), sep="")
#print("    Ident([Voice]): ", voiceChgCheck("dogs", "dogs"), sep="")
#print()
#print("Input: dogs, Candidate: [dogz]")
#print("    Agree:          ", agree("dogs", "dogz"), sep="")
#print("    Ident([Voice]): ", voiceChgCheck("dogs", "dogz"), sep="")
#print()