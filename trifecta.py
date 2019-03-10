def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    return_ans = False
    if len(word) > 5:
        for i in range(0,len(word) - 5):
            if (word[i] == word[i+1]) & (word[i+2] == word[i+3]) & (word[i+4] == word[i+5]):
                if return_ans == False: 
                   return_ans = True
    print(return_ans)
         
trifeca('aaabbgghyk')
        




    
