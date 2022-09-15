import pyautogui as pg


def Open_rws1():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\icon_RWS_38#.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.doubleClick()
            break
        pg.sleep(0.1)


def open_register():
    while True:
        window = pg.locateOnScreen('Screen\\registerC#\\register_win#.png', confidence=0.8)
        if window:
            login = pg.locateOnScreen('Screen\\registerC#\\login.png', confidence=0.8)
            pg.moveTo(login)
            pg.click()
            pg.write('NAST')
            password = pg.locateOnScreen('Screen\\registerC#\\password.png', confidence=0.8)
            pg.moveTo(password)
            pg.click()
            pg.write('NAST')
            password = pg.locateOnScreen('Screen\\registerC#\\register_ok.png', confidence=0.8)
            pg.moveTo(password)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws2():
    while True:
        icon_1 = pg.locateOnScreen('Screen\\registerC#\\1.png', confidence=0.8)
        if icon_1:
            pg.moveTo(icon_1)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws3():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\2.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.sleep(0.2)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws4():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\3.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.sleep(0.2)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws5():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\4.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.sleep(0.2)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws6():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\5.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.sleep(0.2)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws7():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\6.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws8():
    while True:
        icon = pg.locateOnScreen('Screen\\registerC#\\7.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


Open_rws1()
open_register()
Open_rws2()
Open_rws3()
Open_rws4()
Open_rws5()
Open_rws6()
Open_rws7()
Open_rws8()
