from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor,QPixmap
from settings import *
from editor_class import EDITOR

def editor_linewidth_changed(main,value):
    main.editor_line_width=value

def editor_nodesize_changed(main,value):
    main.editor_node_size=value

def editor_linecolor_changed(main):
    color = QColorDialog.getColor()
    clr = color.name()
    colr = ""
    for i in clr:
        colr+= str(i)
    if colr =="#000000":
        pass
    else:
        main.editor_line_color_ui=QColor(color)
        main.editor_line_color_text = colr
        main.editorLineColorpix.fill(main.editor_line_color_ui)
        main.editorLineColorPreview.setPixmap(main.editorLineColorpix)
  
def editor_nodecolor_changed(main):
    color = QColorDialog.getColor()
    clr = color.name()
    colr = ""
    for i in clr:
        colr+= str(i)
    if colr =="#000000":
        pass
    else:
        main.editor_node_color_ui=QColor(color)
        main.editor_node_color_text = colr
        main.editorNodeColorpix.fill(main.editor_node_color_ui)
        main.editorNodeColorPreview.setPixmap(main.editorNodeColorpix)
  
def editor_uid_toggled(main):
    main.editor_UID_toggled = not main.editor_UID_toggled
    print(main.editor_UID_toggled)

def editor_name_changed(main,value):
    main.editor_name=value

def editor_username_changed(main,value):
    main.editor_username=value

def add_new_editor(main):
    new_editor=EDITOR(
        main.editor_name,
        main.editor_username,
        main.editor_line_color_text,
        main.editor_node_color_text,
        main.editor_node_size,
        main.editor_node_shape,
        main.editor_line_width)
    main.currentEditorsOrdered.append(new_editor)
    main.editorTable.clear()
    for editor in main.currentEditorsOrdered:
        editor.construct_list_item(main)
    clear_editor_info(main)


def clear_editor_info(main):
        main.editor_name=''
        main.editor_username=''
        main.editor_line_color_text=''
        main.editor_node_color_text=''
        main.editor_node_size=1
        main.editor_node_shape='circle'
        main.editor_line_width=5 
  
        main.editorNameField.setText('')
        main.editorUsernameField.setText('')
        main.editorLineWidthSpinner.setValue(5)
        main.editorNodeWidthSpinner.setValue(10)
        main.editorNodeColorpix = QPixmap(15, 15)
        main.editorNodeColorpix.fill(QColor(WHITE))
        main.editorNodeColorPreview.setPixmap(main.editorNodeColorpix)

        main.editorLineColorpix = QPixmap(15, 15)
        main.editorLineColorpix.fill(QColor(WHITE))
        main.editorLineColorPreview.setPixmap(main.editorLineColorpix)
        
        main.editorNodeShapePix=QPixmap(15,15)
        main.editorNodeShapePix.fill(QColor(WHITE))
        main.editorNodeShapePreview.setPixmap(main.editorNodeShapePix)
