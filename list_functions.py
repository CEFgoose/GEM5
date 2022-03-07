from PyQt5.QtCore import *
#from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import *
from confirm_widget import *

def editor_list_clicked(main):
    main.selectedEditors=[]
    selectedEditorIndexes=main.editorTable.selectedItems()
    for index in selectedEditorIndexes:
        index=main.editorTable.indexOfTopLevelItem(index)
        main.selectedEditors.append(main.currentEditorsOrdered[index])
    for editor in main.selectedEditors:
        print(editor.username)


def remove_editors(main):
    proceed=confirmationWidget(main,"Remove selectededitors","Are you sure you want to remove selected editors?")
    if proceed:
        for editor in main.selectedEditors:
            main.currentEditorsOrdered.remove(editor)
        selectedEditorIndexes=main.editorTable.selectedItems()
        for index in selectedEditorIndexes:
            index=main.editorTable.indexOfTopLevelItem(index)
            main.editorTable.takeTopLevelItem(index)



def remove_all_editors(main):
    proceed=confirmationWidget(main,"Remove all editors","Are you sure you want to remove all editors?")
    if proceed:
        main.selectedEditors=[]
        main.currentEditorsOrdered=[]
        main.editorTable.clear()


def move_up(main):
    for editor in main.selectedEditors:
        moving_up_index=main.currentEditorsOrdered.index(editor)
        moving_down_index=main.currentEditorsOrdered.index(editor)-1
        moving_up_editor=main.currentEditorsOrdered[moving_up_index]
        moving_down_editor=main.currentEditorsOrdered[moving_down_index] 
        main.currentEditorsOrdered[moving_up_index]=moving_down_editor
        main.currentEditorsOrdered[moving_down_index]=moving_up_editor
    main.editorTable.clear()
    for editor in main.currentEditorsOrdered:
        editor.construct_list_item(main)


def move_down(main):
    for editor in main.selectedEditors:
        moving_down_index=main.currentEditorsOrdered.index(editor)
        moving_up_index=main.currentEditorsOrdered.index(editor)+1
        if moving_up_index>len(main.currentEditorsOrdered)-1:
            moving_up_index=0
        moving_down_editor=main.currentEditorsOrdered[moving_down_index]
        moving_up_editor=main.currentEditorsOrdered[moving_up_index] 
        main.currentEditorsOrdered[moving_up_index]=moving_down_editor
        main.currentEditorsOrdered[moving_down_index]=moving_up_editor
    main.editorTable.clear()
    for editor in main.currentEditorsOrdered:
        editor.construct_list_item(main)
    
    
