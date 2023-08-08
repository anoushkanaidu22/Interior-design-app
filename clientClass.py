import random
#Each client is an object of this class
class Client:
    def __init__(self,name,imageLink,theme,budget,screenColor):
        self.name=name
        self.imageLink=imageLink
        self.theme=theme
        self.budget=budget
        self.screenColor=screenColor
    def getName(self):
        return self.name
    def getInfo(self):
        return f'Hello! My name is {self.name} and I would like \n a {self.theme} theme for my room! \n Your budget is ${self.budget}. I look forward \n to seeing what you create. Good luck!'
    def getLink(self):
        return self.imageLink
    def getScreenColor(self):
        return self.screenColor
    def getBudget(self):
        return self.budget
    def getTheme(self):
        return self.theme
#client images:
#Rose: from https://steamuserimages-a.akamaihd.net/ugc/1665728174054548044/B10CEA1CED0AECBDA8ACB3EEBDC2607D4E3F4484/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false
#Robert from: https://www.pinkvilla.com/imageresize/robert_downey_jr_opens_up_on_playing_iron_man.jpg?width=752&t=pvorg
#Ratatouille from https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-f3qxzs_4923c203.jpeg
#Superman from ttps://pngimg.com/uploads/superman/superman_PNG5.png

Rose=Client("Rose","https://steamuserimages-a.akamaihd.net/ugc/1665728174054548044/B10CEA1CED0AECBDA8ACB3EEBDC2607D4E3F4484/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false","pink",(random.randint(20,30))*100,"maroon1")
Robert=Client("Robert Downey Jr.","https://www.pinkvilla.com/imageresize/robert_downey_jr_opens_up_on_playing_iron_man.jpg?width=752&t=pvorg","good seating and storage",(random.randint(20,30))*100,"SkyBlue3")
Ratatouille=Client("Ratatouille","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-f3qxzs_4923c203.jpeg","vintage",(random.randint(20,30))*100,"OrangeRed4")
Superman=Client("Superman","https://pngimg.com/uploads/superman/superman_PNG5.png","blue",(random.randint(20,30))*100,"RoyalBlue3")
clients=[Superman,Rose,Robert,Ratatouille]
themes={"pink":"A pink theme is simple: just use as much pink as possible in your room!",\
"vintage":"Vintage interior design involces utilizing styles and decor \n from previous generations to create a pre-modern design. Reference \nthe year in which certain furniture was built!",\
"blue":"A blue theme is simple: just use as much blue as possible in your room!",\
"good seating and storage":"In this room, try to capture as much \n seating and storage as possible. \n Look at how many people each seating option can accomodate, \n and how much volume each storage space can hold."}

