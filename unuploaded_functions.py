from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
def unup_linewidth_changed(main,value):
    main.unup_line_width=value

def unup_nodesize_changed(main,value):
    main.unup_node_size=value

def unup_linecolor_changed(main):
    color = QColorDialog.getColor()
    clr = color.name()
    colr = ""
    for i in clr:
        colr+= str(i)
    if colr =="#000000":
        pass
    else:
        main.unup_line_color_ui=QColor(color)
        main.unup_line_color_text = colr
        main.unupLineColorpix.fill(main.unup_line_color_ui)
        main.unupLineColorPreview.setPixmap(main.unupLineColorpix)

def unup_nodecolor_changed(main):
    color = QColorDialog.getColor()
    clr = color.name()
    colr = ""
    for i in clr:
        colr+= str(i)
    if colr =="#000000":
        pass
    else:
        main.unup_node_color_ui=QColor(color)
        main.unup_node_color_text = colr
        main.unupNodeColorpix.fill(main.unup_node_color_ui)
        main.unupNodeColorPreview.setPixmap(main.unupNodeColorpix)

