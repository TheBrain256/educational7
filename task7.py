def calculate_average(Оценки, Ученики):
    averages = {}
    for i in range(len(Оценки)):
        total = sum(Оценки[i])
        average = total / len(Оценки[i])
        averages[list(Ученики)[i]] = average
    return averages

Оценки = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Ученики = {'Джонни', 'Бильбо', 'Стив', 'Гендрик', 'Аарон'}

averages = calculate_average(Оценки, Ученики)

for Ученики, average in averages.items():
    print(f'{Ученики}: {average}')