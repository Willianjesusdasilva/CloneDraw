from PIL import Image
import pyautogui

color = (255, 255, 255)
data_cord = []
im = Image.open('test.png')
size = width, heigth = im.size

rgb_im = im.convert('RGB')
print(len(data_cord))
for x in range(size[0]):
    
    for y in range(size[1]):
        
        r, g, b = rgb_im.getpixel((x, y))
        if (r,g,b) != color:
            data_cord.append([str(x),str(y)])
            print(len(data_cord))

for i in data_cord:
    pyautogui.moveTo(int(i[0]) + 250, int(i[1]) + 250,
                     0.001)
    pyautogui.click(button="left")
