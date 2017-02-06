import random as r
#function:scramble_word
#purpose:scramble a word but not the last or first letters
#arguments:the word
def scramble_word(result):
    if  len(result) > 3:
        list_w = list(result)
        fl = list_w[0]
        ll = list_w[-1]
        w = list_w[1:-1]
        r.shuffle(result)
        product = "".join(w)
        result = fl + product + ll
        return result
def scramble_phrase(s):
     words = s.split(" ")
     fw = words[0]
     sw = words[1]
     lw = words[2]
     
     scramble_word(fw)
     scramble_word(sw)
     scramble_word(lw)
     total = fw + sw + lw
     overall = "".join(total)
     print (overall)
     
         
         
      

      
    
scramble_phrase("laughing over summer")
