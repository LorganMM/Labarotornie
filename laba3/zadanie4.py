from datetime import datetime, timedelta

try:
    print('Введите дату рождения в формате ДД/ММ/ГГ')
    hb_date = datetime.strptime(input(), "%d/%m/%y")
except ValueError:
    print("Неверный формат")
    exit()

days = 10000
minutes = 1000000
seconds = 100000000

pr_days = timedelta(days=days)
pr_minutes = timedelta(minutes=minutes)
pr_seconds = timedelta(seconds=seconds)

hb_days = hb_date + pr_days
hb_minutes = hb_date + pr_minutes
hb_seconds = hb_date + pr_seconds

print("10.000 дней будет: ", hb_days)
print("1.000.000 минут будет: ", hb_minutes)
print("1.000.000.000 секунд будет: ", hb_seconds)