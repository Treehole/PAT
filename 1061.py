# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/22 22:24'

student_count, question_count = input().split()
scores = input().split()
answers = input().split()
for i in range(int(student_count)):
    total = 0
    student_answers = input().split()
    for j in range(int(question_count)):
        if student_answers[j] == answers[j]:
            total += int(scores[j])
    print(total)