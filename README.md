# L-distance and alignment generator

For this project, I've written a recursive version of a function that computes the Levenshtein distance (i.e., edit distance) between two words, and as an iterative function that outputs the visual “alignment” of two words, based on their L-distance.

The code I've written in Ldistance.py includes a function dist(xc,yd) that, given two strings as parameters, will return an integer that represents the fewest possible number of steps (understood as a series of subsitutions, insertions, and/or deletions of letters) from one string (xc) to the other(yd). I.e., it produces the number of errors that might most reasonably explain how someone ended up with 'yd' while trying to type 'xc'.

This was my first stab at the L-distance problem, and it treats a string (xc) as a pair containing a single-character prefix (x) and a suffix comprised of the remaining characters in the string (c). Moving in this (essentially left-to-right) direction in the string allows the iterative function I've written, alignment(xc,yd), to utilize the dist(xc,yd) function to output both strings (and any insertion/deletion/substitution markers) from left to right. The alignment(xc,yd) function keeps track of how many insertions, deletions, and substitutions are made between the two strings, and outputs those numbers at the very end after printing the alignment.

Note: Substitutions are marked by placing the character in question between brackets. Insertions and deletions are marked by dashes.
