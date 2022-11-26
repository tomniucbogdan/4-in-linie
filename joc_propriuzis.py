from turtle import *
from state import *
from random import randrange

ture = {'Red': 'Yellow', 'Yellow': 'Red'}
state = State()


def desenare_tabla(startx, starty):
    up()
    goto(startx, starty)
    fillcolor('#643D01')
    begin_fill()
    down()
    for i in range(2):
        forward(700)
        right(90)
        forward(600)
        right(90)
    end_fill()


def linii_verticale(startx, starty, endx, endy):
    up()
    goto(startx, starty)
    down()
    goto(endx, endy)


def linii_orizontale(startx, starty, endx, endy):
    up()
    goto(startx, starty)
    down()
    goto(endx, endy)


def grid():
    Screen().bgcolor("#020C53")
    # linii verticale
    for i in range(-350, 450, 100):
        linii_verticale(i, -300, i, 300)
    # linii orizontale
    for j in range(300, -400, -100):
        linii_orizontale(-350, j, 350, j)
    # cercuri placa
    for x in range(-300, 350, 100):
        for y in range(-250, 300, 100):
            up()
            goto(x, y)
            dot(100, 'white')


def orizontal(culori):
    for i in range(5, 0, -1):
        red = 0
        yellow = 0
        for j in range(7):
            if culori[i - 1][j] is None:
                red = 0
                yellow = 0
            else:
                if culori[i - 1][j] == 'Red':
                    red = red + 1
                    yellow = 0
                    if red >= 4:
                        return True
                else:
                    if culori[i - 1][j] == 'Yellow':
                        yellow = yellow + 1
                        red = 0
                        if yellow >= 4:
                            return True


def vertical(culori):
    for j in range(7):
        red = 0
        yellow = 0
        for i in range(6, 0, -1):
            if culori[i - 1][j] == 'Red':
                red = red + 1
                yellow = 0
                if red >= 4:
                    return True
            else:
                if culori[i - 1][j] == 'Yellow':
                    yellow = yellow + 1
                    red = 0
                    if yellow >= 4:
                        return True


def diagonalds(culori, count, slot):
    x = count
    y = slot
    red = 0
    yellow = 0
    for i in range(0, 6):
        if culori[x - i][y - i] == 'Red':
            red = red + 1
            yellow = 0
            if red >= 4:
                return True
        else:
            if culori[x - i][y - i] == 'Yellow':
                yellow = yellow + 1
                red = 0
                if yellow >= 4:
                    return True


def castigator(culori, count, slot):
    if orizontal(culori):
        return True
    if vertical(culori):
        return True
    if count >= 3:
        if diagonalds(culori, count, slot):
            return True


def player(x, y):
    cul = state.player
    sloturi = state.sloturi
    culori = state.culori
    slot = 0
    count = sloturi[slot]
    # coordonate x si y
    if -350 <= x <= -250:
        x = -300
        slot = 0
        count = sloturi[slot]
        y = count * 100 - 250
    else:
        if -250 <= x <= -150:
            x = -200
            slot = 1
            count = sloturi[slot]
            y = count * 100 - 250
        else:
            if -150 <= x <= -50:
                x = -100
                slot = 2
                count = sloturi[slot]
                y = count * 100 - 250
            else:
                if -50 <= x <= 50:
                    x = 0
                    slot = 3
                    count = sloturi[slot]
                    y = count * 100 - 250
                else:
                    if 50 <= x <= 150:
                        x = 100
                        slot = 4
                        count = sloturi[slot]
                        y = count * 100 - 250
                    else:
                        if 150 <= x <= 250:
                            x = 200
                            slot = 5
                            count = sloturi[slot]
                            y = count * 100 - 250
                        else:
                            if 250 <= x <= 350:
                                x = 300
                                slot = 6
                                count = sloturi[slot]
                                y = count * 100 - 250
                            else:
                                pass

    up()
    goto(x, y)
    dot(100, cul)
    culori[count][slot] = cul
    print(f"{count}, {slot}")
    if castigator(culori, count, slot):
        nr = int(textinput("Sfarsit joc", f"{cul} a castigat\n 1.Restart\n 2.Exit"))
        if nr == 1:
            restart()
        else:
            bye()
    sloturi[slot] = count + 1
    state.player = ture[cul]


def calculator(x, y):
    player = state.player
    sloturi = state.sloturi
    culori = state.culori
    slot = 0
    count = sloturi[slot]
    if player == 'Yellow':
        x = randrange(-290, 290)
    # coordonate x si y
    if -350 <= x <= -250:
        x = -300
        slot = 0
        count = sloturi[slot]
        y = count * 100 - 250
    else:
        if -250 <= x <= -150:
            x = -200
            slot = 1
            count = sloturi[slot]
            y = count * 100 - 250
        else:
            if -150 <= x <= -50:
                x = -100
                slot = 2
                count = sloturi[slot]
                y = count * 100 - 250
            else:
                if -50 <= x <= 50:
                    x = 0
                    slot = 3
                    count = sloturi[slot]
                    y = count * 100 - 250
                else:
                    if 50 <= x <= 150:
                        x = 100
                        slot = 4
                        count = sloturi[slot]
                        y = count * 100 - 250
                    else:
                        if 150 <= x <= 250:
                            x = 200
                            slot = 5
                            count = sloturi[slot]
                            y = count * 100 - 250
                        else:
                            if 250 <= x <= 350:
                                x = 300
                                slot = 6
                                count = sloturi[slot]
                                y = count * 100 - 250
                            else:
                                pass

    up()
    goto(x, y)
    dot(100, player)
    culori[count][slot] = player
    if castigator(culori, count, slot):
        nr = int(textinput("Sfarsit joc", f"{player} a castigat\n 1.Restart\n 2.Exit"))
        if nr == 1:
            restart()
        else:
            bye()
    sloturi[slot] = count + 1
    state.player = ture[player]


def restart():
    reset()
    hideturtle()
    desenare_tabla(-350, 300)
    grid()
    state.reset()


def run():
    Screen().setup(1366, 768, 0, 0)
    Screen().title("4 in linie")
    hideturtle()
    speed(150)
    tracer(0, 0)
    desenare_tabla(-350, 300)
    grid()
    mod_joc = int(textinput("MOD JOC", f"1. Versus Player\n 2. Versus Calculator"))
    if mod_joc == 1:
        Screen().onclick(player)
    else:
        Screen().onclick(calculator)
    done()
