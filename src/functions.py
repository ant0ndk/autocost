import os
import webbrowser

from PIL import Image, ImageDraw, ImageFont


class Dialog():
    def logo():
        print('----------------------------------')
        print('| ▄▀█ █░█ ▀█▀ █▀█ █▀▀ █▀█ █▀ ▀█▀ |')
        print('| █▀█ █▄█ ░█░ █▄█ █▄▄ █▄█ ▄█ ░█░ |')
        print('----------------------------------')
        print('| Калькулятор расчета стоимости  |')
        print('|      владения автомобилем      |')
        print('----------------------------------')

    def help():
        print('Тут вы можете посмотреть список всех доступных команд:')
        print('/help  - помощь')
        print('/autocost  - рассчитать стоимость владения автомобилем')
        print('/clear - очистить консоль')
        print('/donate - пожертовать на разработку новых приложений')
        print('/exit - выйти')

    def clear():
        os.system("cls")
        Dialog.logo()
        print()
        print('Введите команду (для просмотра всех команд наберите \'/help\')')

    def donate():
        webbrowser.open_new_tab('qiwi.com/n/MODYL068')

    def autocost():
        os.system("cls")
        Dialog.logo()
        print()
        print('Давайте посчитаем стоимоть владения автомобилем в год.')
        print('Введите данные, актуальные для вашего автомобиля.')
        print('С учетом нестабильной ситуации на рынке программа не считает')
        print('потерю в цене автомобиля за год.')
        name = input('Марка: ')
        price = int(input('Стоимость: '))
        hp = int(input('Мощность двигателя: '))
        if hp < 100:
            nalog = 2.5 * hp
        elif hp < 150:
            nalog = 3.5 * hp
        elif hp < 200:
            nalog = 5 * hp
        elif hp < 250:
            nalog = 7.5 * hp
        else:
            nalog = 15 * hp
        lost_cash = price*0.05
        credit_sum = float(input('Сумма кредита: '))
        credit_date = float(input('Срок кредита(в годах): '))
        credit_pc = float(input('Процент по кредиту: '))
        if credit_date != 0:
            credit_year = float((credit_sum / credit_date) * (credit_pc / 100))
        else:
            credit_year = 0
        wash_cost = float(input('Стоимость 1 мойки автомобиля: '))
        wash_cost = wash_cost * 24
        odo = float(input('Пробег в год: '))
        fuel = float(input('Цена литра топлива: '))
        rashod = float(input('Расход топлива (л/100км): '))
        fuel_year = (rashod / 100) * odo * fuel
        strahovanie = float(input('Стоимость страховки на год: '))
        shinka = float(input('Стоимость 1 шиномонтажа: ')) * 2
        parking = float(input('Стоимость парковки в день: ')) * 20 * 12
        arenda = float(input('Стоимость аренды машиноместа/гаража: '))
        to = float(input('Стоимость 1 Тех. Обсуживания: '))
        dop_cost = float(input('Дополнительные расходы(в год): '))
        itog = nalog + lost_cash + credit_year + wash_cost + strahovanie
        itog += shinka + parking + arenda + to + dop_cost + fuel_year
        km_cost = itog / odo
        image = Image.open("example-1.jpg")
        image = image.convert('RGB')
        font = ImageFont.truetype("times.ttf", 26)
        drawer = ImageDraw.Draw(image)
        drawer.text((900, 482),
                    name,
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 528),
                    str(price),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 574),
                    str(hp),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 620),
                    str(nalog),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 666),
                    str(lost_cash),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 712),
                    str(credit_year),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 758),
                    str(wash_cost),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 804),
                    str(fuel_year),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 850),
                    str(strahovanie),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 896),
                    str(shinka),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 942),
                    str(parking),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 988),
                    str(arenda),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 1034),
                    str(to),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 1080),
                    str(dop_cost),
                    (0, 0, 0),
                    font=font)
        drawer.text((900, 1126),
                    str(itog),
                    (255, 0, 0),
                    font=font)
        drawer.text((900, 1172),
                    str(km_cost),
                    (0, 0, 255),
                    font=font)
        print('---')
        print('Отчет будет сохранен в формате PDF.')
        report_name = str(input('Пожалуйста, введите название(без формата): '))
        report_name = report_name + '.pdf'
        image.save(report_name)
        print('--- ОТЧЕТ УСПЕШНО СФОРМИРОВАН ---')
