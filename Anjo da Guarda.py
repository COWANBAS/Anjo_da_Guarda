import psutil
import time
import keyboard
from PIL import ImageGrab

Cor = (255, 0, 0)  
Local = (100, 100, 200, 20) 

def is_tibia_running():
    return any(
        process.info['name'] and process.info['name'].lower() == 'client'
        for process in psutil.process_iter(['name'])
    )

def press_shift_2():
    keyboard.press('shift')
    keyboard.press_and_release('2')
    keyboard.release('shift')

def cor_detectada():
    x0, y0, largura, altura = Local
    screenshot = ImageGrab.grab(bbox=(x0, y0, x0 + largura, y0 + altura)) 
    pixels = screenshot.load()  

    for x in range(largura):
        for y in range(altura):
            r, g, b = pixels[x, y]  
            if (r, g, b) == Cor:
                return True  
    return False  

def main():
    tibia_aberto = False

    while True:
        if is_tibia_running():  
            if not tibia_aberto:
                tibia_aberto = True  

            if cor_detectada():  
                press_shift_2()  
        else:
            if tibia_aberto:
                tibia_aberto = False  

        time.sleep(0.01)  

if __name__ == "__main__":
    main()
