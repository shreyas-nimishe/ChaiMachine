
from ... import ChaiMachine, Beverages

def initializeTests():
    chaiMachine = ChaiMachine(water=cur_water, 
        milk = 300, 
        tea = 60,
        ginger = 30,
        sugar = 60,
        coffee = 50,
        elaichi = 45
    )


#do this for all drinks
def testMakeWaterWhenAvailaible():
	assert chaiMachine.isAvailaible("water") == True

def testMakeWaterWhenUnavailaible():
	chaiMachine.makeDrink("water")
	chaiMachine.makeDrink("water")

	assert chaiMachine.isAvailaible("water") == False

def testFillWater():

	assert chaiMachine.isAvailaible("water") == False
	
	chaiMachine.fill("water", 50)

	assert chaiMachine.isAvailaible("water") == True


if __name__ == "__main__":

    initializeTests()
    testMakeDrink()
    testMakeWaterWhenAvailaible()
    testMakeWaterWhenUnavailaible()
    testFillWater()


    print("Everything passed")