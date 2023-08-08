import math
#every piece of furniture is part of this class, which has subclasses for each category
class Furniture:
    def __init__(self,name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState):
        self.name=name
        self.color=color
        self.theme=theme
        self.link=link
        self.price=price
        self.dimensions=dimensions #total length,total height
        self.year=year
        self.cx=cx
        self.cy=cy
        self.ogPos=ogPos
        self.mode=mode
        self.budgState=budgState
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def getLink(self):
        return self.link
    def getDimensions(self):
        return self.dimensions
    def getYear(self):
        return self.year
    def getPrice(self):
        return self.price
#checks for collisions: if the distance between the two centers of the objects is less than
#the sum of half of their widths and half of their heights, then they have collided
    def collided(self,other):
        if math.dist((self.cx,self.cy),(other.cx,other.cy))<=self.dimensions[0]/2+other.dimensions[0]/2 and\
            math.dist((self.cx,self.cy),(other.cx,other.cy))<=self.dimensions[1]/2+other.dimensions[1]/2:
            return True
        else:
            return False


def distance(x0,y0,x1,y1):
    distance=math.sqrt((x0-x1)**2+(y0-y1)**2)
    return distance

class Couch(Furniture):
    def __init__(self,name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState,seating):
        self.seating=seating
        super().__init__(name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState)
    def getSeats(self):
        return self.seating
class Storage(Furniture):
    def __init__(self,name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState,volume):
        self.volume=volume
        super().__init__(name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState)
    def getVolume(self):
        return self.volume
class Lamp(Furniture):
    def __init__(self,name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState):
        super().__init__(name,theme,color,link,price,dimensions,cx,cy,year,ogPos,mode,budgState)

# brownCouch image from: https://www.pngall.com/wp-content/uploads/4/Sofa-PNG-Image.png
# pinkCouch image from: https://i.pinimg.com/originals/c3/bd/45/c3bd457319a3d456a165db19c0a88ad2.png
# blueCouch image from: https://www.pngmart.com/files/7/Sofa-Bed-Transparent-Background.png
# oldRug image from: https://www.pngall.com/wp-content/uploads/2017/03/Rug-Download-PNG.png
# oldLamp image from: https://cdn.pixabay.com/photo/2017/05/17/11/20/table-lamp-2320606_1280.png
# pinkLamp image from: https://www.marcusofficefurniture.com/wp-content/uploads/PIXIE-LED-PINK_800w_500h.png
# blueLamp image from: https://nilecreations.com/wp-content/uploads/2018/03/lamp-1.png
# bookshelf image from: https://www.pngmart.com/files/7/Bookshelf-PNG-File.png
# drawer image from: https://chairish-prod.freetls.fastly.net/image/product/master/4b112f9d-09c0-4f5c-a7a3-60b6f9cbbb29/verona-two-drawer-nightstand-in-hot-pink-4194
# blueDrawer image from: http://cdn.shopify.com/s/files/1/0203/4607/7284/products/LB-VBD12-3_2_1200x1200.png?v=1612162926
brownCouch=Couch("brownCouch","vintage","brown","https://www.pngall.com/wp-content/uploads/4/Sofa-PNG-Image.png",1000,(246,100),120,720,1981,(120,720),"couchesMode",True,4)
pinkCouch=Couch("pinkCouch","pink","pink","https://i.pinimg.com/originals/c3/bd/45/c3bd457319a3d456a165db19c0a88ad2.png",500,(260,100),400,720,2015,(400,720),"couchesMode",True,3)
blueCouch=Couch("blueCouch","blue","blue","https://www.pngmart.com/files/7/Sofa-Bed-Transparent-Background.png",800,(214,110),650,710,2020,(650,710),"couchesMode",True,3)
oldLamp=Lamp("oldLamp","vintage","plain","https://cdn.pixabay.com/photo/2017/05/17/11/20/table-lamp-2320606_1280.png",70,(54,90),180,730,1984,(180,730),"lampsMode",True)
pinkLamp=Lamp("pinkLamp","pink","pink","https://www.marcusofficefurniture.com/wp-content/uploads/PIXIE-LED-PINK_800w_500h.png",50,(54,80),480,720,2022,(480,720),"lampsMode",True)
blueLamp=Lamp("blueLamp","blue","blue","https://nilecreations.com/wp-content/uploads/2018/03/lamp-1.png",80,(50,80),600,720,2019,(600,720),"lampsMode",True)
bookshelf=Storage("bookshelf","vintage","tan","https://www.pngmart.com/files/7/Bookshelf-PNG-File.png",400,(70,115),200,700,1982,(200,700),"storageMode",True,80)
drawer=Storage("drawer","pink","pink","https://chairish-prod.freetls.fastly.net/image/product/master/4b112f9d-09c0-4f5c-a7a3-60b6f9cbbb29/verona-two-drawer-nightstand-in-hot-pink-4194",200,(90,90),400,730,2018,(400,730),"storageMode",True,40)
blueDrawer=Storage("drawer","blue","blue","http://cdn.shopify.com/s/files/1/0203/4607/7284/products/LB-VBD12-3_2_1200x1200.png?v=1612162926",200,(60,70),600,730,2010,(600,730),"storageMode",True,30)
couchList=[brownCouch,pinkCouch,blueCouch]
lampList=[oldLamp,pinkLamp,blueLamp]
storageList=[bookshelf,drawer,blueDrawer]
furnitureList=[brownCouch,pinkCouch,blueCouch,oldLamp,pinkLamp,blueLamp,bookshelf,drawer,blueDrawer]
