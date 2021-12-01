from prettytable import PrettyTable

from data import dt

x = PrettyTable()

x.field_names = ['Банк', 'курс на 1.10($)', 'курс на 1.11($)', 'курс на 1.12($)',
                 'курс на 1.10(ФРН)', 'курс на 1.11(ФРН)', 'курс на 1.12(ФРН)', 'Рік']

for i in range (0, len(dt)):

    x.add_rows(
    [
        dt[i]
    ]
    )

def opentabble():
    print('\nАНАЛІЗ ЗМІНИ КУРСУ')
    print(x)