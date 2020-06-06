
  
import random


class ChaiMachine:
    def __init__(self):
        self.materials = dict( water=0, milk=0, tea=0, ginger = 0, sugar = 0, coffee = 0, elaichi = 0)


    def __init__(self, water, milk, tea, ginger, sugar, coffee, elaichi):
        self.materials = dict( water=0, milk=0, tea=0, ginger = 0, sugar = 0, coffee = 0, elaichi = 0)

        self.materials["water"] += water/50
        self.materials["milk"] += milk/10
        self.materials["tea"] += tea/10
        self.materials["ginger"] += ginger/5
        self.materials["sugar"] += sugar/10
        self.materials["coffee"] += coffee/10
        self.materials["elaichi"] += elaichi/5


    def fill(self, material, quantity):

        if(material in ["milk", "tea", "sugar", "coffee"]):
            quantity /= 10
        elif(material in["elaichi", "ginger"]):
            quantity /= 5
        else:
            quantity /= 50

        self.materials[material] += quantity


    def isAvailaible(self, drink):
        warnings = []
        status = True;

        print(self.materials )

        for key in self.materials:
            if(self.materials[key] < drink[key]):
                status = False
            
            if(self.materials[key] < 5 ):
                warnings.append(key);


        #print(warnings)
        for warn in warnings:
            print("Warning: Low " + warn + " ,less than 5 units left")
        
        return status


    def makeDrink(self, drink):


        if(self.isAvailaible(drink)):
            for material in self.materials:
                self.materials[material] -= drink[material]

            print("\nHello!, Your " + drink["name"] + " is ready!\n\n\n")
        else:
            
            print("\nSorry!, Your " + drink["name"] + " is currently unavailaible!\n\n\n")
        