import keyboard
import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(2)

button_pressed = False

def on_key_press(e):
    global button_pressed
    
    if not button_pressed:
        print(f'button {e.name} pressed')
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('press.mp3'))
        button_pressed = True
    else:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('release.mp3'))
        button_pressed = False  
    
keyboard.hook(on_key_press)

keyboard.wait("esc")  # to close the program