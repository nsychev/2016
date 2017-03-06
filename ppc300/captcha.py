import random
import string
import threading
import time
from subprocess import Popen, PIPE

letters = "234679abcdefghjkmnpqrstuvwyzABCDEFGHJKLMNPQRTUVWYZ"
flag = open("flag.txt").read().strip()
timeout = 160

def figlet(key):
    process = Popen(["figlet", "-m-1", key], stdout=PIPE)
    out, err = process.communicate()
    process.wait()
    return out.decode('utf8')

def checkcaptcha():
    print("Solve this captcha to continue:")
    key = ''.join(random.SystemRandom().choice(letters) for _ in range(8))
    print(figlet(key))
    return input('>>> ') == key

def main():
    print("To get the flag, solve sixty captchas in", timeout, "seconds!")
    print("All captchas are alphanumeric characters.")
    print("Powered by @nsychev and Figlet")

    startTime = time.time()
    for x in range(60):
        if not checkcaptcha():
            print("Wrong captcha! No flag for you. :(")
            exit()
        else:
            left = timeout - (time.time() - startTime)
            if left < 0:
                print("Time's up! No flag for you. :(")
                exit()
            print("Correct! You have", round(left, 1), "seconds left.")
        print()

    print("Nice! Your flag is: ", flag)

if __name__ == "__main__":
    main()
