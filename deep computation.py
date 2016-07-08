class level:
    def __init__(self,ID,haarSize=(1,1),outputs=1):
        self.haarSize=haarSize
        self.outputs=outputs
        self.name=str(ID)
        self.haars=[[[0 for x in range(haarSize[0])] for y in haarSize[1]] for z in outputs]

    def proces(self,inputMatrix=(1,1,1)):
        outputSize=(inputs[0]-self.haarSize[0],inputs[1]-self.haarSize[1],self.outputs)
        outputMatrix=[]
        for i in range(self.outputs):
            outputMatrix.append(haarResult(self.haars[i],inputMatrix[i]))

    def haarResult(haar,matrix):
        result=0
        for (haarRow, martrixRow) in zip(haar,matrix):
            for (haarValue,matrixValue)in zip(haar,matrix):
                result+=haarValue*matrixValue
        return result/(len(haar)*len(haar[0]))
    
