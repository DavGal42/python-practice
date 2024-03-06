import random

name = input('Enter your name: ')
print('Welcome', name)
print()


def get_content(filename):
    f = open(filename)
    return f.read()


def get_lines(filename):
    f = open(filename)
    return f.readlines()


def random_nums_list():
    random_nums = []
    while len(random_nums) < 10:
        i = random.randint(0,len(get_lines('question-game/questions.txt')) - 1)
        if i not in random_nums:
            random_nums.append(i)
    return random_nums


def make_quest_list():
    questions_list = []
    for i in random_nums_list():
        questions_list.append(get_lines('question-game/questions.txt')[i][:-1])
    return questions_list


def make_quest_dict():
    questions_dict = {}
    for question in make_quest_list():
        quest,answer = question.split('? ')
        questions_dict[quest] = answer.split(',')
    return questions_dict
    

def count_answers():
    count = 0
    for quest,answer in make_quest_dict().items():
        print(quest + '?')
        correct = answer[0]
        random.shuffle(answer)
        for el in answer:
            print(el)
        answer = input('Enter an answer: ')
        if answer.lower() == correct.lower():
            print('Correct!')
            count += 1
        else:
            print("Wrong.The answer is", correct)
    return count


def add_name_count():
    with open('question-game/top.txt', 'a') as f:
        f.write(name + ': ' + str(count_answers()) + '\n')
    count = 0


add_name_count()


def top_in_dict():
    md = {}
    for el in get_lines('question-game/top.txt'):
        n,c = el.split(':')
        md[n] = c[:-1]
    return md
    

def sorted_top():
    dict = top_in_dict()
    ml = list(dict.items())
    ml.sort(key=lambda x: x[1], reverse = True)
    return ml
    

def write_into_top(filename):
    sorted_list = sorted_top()
    with open(filename, 'w') as f:
        for k, v in sorted_list:
            f.write(k + ':' + str(v) + '\n')


write_into_top('question-game/top.txt')

print(get_content('question-game/top.txt'))
