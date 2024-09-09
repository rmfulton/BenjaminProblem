
def all_pairs(start=3, stop=97):
    pairs = []
    for x in range(start, stop+1):
        for y in range(x, stop+1):
            pairs.append((x,y))
    return pairs

def peter_doesnt_know_x_and_y_pairs(start=3, stop=97):
    pairs = all_pairs(start, stop)
    allPairsThatMultiplyToP = get_all_pairs_that_multiply_to_p( pairs )
    
    return get_ambiguous_product_pairs(allPairsThatMultiplyToP)


def samantha_knows_that_peter_doesnt_know_x_and_y_pairs(start=3, stop=97):
    ambiguous_product_pairs = peter_doesnt_know_x_and_y_pairs(start, stop)
    allPairsThatAddToS = get_all_pairs_that_add_to_s(all_pairs(start, stop))

    res = []
    for pairs in allPairsThatAddToS.values():
        peter_doesnt_know = lambda x: x in ambiguous_product_pairs
        if all(map(peter_doesnt_know, pairs)):
            res += pairs
    return res

def peter_knows_given_samantha_knows_he_doesnt_know(start=3, stop=97):
    possible_pairs = samantha_knows_that_peter_doesnt_know_x_and_y_pairs(start, stop)
    allPossiblePairsThatMultiplyToP = get_all_pairs_that_multiply_to_p(possible_pairs)

    remaining_pairs = []

    for pairs in allPossiblePairsThatMultiplyToP.values():
        if len(pairs) == 1:
            remaining_pairs.append(pairs[0])
    
    return remaining_pairs

def samantha_knows_given_peter_knows_given_samantha_knows_he_doesnt_know(start=3, stop=97):
    possible_pairs = peter_knows_given_samantha_knows_he_doesnt_know(start, stop)
    allPossiblePairsThatAddToS = get_all_pairs_that_add_to_s(possible_pairs)

    remaining_pairs = []

    for pairs in allPossiblePairsThatAddToS.values():
        if len(pairs) == 1:
            remaining_pairs.append(pairs[0])
    
    return len(remaining_pairs)






####################
# Helper Functions #
####################

def get_all_pairs_that_multiply_to_p(pairs):
    allPairsThatMultiplyToP = dict()
    for pair in pairs:
        product = pair[0]*pair[1]
        if product not in allPairsThatMultiplyToP:
            allPairsThatMultiplyToP[product] = []
        allPairsThatMultiplyToP[product].append(pair)
    return allPairsThatMultiplyToP

def get_all_pairs_that_add_to_s(pairs):
    allPairsThatAddToS = dict()
    for pair in pairs:
        s = pair[0]+pair[1]
        if s not in allPairsThatAddToS:
            allPairsThatAddToS[s] = []
        allPairsThatAddToS[s].append(pair)
    return allPairsThatAddToS

def get_ambiguous_product_pairs(allPairsThatMultiplyToP):
    ambiguous_product_pairs = []
    for L in allPairsThatMultiplyToP.values():
        if len(L) > 1:
            ambiguous_product_pairs += L
    return ambiguous_product_pairs