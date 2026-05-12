'''
#chapter 10 Reading and Writing Files
from pathlib import Path
import os

print(Path('spam') / 'bacon' / 'eggs')
Path('spam') / Path('bacon/eggs')
Path('spam') / Path('bacon', 'eggs')
#both is valid

print(Path.home())

import shelve
'''

import random

# 1. 定义测验题库：美国50个州 -> 对应首府（核心数据，可自定义替换）
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

quiz_num=35
for num in range(quiz_num):
    quiz_file=open(f'quiz_{num}.txt','w',encoding='utf-8')
    answer_file=open(f'answer_{num}.txt','w',encoding='utf-8')

    quiz_file.write("Name:\n\nDate:\n\nClass:\n\n")
    quiz_file.write((' '*20) + f'State Capital Quiz {num}\n\n')

    states=list(capitals.keys())
    random.shuffle(states)

    for qnum in range(quiz_num):
        correct_answer=capitals[states[qnum]]
        wrong_answer=list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer=random.sample(wrong_answer,3)
        answer_option=[correct_answer] + wrong_answer
        random.shuffle(answer_option)

        quiz_file.write(f'{num}. What is the capital of {states[qnum]}?\n')
        for i in range(4):
            quiz_file.write(f"{'ABCD'[i]}. {answer_option[i]}\n")
        quiz_file.write('\n')

        answer_file.write(f"{qnum + 1}. {'ABCD'[answer_option.index(correct_answer)]}\n")

    quiz_file.close()
    answer_file.close()