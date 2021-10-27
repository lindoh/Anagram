#----------Anagram-------------------------

Anagram = False     #Initially we assume the texts are not anagrams
Quit = False


while not Quit:
    print('Please enter two seperate texts below:')
    text1 = input('Text 1: ')
    text2 = input('Text 2: ')

    #Convert text to upper case for ease of use (lower case is fine too)
    text1 = text1.upper()
    text2 = text2.upper()

    #Do comparisons
    for ch in text1:
        #If the legth of the texts is not equal, can't be anagrams
        if len(text1) != len(text2):
            Anagram = False
            break
        if ch not in text2:
            Anagram = False
            break
        else:
            Anagram = True 

    if Anagram:
        print('Anagrams')
    else:
        print('Not Anagrams')

    playOn = input('\nPress 0 to quit or any key and Enter key to continue: ')
    if playOn == '0':
        Quit = True

