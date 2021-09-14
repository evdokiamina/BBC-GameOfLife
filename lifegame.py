import numpy as np
import pylab
import matplotlib.pyplot as plt  
import matplotlib.animation as animation 

maxRange = 100
minRange = 2

class GameOfLife:

    def __init__(self, minRange, maxRange):
        self.lifeGrid = np.zeros((maxRange, maxRange), dtype='i').reshape(maxRange,maxRange)
        numberOfLiveCells = np.random.randint(minRange*minRange, maxRange*maxRange)
        for i in range(numberOfLiveCells):
            rand_x = np.random.randint(0, maxRange)
            rand_y = np.random.randint(0, maxRange)
            if self.lifeGrid[rand_x, rand_y] == 0:
                self.lifeGrid[rand_x, rand_y] = 1
    
    def getLiveNeighbours(self, lifeGrid, pos_x, pos_y, maxRange):
        count = 0
        for i in [pos_x-1, pos_x, pos_x+1]:
            for j in [pos_y-1, pos_y, pos_y+1]:
                if (i>=0 and j>=0) and (i<maxRange and j<maxRange) and i!=j:
                    if lifeGrid[i,j] == 1:
                        count += 1
        return count

    def playGame(self, frameNum, img, lifeGrid, maxRange):
        tempGrid = lifeGrid.copy()
        for i in range(maxRange):
            for j in range(maxRange):
                tempCount = self.getLiveNeighbours(lifeGrid, i, j, maxRange)
                if lifeGrid[i,j] == 1:
                    if (tempCount>3 or tempCount<2):
                        tempGrid[i,j] = 0
                else:
                    if tempCount==3:
                        tempGrid[i,j] = 1
        img.set_data(tempGrid)
        self.lifeGrid[:]= tempGrid[:]
        return img,

    def main(self):
        # set up animation 
        fig, ax = plt.subplots() 
        img = ax.imshow(self.lifeGrid, interpolation='nearest') 
        ani = animation.FuncAnimation(fig, self.playGame, fargs=(img, self.lifeGrid, maxRange, ),
                                    frames = 50,
                                    interval=100,
                                    save_count=50)

        plt.show()        

if __name__ == '__main__': 
    game = GameOfLife(minRange, maxRange)
    game.main()
       
        

