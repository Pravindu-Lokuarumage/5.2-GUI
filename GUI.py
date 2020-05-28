from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

ledR = LED(14)
ledG = LED(10)
ledB = LED(17)
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight ='bold')
def Quit():
    GPIO.cleanup()
    win.destroy()
def ledToggleRed():
    if ledR.is_lit:
        ledR.off()
        ledButtonRed["text"] = "Turn Red LED on"
    else:
        ledR.on()
        ledButtonRed["text"] = "Turn Red LED off"
        ledG.off()
        ledButtonGreen["text"] = "Turn Green LED on"
        ledB.off()
        ledButtonBlue["text"] = "Turn Blue LED on"
def ledToggleGreen():
    if ledG.is_lit:
        ledG.off()
        ledButtonGreen["text"] = "Turn Green LED on"
    else:
        ledG.on()
        ledButtonGreen["text"] = "Turn Green LED off"
        ledR.off()
        ledButtonRed["text"] = "Turn Red LED on"
        ledB.off()
        ledButtonBlue["text"] = "Turn Blue LED on"
def ledToggleBlue():
    if ledB.is_lit:
        ledB.off()
        ledButtonBlue["text"] = "Turn Blue LED on"
    else:
        ledB.on()
        ledButtonBlue["text"] = "Turn Blue LED off"
        ledG.off()
        ledButtonGreen["text"] = "Turn Green LED on"
        ledR.off()
        ledButtonRed["text"] = "Turn Red LED on"

ledButtonRed = Button(win, text = 'Turn Red LED On', font = myFont, command = ledToggleRed, bg = 'bisque2', height = 1, width = 24)
ledButtonRed.grid(row =1, column = 0)
ledButtonGreen = Button(win, text = 'Turn Green LED On', font = myFont, command = ledToggleGreen, bg = 'bisque2', height = 1, width = 24)
ledButtonGreen.grid(row =2, column = 0)
ledButtonBlue = Button(win, text = 'Turn Blue LED On', font = myFont, command = ledToggleBlue, bg = 'bisque2', height = 1, width = 24)
ledButtonBlue.grid(row =3, column = 0)
Quit = Button(win, text = 'Quit', font = myFont, command = Quit, bg = 'bisque2', height = 1, width = 24)
Quit.grid(row =4, column = 0)
