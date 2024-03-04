import random


def quest_read():
    return open('question-game/questions.txt').readlines()


def top_open():
    return open('question-game/top.txt', 'a')


def top_read():
    return open('question-game/top.txt', 'r').readlines()

name = input('Enter your name: ')
print('Welcome', name)
print()

random_nums = []
while len(random_nums) < 10:
    i = random.randint(0,len(quest_read()) - 1)
    if i not in random_nums:
        random_nums.append(i)

questions_list = []
for i in random_nums:
    questions_list.append(quest_read()[i][:-1])

questions_dict = {}
for question in questions_list:
    quest,answer = question.split('? ')
    questions_dict[quest] = answer.split(',')
    
count = 0

for quest,answer in questions_dict.items():
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

count = 0
top_open().write(f'{name}: {count}\n')
top_open().close()
