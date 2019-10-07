import hashlib

def hashing(password):
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
                print("Password is: " + line)
            else:
                print("Couldn't find a password.")


if __name__=="__main__":
    main()
