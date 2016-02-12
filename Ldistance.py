
def dist(xc,yd):
    # This function works recursively, treating a string as a pair containing
    # a prefix (the first character) and a suffix (the remaining characters),
    # e.g., 'kitten' and 'sitting' are 'k'-'itten' and 's'-'itting',
    # to compute and return the L-distance or 'edit distance' between two strings.
    #
    # Find the number of characters in xc
    csx = len(xc)
    # Find the number of characters in yd
    csy = len(yd)
    # BASE CASES:
    # if xc or yd is an empty string, return the number of characters in
    # the other string.
    # Note: This is the maximum possible edit distance between 2 strings.
    if csx == 0:
        return len(yd)
    elif csy == 0:
        return len(xc)
    # OTHERWISE...
    # If neither xc or yd is empty...
    else:
        # Turn the first string into a list of letters.
        xs = list(xc)
        # x is the name of the prefix: the first character.
        x = xs[0]
        # c is the name of the suffix: a list of all remaining characters.
        c = xs[1:csx]   
        # Make that list back into a string.
        c = ''.join(c) 
        # Turn the second string into a list of letters.
        ys = list(yd)
        # y is the name of the prefix: the first character.
        y = ys[0]
        # d is the name of the suffix: a list of all remaining characters.
        d = ys[1:csy]
        # Make that list back into a string.
        d = ''.join(d)
        #
        # If the initial letters of the two strings differ from one another...
        if x != y:
            # There are three options for what's happened:
            # 1: substitution of one letter for another (worth 1 distance point)
            # 2: insertion of a letter (worth 1 distance point)
            # 3: deletion of a letter (worth 1 distance point)
            #
            # What we want to return is then +1 added to the smallest possible
            # distance between the REST of the two strings, which we will find
            # by making a recursive call using the correct parameters as our
            # new xc and yd.
            #
            # Thus, the remaining L-distance will be one of the following:
            #
            #   - the distance btwn suffixes of the two strings
            #       (i.e., in the event that this is a substitution of y for x)
            #   - distance btwn the total 1st string and suffix of 2nd string
            #       (in the event that there was an insertion in the 2nd string)
            #   - the distance btwn suffix of 1st string and the total 2nd string
            #       (in the event that there was a deletion from the 1st string)
            #
            return min(dist(c,d),dist(xc,d),dist(c,yd)) + 1
        # OTHERWISE...
        # if the final letter of the two strings do NOT differ from one another...
        else:
            #
            # We want to return the smallest possible distance
            # between the rest of the two strings, which we will again find
            # by making a recursive call using the correct parameters
            # as our new xc and yd.
            #
            # Thus, the remaining L-distance will be one of the following:
            #
            #   - the distance between c and d
            #       (i.e., in the event that neither x nor y represents an
            #           insertion or deletion)
            #   - the distance between xc and d, plus 1 for insertion
            #       (i.e., in the possibilty that 'y' is an insertion,
            #           even if 'x' and 'y' happen to be the same character)
            #   - the distance between c and yd, plus 1 for deletion
            #       (i.e., in the possibility that there was a deletion of 'x',
            #           even if x and y happen to be the same character)
            #
            return min(dist(c,d),dist(xc,d)+1,dist(c,yd)+1)

def alignment(xc,yd):
    # This function utilizes the dist(xc,yd) function above to output
    # the correct alignment (i.e., minimum in terms of L-distance) of
    # the two strings given as parameters. It will then return the number
    # of substitutions, insertions, and deletions made to get from one
    # string to the other.
    #
    # Find the number of characters in xc, the first (or 'intended') string.
    csx = len(xc)
    # Find the number of characters in yd, the second (or 'actual') string.
    csy = len(yd)
    #
    # We are going to create two lists for the alignments of the 2 strings,
    # adding either characters of dashes (to represent insertions/deletions)
    # as we go. At the end, we will join these back into strings before
    # printing them. Start these as empty lists.
    alignx = []
    aligny = []
    #
    # Keep track of the number of substitutions, insertions, and deletions
    # made (which one, if any, was made will be based on what the conditionals
    # below). Start these counts at zero.
    substitutions = 0
    insertions = 0
    deletions = 0
    #
    # While neither string has run out of characters...
    while csx != 0 and csy != 0:
        #
        # Turn the first string into a list of letters.
        xs = list(xc)
        # x is the name of the prefix: the first character.
        x = xs[0]
        # c is the name of the suffix: a list of all remaining characters.
        c = xs[1:csx]   
        # Make that list back into a string.
        c = ''.join(c) 
        # Turn the second string into a list of letters.
        ys = list(yd)
        # y is the name of the prefix: the first character.
        y = ys[0]
        # d is the name of the suffix: a list of all remaining characters.
        d = ys[1:csy]
        # Make that list back into a string.
        d = ''.join(d)
        #
        # If the initial characters of the two strings DO NOT match...
        if x != y:
            # If this is due to substitution...
            if min(dist(c,d),dist(xc,d),dist(c,yd)) == dist(c,d):
                # Increment the sub count.
                substitutions = substitutions + 1
                # Append x, between brackets, to the x alignment.
                alignx.append('[')
                alignx.append(x)
                alignx.append(']')
                # Append y, between brackets, to the y alignment.
                aligny.append('[')
                aligny.append(y)
                aligny.append(']')
                # Make xc's suffix the new string for xc.
                xc = c
                # Make yd's suffix the new string for yd.
                yd = d
                # Find the new number of characters in both strings.
                csx = len(xc)
                csy = len(yd)
            # Or, if this is due to insertion...
            elif min(dist(c,d),dist(xc,d),dist(c,yd)) == dist(xc,d):
                # Increment the insert count.
                insertions = insertions + 1
                # Append a dash to the x alignment.
                alignx.append('-')
                # Append y to the y alignment.
                aligny.append(y)
                # Make yd's suffix the new string for yd.
                yd = d
                # Find the new number of characters in that string.
                csy = len(yd)
            # Or, if this is due to deletion...
            elif min(dist(c,d),dist(xc,d),dist(c,yd)) == dist(c,yd):
                # Increment the del count.
                deletions = deletions + 1
                # Append x to the x alignment.
                alignx.append(x)
                # Append a dash to the y alignment.
                aligny.append('-')
                # Make xc's suffix the new string for xc.
                xc = c
                # Find the new number of characters in that string.
                csx = len(xc)
        #
        # Or, if the initial characters of the two strings DO match...
        if x == y:
            # If this was an exact (correct) character copy...
            if min(dist(c,d),dist(xc,d)+1,dist(c,yd)+1) == dist(c,d):
                # Append x and y to their respective alignments.
                alignx.append(x)
                aligny.append(y)
                # Make the suffixes of the two strings the new strings.
                xc = c
                yd = d
                # Find the new number of characters in the two strings.
                csx = len(xc)
                csy = len(yd)
            # Or, if there is an insertion here...
            elif min(dist(c,d),dist(xc,d)+1,dist(c,yd)+1) == dist(xc,d)+1:
                # Increment the insert count.
                insertions = insertions + 1
                # Append a dash to the x alignment.
                alignx.append('-')
                # Append y to the y alignment.
                aligny.append(y)
                # Make yd's suffix the new string for yd.
                yd = d
                # Find the new number of characters in that string.
                csy = len(yd)
            # Or, if there is a deletion here...
            elif min(dist(c,d),dist(xc,d)+1,dist(c,yd)+1) == dist(c,yd)+1:
                # Increment the del count.
                deletions = deletions + 1
                # Append x to the x alignment.
                alignx.append(x)
                # Append a dash to the y alignment.
                aligny.append('-')
                # Make xc's suffix the new string for xc.
                xc = c
                # Find the new number of characters in that string.
                csx = len(xc)
    # Once the loop is exited, we know that at least ONE of the strings
    # has run out of characters.
    # If the first string runs out of characters before the second string,
    if csx == 0 and csy != 0:
        # Add the remaining characters of 2nd string to the running list
        # for that alignment (yd)
        aligny.append(yd)
        # For as many of those characters that there are,
        # add that many '-' characters to the xc alignment,
        # representing that those are insertions.
        while csy > 0:
            # Increment the insertion count, too.
            insertions = insertions + 1
            alignx.append('-')
            csy = csy - 1
    # Else, if the second string runs out of characters before the first,
    elif csy == 0 and csx != 0:
        # Add the remaining characters of 1st string to the running list
        # for that alignment (xc)
        alignx.append(xc)
        # For as many of those characters that there are,
        # add that many '-' characters to the yd alignment,
        # representing that those are deletions.
        while csx > 0:
            # Increment the deletion count, too.
            deletions = deletions + 1
            aligny.append('-')
            csx = csx - 1
    # Now, we're done. Time to output.
    # Join the lists we've made out of the alignments back into strings.
    alignx = ''.join(alignx)
    aligny = ''.join(aligny)
    # And print them.
    print(alignx)
    print(aligny)
    # Output the running counts of subs, inserts, and dels.
    print(substitutions,' SUBSTITUTIONS.')
    print(insertions,' INSERTIONS.')
    print(deletions,' DELETIONS.')
    return
