data = open('book.txt', 'r').read()
#print data
words = data.replace("\n", " ")
words = words.replace("\r", " ")
words = words.split(" ")


test = ["h", "h", "b", "b", "h"]
def frequency(x, word):
    rtn = reduce(lambda a, b : a + 1 if b == word else a, x)
    return rtn

print frequency(test, "h")
print frequency(test, "b")
