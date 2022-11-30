import pygame
from pygame.sprite import Group
import sys
import time
import pygame.font
from pygame.sprite import Sprite
def survave_game():
    class Bullet(pygame.sprite.Sprite):

        def __init__(self, screen, gun):
            """создаем пулю"""
            super(Bullet, self).__init__()
            self.screen = screen
            self.rect = pygame.Rect(0, 0, 2, 12)
            self.color = 139, 195, 74
            self.speed = 4.5
            self.rect.centerx = gun.rect.centerx
            self.rect.top = gun.rect.top
            self.y = float(self.rect.y)

        def update(self):
            """перемещение пули вверх"""
            self.y -= self.speed
            self.rect.y = self.y

        def draw_bullet(self):
            """рисуем пулю на экране"""
            pygame.draw.rect(self.screen, self.color, self.rect)

    def events(screen, gun, bullets):
        """обработка нажатий клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    gun.mright = True
                elif event.key == pygame.K_a:
                    gun.mleft = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    gun.mright = False
                elif event.key == pygame.K_a:
                    gun.mleft = False

    def update(bg_color, screen, stats, sc, gun, inos, bullets):
        """обновление экрана"""
        screen.fill(bg_color)
        sc.show_score()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        gun.output()
        inos.draw(screen)
        pygame.display.flip()

    def update_bullets(screen, stats, sc, inos, bullets):
        """обновление позиции пуль"""
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
        if collisions:
            for inos in collisions.values():
                stats.score += 10 * len(inos)
            sc.image_score()
            check_high_score(stats, sc)
            sc.image_guns()
        if len(inos) == 0:
            bullets.empty()
            create_army(screen, inos)

    def gun_kill(stats, screen, sc, gun, inos, bullets):
        """столкновение пушки и армии"""
        if stats.guns_left > 0:
            stats.guns_left -= 1
            sc.image_guns()
            inos.empty()
            bullets.empty()
            create_army(screen, inos)
            gun.create_gun()
            time.sleep(1)
        else:
            stats.run_game = False
            sys.exit()

    def update_inos(stats, screen, sc, gun, inos, bullets):
        """обновляет позицию пришельцев"""
        inos.update()
        if pygame.sprite.spritecollideany(gun, inos):
            gun_kill(stats, screen, sc,  gun, inos, bullets)
        inos_check(stats, screen, sc, gun, inos, bullets)

    def inos_check(stats, screen, sc,gun, inos, bullets):
        """проверка, добралась ли армия до края экрана"""
        screen_rect = screen.get_rect()
        for ino in inos.sprites():
            if ino.rect.bottom >= screen_rect.bottom:
                gun_kill(stats, screen, sc, gun, inos, bullets)
                break

    def create_army(screen, inos):
        """создание армии пришельцев"""
        ino = Ino(screen)
        ino_width = ino.rect.width
        number_ino_x = int((700 - 2 * ino_width) / ino_width)
        ino_height = ino.rect.height
        number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

        for row_number in range(number_ino_y - 1):
            for ino_number in range(number_ino_x):
                ino = Ino(screen)
                ino.x = ino_width + (ino_width * ino_number)
                ino.y = ino_height + (ino_height * row_number)
                ino.rect.x = ino.x
                ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
                inos.add(ino)

    def check_high_score(stats, sc):
        """проверка новых рекордов"""
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sc.image_high_score()
            with open('highscore.txt', 'w') as f:
                f.write(str(stats.high_score))

    class Gun(Sprite):

        def __init__(self, screen):
            """инициализация пушки"""
            super(Gun, self).__init__()
            self.screen = screen
            self.image = pygame.image.load('pixil-frame-0 (1).png')
            self.rect = self.image.get_rect()
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.center = float(self.rect.centerx)
            self.rect.bottom = self.screen_rect.bottom
            self.mright = False
            self.mleft = False

        def output(self):
            """рисование пушки"""
            self.screen.blit(self.image, self.rect)

        def update_gun(self):
            """обновление позиции пушки"""
            if self.mright and self.rect.right < self.screen_rect.right:
                self.center += 1.5
            if self.mleft and self.rect.left > 0:
                self.center -= 1.5

            self.rect.centerx = self.center

        def create_gun(self):
            """размещение пушки по центру внизу экрана"""
            self.center = self.screen_rect.centerx

    class Ino(pygame.sprite.Sprite):
        """класс одного пришельца"""

        def __init__(self, screen):
            """инициализируем и задаем начальную позицию"""
            super(Ino, self).__init__()
            self.screen = screen
            self.image = pygame.image.load('ino.png')
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)

        def draw(self):
            """вывод пришельца на экран"""
            self.screen.blit(self.image, self.rect)

        def update(self):
            """перемещение пришельцев"""
            self.y += 0.1
            self.rect.y = self.y

    class Scores():
        """вывод игровой информации"""
        def __init__(self, screen, stats):
            """инициализируем подсчет очков"""
            self.screen = screen
            self.screen_rect = screen.get_rect()
            self.stats = stats
            self.text_color = (139, 195, 74)
            self.font = pygame.font.SysFont(None, 36)
            self.image_score()
            self.image_high_score()
            self.image_guns()

        def image_score(self):
            """преобразование текста счета в графическое изображение"""
            self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
            self.score_rect = self.score_img.get_rect()
            self.score_rect.right = self.screen_rect.right - 40
            self.score_rect.top = 20

        def image_high_score(self):
            """преобразование рекорда в графическое изображение"""
            self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
            self.high_score_rect = self.high_score_image.get_rect()
            self.high_score_rect.centerx = self.screen_rect.centerx
            self.high_score_rect.top = self.screen_rect.top + 20

        def image_guns(self):
            """количество жизней"""
            self.guns = Group()
            for gun_number in range(self.stats.guns_left):
                gun = Gun(self.screen)
                gun.rect.x = 15 + gun_number * gun.rect.width
                gun.rect.y = 20
                self.guns.add(gun)

        def show_score(self):
            """вывод счета на экран"""
            self.screen.blit(self.score_img, self.score_rect)
            self.screen.blit(self.high_score_image, self.high_score_rect)
            self.guns.draw(self.screen)

    class Stats():
        """отслеживание статистики"""

        def __init__(self):
            """инициализирует статистику"""
            self.reset_stats()
            self.run_game = True
            with open('highscore.txt  ', 'r') as f:
                self.high_score = int(f.readline())

        def reset_stats(self):
            """статистика, изменяющаяся во время игры"""
            self.guns_left = 2
            self.score = 0
    def run():
        pygame.init()
        screen = pygame.display.set_mode((700, 800))
        pygame.display.set_caption("Космические защитники")
        bg_color = (0, 0, 0)
        gun = Gun(screen)
        bullets = Group()
        inos = Group()
        create_army(screen, inos)
        stats = Stats()
        sc = Scores(screen, stats)

        while True:
            events(screen, gun, bullets)
            if stats.run_game:
                gun.update_gun()
                update(bg_color, screen, stats, sc, gun, inos, bullets)
                update_bullets(screen, stats, sc, inos, bullets)
                update_inos(stats, screen, sc, gun, inos, bullets)
    run()
