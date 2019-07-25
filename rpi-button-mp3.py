import pygame
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()