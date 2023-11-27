"Вариант 4"
import math

print('Всего вариантов заполнения вакантных мест:')
a1 = int(math.factorial(16) / (math.factorial(14) * math.factorial(2)))
a2 = int(math.factorial(14) / (math.factorial(12) * math.factorial(2)))
a3 = int(math.factorial(12) / (math.factorial(9) * math.factorial(3)))
a4 = int(math.factorial(9) / (math.factorial(6) * math.factorial(3)))
a5 = int(math.factorial(6) / (math.factorial(2) * math.factorial(4)))
print('Варианты тимлидов', a1)
print('Варианты проджек-менеджеров', a2)
print('Варианты синьёров', a3)
print('Варианты мидлов', a4)
print('Варианты юниоров', a5)
print('Общее колличество вариантов', (math.factorial(16) / math.factorial(2)))


class Window:
    def sort_key(self, vacan):# Возвращает кортеж из двух значений: суммы опыта работы сотрудников на занимаемой должности и
                                   # суммарной стоимости найма сотрудников на вакансии
        return (vacan[2], vacan[1])
    def __init__(self, skill1, skill2, skill3, skill4, skill5, budget):
        good_sotr1 = []
        good_sotr2 = []
        good_sotr3 = []
        good_sotr4 = []
        good_sotr5 = []
        for i in range(15):  # генерация тимлидов
            for j in range(i + 1, 15):
                for k in range(j + 1, 15):
                    for l in range(k + 1, 15):
                        sotr1 = [rabotniks[i], rabotniks[j]]
                        skill_sum = sum([min_opyt_rab[rabotnik] for rabotnik in sotr1])
                        cost = sum([costs_dict[min_opyt_rab[rabotnik]] for rabotnik in sotr1])
                        sotr2 = [rabotniks[i], rabotniks[j], rabotniks[k]]
                        skill_sum1 = sum([min_opyt_rab[rabotnik] for rabotnik in sotr2])
                        cost = sum([costs_dict[min_opyt_rab[rabotnik]] for rabotnik in sotr2])
                        sotr3 = [rabotniks[i], rabotniks[j], rabotniks[k], rabotniks[l]]
                        skill_sum2 = sum([min_opyt_rab[rabotnik] for rabotnik in sotr3])
                        cost = sum([costs_dict[min_opyt_rab[rabotnik]] for rabotnik in sotr3])
                        if (skill_sum >= 2 * skill1 and cost <= budget):
                            good_sotr1.append((sotr1, cost, skill_sum))
                        if (skill_sum >= 2 * skill2 and cost <= budget):
                            good_sotr2.append((sotr1, cost, skill_sum))
                        if (skill_sum1 >= 3 * skill3 and cost <= budget):
                            good_sotr3.append((sotr2, cost, skill_sum1))
                        if (skill_sum1 >= 3 * skill4 and cost <= budget):
                            good_sotr4.append((sotr2, cost, skill_sum1))
                        if (skill_sum2 >= 4 * skill5 and cost <= budget):
                            good_sotr5.append((sotr3, cost, skill_sum2))
        if good_sotr1:
            good_sotr1.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr1[0][0])
            total_skill = good_sotr1[0][2]
            total_cost = good_sotr1[0][1]
            print(
                f'Мы нашли {len(good_sotr1)} подходящих комбинаций сотрудников тимлидеров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr2:
            good_sotr2.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr2[0][0])
            total_skill = good_sotr2[0][2]
            total_cost = good_sotr2[0][1]
            print(
                f'Мы нашли {len(good_sotr2)} подходящих комбинаций сотрудников проджек-менеджеров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr3:
            good_sotr3.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr3[0][0])
            total_skill = good_sotr3[0][2]
            total_cost = good_sotr3[0][1]
            print(
                f'Мы нашли {len(good_sotr3)} подходящих комбинаций сотрудников синьёров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr4:
            good_sotr4.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr4[0][0])
            total_skill = good_sotr4[0][2]
            total_cost = good_sotr4[0][1]
            print(
                f'Мы нашли {len(good_sotr4)} подходящих комбинаций сотрудников мидлов, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr5:
            good_sotr5.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr5[0][0])
            total_skill = good_sotr5[0][2]
            total_cost = good_sotr5[0][1]
            print(
                f'Мы нашли {len(good_sotr5)} подходящих комбинаций сотрудников юниоров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
            bol = int(input("Нужны все варианты? (да - введите 1, нет - введите 0): "))
            while (bol > 1):
                bol = int(input("да - введите 1, нет - введите 0: "))
            if bol == 1:
                print(
                    f"Список остальных комбинаций вакансий в которых сумма умений больше минимального уровня (был задан {skill1}):")
                for i, trio in enumerate(good_sotr1, start=1):
                    print(
                        f"{i}. {' - '.join(trio[0])}. Общая стоимость: {trio[1]} рублей, " f"сумма умений: {trio[2]} баллов.\n")
                for i, trio in enumerate(good_sotr2, start=1):
                    print(
                        f"{i}. {' - '.join(trio[0])}. Общая стоимость: {trio[1]} рублей, " f"сумма умений: {trio[2]} баллов.\n")
                for i, trio in enumerate(good_sotr3, start=1):
                    print(
                        f"{i}. {' - '.join(trio[0])}. Общая стоимость: {trio[1]} рублей, " f"сумма умений: {trio[2]} баллов.\n")
                for i, trio in enumerate(good_sotr4, start=1):
                    print(
                        f"{i}. {' - '.join(trio[0])}. Общая стоимость: {trio[1]} рублей, " f"сумма умений: {trio[2]} баллов.\n")
                for i, trio in enumerate(good_sotr5, start=1):
                    print(
                        f"{i}. {' - '.join(trio[0])}. Общая стоимость: {trio[1]} рублей, " f"сумма умений: {trio[2]} баллов.\n")
            if bol == 0:
                print("Спасибо за использование программы!")
        else:
            print('К сожалению, нам не удалось найти комбинацию, которая удовлетворяет вашим требованиям.')
        print('\nРабота программы завершена.\n')


rabotniks = ["Артём", "Игорь", "Лев", "Александр", "Дмитрий", "Варвара", "Антонина", "Полина", "Арина", "Павел",
                 "Татьяна", "София", "Елизовета", "Константин", "Максим", "Иван"]
    # Задаём опыт работы каждого сотрудника
min_opyt_rab = {"Артём": 0, "Игорь": 1, "Лев": 2, "Александр": 3, "Дмитрий": 4, "Варвара": 5, "Антонина": 6,
                    "Полина": 7, "Арина": 8, "Павел": 9, "Татьяна": 10,
                    "София": 11, "Елизовета": 12, "Константин": 13, "Максим": 14, "Иван": 15}
costs_dict = {0: 1000, 1: 2000, 2: 3000, 3: 4000, 4: 5000, 5: 5500, 6: 5600, 7: 5700, 8: 5800, 9: 5900, 10: 6400,
                  11: 6600, 12: 6650, 13: 6700, 14: 6750, 15: 7000}

print('\nНайдём лучший вариант для компании с ограниченным бюджетом')
print('\nВведите минимальный опыт работы для каждой специальности (от 0 до 15)\n')
skill1 = int(input('тимлид:\n'))
skill2 = int(input('проджек-менеджер:\n'))
skill3 = int(input('синьер:\n'))
skill4 = int(input('мидл:\n'))
skill5 = int(input('юниор:\n'))
while (skill1 < 0 or skill1 > 15) or (skill2 < 0 or skill2 > 15) or (skill3 < 0 or skill3 > 15) or (skill4 < 0 or skill4 > 15) or (skill5 < 0 or skill5 > 15):
    print('\nВведите минимальный опыт работы для каждой специальности (от 0 до 15)\n')
    skill1 = int(input('тимлид:\n'))
    skill2 = int(input('проджек-менеджер:\n'))
    skill3 = int(input('синьер:\n'))
    skill4 = int(input('мидл:\n'))
    skill5 = int(input('юниор:\n'))
budget = int(input('\nВведите максимальный бюджет для найма сотрудников в компанию (начиная от 10000 рублей): '))
while budget < 10000:
    budget = int(input('\nВведите максимальный бюджет для найма сотрудников в компанию (начиная от 10000 рублей):\n'))

hh = Window(skill1, skill2, skill3, skill4, skill5, budget)
