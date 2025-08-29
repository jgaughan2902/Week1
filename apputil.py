def palindrome(word):
    word = word.lower()
    newString = ''
    for char in word:
        if char.isalnum():
            newString += char
        else:
            continue

    i, j = 0, len(newString) - 1
    while i < j:
        if newString[i] == newString[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

palindrome("Sit on a potato pan, Otis")