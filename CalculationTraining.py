# For training a calculation skill

import random
import time

print('\n\n-----------------------------------------')
print('    This is Calculation Traing     \n')
print('    If you are ready, press the enter key for starting   \n')

# Press the enter key to start
while True:
    key = input()

    if key == '':
        break

# Get the start time
start_time = time.time()

loop_num = 1
correct_num = 0
print('\nInput the answer\n')

# Finish when 10 times corrects
while True:
    if correct_num < 10:
        num1 = random.randrange(100)
        num2 = random.randrange(100)
        answer = num1 + num2

        # Create questions.
        question = 'Question' + str(loop_num) + '\n' + str(num1) + '+' +  str(num2) + '= ??'
        print(question + '\n')

        # Only number is allowed
        while True:
            input_answer = input()

            if input_answer and input_answer.isdigit():
                input_answer = int(input_answer)
                break
            
            print('Please, enter NUMBER!\n')

        if answer == input_answer:
            correct_num += 1
            print('              Correct!\n              ' + str(correct_num) + '/10\n')
        else:
            print('              Wrong,\n              the answer is ' + str(answer) + '\n              ' + str(correct_num) + '/10\n')

        loop_num += 1
    else:
        break

# Get the test time by subtracting the start time
test_time = time.time() - start_time

# Print a Bye message
print('\nNow, you passed 10 times!\nIt took ' + str(test_time) + '.\n\nBye!')