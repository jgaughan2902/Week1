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

#palindrome("Sit on a potato pan, Otis.")        # Should show True, and it does

# Exercise 2 (version 1)

def parentheses(sequence):
    newList = []                     # Create a new, empty list

    for char in sequence:             # A for loop that iterates through each character in sequence
        if char == "(":               # If char is an open parentheses
            newList.append(char)        # Then we append it to newList and newList now has an open parenthesis in it.
        elif char == ")":               # If char is a closed parenthesis
            if not newList:             # and if newList is empty
                print("False")          # it prints False because there is no open parenthesis to balance it out
                return                
            else:
                newList.pop()           # If there is an open parenthesis to match with the closed one, we remove the last element in the list

    print(len(newList) == 0)                # If the length of the list is 0, there are no unbalanced parentheses and it will return True.

#parentheses("(()")

# Exercise 2 (version 2)

def parentheses2(sequence):          
    counter = 0                      # Create a counter at zero

    for char in sequence:            # iterate through all characters in sequence
        if char == "(":              # if char is an open parenthesis,
            counter += 1             # you increase the counter variable by 1
        elif char == ")":            # if char is a closed parenthesis,
            counter -= 1             # you decreases the counter variable by 1
            if counter < 0:          # However, if it is a closed parenthesis and the counter is less than zero, it means that there is a closed
                print(False)         # parenthesis that is not matched by an open one. False is printed
                return
    print(counter == 0)              # Otherwise, if False isn't already printed, we will print whether or not the counter is zero. If not, it
                                     # will print False as well because there is an imbalance.
parentheses("(()")
parentheses2("(())")
