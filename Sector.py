import Pixel
from Pixel import *
from Color import *

negro = Color("Negro", (0, 0, 0))
azul = Color("Azul", (0, 0, 255))
verde = Color("Verde", (0, 255, 0))
celeste = Color("Celeste", (0, 255, 255))
rojo = Color("Rojo", (255, 0, 0))
morado = Color("Morado", (255, 0, 255))
amarillo = Color("Amarillo", (255, 255, 0))


class Sector:
    def __init__(self, xMin, xMax, yMin, yMax):
        self.listPixels = []
        self.porcentageColor = 0.0
        self.probability = 1.0
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.matrizColores = [[negro, azul, verde, celeste, rojo, morado, amarillo], [0, 0, 0, 0, 0, 0, 0]]

    def getPixels(self):
        return self.listPixels

    def printPixels(self):
        for pixel in self.listPixels:
            print("(" + str(pixel.getCordX()) + "," + str(pixel.getCordY()) + ") " + str(pixel.getColor()))

    def getPorcentage(self):
        return self.porcentageColor

    def setPixels(self, pixels):
        self.listPixels = pixels

    def porcentaje(self):
        R = 0
        G = 0
        B = 0
        i = 0
        for pixel in self.listPixels:
            R = R + pixel.getColor()[0]
            G = G + pixel.getColor()[1]
            B = B + pixel.getColor()[2]
            i = i + 1
        if i == 0:
            return (255, 255, 255)
        else:
            return (R / i, G / i, B / i)

    def getPoints(self):
        pixelsPoligono = []
        for pixel in self.listPixels:
            pixelsPoligono.append(pixel)

        return pixelsPoligono

    def porcentajePorColor(self):
        cantidadMuestra = len(self.listPixels)
        largoColor = 0
        while largoColor < len(self.matrizColores[0]):
            color = self.matrizColores[0][largoColor]
            cantidadColores = self.matrizColores[1][largoColor]
            if cantidadMuestra > 0:
                color.porcentage = 100/cantidadMuestra * cantidadColores
                if(color.porcentage > 0):
                    print("Cantidad Color:", cantidadColores)
                    print("Color: ", color.nombre, " Porcentaje: ", color.porcentage)
            largoColor += 1

    def aumentarNegros(self):
        self.matrizColores[1][0] += 1

    def aumentarAzules(self):
        self.matrizColores[1][1] += 1

    def aumentarVerde(self):
        self.matrizColores[1][2] += 1

    def aumentarCeleste(self):
        self.matrizColores[1][3] += 1

    def aumentarRojo(self):
        self.matrizColores[1][4] += 1

    def aumentarMorado(self):
        self.matrizColores[1][5] += 1

    def aumentarAmarillo(self):
        self.matrizColores[1][6] += 1
