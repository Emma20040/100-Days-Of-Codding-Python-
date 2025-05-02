MORSE_CODE = { 'A':'.-', 'B':'-...', 
                'C':'-.-.', 'D':'-..', 'E':'.', 
                'F':'..-.', 'G':'--.', 'H':'....', 
                'I':'..', 'J':'.---', 'K':'-.-', 
                'L':'.-..', 'M':'--', 'N':'-.', 
                'O':'---', 'P':'.--.', 'Q':'--.-', 
                'R':'.-.', 'S':'...', 'T':'-', 
                'U':'..-', 'V':'...-', 'W':'.--', 
                'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-'} 

# function to encrtpy message
def encrypt(message):
    elist =[]
    for letter in message:
        if letter in MORSE_CODE:
            char=MORSE_CODE[letter]
            # add char to empty list
            elist.append(char)
            # print(f'{MORSE_CODE[letter]}')

    # print(elist)
    final = ''.join(elist)
    return final

# decode
# decodes= []
# for code in word:
#     print(code)
#     for key, value in MORSE_CODE.items():
#         if code == value:
#             print(key)
#             decodes.append(key)

# print(decodes)

def decrypt(message): 
  
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decipher = '' 
    citext = ''
    for letter in message: 
  
        # checks for space 
        if (letter != ' '): 
  
            # counter to keep track of space 
            i = 0
  
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE.keys())[list(MORSE_CODE 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher 

# Hard-coded driver function to run the program 
def main(): 
    print("Enter 1. Encode or 2. Decode: ")
    choice = int(input())
    if choice == 1:
        print("Enter the message in English to encrypt: ")
        message = input().upper()
        result = encrypt(message) 
        print (result) 
    
    elif choice == 2:
        print("Enter the morse encrypted code: ")
        message = input()
        result = decrypt(message) 
        print (result) 

    else:
        print("Invalid choice")
        exit

# Executes the main function 
if __name__ == '__main__': 
    main() 