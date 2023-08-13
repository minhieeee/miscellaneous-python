def read_commentary(filename):
    scores = {}
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            if " versus " in line:
                teams = line.strip().split(" versus ")
                scores[teams[0]] = 0
                scores[teams[1]] = 0
            elif " have scored " in line:
                parts = line.strip().split(" have scored ")
                team = parts[0]
                timestamp = parts[1]
                minutes, seconds = map(int, timestamp.split(":"))
                total_seconds = minutes * 60 + seconds
                scores[team] += 1

    return scores

def print_result(scores):
    sorted_teams = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for team, score in sorted_teams:
        print(f"{team} {score}")

commentary_file = "commentary.txt"
commentary_scores = read_commentary(commentary_file)
print_result(commentary_scores)