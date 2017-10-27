"""
A tool for quickly and easily updating information on live MTG Streams

By: Jeff Hoogland
"""

import sys, os
from PySide.QtGui import *
from PySide.QtCore import *
from ui_MainWindow import Ui_MainWindow

from os import listdir
import os.path
import shutil

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.DataPath = "/media/Storage/Hex Images/Coverage Stuff/Data Files"
        self.SlidesPath = "/media/Storage/Hex Images/Coverage Stuff/PlayerSlides"
        
        self.SlideNames = []
        
        if not os.path.isdir(self.DataPath):
            os.makedirs(self.DataPath)
        
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL("timeout()"), self.update)
        self.timer.start(1500)
        
        self.show()
        
        self.assignWidgets()
        self.populateSlides()
    
    def update(self):
        #print("Tick")
        self.writeToFile("%s/CasterLeft.txt"%self.DataPath, self.casterName1.displayText())
        self.writeToFile("%s/CasterRight.txt"%self.DataPath, self.casterName2.displayText())
        self.writeToFile("%s/CastersShort.txt"%self.DataPath, self.castersShort.displayText())
        self.writeToFile("%s/TwitterHandles.txt"%self.DataPath, self.twitterHandles.displayText())
        self.writeToFile("%s/RoundCount.txt"%self.DataPath, self.roundInformation.displayText())
        self.writeToFile("%s/PlayerRecord1.txt"%self.DataPath, self.playerRecord1.displayText())
        self.writeToFile("%s/PlayerRecord2.txt"%self.DataPath, self.playerRecord2.displayText())
        self.writeToFile("%s/EventHashTag.txt"%self.DataPath, self.hashTag.displayText())
        self.writeToFile("%s/GameWinsTop.txt"%self.DataPath, self.gameWinsTop.displayText())
        self.writeToFile("%s/GameWinsBottom.txt"%self.DataPath, self.gameWinsBottom.displayText())
    
    def writeToFile(self, targetFile, writeText):
        if writeText:
            #print("Writing %s with text %s"%(targetFile, writeText))
            with open(targetFile, 'w') as myfile: #file is a builtin, don't name your file 'file'
                myfile.write(writeText)
    
    def assignWidgets(self):
        self.slideSelector.activated[str].connect(self.slideSelected)  
    
    def populateSlides(self):
        for f in listdir(self.SlidesPath):
            if f[-4:] == ".png":
                self.SlideNames.append(f)
        self.SlideNames.sort()
        for s in self.SlideNames:
            self.slideSelector.addItem(s)
        self.slideSelected(self.SlideNames[0])
    
    def slideSelected(self, slideName):
        OBSSlide = "%s/CurrentSlide.png"%self.SlidesPath
        #print(OBSSlide)
        if os.path.isfile(OBSSlide):
            os.remove(OBSSlide)
        shutil.copy("%s/%s"%(self.SlidesPath, slideName), OBSSlide)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit( ret )
