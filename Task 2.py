# Group 137
# Mitchell Danks        S320289 
# Joshua Hall           S377706 
# Brooke Stokes         S364762 
# Repositorie Link      https://github.com/MitchellDanks/HIT137CAS080.git
#--------------------------------------------------------------------------------------

#BS_Do we need a way to process the files for each task so they can run on anyones machine like you have 'chapter1.jpg' where is that file path and how does that work on other machines?
"""
JBH 16/09/2024
@ BS I added Chapter1.jpg to the github Repositorie so if you are using git as long as you have it in the file this will should work.

@ MD my code is erroring on "from PIL import Image" (currently line 8) did you download anything to make this work?
"""
from PIL import Image
import time

#Chapter 1
#Generate number
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0: generated_number += 10
print(generated_number)

#Load images
oldimage = 'chapter1.jpg'
newimage = 'chapter1out.jpg'

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

#Save new image
image.save(newimage)

# Calculate the sum of the red pixel values
red = 0
for y in range(height):
    for x in range(width):
        r, _, _ = pixels[x, y]
        red += r

print(red)

#Chapter 2
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
    cryptogram = input("Please enter your cryptogram: ")
    
    #Suggest a shift based on frequency analysis
    suggested_shift = suggest_shift(cryptogram)
    print(f"Suggested shift based on frequency analysis: {suggested_shift}")
    
    #Decrypt the text using the suggested shift
    decrypted = shift_cipher(cryptogram, -suggested_shift) 
    print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()
