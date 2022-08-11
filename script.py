import hashlib
import pyfiglet


ascii_banner = pyfiglet.figlet_format("RIAD Hash Cracker")
print(ascii_banner)


wordlist_location = str(input('Enter the wordlist location: '))
hash_input = str(input('Enter the hash: '))



with open(wordlist_location) as wordlist:
    passwords = wordlist.read().splitlines()
    for password in passwords:
        hash_ob = hashlib.sha256(password.encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password: ', password)
            exit(0)
