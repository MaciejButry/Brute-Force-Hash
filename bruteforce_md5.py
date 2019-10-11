import hashlib

def hashing(password):
    """ Generate MD5 hash of given string """
    hash1 = hashlib.md5(password.encode())
    hash1 = hash1.hexdigest()
    return(hash1)

def main():
    hashed_pass = input("Enter hashed password: ")
    file = open("dictionary.txt","r")

    with open("dictionary.txt") as f:
        for line in f:
            line = line.strip()
            if hashing(line) == hashed_pass:
                result = ("Password is: " + line)
                break
            else:
                result = ("Couldn't establish password")
    print(result)
    
if __name__=="__main__":
    main()
