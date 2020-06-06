import ChaiMachine as chai
from Beverages import *
import sys

def main():

    beverages = [NONE, GINGER_TEA, ELAICHI_TEA, COFFEE, MILK, WATER]
    materials = ["none", "water", "milk", "tea", "ginger", "elaichi", "coffee", "sugar"]

    print("FILL INGRIDIENTS IN mL \n")
    cur_water = int(input("Enter water : "))
    cur_milk = int(input("Enter milk : "))
    cur_tea = int(input("Enter tea : "))
    cur_ginger = int(input("Enter ginger : "))
    cur_sugar = int(input("Enter sugar : "))
    cur_coffee = int(input("Enter coffee : "))
    cur_elaichi = int(input("Enter elaichi : "))

    # cur_water = 2
    # cur_milk = 2
    # cur_tea = 2
    # cur_ginger = 2
    # cur_sugar = 2
    # cur_coffee = 2
    # cur_elaichi = 2



    chaiMachine = chai.ChaiMachine(water=cur_water, 
        milk = cur_milk, 
        tea = cur_tea,
        ginger = cur_ginger,
        sugar = cur_sugar,
        coffee = cur_coffee,
        elaichi = cur_elaichi
    )

    while(True):
        print("\nPick a Choice:\n1] GINGER TEA\n2]ELAICHI TEA\n3] COFFEE\n4] MILK\n5]WATER 6] FILL INGRIDIENTS\n7]EXIT \n ")
        
        cur_order = int(input())
        if(cur_order <= 5):
            chaiMachine.makeDrink(beverages[cur_order])
        elif(cur_order == 6):
            print("\n\tPick a ingridient:\n1] WATER\n2] MILK\n3] TEA LEAVES\n4] GINGER SYRUP\n5] ELAICHI SYRUP\n6] COFFEE\n7]SUGAR\n ")
            cur_fill_order = int(input())
            print("Enter Quantity in mL: ")
            cur_quantity = int(input())
            chaiMachine.fill(materials[cur_fill_order], cur_quantity)
        elif(cur_order == 7):
            sys.exit()


        #chaiMachine.
        #chaiMachine.displayWarnings()

if __name__ == "__main__":
    main()