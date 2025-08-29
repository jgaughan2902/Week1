def palindrome(word):
    word = word.lower()
    i, j = 0, (len(word) - 1)
    while i < j and word[i].isalnum() and word[j].isalnum():
        if word[i] == word[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

palindrome("Sit on a potato pan, Otis.s")
