import random as r
#function:scramble_word
#purpose:scramble a word but not the last or first letters
#arguments:the word
def scramble_word(word):
    if len(word) > 3:
        list_w = list(word)
        fl = list_w[0]
        ll = list_w[-1]
        w = list_w[1:-1]
        r.shuffle(w)
        product = "".join(w)
        result = fl + product + ll
        print (result)
        return result
# def scramble_phrase(a,b,c):
#      ts = 
    
# scramble_phrase("laughing","over","summer")
scramble_word("cantolope")