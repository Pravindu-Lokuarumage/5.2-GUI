from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

ledR = LED(14)
ledG = LED(10)
ledB = LED(3)

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight ='bold')

def ledToggleRed():
    if ledR.is_lit:
        ledR.off()
        ledButton["text"] = "Turn Red LED on"
    else:
        ledR.on()
        ledButton["text"] = "Turn Red LED off"
def ledToggleGreen():
    if ledG.is_lit:
        ledG.off()
        ledButton["text"] = "Turn Green LED on"
    else:
        ledG.on()
        ledButton["text"] = "Turn Green LED off"
def ledToggleBlue():
    if ledB.is_lit:
        ledB.off()
        ledButton["text"] = "Turn Blue LED on"
    else:
        ledB.on()
        ledButton["text"] = "Turn Blue LED off"

ledButtonRed = Button(win, text = 'Turn Red LED On', font = myFont, command = ledToggleRed, bg = 'bisque2', height = 1, width = 24)
ledButtonRed.grid(row =0, column = 1)
ledButtonGreen = Button(win, text = 'Turn Green LED On', font = myFont, command = ledToggleGreen, bg = 'bisque2', height = 1, width = 24)
ledButtonGreen.grid(row =0, column = 2)
ledButtonBlue = Button(win, text = 'Turn Blue LED On', font = myFont, command = ledToggleBlue, bg = 'bisque2', height = 1, width = 24)
ledButtonBlue.grid(row =0, column = 3)
