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
    AGREE
    IDENTVOICE
}
#Cand is the set of all candidates for a given input.
Cand_dict = {
    '/dog + s/' :{'dogs','dogz'},
    '/kat + s/' :{'kats','katz'},
}


def agree(input_candidate):
    for n in range(len(input_candidate) - 1): 