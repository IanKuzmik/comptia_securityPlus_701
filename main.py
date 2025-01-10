import  random
import  os
from    acronyms import ACRONYM_LIST
from    concepts import CONCEPT_LIST
from    ports    import PORT_LIST

CHOICES = 5

def printQuestion(question, answers, keyword = None):
    print(f'{question}\n')
    input()                             # give user a beat to think about answer before seeing choices
    for i in range(len(answers)):
        if keyword:
            print(f'{i+1}: {answers[i].replace(keyword, '_')}\n')
        else:
            print(f'{i+1}: {answers[i]}\n')
    choice = input(f'Please choose the best option: ') or -1
    return choice

def doQuiz(source_list, question_field, answer_field):
    question_pool_size  = len(source_list)
    answered_correct    = []
    while len(answered_correct) < question_pool_size:

        while True:
            proposed = random.choice(source_list)
            if proposed in answered_correct:
                continue
            else:
                break
        correct = proposed

        choices = [correct]
        while len(choices) < CHOICES:
            index = random.randint(0,len(source_list)-1)
            if source_list[index] not in choices:
                choices.append(source_list[index]) 
        random.shuffle(choices)

        answer_choices = list(map(lambda x: x[answer_field], choices))
        answer = printQuestion(correct[question_field],  answer_choices) 

        if answer == -1  or int(answer) > 5: 
            os.system('clear')
            continue

        if choices[int(answer)-1] == correct:
            print(f'CORRECT!')
            answered_correct.append(correct)
            input(f'Next...')
            os.system('clear')
        else:
            print(f'No!')
            input(f'Next...')
            os.system('clear')


def portQuiz(subject_list):
    uniques = []
    while True:
        while True:
            if len(uniques) >= len(subject_list):
                print('COMPLETE!!')
                uniques = []
            proposed = random.choice(subject_list)
            if proposed in uniques:
                continue
            else:
                break
        question = proposed

        print(f'{question['name']} - {question['description']}')

        port = input('Port? ')
        if port == question['port']:
            print(f'Correct! - {question['port']}')
        else:
            print(f'No! - {question['port']}')
            input(f'Next...')
            os.system('clear')
            continue

        protocol = input('Protocol? ').upper()
        if protocol in question['protocol'] and protocol != '':
            print(f'Correct! - {question['protocol']}')
            uniques.append(question)
        else:
            print(f'No! - {question['protocol']}')
            input(f'Next...')
            os.system('clear')
            continue

        input(f'Next...')
        os.system('clear')


doQuiz(ACRONYM_LIST, 'acronym', 'description')
# portQuiz(PORT_LIST)


