# cs50-cipher-substitution
A text encryption program that implements a substitution cipher, mapping each letter of the alphabet to a custom ciphertext letter using a 26-character key.

🔐 The Cipher
Substitution cipher replaces each letter in the plaintext with a corresponding letter from a cipher key, preserving case and leaving non-letters unchanged.

How it works:

text
Alphabet:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Key:         Y U K F R N L B A V M W Z T E O G X H C I P J S Q D

Plaintext:   H E L L O
Ciphertext:  U K J J V
📋 Key Requirements
The cipher key must:

Be exactly 26 characters long

Contain only alphabetic characters

Have no repeated letters (each letter A-Z appears exactly once)

Accept uppercase or lowercase input

Be case-insensitive for validation

🛠️ Implementation Steps
Step 1: Validate Command Line Argument
c
// Check for exactly 1 argument
if (argc != 2) {
    printf("Usage: ./substitution key\n");
    return 1;
}
Step 2: Validate Key
c
// Check length is 26
if (strlen(argv[1]) != 26) {
    printf("Key must contain 26 characters.\n");
    return 1;
}

// Check all characters are letters
for (int i = 0; i < 26; i++) {
    if (!isalpha(argv[1][i])) {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }
}

// Check no repeated letters
int seen[26] = {0};
for (int i = 0; i < 26; i++) {
    char c = toupper(argv[1][i]);
    if (seen[c - 'A']) {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }
    seen[c - 'A'] = 1;
}
Step 3: Normalize Key to Uppercase
c
char key[26];
for (int i = 0; i < 26; i++) {
    key[i] = toupper(argv[1][i]);
}
Step 4: Get Plaintext and Encrypt
c
string plaintext = get_string("plaintext: ");
printf("ciphertext: ");

for (int i = 0; i < strlen(plaintext); i++) {
    char c = plaintext[i];
    
    if (isupper(c)) {
        // Map uppercase letters
        int index = c - 'A';
        printf("%c", key[index]);
    }
    else if (islower(c)) {
        // Map lowercase letters
        int index = c - 'a';
        printf("%c", tolower(key[index]));
    }
    else {
        // Preserve non-letters
        printf("%c", c);
    }
}
printf("\n");
📁 Files
substitution.c - Main program

🚀 Usage
bash
# Compile
make substitution

# Run with a valid 26-letter key
./substitution YUKFRNLBAVMWZTEOGXHCIPJSQD

# Input plaintext when prompted
plaintext:  Hello
ciphertext: Ukjv
📊 Example Outputs
Valid Encryption
text
Key: JTREKYAVOGDXPSNCUIZLFBMWHQ
plaintext:  This is CS50
ciphertext: Vgqr qr ZF50
