from PIL import ImageTk
import PIL.Image
import PIL.ImageOps
from tkinter import *
import time
import random
import copy



class App(Tk):
    def __init__ (self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        
        self.WIDTH_SCREEN = self.winfo_screenwidth() 
        self.HEIGHT_SCREEN = self.winfo_screenheight()

        self.canvas = Canvas(self, width = self.WIDTH_SCREEN, height = self.HEIGHT_SCREEN, bg = 'black')
        self.canvas.pack()

        self.width_logo = int(self.WIDTH_SCREEN / 10)
        self.height_logo = int(self.HEIGHT_SCREEN / 10)

        self.speed_x = .1
        self.speed_y = .1

        self.start_x = random.randint(0, self.WIDTH_SCREEN - self.width_logo)
        self.start_y = random.randint(0, self.HEIGHT_SCREEN - self.height_logo)

        self.current_x = self.start_x
        self.current_y = self.start_y

        self.img = None
        self.logos = []
        
        self.last_random = None
        self.prep_img()
        self.tkimage = ImageTk.PhotoImage(self.img)

        self.id = self.canvas.create_image(self.start_x, self.start_y, image = self.tkimage, anchor = NW)

        self.after(1, self.draw())


    def prep_img(self):
        self.img = PIL.Image.open("dvd_logo_master.png")
        self.img = self.img.resize((self.width_logo, self.height_logo), PIL.Image.ANTIALIAS)
        self.img = self.img.convert('RGB')


    def load_new_filter(self):
        r = random.randint(1,255)
        g = random.randint(1,255)
        b = random.randint(1,255)
        color = r, g, b

        helper = PIL.ImageOps.grayscale(self.img)
        helper = PIL.ImageOps.colorize(helper, (0, 0, 0), color)
        self.tkimage2 = ImageTk.PhotoImage(helper)
        self.canvas.itemconfig(self.id, image = self.tkimage2)
        

    def draw(self):
        if (self.current_x <= 0) or (self.current_x + self.width_logo >= self.WIDTH_SCREEN):
            self.speed_x = -self.speed_x
            self.load_new_filter()
        if (self.current_y <= 0) or (self.current_y + self.height_logo >= self.HEIGHT_SCREEN):
            self.speed_y = -self.speed_y
            self.load_new_filter()

        self.current_x += self.speed_x
        self.current_y += self.speed_y
        #print(str(self.current_x) + ", " + str(self.current_y))
        self.canvas.move(self.id, self.speed_x, self.speed_y)
        self.after(1, self.draw)



App().mainloop()
