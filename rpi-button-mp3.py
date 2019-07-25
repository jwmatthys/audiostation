import pygame
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
       if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()
