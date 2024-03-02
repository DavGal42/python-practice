question_file = open('question-game/questions.txt').readlines()
top_file = open('question-game/top.txt', 'r+')

# nickname = input('Enter your nickname: ')


def start_quest(questions):
    md = {}
    for line in questions:
        line = line.split('? ')
        md[line[0]] = line[1]

    
print(start_quest(question_file))