import warnings
warnings.filterwarnings('ignore')

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from skimage import io
import numpy as np
import pyclesperanto_prototype as cle
from plotcanvas import PlotCanvas
from termcolor import colored
from MasterSegmenter import MasterSegmenter
import os
import colorcet as cc

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 601)
        MainWindow.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Canvas_1 = PlotCanvas(self.centralwidget)
        self.Canvas_1.setGeometry(QtCore.QRect(30, 10, 400, 400))
        self.Canvas_1.setObjectName("Canvas_1")
        self.Canvas_2 = PlotCanvas(self.centralwidget)
        self.Canvas_2.setGeometry(QtCore.QRect(450, 10, 400, 400))
        self.Canvas_2.setObjectName("Canvas_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(100, 460, 121, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_threshold = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_threshold.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_threshold.setObjectName("label_threshold")
        self.gridLayout_2.addWidget(self.label_threshold, 1, 0, 1, 1)
        self.INPUT_BGnoise = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.INPUT_BGnoise.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_BGnoise.setObjectName("INPUT_BGnoise")
        self.gridLayout_2.addWidget(self.INPUT_BGnoise, 0, 1, 1, 1)
        self.label_BGnoise = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_BGnoise.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_BGnoise.setObjectName("label_BGnoise")
        self.gridLayout_2.addWidget(self.label_BGnoise, 0, 0, 1, 1)
        self.INPUT_Threshold = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.INPUT_Threshold.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Threshold.setObjectName("INPUT_Threshold")
        self.gridLayout_2.addWidget(self.INPUT_Threshold, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(250, 460, 121, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_outline = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_outline.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_outline.setObjectName("label_outline")
        self.gridLayout_3.addWidget(self.label_outline, 1, 0, 1, 1)
        self.INPUT_Spot = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.INPUT_Spot.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Spot.setObjectName("INPUT_Spot")
        self.gridLayout_3.addWidget(self.INPUT_Spot, 0, 1, 1, 1)
        self.label_spot = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_spot.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_spot.setObjectName("label_spot")
        self.gridLayout_3.addWidget(self.label_spot, 0, 0, 1, 1)
        self.INPUT_Outline = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.INPUT_Outline.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Outline.setObjectName("INPUT_Outline")
        self.gridLayout_3.addWidget(self.INPUT_Outline, 1, 1, 1, 1)
        self.Slider_1 = QtWidgets.QSlider(self.centralwidget)
        self.Slider_1.setGeometry(QtCore.QRect(30, 420, 400, 16))
        self.Slider_1.setStyleSheet("QSlider::handle:horizontal {\n"
"background-color: rgb(135, 203, 203);\n"
"border: 1px solid #5c5c5c;\n"
"width: 10px;\n"
"border-radius: 3px;\n"
"}")
        self.Slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_1.setObjectName("Slider_1")
        self.BUTTON_Segment = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_Segment.setGeometry(QtCore.QRect(540, 460, 81, 41))
        self.BUTTON_Segment.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgb(90, 90, 90);\n"
"font-weight: bold\n"
"")
        self.BUTTON_Segment.setObjectName("BUTTON_Segment")
        self.BUTTON_SEGMENTALL = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_SEGMENTALL.setGeometry(QtCore.QRect(650, 450, 91, 61))
        self.BUTTON_SEGMENTALL.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgb(90, 90, 90);\n"
"font-weight: bold")
        self.BUTTON_SEGMENTALL.setObjectName("BUTTON_SEGMENTALL")
        self.Slider_2 = QtWidgets.QSlider(self.centralwidget)
        self.Slider_2.setGeometry(QtCore.QRect(450, 420, 400, 16))
        self.Slider_2.setStyleSheet("QSlider::handle:horizontal {\n"
"background-color: rgb(135, 203, 203);\n"
"border: 1px solid #5c5c5c;\n"
"width: 10px;\n"
"border-radius: 3px;\n"
"}")
        self.Slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_2.setObjectName("Slider_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(580, 530, 118, 23))
        self.progressBar.setStyleSheet("selection-background-color: rgb(135, 203, 203);\n"
"color:rgb(0,0,0)")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Button_Open = QtWidgets.QAction(MainWindow)
        self.Button_Open.setObjectName("Button_Open")
        self.menuFile.addAction(self.Button_Open)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MasterSegmenter_v1"))
        self.label_threshold.setText(_translate("MainWindow", "Threshold"))
        self.INPUT_BGnoise.setText(_translate("MainWindow", "20"))
        self.label_BGnoise.setText(_translate("MainWindow", "BG noise"))
        self.INPUT_Threshold.setText(_translate("MainWindow", "200"))
        self.label_outline.setText(_translate("MainWindow", "σ outline"))
        self.INPUT_Spot.setText(_translate("MainWindow", "1"))
        self.label_spot.setText(_translate("MainWindow", "σ spot"))
        self.INPUT_Outline.setText(_translate("MainWindow", "1"))
        self.BUTTON_Segment.setText(_translate("MainWindow", "SEGMENT"))
        self.BUTTON_SEGMENTALL.setText(_translate("MainWindow", "SEGMENT \n"
" FOLDER"))
        self.menuFile.setTitle(_translate("MainWindow", "File..."))
        self.Button_Open.setText(_translate("MainWindow", "Open TIFF"))
        
        ##############################
        # INITIALIZE GPU
        ##############################
        GPUs = cle.available_device_names()
        cle.select_device(GPUs[0])
        print('-'*60)
        print(colored('The GPU ' + GPUs[0] + ' has been selected for MasterSegmenter', 'cyan'))
        print('-'*60)


        ##############################
        # GADGET DISABLING
        ##############################
        self.Slider_1.setEnabled(False)
        self.Slider_2.setEnabled(False)
        self.BUTTON_Segment.setEnabled(False)
        self.BUTTON_SEGMENTALL.setEnabled(False)
        
        ##############################
        # BUTTON CONNECTION
        ##############################
        self.Button_Open.triggered.connect(self.OpenDialogTIFF)
        self.Slider_1.valueChanged.connect(self.Explore_ZStack)
        self.Slider_2.valueChanged.connect(self.Explore_ZStack_2)
        self.BUTTON_Segment.clicked.connect(self.Segment)
        self.BUTTON_SEGMENTALL.clicked.connect(self.SegmentAll)
        
        # custom colormap        
        from matplotlib.colors import LinearSegmentedColormap
        #self.mycmap = [[0,255,128]]*256 # greenish
        self.mycmap = cc.glasbey_bw_minc_20_minl_30
        self.mycmap[0]=[0,0,0] # add black as first value
        self.my_cmap=LinearSegmentedColormap.from_list('mycmap', self.mycmap)
###############################################################################
        # My functions, in order of usage in the program
###############################################################################
        
        
        
# FUNCTION TO OPEN FILE DIALOG AND IMPORT TIFF          	 
    def OpenDialogTIFF(self):
        fileNameTIFF = QFileDialog.getOpenFileName(self, 'Open File', '/media/alejandro/Coding/MyGits/MasterSegmenter_GitHub/', 
                                                   ('Image Files(*.tiff, *.tif)') )   
        # avoid crash, else pick name
        if fileNameTIFF[0] == '':
            return None
        else:    
            self.fileNameTIFF = fileNameTIFF[0]
            self.FolderName = os.path.dirname(fileNameTIFF[0])
            print('Loading image...')
        # load (the slow operation)
        self.LoadedTIFF = io.imread(self.fileNameTIFF)    
        # show first frame
        self.ax_1 = self.Canvas_1.figure.add_subplot(111)
        self.ax_1.imshow(self.LoadedTIFF[0,:,:])
        self.ax_1.axis('off')
        self.Canvas_1.draw()
#        # show frame number
        self.NumberOfLayers = np.shape(self.LoadedTIFF)[0]        
##        self.FrameNumber = str(1) + ' / ' +str(self.NumberOfLayers)
##        self.frametext = self.ax_1.text(0.05, 0.95, self.FrameNumber ,verticalalignment='top', 
##         horizontalalignment='left', transform=self.ax_1.transAxes,
##         color='white', fontsize=8)
##        self.Canvas_1.draw()
        
        # activate and update range of z slider, segment button
        self.Slider_1.setEnabled(True)
        self.Slider_1.setMinimum(0)
        self.Slider_1.setMaximum(self.NumberOfLayers-1)
        self.BUTTON_Segment.setEnabled(True)
    
# EXPLORE Z STACK
    def Explore_ZStack(self):
        # get scroll value
        self.ZPositionSlider = self.Slider_1.value()
        # clear axes and plot again the selected frame
        self.Canvas_1.axes.cla()
        self.ax_1.imshow(self.LoadedTIFF[self.ZPositionSlider, :, :]) 
        
#        # show new frame number
#        self.frametext.remove()
#        self.FrameNumber = str(self.ZPositionSlider+1) + ' / '+str(self.NumberOfLayers)
#        self.frametext = self.ax_1.text(0.05, 0.95, self.FrameNumber ,verticalalignment='top', 
#         horizontalalignment='left', transform=self.ax_1.transAxes,
#         color='white', fontsize=8)
        self.Canvas_1.draw()



# Segment and show the loaded tiff   
    def Segment(self):
        print('Segmenting...')
        # fetch inputs
        self.backg_r = int(self.INPUT_BGnoise.text())
        self.thr = int(self.INPUT_Threshold.text())
        self.s_spot = int(self.INPUT_Spot.text())
        self.s_outl = int(self.INPUT_Outline.text())
        
        # Run and echo
        self.imbeads, self.n, self.radii = MasterSegmenter(self.fileNameTIFF,
                                                           backg_r=self.backg_r, 
                                                           threshold=self.thr, 
                                                           spot_sigma=self.s_spot, 
                                                           outline_sigma=self.s_outl)
        print(f'# beads found: {self.n}')
        print(colored('SEGMENTED \n', 'green'))
        
        # Plot segmentation on second canvas (include antialiasing)
        self.ax_2 = self.Canvas_2.figure.add_subplot(111)
        self.ax_2.imshow(self.imbeads[0,:,:], cmap=self.my_cmap,interpolation='nearest')#self.my_cmap)
        self.ax_2.axis('off')
        self.Canvas_2.draw()
        
        # Activate slider and update
        self.Slider_2.setEnabled(True)
        self.Slider_2.setMinimum(0)
        self.Slider_2.setMaximum(self.NumberOfLayers-1)
        
        # Activate the option "Segment all"
        self.BUTTON_SEGMENTALL.setEnabled(True)

# EXPLORE Z STACK OF SEGMENTED IMAGE
    def Explore_ZStack_2(self):
        # get scroll value
        self.ZPositionSlider_2 = self.Slider_2.value()
        
        # If we synchronize the other scroll, it will also plot
        #self.Slider_1.setValue(self.ZPositionSlider_2)
        
        # Plot segmented picture
        self.Canvas_2.axes.cla()
        self.ax_2.imshow(self.imbeads[self.ZPositionSlider_2, :, :], cmap=self.my_cmap,interpolation='nearest') 
        self.Canvas_2.draw()

               
# Segment the whole folder with the desired parameters and save output
    def SegmentAll(self):
        # Look for .tiffs in the folder and list them
        self.AllowedExtensions = (".tiff", ".tif")
        self.AllTIFFS = [f for f in os.listdir(self.FolderName) if f.endswith(tuple(self.AllowedExtensions))]
        self.SaveDir = os.path.join(self.FolderName, 'Segmentations')
        os.mkdir(self.SaveDir)
        
        for i, tiff in enumerate(self.AllTIFFS):
            filename_t = os.path.join(self.FolderName, tiff)
            print(colored('SEGMENTING '+filename_t+'...', 'magenta'))
            # Run iteration            
            self.imbeads_t, self.n_t, self.radii_t = MasterSegmenter(filename_t,
                                                           backg_r=self.backg_r, 
                                                           threshold=self.thr, 
                                                           spot_sigma=self.s_spot, 
                                                           outline_sigma=self.s_outl)
            print(f'Found beads: {self.n_t} \n')
            # Save image depending on how many beads we have, to save space
            if self.n_t <= 255:    
                io.imsave(os.path.join(self.SaveDir,tiff), self.imbeads_t.astype('uint8'))
            else:
                io.imsave(os.path.join(self.SaveDir,tiff), self.imbeads_t.astype('uint16'))
                
            # Save bead radii
            filename_txt = os.path.join(self.SaveDir, tiff.rsplit('.')[0]+'.txt')
            with open(filename_txt, 'w') as f:
                f.write('\n'.join(map(str, self.radii_t)))
                
            
            # Update progress bar
            self.progressBar.setValue(int((i+1)*100/len(self.AllTIFFS)))
        print(colored('SEGMENTATION COMPLETE', 'green'))

            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
