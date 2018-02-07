preVal, val, nextVal= 0 , 0 , 0,
peakList = []
items = {2:"test", 6.5:"test2"} #float keys

#Peak weight loop
#Adds the most recent value in the stream, calculates if the previous value was a peak
def peakValLoop(nextVal):
    if(val > preVal and val > nextVal):
        peakList.append(val)
    preVal = val
    val = nextVal

#Obtain items from peak weight values
#Assuming unique weight values per item    
def getSaleFromWeights(weights):
    weights.insert(0,0) #Initial emoty state for difference calculations
    weightDelta = []
    saleItems = []
    for i in range(len(weights)-1,0,-1):
        weightDelta.append(weights[i]-weights[i-1])
    for i in weightDelta:
        for j in items.keys():
            if approxEqual(i,j):
                saleItems.append(items[j])
    return saleItems
            
            
def approxEqual(x,y,tolerance=0.5):
    if abs(x-y) <= tolerance:
        return True
    else:
        return False