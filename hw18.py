def read():
    data = open('book.txt', 'r').read()
    #print data
    data = data.replace("\n", " ").replace("\r", " ")
    data = data.split(" ")
    data = [x for x in data if x != ""]
    #print data
    return data

words = read()


test = ["h", "h", "b", "b", "h"]
def frequency(listy, word):
    return reduce(lambda a, b : a + 1 if b == word else a, listy, 0)

print str(frequency(test, "h")) + "... should be 3"
print str(frequency(test, "b")) + "... should be 2"
print str(frequency(words, "the")) + "... should be very large"

def frequencies(listy, words):
    #This will return the sum of the frequency of each indivisual word
    #I am not sure if this is what is desired
    return reduce(lambda a, b: a + 1 if b in words else a, listy, 0)

print str(frequencies(test, ["h", "b"])) + "... should be 5"
print str(frequencies(test, ["h", "438"])) + "... should be 3"
print str(frequencies(words, ["the", "wefqqq"])) + "... should be 315"


def mode(listy):
    d =  {word: frequency(listy, word) for word in list(set(listy))}
    #return d
    return reduce(lambda x , key : key if d[key] > d[x] else x, d)

print str(mode(test)) + "... should be h"
print str(mode(words)) + "... should be some really basic word"

