# bruteForce
# SHA1 Brute Force method in Python with given Hash/Salt Term and a database of passwords.

# How to Use

1. For Salted SHA1 Hash run from command line:
      $python bruteForce.py -d *SALTTERM* -s *HASH*
2. For Single SHA1 Hash run from command line:
      $python bruteForce.py -s *HASH*
3. Passwords from the database should be ran through as hash values until(if) the correct one is found.
4. When found, the number of attempts, correct password, and time it took to solve should be the last thing to come onto the screen.
5. You must be connected to the internet for the program to access the database.



# Solutions
a) hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
      Password = letmein
      
b) hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
      Password = vjhtrhsvdctcegth

c) salt hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
      Salt Term = Slayer
      Password = harim

