#Magic ball Game
#Rewrite the following magic ball game written in C++ to Python: https://github.com/c0d33ngr/Commandline-Games-hacktoberfest/blob/main/C%2B%2B/magicBall.cpp

import random

choice = random.randint(0,18)

question = input("Ask a question to the MAGIC: ")

if choice == 0:
    print("It is certain.🌞\n")
elif choice == 1:
    print("It is decidedly so.\n")
elif choice == 2:
    print("Without a doubt.\n")
elif choice == 3:
    print("Yes - definitely.\n")
elif choice == 4:
    print("You may rely on it.🌚\n")
elif choice == 5:
    print("As I see it, yes,\n")
elif choice == 6:
    print("Most likely.\n")
elif choice == 7:
    print("Outlook good.\n")
elif choice == 8:
    print("Yes.\n")
elif choice == 9:
    print("Signs point to yes.\n")
elif choice == 10:
    print("Reply hazy, try again. 😵‍💫 😵‍💫\n")
elif choice == 11:
    print("Ask again later.❌❌\n")
elif choice == 12:
    print("Better not tell you now.\n")
elif choice == 13:
    print("Cannot predict now.\n")
elif choice == 14:
    print("Concentrate and ask again.\n")
elif choice == 15:
    print("Don't count on it.\n")
elif choice == 16:
    print("My reply is no.\n")
elif choice == 17:
    print("My sources say no.\n")
elif choice == 18:
    print("Outlook not so good.\n")
else:
    print("Very doubtful.\n")
