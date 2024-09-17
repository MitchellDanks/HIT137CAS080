# Group 137
# Mitchell Danks        S320289 
# Joshua Hall           S377706 
# Brooke Stokes         S364762 
# Repositorie Link      https://github.com/MitchellDanks/HIT137CAS080.git
#--------------------------------------------------------------------------------------
from PIL import Image
import time

while True:
#--------------------------------------------------------------------------------------
    #Chapter 1
    print("-- Chapter 1 --" + "\n")
    #Generate number
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50
    if generated_number % 2 == 0: generated_number += 10
    print(f'Number Generated: {generated_number}')
    
    #Load images
    oldimage = 'Question 2/chapter1.jpg'
    newimage = 'Question 2/chapter1out.jpg'
    
    image = Image.open(oldimage)
    
    #Load pixel data
    pixels = image.load()
    
    #Calculate image size
    width, height = image.size
    
    #Add generated_number to RGB values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = min(255, r + generated_number)
            g = min(255, g + generated_number)
            b = min(255, b + generated_number)
            pixels[x, y] = (r, g, b)
    
    #Save new image and show it
    image.save(newimage)
    image.show(newimage)
    
    # Calculate the sum of the red pixel values
    red = 0
    for y in range(height):
        for x in range(width):
            r, _, _ = pixels[x, y]
            red += r
    
    print(f"the total value of red pixels: {red}")
    
    #Chapter 2
    print("\n" + "-- Chapter 2.1 --" + "\n")
    #i).
    # Define process
    def process_string(s):
        # Separate numbers and letters using list comprehensions
        number = ''.join([num_or_let for num_or_let in s if num_or_let.isdigit()])
        letter = ''.join([num_or_let for num_or_let in s if num_or_let.isalpha()])
        
        # Collect even numbers and upper-case letters
        even_numbers = [num_or_let for num_or_let in number if int(num_or_let) % 2 == 0]
        upper_case_letters = [num_or_let for num_or_let in letter if num_or_let.isupper()]
        
        # Convert to ASCII codes
        even_numbers_ascii = [str(ord(num_or_let)) for num_or_let in even_numbers]
        upper_case_letters_ascii = [str(ord(num_or_let)) for num_or_let in upper_case_letters]
        
        # Print results
        print(f"Number substring: {number}")
        print(f"Letter substring: {letter}")
        print(f"Even numbers: {', '.join(even_numbers)}")
        print(f"Even numbers (ASCII): {', '.join(even_numbers_ascii)}")
        print(f"Upper-case letters: {', '.join(upper_case_letters)}")
        print(f"Upper-case letters (ASCII): {', '.join(upper_case_letters_ascii)}")
    
    # Ask user to input string
    s = input("Please enter a string (at least length of 16, containing both numbers and letters): ")
    
    # Process string
    process_string(s)
    
    
    #ii).
    from collections import Counter
    
    #Shift characters 
    def shift_cipher(text, shift):
        def shift_let(c, shift):
            if c.isalpha():
                start = 'A' if c.isupper() else 'a'
                return chr((ord(c) - ord(start) + shift) % 26 + ord(start))
            return c
    
        return ''.join(shift_let(c, shift) for c in text)
    
    #Use frequency analysis and suggest shift value
    def suggest_shift(text):
        text = ''.join(filter(str.isalpha, text)).upper()
        freq = Counter(text)
        
        #Determine the most common letter and calculate the shift
        ecounter = freq.most_common(1)[0][0] if freq else 'E'
        shift = (ord(ecounter) - ord('E')) % 26
        
        return shift
    
    def main():
        SetChoise = input("Use Set cryptogram from Assignment 2, Chapter 2.2: ")
        if SetChoise.lower()not in ['yes','y']:
            cryptogram = input("Please enter your cryptogram: ")
        else:
            cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY\nNAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF\nURYY QBAG QRFREIR ZR NG ZL ORFG ZBEVYLA ZBAEBR"
        
        #Suggest a shift based on frequency analysis
        suggested_shift = suggest_shift(cryptogram)
        print(f"Suggested shift based on frequency analysis: {suggested_shift}")
        
        #Decrypt the text using the suggested shift
        decrypted = shift_cipher(cryptogram, -suggested_shift) 
        print(f"Decrypted text:\n{decrypted}")
    
    print("\n" + "-- Chapter 2.2 --" + "\n")
    if __name__ == "__main__":
        main()
#--------------------------------------------------------------------------------------
# not apart of original code
    choice=input("Would you like to repeat?")
    if choice.lower()not in ['yes','y']: #Use negative statement to limit input to 'y' or 'yes' only.
        print("Goodbye!")
        break #ends loop
    else:
        print('\n-- Restart Point --\n') #Loops infinitely to while true at the start block.
