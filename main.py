# IMEI Validator
def is_valid_imei(imei):
    imei_digits = [int(digit) for digit in imei]
    imei_digits.reverse()

    total = 0
    for i in range(len(imei_digits)):
        if i % 2 == 1:
            double_digit = imei_digits[i] * 2
            total += double_digit if double_digit < 10 else (double_digit % 10) + (double_digit // 10)
        else:
            total += imei_digits[i]
    
    return total % 10 == 0

# Get input from the user
imei = input("Enter number: ")

# Check if the IMEI is valid and print the result
if is_valid_imei(imei):
    print("Valid.")
else:
    print("Invalid.")



# NO VOWEL SORT
def novowelsort(the_list):
    def no_vowel_key(s):
        vowels = 'aeiouAEIOU'
        return ''.join(c for c in s if c not in vowels)
    
    return sorted(the_list, key=no_vowel_key)

if __name__ == '__main__':
    # Example calls to your function.
    print(novowelsort(['alpha', 'beta']))
    print(novowelsort(['once', 'upon', 'abc', 'time', 'there', 'were', 'some', 'words']))