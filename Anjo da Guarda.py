import psutil
import time
from PIL import ImageGrab
from pynput.keyboard import Controller, Key

Cor = (210, 106, 106) 
Local = (193, 7, 143, 6) 

keyboard_controller = Controller()

def is_tibia_running():
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] and process.info['name'].lower() == 'client':
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  
    return False

def press_shift_2():
    keyboard_controller.press(Key.shift)  
    keyboard_controller.press('2')
    keyboard_controller.release('2')
    keyboard_controller.release(Key.shift)  

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
    cor_detectada_ultima_vez = False  

    while True:
        if is_tibia_running():  
            if not tibia_aberto:
                tibia_aberto = True  
            if cor_detectada():  
                if not cor_detectada_ultima_vez:  
                    press_shift_2()  
                    cor_detectada_ultima_vez = True  
            else:
                cor_detectada_ultima_vez = False  
        else:
            if tibia_aberto:
                tibia_aberto = False  

        time.sleep(0.01)  

if __name__ == "__main__":
    main()
