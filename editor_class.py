from PyQt5.QtCore import *
from PyQt5.QtGui import QColor,QPixmap,QIcon
from PyQt5.QtWidgets import QTreeWidgetItem
from shapes import *
from settings import*
class EDITOR(object):
    def __init__(self,firstname,username,lineColorText,nodeColorText,iconSize,iconShape,lineWidth):
        self.firstName= firstname
        self.username = username
        self.lineColorText = lineColorText
        self.nodeColorText = nodeColorText
        self.lineColorUI = QColor(self.lineColorText)
        self.nodeColorUI = QColor(self.nodeColorText)
        self.iconSize = iconSize
        self.lineWidth = lineWidth
        self.nodeShapeText=iconShape
        self.nodeShape = QPixmap(allShapes[iconShape])
        self.nodeShape = self.nodeShape.scaled(30, 30)
        self.nodeMask = self.nodeShape.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
        self.nodeShape.fill(self.nodeColorUI)
        self.nodeShape.setMask(self.nodeMask)
        self.lineColorPixmap=QPixmap(15, 15)
        self.listIndex=0

    def construct_list_item(self,main):
        self.list_entry=QTreeWidgetItem()
        self.display_info()
        main.editorTable.addTopLevelItem(self.list_entry)

    def display_info(self):
        self.list_entry.setText(0, str(self.firstName))
        self.list_entry.setText(1, str(self.username))
        self.lineColorPixmap.fill(self.lineColorUI)
        self.list_entry.setText(2,str(self.lineWidth))   
        self.list_entry.setIcon(2, QIcon(self.lineColorPixmap))

        self.list_entry.setIcon(3, QIcon(self.nodeShape))
        self.list_entry.setText(3,'%s - %s'%(str(self.iconSize),self.nodeShapeText))