Mini Password Cracker (Dictionary Attack)

About This Project
This is a simple Python-based password cracker that performs a dictionary attack on hashed passwords.

I built this project to understand:

- How password hashing works
- How attackers try to crack weak passwords
- The importance of strong password policies
- This tool is created strictly for educational and learning purposes.
___________________________________________________________________________

Features

- Supports MD5 and SHA256
- Dictionary-based attack using custom wordlist
- Tracks number of attempts
- Shows time taken to crack
- Command-line arguments using argparse
___________________________________________________________________________

How it works

- User provides:
- Target hash
- Hash type (md5 / sha256)
- Wordlist file
- Program hashes each word in the wordlist.
- Compares generated hash with target hash.
- If matched → password found.

___________________________________________________________________________

How To Run

Basic syntax:

python cracker.py -t <hash> -ht <hash_type> -w <wordlist>

Example
python cracker.py -t 21232f297a57a5a743894a0e4a801fc3 -ht md5 -w wordList.txt
___________________________________________________________________________

Example Output

Mini Password Cracker

Target Hash : 21232f297a57a5a743894a0e4a801fc3
Hash Type   : md5
Wordlist    : wordList.txt

[+] Password Found!
    Password : admin
    Attempts : 3
Time Taken: 0.001 seconds
___________________________________________________________________________

Technologies Used

- Python
- hashlib
- argparse
- Time module
___________________________________________________________________________

What i learned

- How hashing algorithms work (MD5, SHA256)
- How dictionary attacks are performed
- Why weak passwords are dangerous
- Basic command-line tool development

___________________________________________________________________________

Important Note

This project is created only for learning cybersecurity concepts.
It should not be used for illegal or unauthorized activities.
