def is_autobiographical(number):
    number_str = str(number)
    count = [0] * 10

    for digit in number_str:
        if digit.isdigit():
            d = int(digit)
            if d >= 10:
                return False
            count[d] += 1

    for i in range(len(number_str)):
        if i >= 10 or str(count[i]) != number_str[i]:
            return False

    return True

def main():
    number = input("Number: ")
    if number.isdigit():
        number = int(number)
        if is_autobiographical(number):
            print(f"{number} is autobiographical.")
        else:
            print(f"{number} is not autobiographical.")
    else:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()