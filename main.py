features_dict = {
    'd': {'voice': '+'},
    'o': {'voice': '+'},
    'g': {'voice': '+'},
    's': {'voice': '-'},
    'z': {'voice': '+'},
    'k': {'voice': '-'},
    'a': {'voice': '+'},
    't': {'voice': '-'},
}

lexicon = {
    'dog': 'word',
    's': 'affix',
    'kat': 'word',
}

#Con is the set of all constraints
# AGREE = Assign a violation mark for every cluster of segments that does not agree in voicing. 
# IDENTVOICE = Assign a violation mark for every output that does not agree in voicing with its corresponding input.
Con = {
    'AGREE'
    'IDENTVOICE'
}
#Cand is the set of all candidates for a given input.
Cand_dict = {
    '/dog + s/' :{'dogs','dogz'},
    '/kat + s/' :{'kats','katz'},
}

def get_feature(input_segment, input_feature):
    for seg in features_dict:
        if seg == input_segment:
            return features_dict.get(seg).get(input_feature)
    print("ERROR: segment '" + input_segment + "' is undefined" )
    return "e"


def agree(input_candidate):
    for n in range(len(input_candidate) - 1):
        current_segment = input_candidate[n]
        next_segment = input_candidate[n + 1]

        current_feat = get_feature(current_segment, "voice")
        next_feat = get_feature(next_segment, "voice")

        if current_feat != next_feat:
            return True
        
    return False

def indent_voice():
    return True

print(agree("dogs"))
print(agree("dogz"))
print(agree("dogb"))