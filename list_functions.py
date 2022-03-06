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
    
    

    '''
    def MOVEDOWN_clicked(self):
        if self.NRSELECT != "":
            MOVETO = int(int(self.NRSELECT) + 1)
            MOVEFROM = int(self.NRSELECT)

            if str(MOVETO) in self.TEMPUSERS.keys():
                if self.TEMPUSERS[str(MOVETO)] == 0:
                    self.GEMarray[(MOVETO)][0] = self.TEMPUSERS[str(MOVEFROM)].NAME
                    self.GEMarray[(MOVETO)][1] = self.TEMPUSERS[str(MOVEFROM)].UID
                    self.GEMarray[(MOVETO)][2] = self.TEMPUSERS[
                        str(MOVEFROM)
                    ].LINECOLORUI
                    self.GEMarray[(MOVETO)][3] = self.TEMPUSERS[str(MOVEFROM)].icon
                    self.GEMarray[(MOVEFROM)][0] = ""
                    self.GEMarray[(MOVEFROM)][1] = ""
                    self.GEMarray[(MOVEFROM)][2] = clear
                    self.GEMarray[(MOVEFROM)][3] = clear
                    self.TEMPUSERS[str(MOVETO)] = self.TEMPUSERS[str(MOVEFROM)]
                    self.TEMPUSERS[str(MOVEFROM)] = 0
                    self.SETNR()
                else:
                    self.MOVETOUSER = self.TEMPUSERS[str(MOVEFROM)]
                    self.MOVEFROMUSER = self.TEMPUSERS[str(MOVETO)]
                    self.GEMarray[(MOVEFROM)][0] = self.MOVEFROMUSER.NAME
                    self.GEMarray[(MOVEFROM)][1] = self.MOVEFROMUSER.UID
                    self.GEMarray[(MOVEFROM)][2] = self.MOVEFROMUSER.LINECOLORUI
                    self.GEMarray[(MOVEFROM)][3] = self.MOVEFROMUSER.icon
                    self.GEMarray[(MOVETO)][0] = self.MOVETOUSER.NAME
                    self.GEMarray[(MOVETO)][1] = self.MOVETOUSER.UID
                    self.GEMarray[(MOVETO)][2] = self.MOVETOUSER.LINECOLORUI
                    self.GEMarray[(MOVETO)][3] = self.MOVETOUSER.icon
                    self.TEMPUSERS[str(MOVETO)] = self.MOVETOUSER
                    self.TEMPUSERS[str(MOVEFROM)] = self.MOVEFROMUSER
                    self.SETNR()
    '''