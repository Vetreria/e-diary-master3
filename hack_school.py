import random
from django.db import models
from datacenter.models import (Chastisement, Commendation, Lesson, Mark, Schoolkid, Subject)


def name_check():
    child = input("Введите ФИО ученика: ")
    try:
        child_name = Schoolkid.objects.get(full_name__contains=child)
        print(child_name)
        return child_name
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist("Такого ученика нет")
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned('Найдено несколько учеников, уточните ФИО')


def fix_marks():
    Mark.objects.filter(schoolkid=name_check(), points__in=[2, 3]).update(points = 5)


def remove_chastisements():
    Chastisement.objects.filter(schoolkid=name_check()).delete()


def create_commendation():
    schoolkid = name_check()
    comments=['Молодец!', 'Отлично!', 'превосходно', 'великолепно', 'блестяще', 'мастерски', 'добросовестно']
    target_lesson = input("Введите предмет: ")
    hack_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=target_lesson).order_by('?').first()
    Commendation.objects.create(text=random.choice(comments), created=hack_lesson.date, schoolkid=schoolkid, subject =hack_lesson.subject, teacher=hack_lesson.teacher)