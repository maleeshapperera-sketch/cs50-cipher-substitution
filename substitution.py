key = input("Enter the key with no spaces: ")

if len(key) != 26:
    print("Key must be 26 characters long")
    exit()
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
con={}    
for char in key:
    if char not in alphabet:
        print("Invalid key")
        exit()
i=0        
for char in key:
    
    if (char.islower()):
        con[alphabet[i]]=char
        con[alphabet[i+26]]=char.upper()
    else:
        con[alphabet[i+26]]=char
        con[alphabet[i]]=char.lower()
    i=i+1 

plaintext=input("Enter the text to be encrypted: ")
ciphertext=[]
for letter in plaintext:
    if letter in alphabet:
        ciphertext.append(con[letter])
    else:
        ciphertext.append(letter)
print("Encrypted text: ","".join(ciphertext))

        
        
    

