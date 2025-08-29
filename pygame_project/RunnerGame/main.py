import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walk_frames = [
            pygame.image.load('pygame_project/RunnerGame/assets/player_walk_1.png').convert_alpha(),
            pygame.image.load('pygame_project/RunnerGame/assets/player_walk_2.png').convert_alpha()
        ]
        self.jump_frame = pygame.image.load('pygame_project/RunnerGame/assets/jump.png').convert_alpha()
        self.index = 0
        self.image = self.walk_frames[self.index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jump_count = 0
        self.jump_sound = pygame.mixer.Sound('pygame_project/RunnerGame/assets/jump.mp3')
        self.jump_sound.set_volume(0.3)
        self.mask = pygame.mask.from_surface(self.image)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump_count < 2:
            self.gravity = -20
            self.jump_sound.play()
            self.jump_count += 1

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.jump_count = 0

    def animate(self):
        if self.rect.bottom < 300:
            self.image = self.jump_frame
        else:
            self.index += 0.1
            if self.index >= len(self.walk_frames):
                self.index = 0
            self.image = self.walk_frames[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.input()
        self.apply_gravity()
        self.animate()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type, speed_boost=0):
        super().__init__()
        if type == 'fly':
            self.frames = [
                pygame.image.load('pygame_project/RunnerGame/assets/Fly1.png').convert_alpha(),
                pygame.image.load('pygame_project/RunnerGame/assets/Fly2.png').convert_alpha()
            ]
            self.y_pos = 210
            self.speed = 8 + speed_boost
        else:
            self.frames = [
                pygame.image.load('pygame_project/RunnerGame/assets/snail1.png').convert_alpha(),
                pygame.image.load('pygame_project/RunnerGame/assets/snail2.png').convert_alpha()
            ]
            self.y_pos = 300
            self.speed = 6 + speed_boost

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), self.y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    def animate(self):
        self.index += 0.15
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.animate()
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_sprite():
    global lives, shield_active, shield_uses
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True, pygame.sprite.collide_mask):
        if shield_active:
            shield_active = False
        elif shield_uses > 0:
            shield_uses -= 1
            shield_active = False
        else:
            lives -= 1
            if lives <= 0:
                obstacle_group.empty()
                return False
    return True

def load_high_score():
    try:
        with open("pygame_project/RunnerGame/highscore.txt", "r") as file:
            return int(file.read())
    except:
        return 0

def save_high_score(score):
    if score > high_score:
        with open("pygame_project/RunnerGame/highscore.txt", "w") as file:
            file.write(str(score))

def activate_superpower():
    global superpower_active, superpower_uses
    if superpower_uses > 0 and not superpower_active:
        superpower_active = True
        superpower_uses -= 1
        for obs in obstacle_group:
            obs.kill()

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Advanced Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame_project/RunnerGame/assets/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
paused = False
lives = 2
high_score = load_high_score()
shield_uses = 3
shield_active = False
superpower_uses = 1
superpower_active = False

# Sound
bg_music = pygame.mixer.Sound('pygame_project/RunnerGame/assets/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Background
sky_surface = pygame.image.load('pygame_project/RunnerGame/assets/Sky.png').convert()
ground_surface = pygame.image.load('pygame_project/RunnerGame/assets/ground.png').convert()

# Visual assets
player_stand = pygame.image.load('pygame_project/RunnerGame/assets/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Advanced Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

game_message = test_font.render('Press Space to Start', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 330))

heart_img = pygame.image.load('pygame_project/RunnerGame/assets/heart.png').convert_alpha()
heart_img = pygame.transform.scale(heart_img, (30, 30))

shield_icon = pygame.image.load('pygame_project/RunnerGame/assets/shield.png').convert_alpha()
shield_icon = pygame.transform.scale(shield_icon, (30, 30))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(score)
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_s and shield_uses > 0 and not shield_active:
                    shield_active = True
                if event.key == pygame.K_f:
                    activate_superpower()
            if event.type == obstacle_timer and not paused:
                difficulty_boost = score // 10
                formation = choice(['single', 'double_same', 'double_mixed'])

                if formation == 'single':
                    obstacle_group.add(Obstacle(choice(['fly', 'snail']), difficulty_boost))
                elif formation == 'double_same':
                    obstacle_type = choice(['fly', 'snail'])
                    for i in range(2):
                        x_offset = 50 * i
                        obs = Obstacle(obstacle_type, difficulty_boost)
                        obs.rect.x += x_offset
                        obstacle_group.add(obs)
                elif formation == 'double_mixed':
                    obs1 = Obstacle('fly', difficulty_boost)
                    obs2 = Obstacle('snail', difficulty_boost)
                    obs2.rect.x += 50
                    obstacle_group.add(obs1)
                    obstacle_group.add(obs2)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                    lives = 2
                    score = 0
                    shield_uses = 3
                    shield_active = False
                    superpower_uses = 1
                    superpower_active = False
                elif event.key == pygame.K_r:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                    lives = 2
                    score = 0
                    shield_uses = 3
                    shield_active = False
                    superpower_uses = 1
                    superpower_active = False
                    obstacle_group.empty()

    if game_active:
        if not paused:
            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 300))

            score = display_score()

            for i in range(lives):
                screen.blit(heart_img, (720 + i * 35, 10))

            for i in range(shield_uses):
                screen.blit(shield_icon, (10 + i * 35, 10))

            player.draw(screen)
            player.update()

            obstacle_group.draw(screen)
            obstacle_group.update()

            game_active = collision_sprite()
        else:
            pause_text = test_font.render('Paused', False, (255, 255, 255))
            pause_rect = pause_text.get_rect(center=(400, 180))
            screen.blit(pause_text, pause_rect)
    else:
        screen.fill((30, 30, 30))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)

        high_score = max(high_score, score)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 330))
            screen.blit(score_message, score_message_rect)

            high_score_msg = test_font.render(f'High Score: {high_score}', False, (255, 255, 0))
            high_score_rect = high_score_msg.get_rect(center=(400, 280))
            screen.blit(high_score_msg, high_score_rect)

            restart_msg = test_font.render('Press R to Restart', False, (255, 255, 255))
            restart_rect = restart_msg.get_rect(center=(400, 370))
            screen.blit(restart_msg, restart_rect)

    pygame.display.update()
    clock.tick(60)
