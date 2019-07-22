# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/22 21:56'

student_count = int(input())
shiji_numbers = []
kaoshi_numbers = []
for i in range(student_count):
    exam_number, shiji_number, kaoshi_number = input().split()
    shiji_numbers.append(shiji_number)
    kaoshi_numbers.append([exam_number, kaoshi_number])
chidao_student_count = int(input())
for shiji_number in input().split():
    index = shiji_numbers.index(shiji_number)
    print(kaoshi_numbers[index][0], kaoshi_numbers[index][1])