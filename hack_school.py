from django.db import models
from datacenter.models import (Chastisement, Commendation, Lesson, Mark, Schoolkid, Subject)


def name_check():
    child = input("Введите ФИО ученика: ")
    try:
        child_name = Schoolkid.objects.get(full_name__contains=child)
        print(child_name)
        return child_name
    except Schoolkid.DoesNotExist:
        print("Такого ученика нет")
    except Schoolkid.MultipleObjectsReturned:
        print('Или ничего не ввели или много совпадений, уточните имя')


def fix_marks():
    bad_points = Mark.objects.filter(schoolkid=name_check(), points__in=[2, 3])
    for bed_point in bad_points:
        bed_point.points = 5
        bed_point.save()


def remove_chastisements():
    teacher_texts=Chastisement.objects.filter(schoolkid=name_check())
    for teacher_text in teacher_texts:
        teacher_text.delete()


def create_commendation():
    schoolkid = name_check()
    target_lesson = input("Введите предмет: ")
    hack_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter[0], subject__title=target_lesson)[0]
    Commendation.objects.create(text='Молодец!', created=hack_lesson.date, schoolkid=schoolkid, subject =hack_lesson.subject, teacher=hack_lesson.teacher)