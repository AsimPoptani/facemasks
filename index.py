# Please be aware this will calculate the optimal soloution but it will take time
# It is a brute force approach
# Also please be aware that I have only spent about 35 mins on this and it can be improved by using numpy matrix instead of for loops


import math ,numpy
def soloution(A,B,C):
    return min(A,B,C)

# Feel free to modify this. This is how long each cutter has.
timeGiven=(5*8*60*60)+5*60*5

# Feel free to modify this.
# Prep time in seconds
prepTime=30 


# Feel free to modify this.
# Workers e.g. AB = product A on Boxcutter
# Workers [timeToCut,numberOfItems,nItemsMade,timeTakenMatrix,unitsCreatedMatrix]
workers = {
        "AB": [(6*60)+51,21],
        "BB": [(8*60)+8,30],
        "CB": [(5*60),40],
        "AG": [(9*60),9],
        "CG": [(8*60)+40,21]
    }

# Loop through workers
for _, value in workers.items():
    # Add 30 seconds to each item 
    value[0]=value[0]+30
    # How many times can this product be made solely
    value.append(math.floor(timeGiven/value[0]))
    # Precalculate in a matrix the time it takes to make the product
    timeTaken=numpy.arange(value[2]+1) * value[0]
    # Precalculate in a matrix the number of units created
    partsCreated=numpy.arange(value[2]+1) * value[1]
    # Add it to the workers
    value.append(timeTaken)
    value.append(partsCreated)


# Keeps track of best soloution so far
bestSoloution=0
# Some loops :(
# Main Logic 
for AB in range(workers['AB'][2]+1):
    BoxcutterTime = int(timeGiven) -  workers['AB'][3][AB]
    GTime = int(timeGiven)
    for BB in range(int(BoxcutterTime/workers['BB'][0])+1):
        BoxcutterTime2=int(BoxcutterTime-workers['BB'][3][BB])
        if  BoxcutterTime2<0 or GTime<0:
            exit()
            continue
        
        CB=int(BoxcutterTime2/workers['CB'][0])
        BoxcutterTime3=BoxcutterTime2-workers['CB'][3][CB]
        if (not BoxcutterTime3>0) or (not GTime>0):
            continue
        
        for AG in range(int(GTime/workers['AG'][0])+1):
            GTime2=GTime-workers['AG'][3][AG]
            if (not BoxcutterTime3>0) or (not GTime2>0):
                continue
            CG= int(GTime2/workers['CG'][0])
                
            GTime3=GTime2-workers['CG'][3][CG]
            if (not BoxcutterTime>0) or (not GTime3>0):
                continue
            
            A=workers['AB'][4][AB]+workers['AG'][4][AG]
            B=workers['BB'][4][BB]
            C=workers['CB'][4][CB]+workers['CG'][4][CG]
            value=soloution(A,B,C)
            if value>bestSoloution:
                bestSoloution=value
                print(f"Facemasks Created: {bestSoloution} - Machine A: Ax{AB} Bx{BB} Cx{CB} Machine B: Ax{AG} Cx{CG} - Time elapsed M A:{timeGiven-BoxcutterTime3}s Time elapsed M B:{timeGiven-GTime3}s Units: A:{A} B:{B} C:{C}")
            
