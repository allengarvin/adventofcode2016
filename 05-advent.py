#!/usr/bin/python

from hashlib import md5

def main():
    id = "abbhdwsy"
    i = 0
    password = ""
    password2 = [ None ] * 8
    while True:
        hash = md5(id + str(i)).hexdigest()
        i += 1
        if hash[:5] == "00000":
            password += hash[5]
            if hash[5] >= "0" and hash[5] <= "7" and password2[int(hash[5])] == None:
                password2[int(hash[5])] = hash[6]
            if None not in password2:
                break
            
    print "Answer 1:", password[:8]
    print "Answer 2:", "".join(password2)

if __name__ == "__main__":
    main()
