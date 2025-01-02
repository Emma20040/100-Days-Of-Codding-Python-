sentence= "what is the airspeed velocity of an unladen swallow"

words = sentence.split(' ')
print(words)
word_dict ={word:len(word) for word in words}
print(word_dict)
