import time
import csv

from numpy import str0

class DataHandler():
    def __init__(self,fileName):
        self.file=fileName
        self.timer=0
        self.gameActions=[]
        self.gameRewards=[]
        self.gameTime=[]
        self.epsilons=[]
        self.lr=[]
        self.lastWrite=0
        self.writeCount=2
        self.newAdded=0

    def startGame(self):
        temp=[]
        temp2=[]
        self.timer=time.time()
        self.gameActions.append(temp)
        self.gameRewards.append(temp2)

    def add(self,action,reward):
        self.gameActions[-1].append(action)
        self.gameRewards[-1].append(reward)
    
    def endGame(self,epsilon,learningRate):
        endTime=time.time()
        temp=[]
        self.gameTime.append(temp)
        self.gameTime[-1].append(endTime-self.timer)
        temp2=[]
        self.epsilons.append(temp2)
        self.epsilons[-1].append(epsilon)
        temp3=[]
        self.lr.append(temp3)
        self.lr[-1].append(learningRate)
        self.newAdded+=1
        if(self.newAdded==self.writeCount):
            self.saveToFile()

    def saveToFile(self):
        print("opening "+self.file)
        file = open(self.file, 'a')
        writer=csv.writer(file)
        for i in range(self.lastWrite,self.lastWrite+self.newAdded):
            temp=["Game "+str(i),""]
            writer.writerow(temp)
            temp2=["Actions ",""]
            writer.writerow(temp2)
            writer.writerow(self.gameActions[i])
            temp3=["Rewards ",""]
            writer.writerow(temp3)
            writer.writerow(self.gameRewards[i])
            temp4=["Time in seconds ",""]
            writer.writerow(temp4)
            writer.writerow(self.gameTime[i])
            temp5=["Epsilon ",""]
            writer.writerow(temp5)
            writer.writerow(self.epsilons[i])
            temp6=["Learning rate ",""]
            writer.writerow(temp6)
            writer.writerow(self.lr[i])
        self.lastWrite+=self.newAdded
        self.newAdded=0
        file.close()





