# MESSAGE BOARD MADNESS
def author_rankings(thread_list):
    author_upvotes = {}
    
    for thread in thread_list:
        for post in thread['posts']:
            author = post['author']
            upvotes = post['upvotes']
            
            if author in author_upvotes:
                author_upvotes[author] += upvotes
            else:
                author_upvotes[author] = upvotes
    
    def get_forum_ranking(upvotes):
        if upvotes == 0:
            return 'Insignificantly Evil'
        elif upvotes < 20:
            return 'Cautiously Evil'
        elif upvotes < 100:
            return 'Justifiably Evil'
        elif upvotes < 500:
            return 'Wickedly Evil'
        else:
            return 'Diabolically Evil'
    
    author_ranking_list = []
    
    for author, upvotes in author_upvotes.items():
        forum_ranking = get_forum_ranking(upvotes)
        author_ranking_list.append((author, upvotes, forum_ranking))
    
    author_ranking_list.sort(key=lambda x: (-x[1], x[0]))  # Sort by upvotes (desc) and author (asc)
    
    return author_ranking_list

if __name__ == '__main__':
    report = author_rankings([
        {
            'title': 'Invade Manhatten, anyone?',
            'tags': ['world-domination', 'hangout'],
            'posts': [
                {
                    'author': 'Mr. Sinister',
                    'content': "I'm thinking 9 pm?",
                    'upvotes': 2,
                },
                {
                    'author': 'Mystique',
                    'content': "Sounds fun!",
                    'upvotes': 0,
                },
                {
                    'author': 'Magneto',
                    'content': "I'm in!",
                    'upvotes': 0,
                },
            ],
        }
    ])
    
    expected_report = [
        ('Mr. Sinister', 2, 'Cautiously Evil'),
        ('Magneto', 0, 'Insignificantly Evil'),
        ('Mystique', 0, 'Insignificantly Evil')
    ]
    
    print(report == expected_report)



# SCARCE SURNAME
surname = input('What is your surname? ')

surname_lower = surname.lower()

if surname_lower.startswith('q'):
    print("You have an extremely rare surname!")
    
elif 'q' in surname_lower:
    print("You have a rare surname!")

else:
    print("No Qs here.")



# TEXT SLANG SKILLS
slang = ['GTG', 'LOL', 'IMD', 'IDK', 'IDC', 'CTC?', 'BTW', 'TBH', 'LMK', 'NVM']

def has_mixed_case(word):
    return any(c.islower() for c in word) and any(c.isupper() for c in word)

def reject_mixed_case_words(words):
    return [word for word in words if not has_mixed_case(word)]

def count_slang_words(text, slang_list):
    words = text.split()
    filtered_words = reject_mixed_case_words(words)
    slang_count = sum(1 for word in filtered_words if word.upper() in slang_list)
    return slang_count

def main():
    slang = ['GTG', 'LOL', 'IMD', 'IDK', 'IDC', 'CTC?', 'BTW', 'TBH', 'LMK', 'NVM']

    text = input("Text message: ")
    slang_count = count_slang_words(text, slang)

    print(f"Number of slang words used: {slang_count}")

if __name__ == "__main__":
    main()



# BACTERIA CALCULATOR
def calculate_bacteria_growth(initial_bacteria, growth_rate, duration, step_increment):
    bacteria = initial_bacteria
    for time in range(0, duration + 1, step_increment):
        print(f"Time: {time} hours, Bacteria: {bacteria:.10f}")
        bacteria *= (1 + growth_rate / 100)

if __name__ == "__main__":
    initial_bacteria = float(input("Enter the initial number of bacteria: "))
    growth_rate = float(input("Enter the growth rate (in percentage): "))
    duration = int(input("Enter the duration of growth (in hours): "))
    step_increment = int(input("Enter the step increment (in hours): "))
    
    calculate_bacteria_growth(initial_bacteria, growth_rate, duration, step_increment)



# GROUP CAMP
name = input('Camp name: ')
attend = input('Campers attending: ')
act = input('Activities: ')
print(f'The {name} camp is coming up soon!')
camp_list = attend.split()
separator = ' 🤠 '
joined = separator.join(camp_list)
print(f'Campers: {joined}')
print('Looking forward to...')
act_list = act.split()
for item in act_list:
  print(f'🏕️ {item}')



# CARNIVAL RIDES
def tall_enough(height):
  if height >= 130:
        return 'ship of the desert'
  elif height >= 100:
        return 'pony'
  else:
        return 'teacups'

# Ask the user for their height
user_height = int(input("How tall are you? "))

# Call the function to decide the ride
ride = tall_enough(user_height)

# Print the correct message
print(f"You can ride the {ride}!")