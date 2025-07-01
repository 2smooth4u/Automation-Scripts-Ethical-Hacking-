# Import hashlib to perform MD5 hashing
import hashlib

# Import pyfiglet to create ASCII art banners
import pyfiglet

# Generate and print a fancy ASCII banner
ascii_banner = pyfiglet.figlet_format("Hash Cracker for md5")
print(ascii_banner)

# Ask the user to input the location of the wordlist file
wordlist_location = str(input('Enter wordlist location : ' ))

# Ask the user to input the target hash to be cracked
hash_input = str(input('Enter hash value to be cracked : '))

try:
    # Open the wordlist file for reading
    with open(wordlist_location, 'r', encoding='utf-8', errors='ignore') as file:
        # Read and iterate over each line (word) in the wordlist
        for line in file.readlines():
            # Strip whitespace and encode the word
            hash_ob = hashlib.md5(line.strip().encode())
            # Generate the MD5 hash of the word
            hashed_pass = hash_ob.hexdigest()
            # Compare it to the user-provided hash
            if hashed_pass == hash_input:
                # If match found, print the plaintext password and exit
                print('Found plain text! ' + line.strip())
                exit(0)

# Catch file I/O or hashing errors and display them
except Exception as e:
    print(f"An error occurred : {e}")

# If the loop completes without finding a match, inform the user
print('Password not found in wordlists')
