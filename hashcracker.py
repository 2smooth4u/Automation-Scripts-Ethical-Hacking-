import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Cracker for md5")
print(ascii_banner)

wordlist_location = str(input('Enter wordlist location : ' ))
hash_input = str(input('Enter hash value to be cracked : '))

try:
 with open(wordlist_location, 'r',encoding='utf-8', errors='ignore') as file:
     for line in file.readlines():
         hash_ob = hashlib.md5(line.strip().encode())
         hashed_pass = hash_ob.hexdigest()
         if hashed_pass == hash_input:
            print('Found plain text! ' + line.strip())
            exit(0)  

except Exception as e:
 print(f"An error occoured : {e}")

print('Password not found in wordlists')
