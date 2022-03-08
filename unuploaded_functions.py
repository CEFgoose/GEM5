from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

#---saves team name to var on change
def team_name_changed(main,value):
    main.team_name=value

#---saves changes to unuploaded line width to var
def unup_linewidth_changed(main,value):
    main.unup_line_width=value

#---saves changes to unuploaded node size to var
def unup_nodesize_changed(main,value):
    main.unup_node_size=value

#---saves changes to unuploaded line color to var & repaints unuploaded line color preview 
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

#---saves changes to unuploaded node color to var & repaints unuploaded node color & shape previews
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

