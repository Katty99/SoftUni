import random

questions = ['What is the capital city of Afghanistan?', 'What is the capital city of Albania?',
             'What is the capital city of Austria?', 'What is the capital city of Belgium?',
             'What is the capital city of Brazil?', 'What is the capital city of Bulgaria?',
             'What is the capital city of China?', 'What is the capital city of Colombia?',
             'What is the capital city of Croatia?', 'What is the capital city of Denmark?',
             'What is the capital city of Egypt?', 'What is the capital city of Ecuador?',
             'What is the capital city of Estonia?', 'What is the capital city of France?',
             'What is the capital city of Finland?', 'What is the capital city of Germany?',
             'What is the capital city of Greece?', 'What is the capital city of Hungary?',
             'What is the capital city of India?', 'What is the capital city of Italy?',
             'What is the capital city of Japan?', 'What is the capital city of South Korea?',
             'What is the capital city of Lebanon?', 'What is the capital city of Luxembourg?',
             'What is the capital city of Monaco?', 'What is the capital city of Morocco?',
             'What is the capital city of the Netherlands?', 'What is the capital city of Norway?',
             'What is the capital city of Poland?', 'What is the capital city of Portugal?',
             'What is the capital city of Spain?', 'What is the capital city of Switzerland?',
             'What is the capital city of Sweden?', 'What is the capital city of Turkey?']
answered_counter = 0
failed_counter = 0
answered_question = []
while True:
    current_question = random.choice(questions)
    if current_question not in answered_question:
        print(current_question)
        answered_question.append(current_question)
    else:
        continue

    if current_question == 'What is the capital city of Afghanistan?':
        answer = input()
        if answer == 'Kabul':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Albania?':
        answer = input()
        if answer == 'Tirana':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Austria?':
        answer = input()
        if answer == 'Vienna':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Belgium?':
        answer = input()
        if answer == 'Brussels':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Brazil?':
        answer = input()
        if answer == 'Brasilia':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Bulgaria?':
        answer = input()
        if answer == 'Sofia':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of China?':
        answer = input()
        if answer == 'Beijing':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Colombia?':
        answer = input()
        if answer == 'Bogota':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Croatia?':
        answer = input()
        if answer == 'Zagreb':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Denmark?':
        answer = input()
        if answer == 'Copenhagen':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Egypt?':
        answer = input()
        if answer == 'Cairo':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Ecuador?':
        answer = input()
        if answer == 'Quito':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Estonia?':
        answer = input()
        if answer == 'Tallinn':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of France?':
        answer = input()
        if answer == 'Paris':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Finland?':
        answer = input()
        if answer == 'Helsinki':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Germany?':
        answer = input()
        if answer == 'Berlin':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Greece?':
        answer = input()
        if answer == 'Athens':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Hungary?':
        answer = input()
        if answer == 'Budapest':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of India?':
        answer = input()
        if answer == 'New Delhi':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Italy?':
        answer = input()
        if answer == 'Rome':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Japan?':
        answer = input()
        if answer == 'Tokyo':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of South Korea?':
        answer = input()
        if answer == 'Seoul':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Lebanon?':
        answer = input()
        if answer == 'Beirut':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Luxembourg?':
        answer = input()
        if answer == 'Luxembourg':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Monaco?':
        answer = input()
        if answer == 'Monaco':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Morocco?':
        answer = input()
        if answer == 'Rabat':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of the Netherlands?':
        answer = input()
        if answer == 'Amsterdam':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Norway?':
        answer = input()
        if answer == 'Oslo':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Poland?':
        answer = input()
        if answer == 'Warsaw':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Portugal?':
        answer = input()
        if answer == 'Lisbon':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Spain?':
        answer = input()
        if answer == 'Madrid':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Switzerland?':
        answer = input()
        if answer == 'Bern':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Sweden?':
        answer = input()
        if answer == 'Stockholm':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    elif current_question == 'What is the capital city of Turkey?':
        answer = input()
        if answer == 'Ankara':
            answered_counter += 1
            print('Correct')
        else:
            failed_counter += 1
            print('Incorrect')
    if answered_counter + failed_counter == 34:
        break
if answered_counter == 34:
    print('You are an expert!')
elif 24 < answered_counter < 34:
    print(f'Good enough! {answered_counter} / 34')
elif 14 < answered_counter <= 24:
    print(f'You have to study a lot more! {answered_counter} / 34')
else:
    print(f'You lose! {answered_counter} / 34')
    
