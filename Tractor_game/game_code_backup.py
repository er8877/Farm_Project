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


def make_grass_wall(number_of_grasses, grass_image, grass_rectangle, end_y, grass_x=0):
    grass_rects_list = []
    grass_rectangle.x = grass_x
    for n in range(number_of_grasses):
        grass_rectangle.y = end_y
        screen.blit(grass_image, grass_rectangle)
        end_y -= 18
    
    return grass_rects_list



screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("kharazmi game")

sky_dir = os.listdir("Tiles/Backgrounds/")
h = []
for fi in range(len(sky_dir)):
    sky_dir[fi] = int(sky_dir[fi].split(".")[0])
sky_dir.sort()

top_sky = []

org_path = "./Tiles/Backgrounds/"
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


sky_img = pygame.image.load("./Tiles/Backgrounds/1.png")
sky_img = pygame.transform.scale(sky_img, (70, 70))
sky2_img = pygame.image.load("./Tiles/Backgrounds/5.png")
sky2_img = pygame.transform.scale(sky2_img, (60, 60))
sky3_img = pygame.image.load("./Tiles/Backgrounds/6.png")
sky3_img = pygame.transform.scale(sky3_img, (60, 60))
sky4_img = pygame.image.load("./Tiles/Backgrounds/7.png")
sky4_img = pygame.transform.scale(sky4_img, (60, 60))
sky5_img = pygame.image.load("./Tiles/Backgrounds/8.png")
sky5_img = pygame.transform.scale(sky5_img, (60, 60))
sky6_img = pygame.image.load("./Tiles/Backgrounds/9.png")
sky6_img = pygame.transform.scale(sky6_img, (60, 60))


grass_img = pygame.image.load("./Tiles/tile_0022.png")
grass_rect = grass_img.get_rect()



dirt_rects = [rects for rects in make_ground(screen, "./Tiles/tile_0005.png", 18)]
                             

tree1_img, tree1_rect = make_tree("./Tiles/tile_0137.png", 450, 232, 20, 20, (20, 20))
tree2_img, tree2_rect = make_tree("./Tiles/tile_0116.png", 450, 228, 20, 20, (20, 20))
tree3_img, tree3_rect = make_tree("./Tiles/tile_0136.png", 450, 211, 20, 20, (20, 20))
tree4_img, tree4_rect = make_tree("./Tiles/tile_0116.png", 450, 162, 20, 20,(20, 20))

leaves, leaves_rect = make_tree("./Tiles/tile_0017.png", 420, 122, 30, 30, (30, 30))
leaves2, leaves2_rect = make_tree("./Tiles/tile_0018.png", 443, 122, 30, 30, (30, 30))
leaves3, leaves3_rect = make_tree("./Tiles/tile_0019.png", 471, 122, 30, 30, (30, 30))
leaves4, leaves4_rect = make_tree("./Tiles/tile_0037.png", 420, 152, 30, 30, (30, 30))
leaves5, leaves5_rect = make_tree("./Tiles/tile_0038.png", 450, 152, 30, 30, (30, 30))
leaves6, leaves6_rect = make_tree("./Tiles/tile_0039.png", 470, 152, 30, 30, (30, 30))
leaves7, leaves7_rect = make_tree("./Tiles/tile_0059.png", 470, 182, 30, 30, (30, 30))
leaves8, leaves8_rect = make_tree("./Tiles/tile_0058.png", 440, 182, 30, 30, (30, 30))
leaves9, leaves9_rect = make_tree("./Tiles/tile_0057.png", 420, 182, 30, 30, (30, 30))

player_collision = False

flag = True

TILE_SIZE2 = 18

game_speed = 30

leaves_list = [(leaves,leaves_rect), (leaves2,leaves2_rect), (leaves3,leaves3_rect), (leaves4,leaves4_rect),
               (leaves5,leaves5_rect), (leaves6,leaves6_rect), (leaves7,leaves7_rect), (leaves8,leaves8_rect), (leaves9,leaves9_rect)]

farmer_player = pygame.image.load("./tractor.png").convert()
farmer_player = pygame.transform.scale(farmer_player, (160, 125))
farmer_rect = pygame.Rect(5, 390, 25, 18)
farmer_player.set_colorkey((255, 255, 255))

tractor_sound = pygame.mixer.Sound("tractor_sound.mp3")
tractor_sound.set_volume(0.5)
# tractor_sound.play(loops=-1)

bg_music = pygame.mixer.Sound("bg_sound.mp3")
bg_music.set_volume(0.7)
# bg_music.play(loops=-1)

enemy_list = [pygame.image.load("./Tiles/Characters/tile_0002.png"), pygame.image.load("./Tiles/Characters/tile_0003.png")]
enemy_list2 = [pygame.image.load("./Tiles/Characters/tile_0004.png"), pygame.image.load("./Tiles/Characters/tile_0005.png")]
enemy_list3 = [pygame.image.load("./Tiles/Characters/tile_0006.png"), pygame.image.load("./Tiles/Characters/tile_0007.png")]

enemy_list = [pygame.transform.scale(enemy, (50, 50)) for enemy in enemy_list]
enemy_list2 = [pygame.transform.scale(enemy2, (50, 50)) for enemy2 in enemy_list2]
enemy_list3 = [pygame.transform.scale(enemy3, (50, 50)) for enemy3 in enemy_list3]

rand_enemy = random.choice([enemy_list, enemy_list2, enemy_list3])
enemy_status = 0
e_x_pos = 0

y_ground_list = ["218", "236", "254", "272", "290", "308", "326", "344", "362", "380", "398", "416", "434"]
y_rand = random.choice(y_ground_list)

game_score = 0

font = pygame.font.Font("./fonts/AtariClassic-gry3.ttf", 25)

enemy_speed = 40

game_over = False

list_of_obstacles = [enemy_list, enemy_list2, enemy_list3]
obstacles = make_multi_enemies(list_of_obstacles)

y_grass = 0

while flag:

    # game_score += 1
    text = font.render(f"Score : {game_score}", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (530, 50)

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
    
    ground_rects_list = make_ground(screen, "./Tiles/tile_0022.png", 18)

    grass_wall = make_grass_wall(25, grass_img, grass_rect, 432)
    grass_wall2 = make_grass_wall(25, grass_img, grass_rect, 432, grass_x=682)

    if enemy_status == 0:
        enemy_status = 1
    else:
        enemy_status = 0


    screen.blit(tree1_img, tree1_rect)
    screen.blit(tree2_img, tree2_rect)
    screen.blit(tree3_img, tree3_rect)
    screen.blit(tree4_img, tree4_rect)
    for (s,r) in leaves_list:
        screen.blit(s,r)
    

    for c, r, s in obstacles:
        screen.blit(c[enemy_status], r)
        r.y += s


    # if r.x <= -750:
        


    screen.blit(farmer_player, farmer_rect)
    if farmer_rect.x >= WINDOW_SIZE[0]-farmer_player.get_width():
        if farmer_rect.y < 390:
            farmer_rect.x = 0
            farmer_rect.y += 18

    

    farmer_player_mask = pygame.mask.from_surface(farmer_player.convert_alpha())
    enemy_mask = pygame.mask.from_surface(c[enemy_status].convert_alpha())
    
    if farmer_player_mask.overlap(enemy_mask, offset=(r.x-farmer_rect.x, r.y - farmer_rect.y)):
        # if r.y - farmer_rect.y == 44:
        game_score -= 7
    
    if game_score == 0:
        game_over = True
    
    if game_score > 0:
        screen.blit(text, text_rect)
    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        
        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_RIGHT:
                farmer_rect.x += 22
                game_score += 5
                pygame.transform.flip(farmer_player, True, False)

            if event.key == pygame.K_LEFT:
                farmer_rect.x -= 22
                pygame.transform.flip(farmer_player, True, False)

            # if event.key == pygame.K_DOWN:
            #     if farmer_rect.y < 390:
            #         farmer_rect.y += 18

            # if event.key == pygame.K_UP:
            #     if farmer_rect.y > 156:
            #         farmer_rect.y -= 18
    

    pygame.display.flip()
    pygame.display.update()
    clock.tick(200000)