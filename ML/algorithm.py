#ok this is the algorthm
import statistics
import random
import numpy as np
#import weather/weathertest.py as wt
#ok so this is a baseine that we can change:






tempOfTheDay = random.randint(-10,110)

def func(tempBorders, lowCounterBoi, medCounterBoi, highCounterBoi, tempOfTheDay):
    print("Hi! How was our advice to you today?")
    print("Was it 'Too Hot', 'Too Cold' or 'Just Right'?")

    
    tempFeeling = input()



    if(tempFeeling== "Too Cold"):
        nearestBorder = tempBorders[tempBorders < tempOfTheDay].max()
        nearestIndex = np.where(tempBorders==nearestBorder)[0][0]
        if(nearestIndex == 1):
            tempBorders[nearestIndex] = (tempOfTheDay - (nearestBorder))*(0.5**lowCounterBoi)+nearestBorder
            lowCounterBoi+=1
        elif(nearestIndex == 2):
            tempBorders[nearestIndex] = (tempOfTheDay - (nearestBorder))*(0.5**medCounterBoi)+nearestBorder
            medCounterBoi+=1
        elif(nearestIndex == 3):
            tempBorders[nearestIndex] = (tempOfTheDay - (nearestBorder))*(0.5**highCounterBoi)+nearestBorder
            highCounterBoi+=1
    elif(tempFeeling== "Too Hot"):
        nearestBorder = tempBorders[tempBorders > tempOfTheDay].min()

        nearestIndex = np.where(tempBorders==nearestBorder)[0][0]

        if(nearestIndex == 1):
            tempBorders[nearestIndex] = nearestBorder - (nearestBorder - (tempOfTheDay))*(0.5**lowCounterBoi)
            lowCounterBoi+=1
        elif(nearestIndex == 2):
            tempBorders[nearestIndex] = nearestBorder - (nearestBorder - (tempOfTheDay))*(0.5**medCounterBoi)
            medCounterBoi+=1
        elif(nearestIndex == 3):
            tempBorders[nearestIndex] = nearestBorder- (nearestBorder - (tempOfTheDay))*(0.5**highCounterBoi)
            highCounterBoi+=1
    elif(tempFeeling == "Just Right" and (tempFeeling >(tempBorders[1] and tempBorders[3]))):
        medCounterBoi+=1
        if(tempBorders[3] - tempOfTheDay < tempOfTheDay- tempBorders[1]):
            highCounterBoi+=1
        else:
            lowCounterBoi+=1
    else:
        print("invalid option")
    return tempBorders


if __name__ == "__main__":
    tempBorders = np.array([-450,15.00001,40.000001,70.000001,2000])
    #lowTempTips = 15
    #medTempTips = 40
    #highTempTips = 70
    lowCounterBoi = 0
    medCounterBoi = 0
    highCounterBoi = 0
    print(tempOfTheDay)
    print(nearestIndex)
    print(lowCounterBoi+medCounterBoi+highCounterBoi)