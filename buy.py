import pyautogui
import time
import keyboard


buy_x = 2367
buy_y = 243

all_x = 1523
all_y = 650


del_x = 1181
del_y = 86

find_x = 133
find_y = 160

first_x = 240   # нажатие на первое обьявление 
first_y = 220

#t = 0            # счетчик смены 
#d = 0            # счетчик выбора смены 

settings_x = 641  # нажатие на настройки
settings_y = 116

value_x = 865  # нажатие на валюту
value_y = 157

rub_x = 888   # нажатие на рубли 
rub_y = 235

amountRUB_x = 1078  # строка с ценой -- напечатать цену 
amountRUB_y = 201 

okset_x = 839  # нажатие на ок
okset_y = 578

warnOK_x = 1281
warnOK_y = 769

flea_x = 1659
flea_y = 1416

cost_round_pliers = 16000
cost_morphine_injector = 15000
cost_golden_rooster_figurine = 56000
cost_roler_submariner = 43000
cost_press_pass = 30500
cost_golden_edd = 41111


e = 5

def fast_buy():
    keyboard.send('f5')

    pyautogui.moveTo(buy_x, buy_y)
    pyautogui.click()
    pyautogui.moveTo(all_x, all_y)
    pyautogui.click()
    keyboard.send("y")
    pyautogui.moveTo(warnOK_x, warnOK_y)
    pyautogui.click()
    time.sleep(0.2)





def change_buy(t,d):


    pyautogui.moveTo(buy_x, buy_y)
    pyautogui.click()   
    pyautogui.moveTo(all_x, all_y)
    pyautogui.click()

    keyboard.send("y")

    keyboard.send('f5')


    pyautogui.moveTo(warnOK_x, warnOK_y)
    pyautogui.click()

    time.sleep(0.4)
    if t % e == 0:
        change(d)

    






def change(d):
    print(d)



    if t//e <= 1 :

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()


        keyboard.write("morphine injector")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('15555')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.2)




    elif t//e==2:

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()



        keyboard.write("round pliers")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('16666')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.3)



    elif t//e==3:

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()



        keyboard.write("rooster")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('56666')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.3)



    elif t//e==4:

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()



        keyboard.write("golden egg")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('42444')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.3)


    elif t//e==5:

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()



        keyboard.write("press pass")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('31111')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.3)




    elif t//e == 6:

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()



        keyboard.write("wooden clock")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('52222')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.3)


    elif t//e == 7 :

        pyautogui.moveTo(del_x, del_y)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(find_x, find_y)
        pyautogui.click()



        keyboard.write("red beard")

        time.sleep(2)
        pyautogui.moveTo(first_x, first_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(settings_x, settings_y)
        time.sleep(0.4)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(value_x, value_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(rub_x, rub_y)
        pyautogui.click()
        time.sleep(0.1)

        pyautogui.moveTo(amountRUB_x, amountRUB_y)
        pyautogui.click()
        time.sleep(0.1)
        keyboard.write('21111')
        time.sleep(0.1)

        pyautogui.moveTo(okset_x, okset_y)
        pyautogui.click()
        time.sleep(0.3)




def fast_change_buy(t,d):

    keyboard.send('f5')

    pyautogui.moveTo(buy_x, buy_y)
    pyautogui.click()   
    pyautogui.moveTo(all_x, all_y)
    pyautogui.click()

    keyboard.send("y")

    keyboard.send('f5')


    pyautogui.moveTo(warnOK_x, warnOK_y)
    pyautogui.click()

    time.sleep(0.4)
    if t % e == 0:
        change(d)




t = 0
d = 0




a = int(input('1-change\n2-fast\n3-fast_change ?\n'))
if a == 1:
    while True:
        keyboard.wait('f6')

        while keyboard.is_pressed('space') == False:

            t = t+1
            if t//e==8: 
                t = 1 
            change_buy(t,d)


elif a == 2:
    while True:
        keyboard.wait('f6')

        while keyboard.is_pressed('space') == False:
            fast_buy()


elif a == 3: 
    while True:
        keyboard.wait('f6')

        while keyboard.is_pressed('space') == False:

            t = t+1
            if t//e==3: 
                t = 1 
            fast_change_buy(t,d)
