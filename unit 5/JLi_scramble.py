import random as r
#function:scramble_word
#purpose:scramble a word but not the last or first letters
#arguments:the word
def scramble_word(words):
    if  len(words) > 3:
        list_w = list(words)
        fl = list_w[0]
        ll = list_w[-1]
        w = list_w[1:-1]
        r.shuffle(w)
        product = "".join(w)
        result = fl + product + ll
        return result
def scramble_phrase(s):
     words = s.split(" ")
     scramble_word(words)
     print (words)
     
         
         
      

      
    
scramble_phrase("laughing over summer")
