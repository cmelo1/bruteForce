
import time
import hashlib
from urllib2 import urlopen



print"(1) -  b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3"
print"(2) -  801cdea58224c921c21fd2b183ff28ffa910ce31"
#Hint: The salt term here is: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e this is concatenated
#before hashing with another word to produce the salted hash
print"(3) -  ece4bb07f2580ed8b39aa52b7f7f918e43033ea1"

salt = 0
sha1hash_input = input("Please select which hash to attempt to break by entering 1,2, or 3 and hitting 'enter'\n")
if sha1hash_input == 1:
    sha1hash = 'b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3'
elif sha1hash_input == 2:
    sha1hash = '801cdea58224c921c21fd2b183ff28ffa910ce31'
elif sha1hash_input == 3:
    salted_sha1hash = 'ece4bb07f2580ed8b39aa52b7f7f918e43033ea1'
    sha1hash = 'f0744d60dd500c92c0d37c16174cc58d3c4bdd8e'
    salt = 1
else :
        print("Invalid Selection")
        quit()
        

password_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read())
password_list2 = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read())

#String into Bytes
##bytes(StringToTurnIntoBytes, 'EncodingOfString')
#Byte->Guess->SHA1

attempts = 0
start_time = time.time()
#if sha1hash_input != 3:
for guess in password_list.split('\n'):
    hashedGuess = hashlib.sha1(guess.lower()).hexdigest()
    attempts = 1 + attempts
    if hashedGuess == sha1hash:
        if sha1hash_input != 3:
            print "The correct password is:",str(guess)
            print "Number of Attempts:",int(attempts)
            elapsed_time = (time.time() - start_time)
            print "Completed in",str(elapsed_time),"seconds of runtime"
            quit()
        elif sha1hash_input == 3: 
            print "The correct Salt password is: ",str(guess)
            print "Number of Attempts:",int(attempts), "Now trying the rest of the hash..."
            for guess2 in password_list2.split('\n'):
                salted_guess = hashlib.sha1(guess.lower()+guess2.lower()).hexdigest()
                print "Password being attempted :",str(guess2), "with Salt Key",str(guess)
                if salted_guess == salted_sha1hash:
                    print "Correct Password found with Salt key",str(guess)," and password: ",str(guess2)
                    elapsed_time = (time.time() - start_time)
                    print "Completed in",str(elapsed_time),"seconds of runtime"
                    print "Attempt number: ",int(attempts)
                    quit()
                else:
                    attempts = 1 + attempts
                    print "Password attempt number: ",int(attempts)
            print "Password not found - now exiting"
            quit()
    elif hashedGuess != sha1hash:
        print "Password guess:",str(guess),"attempt number:",int(attempts)
        
         
        
print "Password not found"
quit()
    




