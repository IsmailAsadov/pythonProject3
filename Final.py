import sqlite3
import cv2
from PIL import Image
i = 0
connection  = sqlite3.connect('final.sl3', 5)
cur = connection.cursor
cur.execute("CREATE TABLE if not exists final_t (input_data TEXT, output_data TEXT);")
image_path = 'cross.jpg'
cross = Image.open(image_path)
stop_it = Image.open("images.png")

cross = cross.convert('RGBA')
stop_it = stop_it.convert('RGBA')
cross.paste(stop_it, (50,10,), stop_it)
cross.save('cross+stop_it.jpg')
if i<10:
    i+=1
    inp = str(input('What do you wanna search for'))
    cur.execute('INSERT INTO final_t (inp) VALUES(?)', (inp))
    print("you search has been added to BD")
else:
    cv2.imshow('cross+stop_it.jpg')
    cv2.waitKey()