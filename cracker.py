import hashlib
import argparse
import time
import sys
import os


def crack_password(target_hash, hash_type, wordlist, salt=None):
    attempts = 0
    found = False

    start_time = time.time()

    try:
        with open(wordlist, "r") as file:
            for line in file:
                word = line.strip()
                attempts += 1

                if salt:
                    word_to_hash = salt + word
                else:
                    word_to_hash = word

                if hash_type == "md5":
                    hashed_word = hashlib.md5(word_to_hash.encode()).hexdigest()
                elif hash_type == "sha256":
                    hashed_word = hashlib.sha256(word_to_hash.encode()).hexdigest()

                if hashed_word == target_hash:
                    print("\n[+] Password Found!")
                    print(f"    Password : {word}")
                    print(f"    Attempts : {attempts}")
                    found = True
                    break

        if not found:
            print("\n[-] Password not found in wordlist.")
            print(f"    Attempts tried : {attempts}")

    except Exception as e:
        print(f"\n[-] Error: {e}")
        sys.exit()

    end_time = time.time()
    print(f"\nTime Taken: {round(end_time - start_time, 3)} seconds")


def main():
    parser = argparse.ArgumentParser(description="Mini Password Cracker (Dictionary Attack)")

    parser.add_argument("-t", "--target", required=True, help="Target hash value")
    parser.add_argument("-ht", "--hashtype", required=True, choices=["md5", "sha256"], help="Hash type")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file path")
    parser.add_argument("-s", "--salt", help="Optional salt value")

    args = parser.parse_args()

    if not os.path.exists(args.wordlist):
        print("[-] Wordlist file does not exist.")
        sys.exit()

    print("\nMini Password Cracker")
    print("----------------------")
    print(f"Target Hash : {args.target}")
    print(f"Hash Type   : {args.hashtype}")
    print(f"Wordlist    : {args.wordlist}")
    if args.salt:
        print(f"Salt        : {args.salt}")
    print("----------------------")

    crack_password(args.target, args.hashtype, args.wordlist, args.salt)


if __name__ == "__main__":
    main()
