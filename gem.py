
import os
import sys
from os import chdir
from os.path import join
import argparse
import json
import tempCSS
import subprocess
import logging
import re
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import *
from settings import *
from import_functions import *
#----------------------MAIN WINDOW CLASS----------------------------

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("GEM - GUI Editor for Mapcss")
        ##----------------MAIN WINDOW VARIABLES---------------------
        self.importOldStyle=False
        self.output_file_dir = os.path.expanduser("~/Documents")
        self.filters = ""
        self.select_filters = "MAPCSS (*.mapcss)"
        self.currentEditors={}
        ##-----------------QICONS & QPIXMAPS--------------------------
        self.kaartLogo='static/icons/kaart.png'
        self.gemLogo='static/icons/GEM.png'
        self.gemIcon  = QtGui.QIcon(self.gemLogo)    
        self.kaartIcon  = QtGui.QIcon(self.kaartLogo)
        ##----------------GUI SETUP---------------------------------

        self.mainWidget=QWidget()
        self.mainWidgetLayout=QVBoxLayout()
        self.mainWidgetLayout.addStretch(1)
        self.mainWidget.setLayout(self.mainWidgetLayout)
        self.setCentralWidget(self.mainWidget)
        ##-----------------------TOP BAR W/ LINK BUTTONS------------
        self.topBar=QWidget()

        self.topBar.setMaximumHeight(40)
        self.topBarLayout=QHBoxLayout()
        self.topBarLayout.setSpacing(0)
        self.topBar.setLayout(self.topBarLayout)

        self.kaartLinkButton=QPushButton()
        self.kaartLinkButton.setIcon(self.kaartIcon)
        self.topBarLayout.addWidget(self.kaartLinkButton)

        self.gemLinkButton=QPushButton()
        self.gemLinkButton.setIcon(self.gemIcon)
        self.topBarLayout.addWidget(self.gemLinkButton)

        self.mainWidgetLayout.addWidget(self.topBar)

        ##----------------------CONTROLS AND TABLE SPLITTER---------
        
        self.bodySplitter=QSplitter(Qt.Horizontal)
        self.mainWidgetLayout.addWidget(self.bodySplitter)

        ##----------------------CONTROLS WIDGET---------------------


        ##----------------------TEAM / FILE NAME BOX----------------
        self.controlsWidget=QGroupBox()

        self.controlsWidget.setTitle("Controls")
        self.controlsWidgetLayout=QVBoxLayout()
        self.controlsWidgetLayout.setSpacing(0)
        self.controlsWidget.setLayout(self.controlsWidgetLayout)
        self.bodySplitter.addWidget(self.controlsWidget)

        self.teamNameBox = QGroupBox()

        self.teamNameBox.setTitle('Team Name')
        self.teamNameBoxLayout=QGridLayout()
        self.teamNameBoxLayout.setSpacing(0)
        self.teamNameBox.setLayout(self.teamNameBoxLayout)
        self.controlsWidgetLayout.addWidget(self.teamNameBox)

        self.teamNameField=QLineEdit()
        self.teamNameBoxLayout.addWidget(self.teamNameField)

        ##--------------------NON UPLOADED HIGHLIGHTS---------------

        self.notUploadedBox=QGroupBox()
        self.notUploadedBox.setTitle("Highlights for non-uploaded changes")
        self.notUploadedBoxLayout=QVBoxLayout()
        self.notUploadedBoxLayout.addStretch(1)
        self.notUploadedBoxLayout.setSpacing(0)
        self.notUploadedBox.setLayout(self.notUploadedBoxLayout)
        self.controlsWidgetLayout.addWidget(self.notUploadedBox)

        #---LINE COLOR
        self.unupLineColorControls=QWidget()
        self.unupLineColorControlsLayout=QHBoxLayout()
        self.unupLineColorControls.setLayout(self.unupLineColorControlsLayout)
        self.notUploadedBoxLayout.addWidget(self.unupLineColorControls)

        self.unupLineColorButton=QPushButton()
        self.unupLineColorButton.setText('LINE COLOR')
        self.unupLineColorControlsLayout.addWidget(self.unupLineColorButton)

        self.unupLineColorPreview=QLabel()
        self.unupLineColorpix = QPixmap(15, 15)
        self.unupLineColorpix.fill(QColor(WHITE))
        self.unupLineColorPreview.setPixmap(self.unupLineColorpix)
        self.unupLineColorControlsLayout.addWidget(self.unupLineColorPreview)

        self.unupLineWidthLabel=QLabel()
        self.unupLineWidthLabel.setText("Line Width")
        self.unupLineColorControlsLayout.addWidget(self.unupLineWidthLabel)

        self.unupLineWidthSpinner=QSpinBox()
        self.unupLineWidthSpinner.setRange(1, 20)
        self.unupLineColorControlsLayout.addWidget(self.unupLineWidthSpinner)
        #---NODE SIZE

        self.unupNodeColorControls=QWidget()
        self.unupNodeColorControlsLayout=QHBoxLayout()
        self.unupNodeColorControls.setLayout(self.unupNodeColorControlsLayout)
        self.notUploadedBoxLayout.addWidget(self.unupNodeColorControls)

        self.unupNodeColorButton=QPushButton()
        self.unupNodeColorButton.setText('NODE COLOR')
        self.unupNodeColorControlsLayout.addWidget(self.unupNodeColorButton)

        self.unupNodeColorPreview=QLabel()
        self.unupNodeColorpix = QPixmap(15, 15)
        self.unupNodeColorpix.fill(QColor(WHITE))
        self.unupNodeColorPreview.setPixmap(self.unupNodeColorpix)
        self.unupNodeColorControlsLayout.addWidget(self.unupNodeColorPreview)

        self.unupNodeWidthLabel=QLabel()
        self.unupNodeWidthLabel.setText("Node Size")
        self.unupNodeColorControlsLayout.addWidget(self.unupNodeWidthLabel)

        self.unupNodeWidthSpinner=QSpinBox()
        self.unupNodeWidthSpinner.setRange(1, 20)
        self.unupNodeColorControlsLayout.addWidget(self.unupNodeWidthSpinner)
       
        #---NODE SHAPE

        self.unupNodeShapeControls=QWidget()
        self.unupNodeShapeControlsLayout=QHBoxLayout()
        self.unupNodeShapeControls.setLayout(self.unupNodeShapeControlsLayout)
        self.notUploadedBoxLayout.addWidget(self.unupNodeShapeControls)

        self.unupNodeShapeLabel=QLabel()
        self.unupNodeShapeLabel.setText('Node Shape')
        self.unupNodeShapeControlsLayout.addWidget(self.unupNodeShapeLabel)

        self.unupNodeShapePreview=QPushButton()
        self.unupNodeShapePreview.resize(35, 30)
        self.unupNodeShapeControlsLayout.addWidget(self.unupNodeShapePreview)

        self.unupNodeShapeSelectButton=QPushButton()
        self.unupNodeShapeSelectButton.setText('SELECT SHAPE')   
        self.unupNodeShapeControlsLayout.addWidget(self.unupNodeShapeSelectButton)   


        ##--------------------EDITOR HIGHLIGHT SETTINGS---------------

        self.editorSettingsBox=QGroupBox()
        self.editorSettingsBox.setTitle("Editor Highlights")
        self.editorSettingsBoxLayout=QVBoxLayout()

        self.editorSettingsBoxLayout.addStretch(1)
        self.editorSettingsBoxLayout.setSpacing(0)
        
        self.editorSettingsBox.setLayout(self.editorSettingsBoxLayout)
        self.controlsWidgetLayout.addWidget(self.editorSettingsBox)

        #---EDITOR NAME
        self.editorNameWidget=QWidget()
        self.editorNameWidgetLayout=QHBoxLayout()
        self.editorNameWidget.setLayout(self.editorNameWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.editorNameWidget)

        self.editorNameLabel=QLabel()
        self.editorNameLabel.setText('Editor Name')
        self.editorNameWidgetLayout.addWidget(self.editorNameLabel)

        self.editorNameField=QLineEdit()
        self.editorNameWidgetLayout.addWidget(self.editorNameField)

        #---EDITOR USERNAME
        self.editorUsernameWidget=QWidget()
        self.editorUsernameWidgetLayout=QHBoxLayout()
        self.editorUsernameWidget.setLayout(self.editorUsernameWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.editorUsernameWidget)

        self.editorUsernameLabel=QLabel()
        self.editorUsernameLabel.setText('OSM Username')
        self.editorUsernameWidgetLayout.addWidget(self.editorUsernameLabel)

        self.editorUsernameField=QLineEdit()
        self.editorUsernameWidgetLayout.addWidget(self.editorUsernameField)

        #--ADD/CLEAR/EDIT EDITOR SETTINGS BUTTONS

        self.editorButtonsWidget=QWidget()
        self.editorButtonsWidgetLayout=QHBoxLayout()
        self.editorButtonsWidget.setLayout(self.editorButtonsWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.editorButtonsWidget)

        self.addEditorButton=QPushButton()
        self.addEditorButton.setText('ADD')
        self.editorButtonsWidgetLayout.addWidget(self.addEditorButton)

        self.clearEditorButton=QPushButton()
        self.clearEditorButton.setText('CLEAR')
        self.editorButtonsWidgetLayout.addWidget(self.clearEditorButton)

        self.editEditorButton=QPushButton()
        self.editEditorButton.setText('EDIT')
        self.editorButtonsWidgetLayout.addWidget(self.editEditorButton)


        #--EDITOR LINE SETTINGS


        self.editorLineSettingsWidget=QWidget()
        self.editorLineSettingsWidgetLayout=QHBoxLayout()
        self.editorLineSettingsWidget.setLayout(self.editorLineSettingsWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.editorLineSettingsWidget)


        self.editorLineColorButton=QPushButton()
        self.editorLineColorButton.setText("LINE COLOR")      
        self.editorLineSettingsWidgetLayout.addWidget(self.editorLineColorButton)


        self.editorNodeColorPreview=QLabel()
        self.editorNodeColorpix = QtGui.QPixmap(15, 15)
        self.editorNodeColorpix.fill(QColor(WHITE))
        self.editorNodeColorPreview.setPixmap(self.editorNodeColorpix)
        self.editorLineSettingsWidgetLayout.addWidget(self.editorNodeColorPreview)

        self.editorLineWidthLabel=QLabel()
        self.editorLineWidthLabel.setText('Line Width')  
        self.editorLineSettingsWidgetLayout.addWidget(self.editorLineWidthLabel) 

        self.editorLineWidthSpinner=QSpinBox()
        self.editorLineWidthSpinner.setRange(1, 20)
        self.editorLineWidthSpinner.setValue(5)
        self.editorLineSettingsWidgetLayout.addWidget(self.editorLineWidthSpinner)         

        #---EDITOR NODE HIGHLIGHT SETTINGS


        self.editorNodeSettingsWidget=QWidget()
        self.editorNodeSettingsWidgetLayout=QHBoxLayout()
        self.editorNodeSettingsWidget.setLayout(self.editorNodeSettingsWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.editorNodeSettingsWidget)

        self.editorNodeColorButton=QPushButton()
        self.editorNodeColorButton.setText('NODE COLOR')
        self.editorNodeSettingsWidgetLayout.addWidget(self.editorNodeColorButton)

        self.editorNodeColorPreview=QLabel()
        self.editorNodeColorpix = QtGui.QPixmap(15, 15)
        self.editorNodeColorpix.fill(QColor(WHITE))
        self.editorNodeColorPreview.setPixmap(self.editorNodeColorpix)
        self.editorNodeSettingsWidgetLayout.addWidget(self.editorNodeColorPreview)

        self.editorNodeWidthLabel=QLabel()
        self.editorNodeWidthLabel.setText('Node Width')  
        self.editorNodeSettingsWidgetLayout.addWidget(self.editorNodeWidthLabel) 

        self.editorNodeWidthSpinner=QSpinBox()
        self.editorNodeWidthSpinner.setRange(1, 20)
        self.editorNodeWidthSpinner.setValue(10)
        self.editorNodeSettingsWidgetLayout.addWidget(self.editorNodeWidthSpinner)            

        #---TOGGLE UID BUTTON
        self.toggleUIDWidget=QWidget()
        self.toggleUIDWidgetLayout=QHBoxLayout()
        self.toggleUIDWidget.setLayout(self.toggleUIDWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.toggleUIDWidget)

        self.toggleUIDLabel=QLabel()
        self.toggleUIDLabel.setText('Toggle UID in JOSM style settings menu')
        self.toggleUIDWidgetLayout.addWidget(self.toggleUIDLabel)

        self.toggleUIDCheckbox=QCheckBox()
        self.toggleUIDWidgetLayout.addWidget(self.toggleUIDCheckbox)        
    
        #---EDITOR NODE SHAPE SETTINGS

        self.editorNodeShapeWidget=QWidget()
        self.editorNodeShapeWidgetLayout=QHBoxLayout()
        self.editorNodeShapeWidget.setLayout(self.editorNodeShapeWidgetLayout)
        self.editorSettingsBoxLayout.addWidget(self.editorNodeShapeWidget)  

        self.editorNodeShapeLabel=QLabel()
        self.editorNodeShapeLabel.setText('Node Shape:')
        self.editorNodeShapeWidgetLayout.addWidget(self.editorNodeShapeLabel)

        self.editorNodeShapePreview = QPushButton()
        self.editorNodeShapePreview.resize(30, 30)
        self.editorNodeShapeWidgetLayout.addWidget(self.editorNodeShapePreview)

        self.editorNodeShapeSelectButton=QPushButton()
        self.editorNodeShapeSelectButton.setText('SELECT SHAPE')
        self.editorNodeShapeWidgetLayout.addWidget(self.editorNodeShapeSelectButton)

        ##--------------------TIME SEARCH SETTINGS--------------------

        self.timeSearchBox=QGroupBox()
        self.timeSearchBox.setTitle("Time Search")
        self.timeSearchBoxLayout=QVBoxLayout()


        self.timeSearchBoxLayout.addStretch(1)
        self.timeSearchBoxLayout.setSpacing(0)

        self.timeSearchBox.setLayout(self.timeSearchBoxLayout)
        self.controlsWidgetLayout.addWidget(self.timeSearchBox)

        #---OPEN CALENDAR WIDGET

        self.openCalendarWidget=QWidget()
        self.openCalendarWidgetLayout=QHBoxLayout()
        self.openCalendarWidget.setLayout(self.openCalendarWidgetLayout)
        self.timeSearchBoxLayout.addWidget(self.openCalendarWidget)  

        self.openCalendarButton=QPushButton()
        self.openCalendarButton.setText('OPEN CALENDAR')
        self.openCalendarWidgetLayout.addWidget(self.openCalendarButton) 

        #---START DATE WIDGET

        self.startDateWidget=QWidget()
        self.startDateWidgetLayout=QHBoxLayout()
        self.startDateWidget.setLayout(self.startDateWidgetLayout)
        self.timeSearchBoxLayout.addWidget(self.startDateWidget) 

        self.startDateLabel=QLabel()
        self.startDateLabel.setText('Start Date:')   
        self.startDateWidgetLayout.addWidget(self.startDateLabel)

        self.startDateField=QLineEdit()
        self.startDateWidgetLayout.addWidget(self.startDateField)        

        #---END DATE WIDGET

        self.endDateWidget=QWidget()
        self.endDateWidgetLayout=QHBoxLayout()
        self.endDateWidget.setLayout(self.endDateWidgetLayout)
        self.timeSearchBoxLayout.addWidget(self.endDateWidget) 

        self.endDateLabel=QLabel()
        self.endDateLabel.setText('end Date:')   
        self.endDateWidgetLayout.addWidget(self.endDateLabel)

        self.endDateField=QLineEdit()
        self.endDateWidgetLayout.addWidget(self.endDateField)           

        #---SET DATES BUTTONS WIDGET

        self.dateButtonsWidget=QWidget()
        self.dateButtonsWidgetLayout=QHBoxLayout()
        self.dateButtonsWidget.setLayout(self.dateButtonsWidgetLayout)
        self.timeSearchBoxLayout.addWidget(self.dateButtonsWidget)

        self.setDatesButton=QPushButton()
        self.setDatesButton.setText('SET DATES')
        self.dateButtonsWidgetLayout.addWidget(self.setDatesButton)

        self.clearDatesButton=QPushButton()
        self.clearDatesButton.setText('CLEAR DATES')
        self.dateButtonsWidgetLayout.addWidget(self.clearDatesButton)

        #---TOGGLE TIME SEARCH WIDGET

        self.toggleTimeSearchWidget=QWidget()
        self.toggleTimeSearchWidgetLayout=QHBoxLayout()
        self.toggleTimeSearchWidget.setLayout(self.toggleTimeSearchWidgetLayout)
        self.timeSearchBoxLayout.addWidget(self.toggleTimeSearchWidget)     

        self.toggleTimeSearchLabel=QLabel()
        self.toggleTimeSearchLabel.setText("Toggle Time Search On/Off")
        self.toggleTimeSearchWidgetLayout.addWidget(self.toggleTimeSearchLabel)

        self.toggleTimeSearchCheckbox=QCheckBox()
        self.toggleTimeSearchWidgetLayout.addWidget(self.toggleTimeSearchCheckbox)


        ##----------------------TABLE WIDGET--------------------------

        self.tableWidget=QGroupBox()
        self.tableWidget.setTitle("Table")
        self.tableWidgetLayout=QVBoxLayout()


        #self.tableWidgetLayout.addStretch(0)
        self.tableWidgetLayout.setSpacing(0)
        self.tableWidgetLayout.setContentsMargins(0,0,0,0)


        self.tableWidget.setLayout(self.tableWidgetLayout)
        self.bodySplitter.addWidget(self.tableWidget)

        self.editorTable=QTreeWidget()
        self.editorTable.setColumnCount(4)
        self.editorTable.setHeaderLabels(['Name','OSM Username','Line','Node'])
        self.editorTable.setSizePolicy (QSizePolicy.Minimum, QSizePolicy.Minimum)
        
        self.editorTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidgetLayout.addWidget(self.editorTable)

        self.tableControlsWidget=QWidget()
        self.tableControlsWidget.setFixedHeight(110)
        self.tableControlsWidgetLayout=QVBoxLayout()
        #self.tableControlsWidgetLayout.addStretch(0)

        self.tableControlsWidgetLayout.setSpacing(0)
        self.tableControlsWidgetLayout.setContentsMargins(0,0,0,0)

        self.tableControlsWidget.setLayout(self.tableControlsWidgetLayout)
        self.tableWidgetLayout.addWidget(self.tableControlsWidget)


        self.topTableButtonsWidget=QWidget()
        
        self.topTableButtonsWidget.setMaximumHeight(40)
        self.topTableButtonsWidgetLayout=QHBoxLayout()
        self.topTableButtonsWidget.setLayout(self.topTableButtonsWidgetLayout)
        self.tableControlsWidgetLayout.addWidget(self.topTableButtonsWidget)


        self.importButton=QPushButton()
        self.importButton.setText("IMPORT")
        self.importButton.clicked.connect(lambda:importCssFile(self))
        self.importButton.setFixedWidth(110)
        self.topTableButtonsWidgetLayout.addWidget(self.importButton)        


        self.removeEditorButton=QPushButton()
        self.removeEditorButton.setText("REMOVE")
        self.removeEditorButton.setFixedWidth(110)
        self.topTableButtonsWidgetLayout.addWidget(self.removeEditorButton)


        self.moveUpButton=QPushButton()
        self.moveUpButton.setText("MOVE UP")
        self.moveUpButton.setFixedWidth(110)
        self.topTableButtonsWidgetLayout.addWidget(self.moveUpButton)

        self.restackButton=QPushButton()
        self.restackButton.setText("RESTACK")
        self.restackButton.setFixedWidth(110)
        self.topTableButtonsWidgetLayout.addWidget(self.restackButton)


        self.bottomTableButtonsWidget=QWidget()
        self.bottomTableButtonsWidget.setMaximumHeight(40)
        self.bottomTableButtonsWidgetLayout=QHBoxLayout()
        self.bottomTableButtonsWidget.setLayout(self.bottomTableButtonsWidgetLayout)
        self.tableControlsWidgetLayout.addWidget(self.bottomTableButtonsWidget)
        self.tableWidgetLayout.addWidget(self.tableControlsWidget)

        self.exportButton=QPushButton()
        self.exportButton.setText("EXPORT")
        self.exportButton.setFixedWidth(110)
        self.bottomTableButtonsWidgetLayout.addWidget(self.exportButton)        

        self.removeAllEditorsButton=QPushButton()
        self.removeAllEditorsButton.setText("REMOVE ALL")   
        self.removeAllEditorsButton.setFixedWidth(110)
        self.bottomTableButtonsWidgetLayout.addWidget(self.removeAllEditorsButton)

        self.moveDownButton=QPushButton()
        self.moveDownButton.setText("MOVE DOWN")
        self.moveDownButton.setFixedWidth(110)
        self.bottomTableButtonsWidgetLayout.addWidget(self.moveDownButton)

        self.isolateButton=QPushButton()
        self.isolateButton.setText("ISOLATE")
        self.isolateButton.setFixedWidth(110)
        self.bottomTableButtonsWidgetLayout.addWidget(self.isolateButton)



























# close ewindow event---------------------------------
    def closeEvent(self, event):
        #save_settings(self)
        # if self.team_obj != self.loaded_team_obj:
        #     autosave_team_file(self)
        # self.deleteLater()
        try:
            print("CLOSE")
            # self.changeset_mode_widget.close()
        except Exception as e:
            print(str(e))
        self.close()
# main loop-------------------------------------------
def main(args):
        app = QApplication(args)
        main=MainWindow()
        main.show()
        sys.exit(app.exec_())

def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback) 
    sys.exit(1) 
sys.excepthook = exception_hook
# main loop init--------------------------------------
while  True:
    main(sys.argv)