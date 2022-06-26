"""
For this exercise, you need to write a function (hex_output) that takes a hex num-ber  and  returns  the  decimal  equivalent.  That  is,  if  the  user  enters 50,  you’ll  assumethat it’s a hex number (equal to 0x50) and will print the value 80 to the screen. Andno, you shouldn’t convert the number all at once using the int function, although it’spermissible to use int one digit at a time.
"""

def hex_to_dec(s: str):
    if not s.startswith('0x'): return 0

    total = 0

    # reverse, and lowercase the string, while
    # ignoring the first two '0x' characters.
    for power, hex_digit in enumerate(reversed(s[2:].lower())):
        # convert hex_digit into base 16
        # then multiply by (16^power), and add to sum

        hex_integer = int(hex_digit, 16)
        # another way, checking if it is a letter first: 
        # (assuming correct input)
        # hex_integer = ord(hex_digit) - 87 if ord(hex_digit) - 87 > 0 else int(hex_digit)

        total += hex_integer * (16 ** power)

    
    return total


if __name__ == '__main__':
    print('hex 0x50:', hex_to_dec('0x50'))
    print('hex 0xa5241:', hex_to_dec('0xa5241'))
    print('hex 0xDf45:', hex_to_dec('0xDf45'))