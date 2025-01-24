import keras
from tkinter import Tk, Canvas, Button
from PIL import Image, ImageDraw
import cv2
import numpy as np
word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}
model = keras.models.load_model('semi_supervised_handwritten_model.h5')
model.summary()
root = Tk()
canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
img = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(img)
last_x, last_y = None, None

def motion(event):
    global last_x, last_y
    x, y = event.x, event.y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, x, y, width=10)
        draw.line((last_x, last_y, x, y), fill="black", width=10)
    last_x, last_y = x, y

def release(event):
    global last_x, last_y
    last_x, last_y = None, None

canvas.bind('<B1-Motion>', motion)
canvas.bind('<ButtonRelease-1>', release)

def save_image():
    resized_img = img.resize((280, 280))
    resized_img.save("drawn_image.jpg")
    print("Image saved as 'drawn_image.jpg'")

def load_image():
    img_cv2 = cv2.imread('drawn_image.jpg')
    if img_cv2 is None:
        print("Error: 'drawn_image.jpg' not found. Please save the image first.")
        return
    
    img_copy = img_cv2.copy()
    img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
    img_cv2 = cv2.resize(img_cv2, (400, 440))
    img_copy = cv2.GaussianBlur(img_copy, (7, 7), 0)
    img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
    img_final = cv2.resize(img_thresh, (28, 28))
    img_final = np.reshape(img_final, (1, 28, 28, 1))
    img_pred = word_dict[np.argmax(model.predict(img_final))]
    cv2.putText(img_cv2, "Image", (20, 25), cv2.FONT_HERSHEY_TRIPLEX, 0.7, color=(0, 0, 230))
    cv2.putText(img_cv2, "Prediction: " + img_pred, (20, 410), cv2.FONT_HERSHEY_DUPLEX, 1.3, color=(255, 0, 30))
    cv2.imshow('handwritten alphabet identification', img_cv2)
    
save_button = Button(root, text="Save Image", command=save_image)
save_button.pack()
root.mainloop()
load_image()
cv2.waitKey(0)
cv2.destroyAllWindows()
