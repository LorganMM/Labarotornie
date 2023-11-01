points = {'Иванов': 20, 'Сидоров': 68, 'Петров': 28, 'Смирнов': 68}

# Добавление своих данных в словарь
points['Милов'] = 100
# Поиск минимального кол-ва баллов
minimal_points = min(points.values())
name_for_minp = [x for x in points if points.get(x) == minimal_points]
# Поиск максимального кол-ва баллов
maximal_points = max(points.values())
name_for_maxp = [x for x in points if points.get(x) == maximal_points]
# Поиск среднего кол-ва баллов
mid_points = sum(points.values()) / len(points)
# Поиск участников у кого балл выше среднего
above_average = [x for x in points if points.get(x) > mid_points]

print(name_for_minp, "- баллов: ", minimal_points)
print(name_for_maxp, "- баллов: ", maximal_points)
print("Средний балл: ",mid_points)
print("Участники у кого балл выше средрего: ",above_average)