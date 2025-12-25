import tkinter
import os 
from PIL import ImageTk, Image





 
class Submarine:
    canvas: tkinter.Canvas
    image : int
    __image_path: str = os.path.join(os.getcwd(), 'submarine.png')

    def __init__(self, canvas):
        self.canvas = canvas 
        image_file = Image.open(self.__image_path).resize((120,100), resample= Image.Resampling.LANCZOS)
        self.__image_src_right= ImageTk.PhotoImage(image_file.transpose(Image.FLIP_LEFT_RIGHT))
        self.__image_src_left= ImageTk.PhotoImage(image_file)
        self.image = self.canvas.create_image(200,200, image=self.__image_src_right)
        # self.image = self.canvas.create_image(200,200, image=self.submarine_left)
        self.direction = "left" 

    def __del__(self):
        self.canvas.delete(self.image)

    
    def move(self,event):

            if event.keysym == "Up":
                self.canvas.move(self.image, 0, -5)
            if event.keysym == "Down":
                self.canvas.move(self.image, 0, 5)
            if event.keysym == "Left":
                self.canvas.move(self.image, -5, 0)
                self.canvas.itemconfig(self.image, image = self.__image_src_left)
            if event.keysym == "Right":
                self.canvas.move(self.image, 5, 0)
                self.canvas.itemconfig(self.image, image = self.__image_src_right)
