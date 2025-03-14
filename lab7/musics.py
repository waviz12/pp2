import pygame
import os

pygame.init()

playlist = []
music_folder = "/Users/daniyartanerbergen/Documents/PP2/labs/lab7/musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

if not playlist:
    print("⚠ Ошибка: В папке нет аудиофайлов!")
    pygame.quit()
    exit()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Darkhan-Juzz")
clock = pygame.time.Clock()

music_elements_folder = "/Users/daniyartanerbergen/Documents/PP2/labs/lab7/music-elements"

background = pygame.image.load(os.path.join(music_elements_folder, "background.png"))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 20)

playb = pygame.image.load(os.path.join(music_elements_folder, "play.png"))
pausb = pygame.image.load(os.path.join(music_elements_folder, "pause.png"))
nextb = pygame.image.load(os.path.join(music_elements_folder, "next.png"))
prevb = pygame.image.load(os.path.join(music_elements_folder, "back.png"))

playb = pygame.transform.scale(playb, (70, 70))
pausb = pygame.transform.scale(pausb, (70, 70))
nextb = pygame.transform.scale(nextb, (70, 70))
prevb = pygame.transform.scale(prevb, (75, 75))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))

    screen.blit(background, (-50, 0))
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))

    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    
    screen.blit(nextb, (460, 587))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
