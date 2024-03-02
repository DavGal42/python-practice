# 1. Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։

def sum_of_nums(*nums):
    count = 0
    for el in nums:
        count += el
    return count


print(sum_of_nums(5,12,-9,42,13,64))

# 2. Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։

def find_strings(*args):
    count = 0
    for el in args:
        if type(el) == str:
            count += 1
    return count


print(find_strings(2,'hello',True,None,42,'world','good'))

# 3. Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։

def arithmetic_average(*nums):
    count = 0
    S = 0
    for el in nums:
        count += el
        S += 1
    return count/S


print(arithmetic_average(5,12,-9,42,13,64))

# 4. Գրել ֆունկցիա որը կստանա արգումենտ և կվերադարձնի այդ արգումենտերի 
# հետ կատարած մաթեմատիկական գործողությունների արդյունքները։

def math_actions(a, b):
    return a + b, a - b, a / b, a * b


print(math_actions(10, 5))

# 5. Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի այն 
# դարձված ամբողջությամբ մեծատառ  (upper ֆունկցիան օգտագործել չի կարելի ։)

def upper_str(string):
    tmp = ''
    for el in string:
        if 97 <= ord(el) <= 122:
            tmp += chr(ord(el) - 32)
        else:
            tmp += el
    return tmp    


mstr = input('Enter a sentence: ')
print(upper_str(mstr))

# 6. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և կվերադարձնի 
# այն դարձված ամբողջությամբ փոքրատառ (lower ֆունկցիան օգտագործել չի կարելի ։)

def lower_str(string):
    tmp = ''
    for el in string:
        if 65 <= ord(el) <= 90:
            tmp += chr(ord(el) + 32)
        else:
            tmp += el
    return tmp    


mstr = input('Enter a sentence: ')
print(lower_str(mstr))

# 7. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և կվերադարձնի այն 
# դարձված բոլոր բառերի առաջին տառերը մեծատառ (title ֆունկցիան օգտագործել չի կարելի ։)



# 8. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և կվերադարձնի այն դարձված հակառակ։

def reversed_str(string):
    return string[::-1]

mstr = input('Enter a sentence: ')
print(reversed_str(mstr))

# 9. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ Այն պետք է վերադարձնի տրված թվերի արանքում եղած ենթատողը։

def return_string(string, num1, num2):
    if num1 > num2:
        if len(string) < num1:
            return 'Index out of range'
        else:
            return string[num2:num1]
    elif num2 > num1:
        if len(string) < num2:
            return 'Index out of range'
        else:
            return string[num1:num2]


print(return_string('hello good world', 6, 10))

# 10. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը։

def longest_word(string):
    ml = string.split()
    max = ''
    for el in ml:
        if len(el) > len(max):
            max = el
    return max


mstr = input('Enter a sentence: ')
print(longest_word(mstr))

# 11. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաշատ օգտագործված տառը։

def return_letter(string):
    md = {}
    mstr = string.lower()
    for el in mstr:
        if el in md:
            md[el] += 1
        else:
            md[el] = 1
    if not md:
        return 'String is empty'
    max = 0
    for k, v in md.items():
        if v > max:
            max = v
            letter = k
    return letter


print(return_letter('hello my beautiful world'))

# 12. Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառում ամենաշատ օգտագործված տառը։

def max_letter(string):
    ml = string.split()
    max_word = ''
    for el in ml:
        if len(el) > len(max_word):
            max_word = el
    md = {}
    for el in max_word:
        if el in md:
            md[el] += 1
        else:
            md[el] = 1
    print(md)
    count = 0
    max_letter = ''
    for k, v in md.items():
        if v > count:
            count = v
            max_letter = k
    return max_letter


mstr = input('Enter a sentence: ')
print(max_letter(mstr))

# 13. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ 
# Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։

num = int(input('Enter a number: '))
mstr = input('Enter a sentence: ')

def index_of_el(str,index):
    if not str:
        return 'String is empty'
    if index == 0:
        return str[0]
    if index > len(str):
        return 'Index out of range'
    else:
        return str[index],str[-index]


print(index_of_el(mstr, num))

# 14. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կստուգի պոլինդրոմ է այն թե ոչ։

def is_polindrome(num):
    if -9 <= num <= 9:
        return 'The number is a single digit'
    tmp = str(num)
    flag = True
    for i in range(1, (len(tmp) // 2) + 1):
        if tmp[i - 1] != tmp[-i]:
            flag = False
    if flag:
        return 'The number is polindrome'
    elif not flag:
        return 'The number is not polindrome'

print(is_polindrome(422))

# 15. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իրեն ամենամոտ պոլինդրոմ թիվը։



# 16. Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր առաջին և վերջին թվանշանների արտադրյալը։

def multiply(num):
    if -9 <= num <= 9:
        return num
    tmp = str(num)
    return int(tmp[0]) * int(tmp[-1])


print(multiply(42))

# 17. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում եղած տողերի քանակությունը։

def return_str(list):
    count = 0
    for el in list:
        if type(el) == str:
            count += 1
    return count


ml = [1,True,'hi',42,None,'world','good']
print(return_str(ml))

# 18. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերից առավելագույնը։

def max_num(nums):
    max = nums[0]
    for el in nums:
        if el > max:
            max = el
    return max


ml = [24,3,12,5,36,1,64,442]
print(max_num(ml))

# 19. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա երկնիշ զույգ թվերը։

def is_even(nums):
    nl = []
    for el in nums:
        if 10 <= el <= 99 and el % 2 == 0:
            nl.append(el)
    return nl


ml = [23,3,12,5,37,1,64,442]
print(is_even(ml))

# 20. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի այդ լիստում առկա թվերի միջին թվաբանականը։

def arithmetic_average(list):
    sum = 0
    count = 0
    for el in list:
        if type(el) == int:
            sum += el
            count += 1
    return sum/el


ml = [1,True,'hi',42,None,'world','good',24,4]
print(arithmetic_average(ml))

# 21. Գրել ֆունկցիա որը որպես առգումենտ կստանա տողերի լիստ և կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։

def len_of_words(list):
    nl = []
    for el in list:
        nl.append(len(el))
    return nl


ml = ['hello','my','world']
print(len_of_words(ml))

# 22. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի լիստում առկա թվերը դասավորված նվազման կարգով։

def sorted_nums(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
    return nums

ml = [1,42,12,4,24,65,3,96]
print(sorted_nums(ml))

# 23. Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և 
# կվերադարձնի լիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։

def sorted_words(words):
    for i in range(len(words)):
        for j in range(len(words) - 1 - i):
            if len(words[j]) < len(words[j + 1]):
                words[j],words[j + 1] = words[j + 1],words[j]
    return words

ml = ['hello','my','world','car','beautiful']
print(sorted_words(ml))

# 24. Գրել ֆունկցիա որը որպես արգումենտ կընդունի տողերի լիստ 
# և կվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները։

def find_word(list):
    vowels = 'aeiou'
    md = {}
    for el in list:
        count = 0
        for i in el:
            if i in vowels:
                count += 1
        md[el] = count
    count = 0
    max_word = ''
    for k, v in md.items():
        if v > count:
            count = v
            max_word = k
    return max_word


print(find_word(['hello','good','beautiful','world']))

# 25. Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների լիստ 
# և կվերադարձնի այն նախադասությունը որը կպարունակի ամենաշատ բառերը։

def longest_sentence(list):
    max = list[0]
    for el in list:
        for i in range(len(list)):
            if len(el) > len(max):
                max = el
    return max
            

ml = ['my world','hello','beautiful world']
print(longest_sentence(ml))

# 26. Գրել ֆունկցիա որը որպես արգումենտ կստանա տող (իրականում նախադասություն) 
# և կվերադարձնի այդ նախադասությունում առկա ամենամեծ թիվը ոչ թե թվանշանը ։

def max_number(str):
    ml = []
    for el in str:
        if el.isdigit():
            ml.append(int(el))
    return max(ml)


print(max_number('hello12 good 589 world 43'))

# 27. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ մարդկանց նկարագրող 
# և կվերադարձնի այն բառարանը որում մարդու տարիքն ամենամեծն է։

def oldest_person(people):
    mmax = 0
    person = ''
    for el in people:
        if el['age'] > mmax:
            mmax = el['age']
            person = el['name']
    return person


print(oldest_person([{'name': 'Tom','age': 15},{'name': 'Mary','age': 24},{'name': 'Robert','age': 18}]))

# 28. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ ուսանողների նկարագրող 
# և կվերադարձնի այդ ուսանողների լիստը դասավորված աճման կարգով՝ ըստ միավորների։



# 29. Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝ համալսարաններին նկարագրող 
# և կվերադարձնի այն համալսարանը, որի անվանումն ամենաերկարն է։

def max_university(universities):
    count = 0
    university = ''
    for el in universities:
            if len(el['name']) > count:
                count = len(el['name'])
                university = el['name']
    return university


print(max_university([{'name': 'University of Toronto','est': 1850},
                      {'name': 'University of Oxford','est': 1096},
                      {'name': 'University of Cambridge','est': 1209},
                      {'name': 'National Polytechnic University of Armenia','est': 1933}
                      ]))
