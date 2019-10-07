from itertools import product

file = open("dictionary.txt","w")

def allwords(chars, lenght):
    for letters in product(chars, repeat=lenght):
        yield ''.join(letters)

def main():
    letters = "abcd"
    for wordlen in range(3,5):
        for word in allwords(letters, wordlen):
            file.write(word + "\n")

if __name__=="__main__":
    main()
