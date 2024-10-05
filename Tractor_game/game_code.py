import pygame, os, random, time

pygame.init()
pygame.mixer.set_num_channels(8)

clock = pygame.time.Clock()

TILE_SIZE = 20

WINDOW_SIZE = (700, 500)

collisoins_ist = []

def make_tree(image_address, x, y, width, height, scale):
    read_img = pygame.image.load(image_address)
    read_img = pygame.transform.scale(read_img, scale)
    read_img = pygame.transform.rotate(read_img, 90)
    img_rect = pygame.Rect(x, y, width, height)

    return read_img, img_rect


def make_ground(surf, img_address, tile_size):
    rects = []
    img = pygame.image.load(img_address)
    for x in range(0, WINDOW_SIZE[0], tile_size):
        for y in range(450, WINDOW_SIZE[1], tile_size):
            surf.blit(img, (x, y))
            rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
            rects.append(rect)

    return rects


# def play_music(address, loop_of_playing, volume_of_sound):
def make_multi_enemies(obstacle_list):
    obstacle_rect = []
    for g in range(3):
        character_random = random.choice(obstacle_list)
        random_speed = random.randint(20, 40)
        y_random = -10
        x_random = random.randint(5, 650)
        character_rect = pygame.Rect(x_random, y_random, 50, 50)
        obstacle_rect.append((character_random, character_rect, random_speed))

    return obstacle_rect


def make_grass_wall(number_of_grasses, grass_image, grass_rectangle, start_y, grass_x=0):
    grass_rects_list = []
    for n in range(number_of_grasses):
        current_grass_rect = grass_rectangle.copy() 
        current_grass_rect.x = grass_x
        current_grass_rect.y = start_y - n * 18 
        screen.blit(grass_image, current_grass_rect)
        grass_rects_list.append(current_grass_rect) 

    return grass_rects_list



screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("Tractor Game")

sky_dir = os.listdir("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds")
h = []
for fi in range(len(sky_dir)):
    sky_dir[fi] = int(sky_dir[fi].split(".")[0])
sky_dir.sort()

top_sky = []

org_path = "E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/"
sky_list = []
for files in range(len(sky_dir)):
    read_image = pygame.image.load(org_path+str(sky_dir[files])+".png")
    scale_size = [60, 60]
    if files == 0:
        scale_size[0] = 70
        scale_size[1] = 70
    else:
        scale_size = [60, 60]

    im_rect = pygame.Rect(0, 0, scale_size[0], scale_size[1])
    read_image = pygame.transform.scale(read_image, tuple(scale_size))
    sky_list.append((read_image, im_rect))
top_sky = sky_list[:4]


sky_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/1.png")
sky_img = pygame.transform.scale(sky_img, (70, 70))
sky2_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/5.png")
sky2_img = pygame.transform.scale(sky2_img, (60, 60))
sky3_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/6.png")
sky3_img = pygame.transform.scale(sky3_img, (60, 60))
sky4_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/7.png")
sky4_img = pygame.transform.scale(sky4_img, (60, 60))
sky5_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/8.png")
sky5_img = pygame.transform.scale(sky5_img, (60, 60))
sky6_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles\Backgrounds/9.png")
sky6_img = pygame.transform.scale(sky6_img, (60, 60))


grass_img = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/tile_0022.png")
grass_rect = grass_img.get_rect()



dirt_rects = [rects for rects in make_ground(screen, "E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/tile_0005.png", 18)]
                             
player_collision = False

flag = True

TILE_SIZE2 = 18

game_speed = 30


farmer_player = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game/tractor.png").convert()
farmer_player = pygame.transform.scale(farmer_player, (160, 125))
farmer_rect = pygame.Rect(5, 390, 25, 18)
farmer_player.set_colorkey((255, 255, 255))

tractor_sound = pygame.mixer.Sound("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game/tractor_sound.mp3")
tractor_sound.set_volume(0.5)
tractor_sound.play(loops=-1)

bg_music = pygame.mixer.Sound("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game/bg_sound.mp3")
bg_music.set_volume(0.7)
bg_music.play(loops=-1)

enemy_list = [pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/Characters/tile_0002.png"),
              pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/Characters/tile_0003.png")]
enemy_list2 = [pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/Characters/tile_0004.png"),
               pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/Characters/tile_0005.png")]
enemy_list3 = [pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/Characters/tile_0006.png"),
               pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/Characters/tile_0007.png")]

enemy_list = [pygame.transform.scale(enemy, (50, 50)) for enemy in enemy_list]
enemy_list2 = [pygame.transform.scale(enemy2, (50, 50)) for enemy2 in enemy_list2]
enemy_list3 = [pygame.transform.scale(enemy3, (50, 50)) for enemy3 in enemy_list3]

rand_enemy = random.choice([enemy_list, enemy_list2, enemy_list3])
enemy_status = 0
e_x_pos = 0

y_ground_list = ["218", "236", "254", "272", "290", "308", "326", "344", "362", "380", "398", "416", "434"]
y_rand = random.choice(y_ground_list)

game_score = 0

font = pygame.font.Font("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game/fonts/AtariClassic-gry3.ttf", 25)

enemy_speed = 40

game_over = False

list_of_obstacles = [enemy_list, enemy_list2, enemy_list3]
obstacles = make_multi_enemies(list_of_obstacles)

y_grass = 0

wall = pygame.image.load("E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/tile_0124.png").convert_alpha()
wall_rect = wall.get_rect()

count_obstacle = 0
count_obstacle_list = []

while flag:

    sky_arr = []

    dirt_arr = []

    screen.fill((255, 255, 255))


    for i in range(35):
        for j in range(21):
            for surfs in sky_list:
                surfs[1].x = i*TILE_SIZE
                surfs[1].y = j*TILE_SIZE
                screen.blit(surfs[0], surfs[1])
    

    for ui in range(35):
        for e in range(10):
            for se,re in top_sky:
                re.x = ui*24
                re.y = e*24
                screen.blit(se,re)


    for u in range(0, 700, 230):
        screen.blit(sky2_img, (u, 160))
        screen.blit(sky3_img, (u+60, 160))
        screen.blit(sky4_img, (u+60+60, 160))
        screen.blit(sky5_img, (u+60+60+60, 160))
        sky_arr.append([sky2_img, sky3_img, sky4_img, sky5_img])

    
    for b in range(0, 700):
        for h in range(219, 500):
            screen.blit(sky6_img, (b, h))
    
    ground_rects_list = make_ground(screen, "E:\Ai\America_innoverse_challenges2024\Crop_Health\The_end_of_challenge\Tractor_game\Tiles/tile_0022.png", 18)

    grass_wall = make_grass_wall(25, grass_img, grass_rect, 432)
    grass_wall2 = make_grass_wall(25, grass_img, grass_rect, 432, grass_x=682)
    for grass_rect in grass_wall:
        grass_rect.y += 10 
    for grass_rect in grass_wall2:
        grass_rect.y += 10

    if enemy_status == 0:
        enemy_status = 1
    else:
        enemy_status = 0

    
    for c, r, s in obstacles:
        screen.blit(c[enemy_status], r)
        r.y += s
    

    for c, r, s in obstacles:
        if r.y >= WINDOW_SIZE[1]:
            count_obstacle += 1
            if count_obstacle % 5 == 0:
                obstacles = make_multi_enemies(list_of_obstacles)


    for c, r, s in obstacles:
        farmer_player_mask = pygame.mask.from_surface(farmer_player.convert_alpha())
        enemy_mask = pygame.mask.from_surface(c[enemy_status].convert_alpha())
        
        if farmer_player_mask.overlap(enemy_mask, offset=(r.x-farmer_rect.x, r.y - farmer_rect.y)):
            game_score -= 7
        


    screen.blit(farmer_player, farmer_rect)
    if farmer_rect.x >= WINDOW_SIZE[0]-farmer_player.get_width():
        if farmer_rect.y < 390:
            farmer_rect.x = 0
            farmer_rect.y += 18


    wall = pygame.transform.flip(wall, True, False)    
    cute_wall = make_grass_wall(25, wall, wall_rect, 432)
    cute_wall2 = make_grass_wall(25, wall, wall_rect, 432, grass_x=682)

    

    text = font.render(f"Score : {game_score}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (530, 40)
    
    if game_score == 0:
        game_over = True
    
    if game_score > 0:
        screen.blit(text, text_rect)
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        
        if event.type == pygame.KEYDOWN:
    
            if event.key == pygame.K_RIGHT:
                if farmer_rect.x <= WINDOW_SIZE[0] - farmer_player.get_width():
                    farmer_rect.x += 22
                    game_score += 5
                    pygame.transform.flip(farmer_player, True, False)

            if event.key == pygame.K_LEFT:
                if farmer_rect.x >= 10:
                    farmer_rect.x -= 22
                    pygame.transform.flip(farmer_player, True, False)
    

    pygame.display.flip()
    pygame.display.update()
    clock.tick(200000)