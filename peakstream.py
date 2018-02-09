import statistics as st

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

    
def zscorePeak(y, lag=5, threshold=3.5,influence=0.5): #y=sensor data
    signals = [0]*len(y)
    filteredY = y[0:lag+1]
    avgFilter, stdFilter = [0]*(len(y)+lag),[0]*(len(y)+lag)
    avgFilter[lag] = st.mean(y[1:lag+1])
    stdFilter[lag] = st.stdev(y[1:lag+1])
    
    for i in range(lag+1,len(y)-1):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter[i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1
            filteredY.insert(i,influence * y[i] + (1-influence)*filteredY[i-1]) #Might need to be changed to raw y(i)
        else:
            signals[i] = 0
            filteredY.insert(i,y[i])
        avgFilter[i] = st.mean(filteredY[i-lag:i+1])
        stdFilter[i] = st.stdev(filteredY[i-lag:i+1])
    return signals, filteredY
        

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