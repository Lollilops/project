import pygame
import time
import random

pygame.init()


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

file_m = open("../max.txt", "a+", encoding="utf-16le")
file_m.close()
del file_m

file_l = open("../list.txt", "a+", encoding="utf-16le")
file_l.close()
del file_l

file_s = open("../save.txt", "a+", encoding="utf-16le")
file_s.close()
del file_s

snake_block = 22
mix = float(snake_block)

dis_width = 924
dis_height = 528

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')

clock = pygame.time.Clock()

num = "321"

version = "v.3.0.2"

score_font = pygame.font.SysFont("comicsansms", 30)
font = pygame.font.Font(None, 32)
font_style = pygame.font.SysFont("bahnschrift", 35)
font_style_25 = pygame.font.SysFont("bahnschrift", 25)
size_message = pygame.font.SysFont("comicsansms", 35)
name_font = pygame.font.SysFont("comicsansms", 25)
version_font = pygame.font.SysFont("comicsansms", 15)

game_over = False

image = pygame.image.load("IMG_8919.PNG")

image = pygame.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))

image.set_colorkey((255, 255, 255, 255))


def name_s():
    def name1_0(score):
        value = size_message.render(str(score), True, (0, 0, 255))
        dis.blit(value, [0, 0])
    global font
    input_box = pygame.Rect((dis_width - 160) // 2, (dis_height - 32) // 2, 140, 32)
    color_active = pygame.Color('dodgerblue2')
    text = ''
    global game_over

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                return text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if text == "":
                        text = "_Untitled_"
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                    text = text.replace(" ", "_")
                    text = text.replace("", "")
                    text = text.replace("", "")
                    text = text.replace("	", "")
        dis.fill((0, 255, 0))
        name1_0("Напишите ваше имя:")
        txt_surface = font.render(text, True, color_active)
        width = max(193, txt_surface.get_width() + 3)
        input_box.w = width + 7
        input_box.x = (dis_width - width) // 2
        dis.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(dis, color_active, input_box, 2)
        n_name("Продолжая использовать эту программу,", "", 0,
               dis_height - 60)
        n_name("вы соглашаетесь на обработку персональных данных", "!", 0,
               dis_height - 30)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


def save_file_1(name_sf, lvl_sf, length_of_snake_s, w_c, h_c, wa_c, ha_c, speed):

    global game_over

    if not game_over:
        file_sf1 = open("../save.txt", "a+", encoding="utf-16le")
        file_sf2 = open("../save.txt", encoding="utf-16le").read().split("\n")
        file_sf1.truncate(0)
        file_sf2 = file_sf2[:-1]
        file_flag = False
        for file_reader in range(len(file_sf2)):
            file_reader_1 = file_sf2[file_reader]
            if file_reader_1.count(" ") > 0:
                file_reader_1 = file_reader_1[:file_reader_1.index(" ")]
            else:
                break
            if name_sf == file_reader_1:
                file_sf2[file_reader] = name_sf + " " + lvl_sf + " " + length_of_snake_s + " " + w_c +\
                                        " " + h_c + " " + wa_c + " " + ha_c + " " + speed
                file_flag = True
                break
        if not file_flag:
            file_sf2.append(name_sf + " " + lvl_sf + " " + length_of_snake_s + " " + w_c + " " + h_c +
                            " " + wa_c + " " + ha_c + " " + speed)
        for scan_file_sf2 in file_sf2:
            file_sf1.write(scan_file_sf2 + "\n")
        file_sf1.close()


def save_file_2(name_sf2):

    global game_over

    if not game_over:
        file_sv2 = open("../save.txt", encoding="utf-16le").read().split("\n")
        for file_reader in range(len(file_sv2)):
            file_reader_1 = file_sv2[file_reader]
            if file_reader_1.count(" ") > 0:
                file_reader_1 = file_reader_1[:file_reader_1.index(" ")]
            else:
                break
            if name_sf2 == file_reader_1:
                return file_reader


def your_score(string, score, w, h):
    value = size_message.render(string + str(score), True, blue)
    dis.blit(value, [w, h])


def s_speed(speed):
    value_1 = size_message.render("Your Speed: " + str(speed), True, blue)
    dis.blit(value_1, [0, 30])


def n_name(string, name_1, w, h):
    value_1 = name_font.render(string + str(name_1), True, black)
    if string.count("best") == 1:
        dis.blit(value_1, [(dis_width - value_1.get_width() - w), h])
    elif string == "1":
        value_1 = name_font.render("Player № " + string + ": " + str(name_1) + "(w)", True, black)
        dis.blit(value_1, [0, 0])
    elif string == "2":
        value_1 = name_font.render("Player № " + string + ": " + str(name_1) + "(b)", True, black)
        dis.blit(value_1, [(dis_width - value_1.get_width() - 10), 0])
    else:
        dis.blit(value_1, [w, h])


def v_version(num_v):
    value_1 = version_font.render(str(num_v), True, black)
    dis.blit(value_1, [dis_width - 60, dis_height - 30])


def our_snake(snake_block_0, snake_list, nn):
    for x in snake_list:
        if nn == 1:
            pygame.draw.rect(dis, white, [x[0], x[1], snake_block_0 - 2, snake_block_0 - 2])
        if nn == 2:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block_0 - 2, snake_block_0 - 2])


def game(igra_1, igra_2):
    game_show = size_message.render(str(igra_1) + ":" + str(igra_2), True, black)
    dis.blit(game_show, [(dis_width - game_show.get_width()) // 2, 0])


def message(msg1, color):
    if msg1 == "Pause":
        mesg = font_style.render(msg1, True, True, color)
        dis.blit(mesg, [310, 45])
        msg_list = ['управление: W, A, S, D или стрелки', 'главное меню: Esc', 'pause: Q', 'restart: R',
                    'смена режима(при паузе и score = 0): V', 'сохранение(при паузе): U']
        for msg_reader in range(len(msg_list)):
            mesg_p = name_font.render(msg_list[msg_reader], True, black)
            dis.blit(mesg_p, [(dis_width - mesg_p.get_width() - 10), 75 + 32 * msg_reader])
        msg_pr = font_style_25.render("Для продолжения нажмите на любую клавишу управления", True, black)
        dis.blit(msg_pr, [(dis_width - msg_pr.get_width()) / 2, dis_height - 30])
    elif msg1 == "Pause1":
        mesg = font_style.render(msg1[:-1], True, True, color)
        dis.blit(mesg, [(dis_width - mesg.get_width()) // 2, 45])
        msg_list = ['управление: W, A, S, D или стрелки', 'главное меню: Esc', 'pause: Q', 'restart: R',
                    'смена режима(при паузе и score = 0): V']
        for msg_reader in range(len(msg_list)):
            mesg_p = name_font.render(msg_list[msg_reader], True, black)
            dis.blit(mesg_p, [(dis_width - mesg_p.get_width() - 10), 75 + 32 * msg_reader])
        msg_pr = font_style_25.render("Для продолжения нажмите на любую клавишу управления", True, black)
        dis.blit(msg_pr, [(dis_width - msg_pr.get_width()) / 2, dis_height - 30])
    elif msg1[-1] == "1":
        mesg = font_style.render(msg1[:-1], True, True, color)
        dis.blit(mesg, [(dis_width - mesg.get_width()) // 2, dis_height / 3])
    else:
        mesg = font_style.render(msg1, True, color)
        dis.blit(mesg, [(dis_width - mesg.get_width()) / 2, dis_height / 2])


def list_file(name_l, lvl_l, score, speed, rgb_l):
    file_ol1 = open("../list.txt", "a+", encoding="utf-16le")
    file_ol2 = open("../list.txt", encoding="utf-16le").read().split("\n")
    if len(file_ol2) >= 501:
        file_ol1.truncate(0)
        file_ol2 = file_ol2[1:500]
        for scan_file_ol2 in file_ol2:
            file_ol1.write(scan_file_ol2 + "\n")
    if rgb_l == "0":
        file_ol1.write(name_l + " lvl:" + lvl_l + " rgb:Off score:" + score + " speed:" + speed + " | " +
                       time.strftime("%c") + "\n")
    elif rgb_l == "1":
        file_ol1.write(name_l + " lvl:" + lvl_l + " rgb:On score:" + score + " speed:" + speed + " | " +
                       time.strftime("%c") + "\n")
    file_ol1.close()


def max_file(lvl_m, max_num, name_m):
    file_o1 = open("../max.txt", encoding="utf-16le").read().split()
    while len(file_o1) != 10:
        if len(file_o1) > 10:
            file_o1 = file_o1[:-1]
        if len(file_o1) < 5:
            file_o1.append("0")
        if 5 <= len(file_o1) < 10:
            file_o1.append("non")
    file_o11 = int(file_o1[lvl_m])
    file_o12 = file_o1[lvl_m + 5]
    if file_o11 < max_num:
        file_o11 = max_num
        file_o12 = name_m
        file_o1[lvl_m] = str(file_o11)
        file_o1[lvl_m + 5] = file_o12
    file_o1 = str(file_o1)
    file_o1 = file_o1.replace("]", "")
    file_o1 = file_o1.replace("[", "")
    file_o1 = file_o1.replace("'", "")
    file_o1 = file_o1.replace(",", "")
    file_o2 = open("../max.txt", "a", encoding="utf-16le")
    file_o2.truncate(0)
    if name_m != "ver_MAXon_Mika" and lvl_m != 5:
        file_o2.write(file_o1)
    else:
        file_ol1 = open("../list.txt", "a+", encoding="utf-16le")
        if len(file_o1) <= 150:
            file_ol1.write("Обновление max_file, значения файла: " + file_o1 + " | " + time.strftime("%c") + "\n")
        else:
            file_ol1.write("Обновление max_file" + " | " + time.strftime("%c") + "\n")

        file_ol1.close()
        global game_over
        game_over = True
    file_o2.close()
    n_name("The best Player: ", file_o12, 10, 30)
    n_name("The best score: ", file_o11, 30, 0)


def main_menu(save_zone):
    h = 60
    length = 450

    main_height = (dis_height - 70) // 7

    def dif(score):
        value = size_message.render(str(score), True, (0, 0, 255))
        dis.blit(value, [0, 0])

    def score_dif(number, width):
        if number == 0:
            start_name_mm = "Single Play"
        elif number == 1:
            start_name_mm = "MultiPlay"
        else:
            start_name_mm = "Exit"
        value = size_message.render(start_name_mm, True, blue)
        dis.blit(value, [(dis_width - value.get_width()) // 2, width])

    global game_over
    y = 0

    while not game_over:
        a = [main_height * 5, main_height * 6, main_height * 7]
        match_list = [1, 0, 0]
        match_list[y] = 0
        for event in pygame.event.get():
            x = 0
            if event.type == pygame.QUIT:
                game_over = True
                return y + 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x = -1
                elif event.key == pygame.K_DOWN:
                    x = 1
                elif event.key == pygame.K_w:
                    x = -1
                elif event.key == pygame.K_s:
                    x = 1
                elif event.key == pygame.K_RETURN:
                    return y + 1
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    return y + 1

            if x == -1 and y == 0:
                y = 2
            elif x == 1 and y == 2:
                y = 0
            elif x == 1:
                y += 1
            elif x == -1:
                y -= 1
        match_list[y] = 1
        dis.fill(green)
        if save_zone == 1:
            dif("Saved")
        dis.blit(image, ((dis_width - image.get_width()) // 2, 0))
        for n_match in range(3):
            if n_match == y:
                pygame.draw.rect(dis, red, [(dis_width - length) // 2, a[n_match], length, h])
            else:
                pygame.draw.rect(dis, yellow, [(dis_width - length) // 2, a[n_match], length, h])
        for b in range(len(a)):
            score_dif(b, a[b])

        pygame.display.flip()
        clock.tick(30)


def name_win():
    def name1_w(score, n_w, n_h):
        if score[-1] == ")":
            value = name_font.render(str(score), True, (0, 0, 255))
        else:
            value = size_message.render(str(score), True, (0, 0, 255))
        dis.blit(value, [n_w, n_h])
    global font

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    input_box = pygame.Rect((dis_width - 160) // 2, (dis_height - 32) // 3, 140, 32)
    color = color_inactive
    active = False
    text = ''

    input_box_2 = pygame.Rect((dis_width - 160) // 2, ((dis_height - 32) // 3) * 2, 140, 32)
    color_2 = color_inactive
    active_2 = False
    text_2 = ''

    global game_over
    change = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                return text
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False

                if input_box_2.collidepoint(event.pos):
                    active_2 = not active_2
                else:
                    active_2 = False

                color = color_active if active else color_inactive
                color_2 = color_active if active_2 else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        active = False
                        active_2 = True
                        change = True
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        text = text.replace(" ", "_")
                        text = text.replace("", "")
                        text = text.replace("", "")
                        text = text.replace("	", "")
                        if change:
                            text = text[:-1]
                            color = color_inactive

                if active_2:
                    if event.key == pygame.K_RETURN and not change:
                        if text == "":
                            text = "_Untitled_"
                        if text_2 == "":
                            text_2 = "_Untitled_"
                        if len(text) > 16:
                            text = text[:17]
                        if len(text_2) > 16:
                            text_2 = text_2[:17]
                        return text + " " + text_2
                    elif event.key == pygame.K_BACKSPACE:
                        text_2 = text_2[:-1]
                    else:
                        text_2 += event.unicode
                        text_2 = text_2.replace(" ", "_")
                        text_2 = text_2.replace("", "")
                        text_2 = text_2.replace("", "")
                        text_2 = text_2.replace("	", "")
                        if change:
                            text_2 = text_2[:-1]
                            color_2 = color_active
                    change = False
        dis.fill((0, 255, 0))

        name1_w("Напишите ваши имена:", 0, 0)

        txt_surface = font.render(text, True, color)
        width = max(250, txt_surface.get_width() + 3)
        input_box.w = width + 7
        input_box.x = (dis_width - width) // 2
        dis.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(dis, color, input_box, 2)
        name1_w("Игрок 1(W, A, S, D)", (dis_width - width) // 2, input_box.y - 32)

        txt_surface_2 = font.render(text_2, True, color_2)
        width_2 = max(250, txt_surface_2.get_width() + 3)
        input_box_2.w = width_2 + 7
        input_box_2.x = (dis_width - width_2) // 2
        dis.blit(txt_surface_2, (input_box_2.x + 5, input_box_2.y + 5))
        pygame.draw.rect(dis, color_2, input_box_2, 2)
        name1_w("Игрок 2(Стрелки)", (dis_width - width_2) // 2, input_box_2.y - 32)

        n_name("Продолжая использовать эту программу,", "", 0,
               dis_height - 60)
        n_name("вы соглашаетесь на обработку персональных данных", "!", 0,
               dis_height - 30)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


def menu():
    h = 70
    main_width = (dis_width - h) // 6
    main_height = (dis_height - h) // 2

    def dif(score):
        value = size_message.render(str(score), True, (0, 0, 255))
        dis.blit(value, [0, 0])

    def score_dif(number, width):
        value = size_message.render(str(number), True, blue)
        dis.blit(value, [width, main_height])

    global game_over
    y = 0

    while not game_over:
        a = [main_width, main_width * 2, main_width * 3, main_width * 4, main_width * 5]
        match_list = [1, 0, 0, 0, 0]
        match_list[y] = 0
        for event in pygame.event.get():
            x = 0
            if event.type == pygame.QUIT:
                game_over = True
                return y + 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -1
                elif event.key == pygame.K_RIGHT:
                    x = 1
                elif event.key == pygame.K_a:
                    x = -1
                elif event.key == pygame.K_d:
                    x = 1
                elif event.key == pygame.K_RETURN:
                    return y + 1

            if x == -1 and y == 0:
                y = 4
            elif x == 1 and y == 4:
                y = 0
            elif x == 1:
                y += 1
            elif x == -1:
                y -= 1
        match_list[y] = 1
        dis.fill(green)
        for n_match in range(5):
            if n_match == y:
                pygame.draw.rect(dis, red, [a[n_match], main_height, h, h])
            else:
                pygame.draw.rect(dis, yellow, [a[n_match], main_height, h, h])
        dif("Выберите сложность:")
        for b in range(len(a)):
            score_dif(b + 1, a[b])

        pygame.display.flip()
        clock.tick(30)


def rgb_on():
    h = 70
    main_width = (dis_width - h) // 3
    main_height = (dis_height - h) // 2

    def dif(score):
        value = size_message.render(str(score), True, blue)
        dis.blit(value, [0, 0])

    def score_dif(number, width):
        value_1 = name_font.render("rgb", True, blue)
        value = name_font.render(str(number), True, blue)
        dis.blit(value_1, [width, main_height])
        dis.blit(value, [width, main_height + 30])

    global game_over
    y = 0

    while not game_over:
        a = [main_width, main_width * 2]
        match_list = [1, 0]
        match_list[y] = 0
        for event in pygame.event.get():
            x = 0
            if event.type == pygame.QUIT:
                game_over = True
                return y
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -1
                elif event.key == pygame.K_RIGHT:
                    x = 1
                elif event.key == pygame.K_a:
                    x = -1
                elif event.key == pygame.K_d:
                    x = 1
                elif event.key == pygame.K_RETURN:
                    return y
            if x == -1 and y == 0:
                y = 1
            elif x == 1 and y == 1:
                y = 0
            elif x == 1:
                y += 1
            elif x == -1:
                y -= 1
        match_list[y] = 1
        dis.fill((0, 255, 0))
        for n_match in range(2):
            if n_match == y:
                pygame.draw.rect(dis, red, [a[n_match], main_height, h, h])
            else:
                pygame.draw.rect(dis, yellow, [a[n_match], main_height, h, h])
        for b in range(len(a)):
            if b == 0:
                score_dif("off", a[b])
            else:
                score_dif("on", a[b])
        dif("RGB ON/OFF:")

        pygame.display.update()
        clock.tick(30)
    pygame.quit()


def save_on():
    w = 140
    h = 70
    main_width = (dis_width - w) // 3
    main_height = (dis_height - h) // 2

    def dif(score):
        value = size_message.render(str(score), True, blue)
        dis.blit(value, [0, 0])

    def score_dif(number, width):
        if number == "Новая игра":
            value = name_font.render(str(number), True, blue)
            dis.blit(value, [width, main_height + 10])
        else:
            value_1 = name_font.render("Загрузить", True, blue)
            value = name_font.render(str(number), True, blue)
            dis.blit(value_1, [width, main_height])
            dis.blit(value, [width, main_height + 30])

    global game_over

    y = 0

    while not game_over:
        a = [main_width, main_width * 2]
        match_list = [1, 0]
        match_list[y] = 0
        for event in pygame.event.get():
            x = 0
            if event.type == pygame.QUIT:
                game_over = True
                return y
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -1
                elif event.key == pygame.K_RIGHT:
                    x = 1
                elif event.key == pygame.K_a:
                    x = -1
                elif event.key == pygame.K_d:
                    x = 1
                elif event.key == pygame.K_RETURN:
                    return y
            if x == -1 and y == 0:
                y = 1
            elif x == 1 and y == 1:
                y = 0
            elif x == 1:
                y += 1
            elif x == -1:
                y -= 1
        match_list[y] = 1
        dis.fill(green)
        for n_match in range(2):
            if n_match == y:
                pygame.draw.rect(dis, red, [a[n_match], main_height, w, h])
            else:
                pygame.draw.rect(dis, yellow, [a[n_match], main_height, w, h])
        dif("Найдена игра:")
        for b in range(len(a)):
            if b == 0:
                score_dif("Новая игра", a[b])
            else:
                score_dif("сохранение", a[b])
        pygame.display.update()


def gameloop(lvl_gs, rgb_gs, name_gs, save_gs, length_of_snake_gs, x1_gs, y1_gs, foodx_gs, foody_gs, snake_speed_gs):

    y2_change = 1

    global game_over

    upr = False
    upg = False
    upb = True
    downr = True
    downg = True
    downb = False

    r = 12
    g = 60
    b = 110

    color = (0, 255, 0)

    game_close = False

    x1_change = 0
    y1_change = 0

    snake_list = []

    if save_gs == 0:
        length_of_snake_gs = 1
        x1_gs = dis_width / 2
        y1_gs = dis_height / 2
        foodx_gs = round(random.randrange(0, dis_width - snake_block) / mix) * mix
        foody_gs = round(random.randrange(0, dis_height - snake_block) / mix) * mix

        snake_speed_gs = 5
        if lvl_gs == "2":
            snake_speed_gs = 5
        elif lvl_gs == "3":
            snake_speed_gs = 7
        elif lvl_gs == "4":
            snake_speed_gs = 10
        elif lvl_gs == "5":
            snake_speed_gs = 15
        y2_change = 0
    x1_copy = x1_gs
    y1_copy = y1_gs

    while not game_over:

        while game_close:
            if (lvl_gs == "super hard" or lvl_gs == "5") and (length_of_snake_gs - 1) >= 8:
                dis.fill(color)
                message("You Win! Press C to Play Again or Escape to Quit", red)
                n_name("Your name: ", name_gs, 300, 0)
                n_name("lvl_gs: ", lvl_gs, 0, dis_height - 30)
                your_score("Your Score: ", length_of_snake_gs - 1, 0, 0)
                if y2_change != 1:
                    list_file(name_gs, lvl_gs, str(length_of_snake_gs - 1), str(snake_speed_gs), rgb_gs)
                    y2_change = 1
                max_file(int(lvl_gs) - 1, length_of_snake_gs - 1, name_gs)
                s_speed(snake_speed_gs)
                v_version(version)
                if save_gs == 1:
                    x1_gs = x1_copy
                    y1_gs = y1_copy
                pygame.display.update()
            elif name_gs == "Гриша" or name_gs == "гриша" or name_gs == "Gregory" or name_gs == "gregory":
                dis.fill(color)
                message("You are Беспомощный! Press C to Play Again or Escape to Quit", red)
                n_name("Your name: ", name_gs, 300, 0)
                n_name("lvl_gs: ", lvl_gs, 0, dis_height - 30)
                if y2_change != 1:
                    list_file(name_gs, lvl_gs, str(length_of_snake_gs - 1), str(snake_speed_gs), rgb_gs)
                    y2_change = 1
                max_file(int(lvl_gs) - 1, length_of_snake_gs - 1, name_gs)
                your_score("Your Score: ", length_of_snake_gs - 1, 0, 0)
                s_speed(snake_speed_gs)
                v_version(version)
                if save_gs == 1:
                    x1_gs = x1_copy
                    y1_gs = y1_copy
                pygame.display.update()
            else:
                dis.fill(color)
                message("You Died! Press C to Play Again or Escape to Quit", red)
                n_name("Your name: ", name_gs, 300, 0)
                n_name("lvl: ", lvl_gs, 0, dis_height - 30)
                if y2_change != 1:
                    list_file(name_gs, lvl_gs, str(length_of_snake_gs - 1), str(snake_speed_gs), rgb_gs)
                    y2_change = 1
                max_file(int(lvl_gs) - 1, length_of_snake_gs - 1, name_gs)
                your_score("Your Score: ", length_of_snake_gs - 1, 0, 0)
                s_speed(snake_speed_gs)
                v_version(version)
                if save_gs == 1:
                    x1_gs = x1_copy
                    y1_gs = y1_copy
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_close = False
                        y2_change = 2

                    elif event.key == pygame.K_c:
                        return gameloop(lvl_gs, rgb_gs, name_gs, save_gs, length_of_snake_gs, x1_gs, y1_gs, foodx_gs,
                                        foody_gs, snake_speed_gs)

        lvlch = 0
        stop = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                list_file(name_gs, lvl_gs, str(length_of_snake_gs - 1), str(snake_speed_gs), rgb_gs)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                    y2_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                    y2_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    y2_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    y2_change = 0
                elif event.key == pygame.K_ESCAPE:
                    list_file(name_gs, lvl_gs, str(length_of_snake_gs - 1), str(snake_speed_gs), rgb_gs)
                    y2_change = 2
                elif event.key == pygame.K_q:
                    y1_change = 0
                    y2_change = 1
                    x1_change = 0
                elif event.key == pygame.K_r:
                    return gameloop(lvl_gs, rgb_gs, name_gs, save_gs, length_of_snake_gs, x1_gs, y1_gs, foodx_gs,
                                    foody_gs, snake_speed_gs)
                elif event.key == pygame.K_v:
                    lvlch = 1
                elif event.key == pygame.K_u:
                    lvlch = 2

        if x1_gs >= dis_width or x1_gs < 0 or y1_gs >= dis_height or y1_gs < 0:
            game_close = True
        x1_gs += x1_change
        y1_gs += y1_change
        if rgb_gs == "1":
            if -1 < r < 256:
                if r < 255 and upr:
                    r += 3
                if r == 246:
                    upr = False
                    downr = True
                if r > 0 and downr:
                    r = r - 3
                if r == 0:
                    upr = True
                    downr = False
            if -1 < g < 256:
                if g < 255 and upg:
                    g += 2
                if g == 196:
                    upg = False
                    downg = True
                if g > 0 and downg:
                    g = g - 2
                if g == 0:
                    upg = True
                    downg = False
            if -1 < b < 256:
                if b < 255 and upb:
                    b += 1
                if b == 200:
                    upb = False
                    downb = True
                if b > 0 and downb:
                    b = b - 1
                if b == 0:
                    upb = True
                    downb = False
                color = (r, g, b)
        else:
            color = green
        dis.fill(color)

        if y2_change == 1 and x1_change == 0:
            stop = -length_of_snake_gs - 1
            message("Pause", red)

        pygame.draw.rect(dis, red, [foodx_gs, foody_gs, snake_block - 2, snake_block - 2])
        snake_head = list()
        snake_head.append(x1_gs)
        snake_head.append(y1_gs)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake_gs:
            del snake_list[0]

        for x in snake_list[:stop]:
            if x == snake_head:
                game_close = True

        if y2_change == 1 and x1_change == 0 and lvlch == 1 and length_of_snake_gs == 1:
            lvl_ngs = str(menu())
            rgb_ngs = str(rgb_on())
            snake_speed_gs = 5
            return gameloop(lvl_ngs, rgb_ngs, name_gs, save_gs, length_of_snake_gs, x1_gs, y1_gs, foodx_gs, foody_gs,
                            snake_speed_gs)

        if y2_change == 1 and x1_change == 0 and lvlch == 2 and save_gs == 0:
            save_file_1(name_gs, lvl_gs, str(length_of_snake_gs), str(int(x1_gs)), str(int(y1_gs)), str(int(foodx_gs)),
                        str(int(foody_gs)), str(snake_speed_gs))
            y2_change = 3

        if y2_change == 2 or y2_change == 3:
            if y2_change == 3:
                start_gs = str(main_menu(1))
            else:
                start_gs = str(main_menu(0))
            if start_gs == "1":
                return 1
            elif start_gs == "2":
                return 2
            else:
                return 3

        our_snake(snake_block, snake_list, 1)
        n_name("Your name: ", name_gs, 260, 7)
        n_name("lvl: ", lvl_gs, 0, dis_height - 30)
        max_file(int(lvl_gs) - 1, length_of_snake_gs - 1, name_gs)
        your_score("Your Score: ", length_of_snake_gs - 1, 0, 0)
        s_speed(snake_speed_gs)
        v_version(version)
        if y2_change == 0 or x1_change != 0:
            n_name("Q - Пауза", "", 260, 42)

        pygame.display.update()

        if x1_gs == foodx_gs and y1_gs == foody_gs:
            foodx_gs = round(random.randrange(0, dis_width - snake_block) / mix) * mix
            foody_gs = round(random.randrange(0, dis_height - snake_block) / mix) * mix
            length_of_snake_gs += 1

            save_gs = 0

            if lvl_gs == "2":
                if snake_speed_gs <= 15:
                    snake_speed_gs += 1
            elif lvl_gs == "3":
                if snake_speed_gs <= 20:
                    snake_speed_gs += 1
            elif lvl_gs == "4":
                snake_speed_gs += 1
            elif lvl_gs == "5":
                snake_speed_gs += 3

        clock.tick(snake_speed_gs)

    pygame.quit()
    quit()


def gameloop_m(igra1_gm, igra2_gm, lvl_gm, rgb_gm, name_gm, name1_gm):
    kon = 0

    global game_over
    game_close = False

    upr = False
    upg = False
    upb = True
    downr = True
    downg = True
    downb = False

    r = 12
    g = 60
    b = 110

    color = (0, 255, 0)

    x1_gm = dis_width / 6
    y1_gm = dis_height / 2

    x1_change = 0
    y1_change = 0

    x2 = (dis_width / 6) * 5
    y2 = dis_height / 2

    x2_change = 0
    y2_change = 0

    snake_list_gm = []
    snake_list_2_gm = []
    length_of_snake_gm = 1
    length_of_snake_2_gm = 1

    snake_speed_gm = 5

    if lvl_gm == "2":
        snake_speed_gm = 5
    elif lvl_gm == "3":
        snake_speed_gm = 7
    elif lvl_gm == "4":
        snake_speed_gm = 10
    elif lvl_gm == "5":
        snake_speed_gm = 15

    y_s_change = 0

    foodx_gm = round(random.randrange(0, dis_width - snake_block) / mix) * mix
    foody_gm = round(random.randrange(0, dis_height - snake_block) / mix) * mix

    while not game_over:

        while game_close:
            if kon == 0:
                dis.fill(color)
                if length_of_snake_2_gm > length_of_snake_gm:
                    message(name1_gm + "wins1", red)
                    message("Press C to Play Again or Escape to Quit", red)
                    if y_s_change == 0:
                        igra2_gm += 1
                        y_s_change = 1
                    game(igra1_gm, igra2_gm)
                elif length_of_snake_2_gm == length_of_snake_gm:
                    message("Nobody wins1", red)
                    message("Press C to Play Again or Escape to Quit", red)
                    game(igra1_gm, igra2_gm)
                else:
                    message(name_gm + "wins1", red)
                    message("Press C to Play Again or Escape to Quit", red)
                    if y_s_change == 0:
                        igra1_gm += 1
                        y_s_change = 1
                    game(igra1_gm, igra2_gm)
                n_name("1", name_gm, 0, 1)
                n_name("2", name1_gm, 0, 2)
                n_name("lvl: ", lvl_gm, 0, dis_height - 30)
                your_score("Your score: ", length_of_snake_2_gm - 1, (dis_width -
                                                                      (score_font.render("Your Score: " +
                                                                                         str(length_of_snake_2_gm - 1),
                                                                                         True, blue)).get_width() - 40),
                           30)
                your_score("Your score: ", length_of_snake_gm - 1, 0, 30)
                v_version(version)

                pygame.display.update()

            elif kon == 2:
                dis.fill(color)
                message(name1_gm + " wins1", red)
                message("Press C to Play Again or Escape to Quit", red)
                if y_s_change == 0:
                    igra2_gm += 1
                    y_s_change = 1
                game(igra1_gm, igra2_gm)
                n_name("1", name_gm, 0, 1)
                n_name("2", name1_gm, 0, 2)
                n_name("lvl: ", lvl_gm, 0, dis_height - 30)
                your_score("Your score: ", length_of_snake_2_gm - 1, (dis_width -
                                                                      (score_font.render("Your Score: " +
                                                                                         str(length_of_snake_2_gm - 1),
                                                                                         True, blue)).get_width() - 40),
                           30)
                your_score("Your score: ", length_of_snake_gm - 1, 0, 30)
                v_version(version)

                pygame.display.update()
            elif kon == 1:
                dis.fill(color)
                message(name_gm + " wins1", red)
                message("Press C to Play Again or Escape to Quit", red)
                if y_s_change == 0:
                    igra1_gm += 1
                    y_s_change = 1
                game(igra1_gm, igra2_gm)
                n_name("1", name_gm, 0, 1)
                n_name("2", name1_gm, 0, 2)
                n_name("lvl: ", lvl_gm, 0, dis_height - 30)
                your_score("Your score: ", length_of_snake_2_gm - 1, (dis_width -
                                                                      (score_font.render("Your Score: " +
                                                                                         str(length_of_snake_2_gm - 1),
                                                                                         True, blue)).get_width() - 40),
                           30)
                your_score("Your score: ", length_of_snake_gm - 1, 0, 30)
                v_version(version)

                pygame.display.update()
            else:
                message("Nobody wins1", red)
                message("Press C to Play Again or Escape to Quit", red)
                game(igra1_gm, igra2_gm)
                n_name("1", name_gm, 0, 1)
                n_name("2", name1_gm, 0, 2)
                n_name("lvl: ", lvl_gm, 0, dis_height - 30)
                your_score("Your score: ", length_of_snake_2_gm - 1, (dis_width -
                                                                      (score_font.render("Your Score: " +
                                                                                         str(length_of_snake_2_gm - 1),
                                                                                         True, blue)).get_width() - 40),
                           30)
                your_score("Your score: ", length_of_snake_gm - 1, 0, 30)
                v_version(version)

                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                    list_file(name_gm + ", " + name1_gm, lvl_gm, str(igra1_gm) + ":" + str(igra2_gm),
                              str(snake_speed_gm), rgb_gm)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_close = False
                        list_file(name_gm + ", " + name1_gm, lvl_gm, str(igra1_gm) + ":" + str(igra2_gm),
                                  str(snake_speed_gm), rgb_gm)
                        y_s_change = 2
                    elif event.key == pygame.K_c:
                        return gameloop_m(igra1_gm, igra2_gm, lvl_gm, rgb_gm, name_gm, name1_gm)

        lvlch = 0
        stop = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                list_file(name_gm + ", " + name1_gm, lvl_gm, str(igra1_gm) + ":" + str(igra2_gm), str(snake_speed_gm),
                          rgb_gm)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x2_change = -snake_block
                    y2_change = 0
                elif event.key == pygame.K_RIGHT:
                    x2_change = snake_block
                    y2_change = 0
                elif event.key == pygame.K_UP:
                    y2_change = -snake_block
                    x2_change = 0
                elif event.key == pygame.K_DOWN:
                    y2_change = snake_block
                    x2_change = 0
                elif event.key == pygame.K_ESCAPE:
                    y_s_change = 2
                    list_file(name_gm + ", " + name1_gm, lvl_gm, str(igra1_gm) + ":" + str(igra2_gm),
                              str(snake_speed_gm), rgb_gm)
                elif event.key == pygame.K_q:
                    y2_change = 0
                    y_s_change = 1
                    x2_change = 0
                    y1_change = 0
                    x1_change = 0
                elif event.key == pygame.K_r:
                    return gameloop_m(igra1_gm, igra2_gm, lvl_gm, rgb_gm, name_gm, name1_gm)
                elif event.key == pygame.K_v:
                    lvlch = 1

        snake_change_1 = x1_change or y1_change
        snake_change_2 = x2_change or y2_change
        if snake_change_1 and snake_change_2:
            x1_gm += x1_change
            y1_gm += y1_change
            x2 += x2_change
            y2 += y2_change
            dis.fill(color)
            game(igra1_gm, igra2_gm)

        if x1_gm >= dis_width or x1_gm < 0 or y1_gm >= dis_height or y1_gm < 0:
            game_close = True
            kon = 2

        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_close = True
            kon = 1

        if rgb_gm == "1":
            if -1 < r < 256:
                if r < 255 and upr:
                    r += 3
                if r == 246:
                    upr = False
                    downr = True
                if r > 0 and downr:
                    r = r - 3
                if r == 0:
                    upr = True
                    downr = False
            if -1 < g < 256:
                if g < 255 and upg:
                    g += 2
                if g == 196:
                    upg = False
                    downg = True
                if g > 0 and downg:
                    g = g - 2
                if g == 0:
                    upg = True
                    downg = False
            if -1 < b < 256:
                if b < 255 and upb:
                    b += 1
                if b == 200:
                    upb = False
                    downb = True
                if b > 0 and downb:
                    b = b - 1
                if b == 0:
                    upb = True
                    downb = False
                color = (r, g, b)
        else:
            color = green
        dis.fill(color)

        game(igra1_gm, igra2_gm)

        if y_s_change == 1 and not (snake_change_1 and snake_change_2):
            stop = -length_of_snake_gm - 1
            message("Pause1", red)
        else:
            n_name("Q - Пауза", "", (dis_width // 2) - 60, 42)

        if y_s_change == 2:
            start_gm = str(main_menu(0))
            if start_gm == "1":
                return 1
            elif start_gm == "2":
                return 2
            else:
                return 3

        pygame.draw.rect(dis, red, [foodx_gm, foody_gm, snake_block - 2, snake_block - 2])
        snake_head = list()
        snake_head.append(x1_gm)
        snake_head.append(y1_gm)
        snake_list_gm.append(snake_head)
        snake_head_2 = list()
        snake_head_2.append(x2)
        snake_head_2.append(y2)
        snake_list_2_gm.append(snake_head_2)
        if snake_head == snake_head_2:
            game_close = True
            kon = 0
        if len(snake_list_gm) > length_of_snake_gm:
            del snake_list_gm[0]

        for x in snake_list_gm[:stop]:
            if x == snake_head:
                game_close = True
                kon = 2
            elif x == snake_head_2:
                game_close = True
                kon = 1

        if len(snake_list_2_gm) > length_of_snake_2_gm:
            del snake_list_2_gm[0]

        for x in snake_list_2_gm[:stop]:
            if x == snake_head_2:
                game_close = True
                kon = 1
            elif x == snake_head:
                game_close = True
                kon = 2

        if y_s_change == 1 and x1_change == 0 and lvlch == 1 and length_of_snake_gm - 1 == 0:
            return 2

        our_snake(snake_block, snake_list_gm, 1)
        our_snake(snake_block, snake_list_2_gm, 2)
        n_name("1", name_gm, 0, 1)
        n_name("2", name1_gm, 0, 2)
        n_name("lvl: ", lvl_gm, 0, dis_height - 30)

        your_score("Your score: ", length_of_snake_2_gm - 1, (dis_width -
                                                              (score_font.render("Your Score: " +
                                                                                 str(length_of_snake_2_gm - 1),
                                                                                 True, blue)).get_width() - 40),
                   30)
        your_score("Your score: ", length_of_snake_gm - 1, 0, 30)
        v_version(version)

        pygame.display.update()

        if x1_gm == foodx_gm and y1_gm == foody_gm:
            foodx_gm = round(random.randrange(0, dis_width - snake_block) / mix) * mix
            foody_gm = round(random.randrange(0, dis_height - snake_block) / mix) * mix
            length_of_snake_gm += 1
            if lvl_gm == "2":
                if snake_speed_gm <= 15:
                    snake_speed_gm += 1
            elif lvl_gm == "3":
                if snake_speed_gm <= 20:
                    snake_speed_gm += 1
            elif lvl_gm == "4":
                snake_speed_gm += 1
            elif lvl_gm == "5":
                snake_speed_gm += 3
        if x2 == foodx_gm and y2 == foody_gm:
            foodx_gm = round(random.randrange(0, dis_width - snake_block) / mix) * mix
            foody_gm = round(random.randrange(0, dis_height - snake_block) / mix) * mix
            length_of_snake_2_gm += 1
            if lvl_gm == "2":
                if snake_speed_gm <= 15:
                    snake_speed_gm += 1
            elif lvl_gm == "3":
                if snake_speed_gm <= 20:
                    snake_speed_gm += 1
            elif lvl_gm == "4":
                snake_speed_gm += 1
            elif lvl_gm == "5":
                snake_speed_gm += 3

        clock.tick(snake_speed_gm)

    pygame.quit()
    quit()


start = str(main_menu(0))
game_start = True
while game_start:
    if start == "1":
        name = name_s()
        save_pr = save_file_2(name)
        if save_pr is not None:
            save = save_on()
            if save == 1:
                file_s2 = open("../save.txt", encoding="utf-16le").read().split("\n")
                file_s2 = file_s2[:-1]
                save_1 = file_s2[save_pr].split()

                name = save_1[0]
                lvl = save_1[1]

                length_of_snake = int(save_1[2])
                x1 = int(save_1[3])
                y1 = int(save_1[4])
                foodx = int(save_1[5])
                foody = int(save_1[6])
                snake_speed = int(save_1[7])

                file_s1 = open("../save.txt", "a+", encoding="utf-16le")
                file_s1.truncate(0)
                file_s2 = file_s2[:save_pr] + file_s2[save_pr + 1:]
                for scan_file_s2 in file_s2:
                    file_s1.write(scan_file_s2 + "\n")
                file_s1.close()
                rgb = str(rgb_on())

                start = str(gameloop(lvl, rgb, name, save, length_of_snake, x1, y1, foodx, foody, snake_speed))
            else:
                lvl = str(menu())
                rgb = str(rgb_on())
        else:
            lvl = str(menu())
            rgb = str(rgb_on())
            save = 0

        if save == 0:
            start = str(gameloop(lvl, rgb, name, save, 1, 0, 0, 0, 0, 5))
    elif start == "2":
        start_name = name_win()

        lvl = str(menu())
        rgb = str(rgb_on())

        igra1 = 0
        igra2 = 0
        if not game_over:
            name = start_name[:start_name.index(" ")]
            name1 = start_name[start_name.index(" ") + 1:]
            start = str(gameloop_m(igra1, igra2, lvl, rgb, name, name1))
        del start_name
    elif start == "3":
        game_start = False
