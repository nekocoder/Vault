import pygame

class ScrollingImage:
    def __init__(self, image, location, scrollrate):
        self.image = image
        self.location = location
        self.scrollrate = scrollrate

    def draw(self, screen, gametime):
        offset = (self.scrollrate*gametime)%1000 #hardcoded height of star images
                              #later, maybe add this to constructor if 
        screen.blit(self.image, (self.location[0], self.location[1]-offset))
        screen.blit(self.image, (self.location[0], self.location[1]-offset+1000))
        
