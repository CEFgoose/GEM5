from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor,QPixmap
from settings import *
from editor_class import EDITOR
from shapes import *

#---handles calling add or update user function when add/update editor button cliecked
def add_editor_handler(main):
    if main.addEditorButton.text()=='UPDATE':
        update_editor(main)
        pass
    elif main.addEditorButton.text()=='ADD':
        add_new_editor(main)

#---saves any change to editor line width to var
def editor_linewidth_changed(main,value):
    main.editor_line_width=value

#---saves any change to editor node size to var
def editor_nodesize_changed(main,value):
    main.editor_node_size=value

#---flips editor UID toggled Boolean
def editor_uid_toggled(main):
    main.editor_UID_toggled = not main.editor_UID_toggled


#---saves any change to editor name to var
def editor_name_changed(main,value):
    main.editor_name=value

#---saves any change to editor username to var
def editor_username_changed(main,value):
    main.editor_username=value

##---saves any change to editor line color to var and repaints line color preview
def editor_linecolor_changed(main):
    color = QColorDialog.getColor()
    clr = color.name()
    colr = ""
    for i in clr:
        colr+= str(i)
    if colr =="#000000":
        colr = main.editor_line_color_text
    else:
        main.editor_line_color_ui=QColor(color)
        main.editor_line_color_text = colr
        main.editorLineColorpix.fill(main.editor_line_color_ui)
        main.editorLineColorPreview.setPixmap(main.editorLineColorpix)

#---saves any change to editor node color to var and repaints node color preview and node shape preview 
def editor_nodecolor_changed(main):
    color = QColorDialog.getColor()
    clr = color.name()
    colr = ""
    for i in clr:
        colr+= str(i)
    if colr =="#000000":
        colr=main.editor_node_color_text
    else:
        main.editor_node_color_ui=QColor(color)
        main.editor_node_color_text = colr
        main.editorNodeColorpix = QPixmap(15, 15)
        main.editorNodeColorpix.fill(main.editor_node_color_ui)
        main.editorNodeColorPreview.setPixmap(main.editorNodeColorpix)
        main.editorNodeShapePixmap=QPixmap(allShapes[main.editor_node_shape])
        main.editorNodeShapeMask = main.editorNodeShapePixmap.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
        main.editorNodeShapePixmap.fill(main.editor_node_color_ui)
        main.editorNodeShapePixmap.setMask(main.editorNodeShapeMask)
        main.editorNodeShapePixmap=main.editorNodeShapePixmap.scaled(30,30)
        main.editorNodeShapePreview.setPixmap(main.editorNodeShapePixmap)    

#---Applies any changes in editor settings fields to selected editors then re-renders the editor table with new info
def update_editor(main):
    print(len(main.selectedEditors)) 
    if len(main.selectedEditors)>1:
        editorNames=main.editorNameField.text().split(',')
        editorUsernames=main.editorUsernameField.text().split(',')
        for editor,name in zip(main.selectedEditors,editorNames):
            editor.firstName=name.strip()
        for editor,username in zip(main.selectedEditors,editorUsernames):
            editor.username=username.strip()
        for editor in main.selectedEditors:
            editor.nodeShapeText=main.editor_node_shape
            editor.lineColorText=main.editor_line_color_text
            editor.nodeColorText=main.editor_node_color_text           
            editor.lineColorUI=main.editor_line_color_ui
            editor.nodeColorUI=main.editor_node_color_ui       
            editor.iconSize=int(main.editor_node_size)
            editor.lineWidth=int(main.editor_line_width)
            editor.nodeShape=QPixmap(allShapes[main.editor_node_shape])
            editor.nodeShape= editor.nodeShape.scaled(60, 60)
            editor.nodeMask = editor.nodeShape.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
            editor.nodeShape.fill(editor.nodeColorUI)
            editor.nodeShape.setMask(editor.nodeMask)
        main.editorTable.clear()
        for editor in main.currentEditorsOrdered:
            editor.construct_list_item(main)
        clear_editor_info(main)
    else:
        
        main.selectedEditors[0].firstName=main.editor_name
        main.selectedEditors[0].username=main.editor_username
        main.selectedEditors[0].lineColorUI=main.editor_line_color_ui
        main.selectedEditors[0].nodeColorUI=main.editor_node_color_ui  
        main.selectedEditors[0].lineColorText=main.editor_line_color_text
        main.selectedEditors[0].nodeColorText=main.editor_node_color_text        
        main.selectedEditors[0].iconSize=int(main.editor_node_size)
        main.selectedEditors[0].lineWidth=int(main.editor_line_width)
        main.selectedEditors[0].nodeShapeText=main.editor_node_shape
        main.selectedEditors[0].nodeShape=QPixmap(allShapes[main.editor_node_shape])
        main.selectedEditors[0].nodeShape= main.selectedEditors[0].nodeShape.scaled(60, 60)
        main.selectedEditors[0].nodeMask = main.selectedEditors[0].nodeShape.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
        main.selectedEditors[0].nodeShape.fill(main.selectedEditors[0].nodeColorUI)
        main.selectedEditors[0].nodeShape.setMask(main.selectedEditors[0].nodeMask)
        main.editorTable.clear()
        for editor in main.currentEditorsOrdered:
            editor.construct_list_item(main)
        clear_editor_info(main)
    main.addEditorButton.setText('ADD')

#---creates a new editor class instance from new info in editor settings, adds editor to editor list & table, re-renders editor table with new entry  
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


#---Grabs info on selected editors from editor list and applies it to editor settings fields for change & update
def edit_editor(main):
    main.addEditorButton.setText('UPDATE')
    editing_names=[]
    editing_usernames=[]
    for editor in main.selectedEditors:
        editing_names.append(editor.firstName)
        editing_usernames.append(editor.username)
    editing_names=str(editing_names).replace("[",'')
    editing_names=str(editing_names.replace("]",''))   
    editing_names=str(editing_names.replace("'",''))     
    editing_usernames=str(editing_usernames).replace("[",'')
    editing_usernames=str(editing_usernames.replace("]",''))   
    editing_usernames=str(editing_usernames.replace("'",'')) 
    main.editor_node_color_text= main.selectedEditors[0].nodeColorText
    main.editor_line_color_text= main.selectedEditors[0].lineColorText
    main.editor_node_color_ui= main.selectedEditors[0].nodeColorUI 
    main.editor_line_color_ui= main.selectedEditors[0].lineColorUI
    main.editor_node_shape=main.selectedEditors[0].nodeShapeText
    main.editor_line_width=main.selectedEditors[0].lineWidth
    main.editor_node_size=main.selectedEditors[0].iconSize
    if len(main.selectedEditors)==1:
        main.editorNameField.setText(main.selectedEditors[0].firstName)
        main.editorUsernameField.setText(main.selectedEditors[0].username)
        main.editorLineWidthSpinner.setValue(int(main.editor_line_width))
        main.editorNodeWidthSpinner.setValue(int(main.editor_node_size))
        main.editorNodeColorpix = QPixmap(15, 15)
        main.editorNodeColorpix.fill(main.editor_node_color_ui)
        main.editorNodeColorPreview.setPixmap(main.editorNodeColorpix)
        main.editorLineColorpix = QPixmap(15, 15)
        main.editorLineColorpix.fill(main.editor_line_color_ui)
        main.editorLineColorPreview.setPixmap(main.editorLineColorpix)
        pix=main.selectedEditors[0].nodeShape
        main.editorNodeShapePreview.setPixmap(pix)
    else:
        main.editorNameField.setText(editing_names)
        main.editorUsernameField.setText(editing_usernames)

#---clears all editor settings fields after editor added or updated
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


def hide_users(main):
    for editor in main.selectedEditors:
        editor.hidden=True
        editor.visibility_icon=HIDDEN_ICON

    main.editorTable.clear()
    for editor in main.currentEditorsOrdered:
        editor.construct_list_item(main)

def show_users(main):
    for editor in main.selectedEditors:
        editor.hidden=False
        editor.visibility_icon=VIEW_ICON
    main.editorTable.clear()
    for editor in main.currentEditorsOrdered:
        editor.construct_list_item(main)