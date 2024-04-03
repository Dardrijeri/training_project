'''{
    "model": "tasks.task",
    "pk": 1,
    "fields": {
        "name": "Test",
        "completion": 0,
        "description": "This is test task",
        "date_start": "2024-04-03T00:00:00Z",
        "date_end": "2024-04-04T00:00:00Z",
        "supervisor": "Ivanov",
        "executor": "Petrov",
        "parent": null,
        "lft": 1,
        "rght": 8,
        "tree_id": 1,
        "level": 0
    }
},
{
    "model": "tasks.task",
    "pk": 2,
    "fields": {
        "name": "Test2",
        "completion": 10,
        "description": "This is second test task",
        "date_start": "2024-10-01T00:00:00Z",
        "date_end": "2024-11-29T00:00:00Z",
        "supervisor": "Sidorov",
        "executor": "Petrov",
        "parent": null,
        "lft": 1,
        "rght": 4,
        "tree_id": 2,
        "level": 0
    }
},
{
    "model": "tasks.task",
    "pk": 3,
    "fields": {
        "name": "SubTestTask",
        "completion": 45,
        "description": "This is test subtask",
        "date_start": "2022-04-03T00:00:00Z",
        "date_end": "2023-04-04T00:00:00Z",
        "supervisor": "Ivanov",
        "executor": "Sidorov",
        "parent": 1,
        "lft": 2,
        "rght": 5,
        "tree_id": 1,
        "level": 1
    }
},
{
    "model": "tasks.task",
    "pk": 4,
    "fields": {
        "name": "SubTestTask2",
        "completion": 99,
        "description": "This is test second subtask",
        "date_start": "2024-06-06T00:00:00Z",
        "date_end": "2024-07-07T00:00:00Z",
        "supervisor": "Ivanov",
        "executor": "Ivanov",
        "parent": 1,
        "lft": 6,
        "rght": 7,
        "tree_id": 1,
        "level": 1
    }
},
{
    "model": "tasks.task",
    "pk": 5,
    "fields": {
        "name": "SubTest2Task",
        "completion": 100,
        "description": "This is test2 subtask",
        "date_start": "2024-12-01T00:00:00Z",
        "date_end": "2025-01-20T00:00:00Z",
        "supervisor": "Petrov",
        "executor": "Petrov",
        "parent": 2,
        "lft": 2,
        "rght": 3,
        "tree_id": 2,
        "level": 1
    }
},
{
    "model": "tasks.task",
    "pk": 6,
    "fields": {
        "name": "Test3",
        "completion": 50,
        "description": "This is third test task",
        "date_start": "2020-01-01T00:00:00Z",
        "date_end": "2030-12-12T00:00:00Z",
        "supervisor": "Ivanov",
        "executor": "Petrov",
        "parent": null,
        "lft": 1,
        "rght": 2,
        "tree_id": 3,
        "level": 0
    }
},
{
    "model": "tasks.task",
    "pk": 8,
    "fields": {
        "name": "SubSubTestTask",
        "completion": 0,
        "description": "This is subsubtask",
        "date_start": "2024-01-01T00:00:00Z",
        "date_end": "2024-03-03T00:00:00Z",
        "supervisor": "Ivanov",
        "executor": "Sidorov",
        "parent": 3,
        "lft": 3,
        "rght": 4,
        "tree_id": 1,
        "level": 2
    }
}
'''
import json
from datetime import datetime
from random import randint, choice


def random_change(a, b, change_parent):
    names = ['Кузнецов Давид', 'Клюев Глеб', 'Медведев Даниил', 'Иванов Максим', 'Васильев Михаил', 'Пастухов Евгений',
             'Денисов Глеб', 'Васильева Ксения', 'Суслов Никита', 'Мещеряков Матвей', 'Рожков Марк', 'Кузнецов Савелий',
             'Зубов Данила', 'Шевцова Варвара', 'Попова Надежда', 'Андреев Марк', 'Зимин Даниил', 'Харитонова Софья',
             'Кулаков Антон', 'Сомов Эрик']

    tasks = [
        "Подготовить отчет для руководства", "Провести собрание с клиентом", "Обновить документацию проекта",
        "Закончить разработку нового функционала", "Отправить приглашения на мероприятие",
        "Проверить результаты тестирования", "Составить план маркетинговых мероприятий",
        "Организовать обучающий семинар для сотрудников", "Разработать стратегию продвижения продукта",
        "Планировать бюджет на следующий квартал", "Подготовить материалы для презентации проекта",
        "Собрать обратную связь от пользователей", "Провести анализ конкурентов", "Обновить внутренний портал компании",
        "Закончить подготовку к выставке", "Отправить отчеты по выполненным задачам",
        "Провести техническое совещание с разработчиками", "Подготовить релиз новой версии продукта",
        "Проверить обновления безопасности", "Организовать тимбилдинг для команды"
    ]

    descriptions = [
        "Подготовить детальный отчет о текущем прогрессе проекта, включая информацию о выполненных задачах, проблемах и планах на будущее.",
        "Организовать встречу с ключевым клиентом для обсуждения и уточнения требований к продукту или услуге.",
        "Обновить базу данных клиентов, включая добавление новых записей и обновление существующих контактных данных.",
        "Провести глубокий анализ текущего рынка с целью выявления новых возможностей для роста бизнеса.",
        "Создать прототип новой функциональности, демонстрирующий основные особенности и возможности продукта.",
        "Написать подробную документацию, объясняющую пользователю, как использовать новый инструмент или функцию.",
        "Организовать фокус-группу или опрос пользователей для сбора обратной связи о продукте или услуге.",
        "Провести тестирование на нагрузку, чтобы оценить производительность и надежность системы при максимальной нагрузке.",
        "Подготовить материалы и план для внутреннего семинара или тренинга по обучению сотрудников.",
        "Запустить рекламную кампанию в Интернете с использованием новых баннеров и рекламных текстов для привлечения новых клиентов."
    ]

    dates = ["2024-07-15T08:30:00", "2024-09-02T14:45:00", "2024-11-21T10:20:00", "2025-03-08T18:55:00",
             "2025-01-12T09:10:00", "2024-05-28T13:25:00", "2024-10-03T16:40:00", "2024-12-17T11:05:00",
             "2024-04-19T20:15:00", "2025-02-23T22:50:00"]

    if change_parent:
        fields['parent'] = randint(a, b)
    fields['name'] = choice(tasks)
    fields['description'] = choice(descriptions)
    fields['date_start'] = choice(dates)
    fields['date_end'] = choice(dates)
    fields['supervisor'] = choice(names)
    fields['executor'] = choice(names)
    fields['completion'] = randint(1, 100)


if __name__ == '__main__':
    with open('./tasks/fixtures/tasks.json', 'w') as file:
        model = 'tasks.task'
        pk = 1
        fields = {
            'name': '123',
            'completion': 0,
            'description': '123',
            'date_start': "2024-01-01T00:00:00Z",
            'date_end': "2024-03-03T00:00:00Z",
            'supervisor': '123',
            'executor': '123',
            'parent': None,
            'lft': 0,
            'rght': 0,
            'tree_id': 0,
            'level': 0,
        }
        file.write('[')
        for i in range(100):
            random_change(0, 0, False)
            file.write(json.JSONEncoder().encode({'model': model, 'pk': pk, 'fields': fields}) + ', ')
            pk += 1
        for i in range(100):
            random_change(1, 100, True)
            file.write(json.JSONEncoder().encode({'model': model, 'pk': pk, 'fields': fields}) + ', ')
            pk += 1
        for i in range(100):
            random_change(101, 200, True)
            file.write(json.JSONEncoder().encode({'model': model, 'pk': pk, 'fields': fields}) + ', ')
            pk += 1
        for i in range(100):
            random_change(201, 300, True)
            file.write(json.JSONEncoder().encode({'model': model, 'pk': pk, 'fields': fields}) + ', ')
            pk += 1
        for i in range(100):
            random_change(301, 400, True)
            file.write(json.JSONEncoder().encode({'model': model, 'pk': pk, 'fields': fields}) + ', ')
            pk += 1
        file.write(json.JSONEncoder().encode({'model': model, 'pk': pk, 'fields': fields}))
        file.write(']')
