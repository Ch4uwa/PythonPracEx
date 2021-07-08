# quiz_game.py
import os
import json


def v_1():
    print('Welcome to my computer quiz!')

    playing = input('Do you want to play? (yes/no) ')
    playing = playing.lower()

    if playing != 'yes':
        quit()

    print("Okay! Let's play.")

    answer = input("What does CPU stand for? ")
    if answer == "central processing unit":
        print("Correct!")
    else:
        print("Wrong!")


def v_2():
    quiz = _handleFile()
    questions = quiz['question']
    answers = quiz['answer']
    score = 0

    for i in range(len(answers)):
        answer = input(f'{questions[i]} ').lower()
        if answer == answers[i]:
            print('Correct')
            score += 1
        else:
            print('Incorrect')
    
    print(f'Your score: {score}/4')


def _handleFile():
    # get json questions
    file = 'questions_answers.json'
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file))

    with open(file_path, 'r') as f:
        data = f.read()

    obj = json.loads(data)
    return obj['quiz']


def main():
    v_2()


if __name__ == '__main__':
    main()
