from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QIcon,QPixmap
from shapes import allButtonShapes,allShapes
from settings import *

def shapeSelectWidget(main,select):
    main.shapeSelectWidget=QWidget()
    main.shapeSelectWidgetLayout=QGridLayout()
    main.shapeSelectWidget.setLayout(main.shapeSelectWidgetLayout)

    circleButton=QPushButton()
    circleButton.setIcon(QIcon(allButtonShapes['circle']))
    circleButton.clicked.connect(lambda:setShape(main,'circle',select))
    main.shapeSelectWidgetLayout.addWidget(circleButton,0,0)

    triangleButton=QPushButton()
    triangleButton.setIcon(QIcon(allButtonShapes['triangle']))
    triangleButton.clicked.connect(lambda:setShape(main,'triangle',select))
    main.shapeSelectWidgetLayout.addWidget(triangleButton,0,1)

    squareButton=QPushButton()
    squareButton.setIcon(QIcon(allButtonShapes['square']))
    squareButton.clicked.connect(lambda:setShape(main,'square',select))
    main.shapeSelectWidgetLayout.addWidget(squareButton,0,2)

    pentagonButton=QPushButton()
    pentagonButton.setIcon(QIcon(allButtonShapes['pentagon']))
    pentagonButton.clicked.connect(lambda:setShape(main,'pentagon',select))
    main.shapeSelectWidgetLayout.addWidget(pentagonButton,1,0)

    hexagonButton=QPushButton()
    hexagonButton.setIcon(QIcon(allButtonShapes['hexagon']))
    hexagonButton.clicked.connect(lambda:setShape(main,'hexagon',select))
    main.shapeSelectWidgetLayout.addWidget(hexagonButton,1,1)

    heptagonButton=QPushButton()
    heptagonButton.setIcon(QIcon(allButtonShapes['heptagon']))
    heptagonButton.clicked.connect(lambda:setShape(main,'heptagon',select))
    main.shapeSelectWidgetLayout.addWidget(heptagonButton,1,2)

    octagonButton=QPushButton()
    octagonButton.setIcon(QIcon(allButtonShapes['octagon']))
    octagonButton.clicked.connect(lambda:setShape(main,'octagon',select))
    main.shapeSelectWidgetLayout.addWidget(octagonButton,3,0)

    nonagonButton=QPushButton()
    nonagonButton.setIcon(QIcon(allButtonShapes['nonagon']))
    nonagonButton.clicked.connect(lambda:setShape(main,'nonagon',select))
    main.shapeSelectWidgetLayout.addWidget(nonagonButton,3,1)

    decagonButton=QPushButton()
    decagonButton.setIcon(QIcon(allButtonShapes['decagon']))
    decagonButton.clicked.connect(lambda:setShape(main,'decagon',select))
    main.shapeSelectWidgetLayout.addWidget(decagonButton,3,2)

    main.shapeSelectWidget.show()


def setShape(main,shape,select):
    main.shapeSelectWidget.close()
    if select =="unup":
        main.unupNodeShapePixmap=QPixmap(allShapes[shape])
        main.unupNodeShapeMask = main.unupNodeShapePixmap.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
        main.unupNodeShapePixmap.fill(main.unup_node_color_ui)
        main.unupNodeShapePixmap.setMask(main.unupNodeShapeMask)
        main.unupNodeShapePixmap=main.unupNodeShapePixmap.scaled(20,20)
        main.unupNodeShapePreview.setPixmap(main.unupNodeShapePixmap)
    elif select =="editor":
        main.editor_node_shape=shape
        main.editorNodeShapePixmap=QPixmap(allShapes[shape])
        main.editorNodeShapeMask = main.editorNodeShapePixmap.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
        main.editorNodeShapePixmap.fill(main.editor_node_color_ui)
        main.editorNodeShapePixmap.setMask(main.editorNodeShapeMask)
        main.editorNodeShapePixmap=main.editorNodeShapePixmap.scaled(20,20)
        main.editorNodeShapePreview.setPixmap(main.editorNodeShapePixmap)      