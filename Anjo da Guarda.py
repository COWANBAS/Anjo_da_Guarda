import psutil
import time
import keyboard
import win32gui
import win32api
import win32con

Cor = (255, 0, 0)  
Local = (100, 100, 200, 20)  

def is_tibia_running():
    return any(
        process.info['name']
        and process.info['name'].lower() == 'client' 
        for process in psutil.process_iter(['name'])
    )

def press_shift_2():
    keyboard.press('shift')
    keyboard.press_and_release('2')
    keyboard.release('shift')

def cor_detectada():
    x0, y0, largura, altura = Local
    
    for x in range(x0, x0 + largura):
        for y in range(y0, y0 + altura):
            cor_pixel = win32gui.GetPixel(win32gui.GetDC(0), x, y)
            r = cor_pixel & 0xff
            g = (cor_pixel >> 8) & 0xff
            b = (cor_pixel >> 16) & 0xff
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
