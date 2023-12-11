from tkinter import *
import tkinter as tk
from tkinter import ttk

class Window():
    rabotniks = ["Артём", "Игорь", "Лев", "Александр", "Дмитрий", "Варвара", "Антонина", "Полина", "Арина", "Павел",
                 "Татьяна", "София", "Елизовета", "Константин", "Максим", "Иван"]
    # Задаём опыт работы каждого сотрудника
    min_opyt_rab = {"Артём": 4, "Игорь": 15, "Лев": 2, "Александр": 0, "Дмитрий": 10, "Варвара": 14, "Антонина": 5,
                    "Полина": 8, "Арина": 11, "Павел": 6, "Татьяна": 3,
                    "София": 7, "Елизовета": 9, "Константин": 1, "Максим": 11, "Иван": 13}
    costs_dict = {0: 0, 1: 2000, 2: 3000, 3: 4000, 4: 5000, 5: 5500, 6: 5600, 7: 5700, 8: 5800, 9: 5900, 10: 6400,
                  11: 6600, 12: 6650, 13: 6700, 14: 6750,
                  15: 7000}  # Задаем цены на найм сотрудников в зависимости от их опыта работы

    def __init__(self, width, height, title="Вакансии"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+450+70")
        self.Zarp = Entry(self.root)
        self.Ot = Entry(self.root)
        self.Opm = Entry(self.root)
        self.Os = Entry(self.root)
        self.Om = Entry(self.root)
        self.Ou = Entry(self.root)
    def run(self):
        self.win()
        self.root.mainloop()

    def win(self):
        Label(self.root, text="Зарплата:", justify=LEFT).pack(ipady=5, padx=5, pady=1)
        self.Zarp.pack(ipady=5, padx=5, pady=1)

        Label(self.root, text="Опыт работы тимлидов:", justify=LEFT).pack(ipady=5, padx=5, pady=1)
        self.Ot.pack(ipady=5, padx=5, pady=1)
        Label(self.root, text="Опыт работы проджек-менеджеров:", justify=LEFT).pack(ipady=5, padx=5, pady=1)
        self.Opm.pack(ipady=5, padx=5, pady=1)
        Label(self.root, text="Опыт работы синьёров:", justify=LEFT).pack(ipady=5, padx=5, pady=1)
        self.Os.pack(ipady=5, padx=5, pady=1)
        Label(self.root, text="Опыт работы мидлов:", justify=LEFT).pack(ipady=5, padx=5, pady=1)
        self.Om.pack(ipady=5, padx=5, pady=1)
        Label(self.root, text="Опыт работы юниоров:", justify=LEFT).pack(ipady=5, padx=5, pady=1)
        self.Ou.pack(ipady=5, padx=5, pady=1)


        Button(self.root, text="Подобрать", width=15, command=self.raschet).pack(ipady=5, padx=5, pady=1)

        """"Окно вывода!"""
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(anchor='n', padx=8, pady=8)

        self.scrollbar = ttk.Scrollbar(self.text_frame)
        self.output_text = tk.Text(self.text_frame, width=60, height=40, yscrollcommand=self.scrollbar.set,
                                   font='Arial 12')
        self.scrollbar.config(command=self.output_text.yview)

        self.output_text.pack(side=tk.LEFT, padx=0, pady=0)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=0, pady=0)
    def raschet(self):
        output_text = self.output_text
        rabotniks = self.rabotniks
        min_opyt_rab = self.min_opyt_rab
        costs_dict = self.costs_dict
        skill1 = int(self.Ot.get())
        skill2 = int(self.Opm.get())
        skill3 = int(self.Os.get())
        skill4 = int(self.Om.get())
        skill5 = int(self.Ou.get())
        budget = int(self.Zarp.get())
        while (skill1 < 0 or skill1 > 15) or (skill2 < 0 or skill2 > 15) or (skill3 < 0 or skill3 > 15) or (
                skill4 < 0 or skill4 > 15) or (skill5 < 0 or skill5 > 15):
            output_text.insert(tk.END, '\nВведите минимальный опыт работы для каждой специальности (от 0 до 15)\n')
            return
        while budget < 10000:
            output_text.insert(tk.END,'\nВведите максимальный бюджет для найма сотрудников в компанию (начиная от 10000 рублей):\n')
            return

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
            output_text.insert(tk.END,f'\nМы нашли {len(good_sotr1)} подходящих комбинаций сотрудников тимлидеров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr2:
            good_sotr2.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr2[0][0])
            total_skill = good_sotr2[0][2]
            total_cost = good_sotr2[0][1]
            output_text.insert(tk.END, f'\nМы нашли {len(good_sotr2)} подходящих комбинаций сотрудников проджек-менеджеров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr3:
            good_sotr3.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr3[0][0])
            total_skill = good_sotr3[0][2]
            total_cost = good_sotr3[0][1]
            output_text.insert(tk.END, f'\nМы нашли {len(good_sotr3)} подходящих комбинаций сотрудников синьёров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr4:
            good_sotr4.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr4[0][0])
            total_skill = good_sotr4[0][2]
            total_cost = good_sotr4[0][1]
            output_text.insert(tk.END, f'\nМы нашли {len(good_sotr4)} подходящих комбинаций сотрудников мидлов, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        if good_sotr5:
            good_sotr5.sort(key=self.sort_key)  # сортировка по сумме умений и сумме цен
            best_trio = ' - '.join(good_sotr5[0][0])
            total_skill = good_sotr5[0][2]
            total_cost = good_sotr5[0][1]
            output_text.insert(tk.END, f'\nМы нашли {len(good_sotr5)} подходящих комбинаций сотрудников юниоров, ' f'которые удовлетворяют вашим требованиям.\n'
                f'Наиболее подходящей комбинацией является: {best_trio}.\n' f'Общая стоимость этой комбинации: {total_cost} рублей. \n'
                f'Общая сумма умений всех сотрудников в этой комбинации: {total_skill} баллов.\n')
        else:
            output_text.insert(tk.END, 'К сожалению, нам не удалось найти комбинацию, которая удовлетворяет вашим требованиям.')
        output_text.insert(tk.END, '\nРабота программы завершена.\n')
    def sort_key(self, vacan):
        return (vacan[2], vacan[1])

window = Window(600,700)
window.run()
