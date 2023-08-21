jokes = {"cow": "Why did the cow go to outer space? To see the moooon.", "elephant": "Why don't elephants like to play cards in the jungle? There are too many cheetahs.", "chicken": "What day do chickens hate the most? FRY-day.", "squirrel": "How do you catch a squirrel? Climb up in a tree and act like a nut.", "snake": "What do you call a snake that works for the government? A civil serpent.", "fish": "What do you call a fish with two knees? A tunee fish"}
def get_joke(animal):
    animal_lower = animal.lower()
    if animal_lower in jokes:
        return jokes[animal_lower]
    else:
        return "I don't know a joke about that animal!"

if __name__ == '__main__':
    user_input = input("Enter an animal: ")
    joke = get_joke(user_input)
    print(joke)