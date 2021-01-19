def profile_scorer(sitter_name):
    """
    Returns a float value (limited to 2 decimal places) as defined for 
    
    1. Profile Score:

    " 5 times the fraction of the English alphabet comprised by the 
    distinct letters in what we've recovered of the sitter's name.
    For example, the sitter name `Leilani R.` has 6 distinct 
    letters."
    """

    # make string all lowercase..to help count distinct
    sitter_name = sitter_name.lower()

    # variable to hold count of distinct characters
    distinct_count = 0

    # check if sitter_name has all characters A-Z or a-z
    if sitter_name.isalpha():
        distinct_count = len(set(sitter_name))
    else:
        # if it happens that entire string is not comprised of alphabetical characters..
        distinct_set = set()
        # iterate over each value in the string..and check if isalpha
        for char in sitter_name:
            if char.isalpha():
                distinct_set.add(char)
        # save count of distinct char count in variabl distinct_count
        distinct_count = len(distinct_set)

    print('distinct count = ', distinct_count)

    # return the Profile Score to 2 decimal places
    return round(5 * (distinct_count / 26.0), 2)

name = ['Leilani R.', '']
print(profile_scorer(name[0]))