import pyautogui as pg


def Open_rws1():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\icon_RWS_39centura.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.doubleClick()
            break
        pg.sleep(0.1)


def open_register():
    while True:
        window = pg.locateOnScreen('Screen\\registerCCentuara\\register_win_centura.png', confidence=0.8)
        if window:
            login = pg.locateOnScreen('Screen\\registerCCentuara\\login.png', confidence=0.8)
            pg.moveTo(login)
            pg.click()
            pg.write('NAST')
            password = pg.locateOnScreen('Screen\\registerCCentuara\\password.png', confidence=0.8)
            pg.moveTo(password)
            pg.click()
            pg.write('211212')
            password = pg.locateOnScreen('Screen\\registerCCentuara\\register_ok.png', confidence=0.8)
            pg.moveTo(password)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws2():
    while True:
        icon_1 = pg.locateOnScreen('Screen\\registerCCentuara\\1.png', confidence=0.8)
        if icon_1:
            pg.moveTo(icon_1)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws3():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\2.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws4():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\3.png', confidence=0.8)
        if icon:
            pg.sleep(0.1)
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws5():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\4.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws6():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\5.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws7():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\6.png', confidence=0.8)
        if icon:
            pg.moveTo(icon)
            pg.click()
            break
        pg.sleep(0.1)


def Open_rws8():
    while True:
        icon = pg.locateOnScreen('Screen\\registerCCentuara\\7.png', confidence=0.8)
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