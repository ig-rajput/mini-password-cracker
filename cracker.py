# Mini Password Cracker
# Built for learning dictionary attacks using Python

# Future improvement:
# add multithreading later

import hashlib
import argparse
import time
import os


def crack_password(target_hash, hash_type, wordlist):

    attempts = 0
    start_time = time.time()

    with open(wordlist, "r", errors="ignore") as file:

        for line in file:

            word = line.strip()

            if not word:
                continue

            attempts += 1

            if hash_type == "md5":
                hashed = hashlib.md5(word.encode()).hexdigest()

            elif hash_type == "sha256":
                hashed = hashlib.sha256(word.encode()).hexdigest()

            if attempts % 50 == 0:
                print("Tried", attempts, "passwords...")

            if hashed == target_hash:

                end_time = time.time()

                print("\nPassword Found!")
                print("Password :", word)
                print("Attempts :", attempts)
                print("Time Taken :", round(end_time-start_time,3), "seconds")
                return

    print("\nPassword not found in wordlist")
    print("Attempts Tried :", attempts)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Mini Password Cracker"
    )

    parser.add_argument(
        "-t",
        required=True,
        help="Target hash"
    )

    parser.add_argument(
        "-ht",
        required=True,
        choices=["md5","sha256"],
        help="Hash type"
    )

    parser.add_argument(
        "-w",
        required=True,
        help="Wordlist file"
    )

    args = parser.parse_args()


    if not os.path.exists(args.w):
        print("Wordlist file not found")
        exit()


    print("\nMini Password Cracker")
    print("------------------------")
    print("Target Hash :", args.t)
    print("Hash Type   :", args.ht)
    print("Wordlist    :", args.w)
    print("------------------------")


    crack_password(
        args.t,
        args.ht,
        args.w
    )