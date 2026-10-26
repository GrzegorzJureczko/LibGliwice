import random

from library import models

SAMPLE_BOOKS = [
    ('Pamiętniki Adama i Ewy', 'Mark Twain', 96),
    ('Limes inferior', 'Janusz Andrzej Zajdel', 288),
    ('Małe państwo wielkich nadziei', 'Barbara Grochulska', 320),
    ('Żona podróżnika w czasie', 'Audrey Niffenegger', 464),
    ('Autostopem przez galaktykę', 'Douglas Adams', 208),
    ('Zrozumieć Kod da Vinci', 'Amy Welborn', 176),
    ('Sto lat samotności', 'Gabriel García Márquez', 424),
    ('Z dala od zgiełku', 'Thomas Hardy', 448),
    ('Bubble gum', 'Lolita Pille', 160),
    ('Tajemna historia', 'Donna Tartt', 576),
    ('Shantaram', 'Gregory David Roberts', 800),
    ('Obudzić szczęście', 'Susan Wiggs', 384),
    ('Zakochana Emma', 'Emma Tennant', 288),
    ('Dziwne losy Adelki', 'Emma Tennant', 256),
]

STATUSES = ['dostępna', 'dostępna', 'Wypożyczona', 'niedostępna']


def random_availability():
    # random availability across existing libraries, in the format used by BooksAvailability
    availability = []
    for short_name in models.Libraries.objects.values_list('short_name', flat=True):
        status = random.choice(STATUSES)
        location = 'n/a' if status == 'niedostępna' else 'Wypożyczalnia'
        availability.append((short_name, location, status))
    return availability
