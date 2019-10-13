import math
import sys
from PIL import Image
from GeneticAlgorithm import *
from Pixel import *
from Sector import *

sys.setrecursionlimit(1000000000)

def getColor(pX, pY):
    im = Image.open("garfield.jpg")  # Can be many different formats.
    pix = im.load()
    return pix[pX, pY]  # Get the RGBA Value of the a pixel of an image


def addPixel(pX, pY, pQuadrant, pColor):
    if pColor[0] > 127:
        if pColor[1] > 127:
            if pColor[2] >= 127:
                pQuadrant.increaseLigthYellow()
            else:
                pQuadrant.increaseYellow()
        elif pColor[1] == 127:
            if pColor[2] > 127:
                pQuadrant.increasePink()
            elif pColor[2] == 127:
                pQuadrant.increasePaloRosa()
            else:
                pQuadrant.increaseOrange()
        else:
            if pColor[2] > 127:
                pQuadrant.increaseRose()
            elif pColor[2] == 127:
                pQuadrant.increaseFuchsia()
            else:
                pQuadrant.increaseRed()
    elif pColor[0] == 127:
        if pColor[1] > 127:
            if pColor[2] > 127:
                pQuadrant.increaseLightLightBlue()
            elif pColor[2] == 127:
                pQuadrant.increaseLigthLime()
            else:
                pQuadrant.increaseLime()
        elif pColor[1] == 127:
            if pColor[2] > 127:
                pQuadrant.increaseLile()
            elif pColor[2] == 127:
                pQuadrant.increaseGrey()
            else:
                pQuadrant.increaseYellowGreen()
        else:
            if pColor[2] > 127:
                pQuadrant.increasePurpura()
            elif pColor[2] == 127:
                pQuadrant.increasePurple()
            else:
                pQuadrant.increaseWine()
    else:
        if pColor[1] > 127:
            if pColor[2] > 127:
                pQuadrant.increaseCeleste()
            elif pColor[2] == 127:
                pQuadrant.increaseLigthGreen()
            else:
                pQuadrant.increaseGreen()
        elif pColor[1] == 127:
            if pColor[2] > 127:
                pQuadrant.increaseLigthBlue()
            elif pColor[2] == 127:
                pQuadrant.increaseDarkTurquoise()
            else:
                pQuadrant.increaseDarkGreen()
        else:
            if pColor[2] > 127:
                pQuadrant.increaseBlue()
            elif pColor[2] == 127:
                pQuadrant.increaseDarkBlue()
            else:
                pQuadrant.increaseBlack()
    pQuadrant.listPixels.append(Pixel(pX, pY, pColor))


def obtainSample(pQuantDivi, porcentage):
    return round(1024 * 1024 / pQuantDivi * porcentage)


def createSectors(pQuantDiv, pLengthSector):
    xMin = 0
    yMin = 0
    yMax = pLengthSector
    xMax = pLengthSector
    sectorList = []
    for fila in range(1, pQuantDiv + 1):
        for columna in range(1, pQuantDiv + 1):
            sectorList.append(Sector(xMin, xMax, yMin, yMax))
            xMin += pLengthSector
            xMax += pLengthSector
        xMin = 0
        xMax = pLengthSector
        yMin += pLengthSector
        yMax += pLengthSector
    return sectorList


def mapSample(pSample, randomProbability, pSectorList):
    probability = 0.0
    for quadrant in pSectorList:
        for cant_Sample in range(0, pSample):
            if quadrant.probability > randomProbability:
                randomX = random.randint(quadrant.xMin, quadrant.xMax - 1)
                randomY = random.randint(quadrant.yMin, quadrant.yMax - 1)
                color = getColor(randomX, randomY)
                if color[0] <= 254 and color[1] <= 254 and color[2] <= 254:
                    addPixel(randomX, randomY, quadrant, color)
                    probability += 0.008
                else:
                    probability -= 0.05
        quadrant.probability += probability
        probability = 0.0


def mapSector(pQuantSample, pQuantDiv):
    global svgStringGrande
    sectorList = createSectors(pQuantDiv, round(1023 / pQuantDiv))
    sample = round(pQuantSample / 4)
    for cant in range(1, 5):
        print(cant)
        randomProbability = random.uniform(0.1, 1.0)
        #print("-----------------------------------------------------")
        #print("I: ", cant, "Random:", randomProbability)
        mapSample(sample, randomProbability, sectorList)
        #print("-----------------------------------------------------")
    for j in range(1, 11):
        i = 1
        for sector in sectorList:
            print('Sector', i)
            if len(sector.listPixels) != 0:
                sector.porcentajePorColor()
                Genetic(sector, j)
            #    print('------------------------------------------------------------------')
            i += 1
        if j % 2 == 0 or j == 1:
            terminarSVG(j)


def sampling(pQuantDiv, pPorcentage):
    quantSample = obtainSample(pQuantDiv, pPorcentage)
    print("Cant: ", quantSample)
    mapSector(quantSample, pQuantDiv)


def paintCuadricula(pX, pY, pImage):
    pix = pImage.load()
    pix[pX, pY] = (0, 100, 0)


sampling(16, 0.0001)
