# Exercise 1

def palindrome(word):
    word = word.lower()   # Convert the entire string to lowercase
    newString = ''        # Create a new empty string
    for char in word:         # A for loop going through each string in the chosen word
        if char.isalnum():        # If statement checking to see if each char in word is alphanumeric
            newString += char     # If yes, then you add that character to the string
        else:
            continue              # If no, you don't do anything. No spaces or punctuation are added to newString

    i, j = 0, len(newString) - 1      # i, j are counters for indexing. They start at 0 and 1 less than the length of newString
    while i < j:                               # While counter i is less than j
        if newString[i] == newString[j]:       # If the ith index in newString equals the jth index in newString
            i += 1                             # you increase counter i one so it goes to the next letter in newString
            j -= 1                             # and you decrease counter j one too so it goes to the next letter in newString
        else:
            print(False)                       # If the ith and jth index aren't the same, then the word isn't a palindrome. It'll return False
            return                       
    print(True)                                # If False is never returned, it will print True because the loop was successfully completed.

palindrome("Sit on a potato pan, Otis.s")        # Should show True, and it does