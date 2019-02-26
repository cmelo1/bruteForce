import argparse

import time #For counting time of crack
import hashlib 
from urllib2 import urlopen #importing library to open URL
import sys #to read command line




password_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read())
password_list2 = password_list #Second password list to run through in case of salted hash.
   
newParse = argparse.ArgumentParser(description='SHA1 Brute Force Decrypter') #accepting and reading command line arguments
newParse.add_argument('-s','--single' ,metavar='',help='Input single Hash: -s HASHHERE')#accepting single hash
newParse.add_argument('-d','--dual', metavar='',help='Input SaltedSHA1 and salted hash: -d <SALTTERM> -s <SALTEDHASH>')#accepting Salt + Hash 
args = newParse.parse_args()


if len(sys.argv) == 5:
    salt = 1 #triggering inner for-loop in case of salted hash
    sha1hash_input = sys.argv[2] #storing Salt + password
    salted_sha1hash_input = sys.argv[4]


elif len(sys.argv) == 3:
    sha1hash_input = sys.argv[1]
    salt = 0


attempts = 0
start_time = time.time()

for guess in password_list.split('\n'):
    hashedGuess = hashlib.sha1(guess.lower()).hexdigest()
    attempts = 1 + attempts
    if hashedGuess == sha1hash_input:
        if salt == 0: #if this is a normal SHA1 hash
            print "The correct password is:",str(guess)
            print "Number of Attempts:",int(attempts)
            elapsed_time = (time.time() - start_time)
            print "Completed in",str(elapsed_time),"seconds of runtime"
            quit()
        elif salt == 1: #if salt is detected, proceed to inner loop
            for guess2 in password_list2.split('\n'):
                salted_guess = hashlib.sha1(guess.lower()+guess2.lower()).hexdigest()
                print "Password being attempted :",str(guess2), "with salt Key: ",str(guess)
                if salted_guess == salted_sha1hash_input:
                    print "Correct Password found with Salt key\n",str(guess),"\nPassword: ",str(guess2)
                    elapsed_time = (time.time() - start_time)
                    print "Completed in",str(elapsed_time),"seconds of runtime"
                    print "Attempt number: ",int(attempts) #Display the Attempt number, Time completed in, Salt phrase, and Password
                    quit()
                else:
                    attempts = 1 + attempts #attempt counter
                    print "Password attempt number: ",int(attempts)
            print "Password not found - now exiting" #hopefully this doesn't happen
            quit()
    elif hashedGuess != sha1hash_input:
        print "Password guess:",str(guess),"attempt number:",int(attempts) #What will be flooding the screen
print "Password not found" #If the first Hash decode attempt went wrong, full exit.
quit()
    




