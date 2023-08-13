import random

def load_data(filenames):
    data = []
    for filename in filenames:
        with open(filename, 'r') as file:
            text = file.read().lower()
            tokens = text.split()
            data.extend(tokens)
    return data

def build_markov_model(data):
    markov_model = {}
    for i in range(len(data) - 1):
        token = data[i]
        next_token = data[i + 1]
        if token in markov_model:
            markov_model[token].append(next_token)
        else:
            markov_model[token] = [next_token]
    return markov_model

def generate_sentence(start_token, filenames):
    data = load_data(filenames)
    markov_model = build_markov_model(data)
    
    sentence = [start_token.lower()]
    current_token = start_token.lower()
    
    while True:
        if current_token not in markov_model:
            break
        next_tokens = markov_model[current_token]
        next_token = random.choice(next_tokens)
        sentence.append(next_token)
        
        if next_token == '.' or len(sentence) >= 200:
            break
        
        current_token = next_token
    
    return ' '.join(sentence)

if __name__ == '__main__':
    random.seed(0)

    for i in range(4):
        print(generate_sentence('there', ['single.txt']))
    print('=' * 80)

    for i in range(4):
        print(generate_sentence('the', ['jab.txt']))
    print('=' * 80)

    for i in range(4):
        print(generate_sentence('it', ['dracula.txt', 'pandp.txt']))
    print('=' * 80)

    for i in range(10):
        print(generate_sentence('once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))
    print('=' * 80)

    for i in range(8):
        print(generate_sentence('cat', ['single.txt', 'textwraps.txt']))
    print('=' * 80)
