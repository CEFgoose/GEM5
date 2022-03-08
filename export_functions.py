from REGEXES import *
import tempCSS



def export_clicked(main):
    if main.teamNameField.text() != "":
        main.addEditors = []
        for editor in main.currentEditorsOrdered:
            if main.isolate_users == True:
                if editor.isolated:
                    main.addEditors.append(editor)
        
            else:    
                main.addEditors.append(editor)
        
        # 'set the file name for the new export and meta block title using the corresponding team name'
        
        main.FILENAME = str("Kaart_QC_%s.mapcss"%(main.team_name))
        main.TITLE = "QC Styles For %s Team"%(main.team_name)
        if main.time_search_active:
            for editor in main.addEditors:
                if main.editor_UID_toggled:
                    editor.USERBLOCK = re.sub(FINDUSERNAME, editor.firstName, tempCSS.TOGGLEDTIMESEARCHBLOCK)
                else:
                    editor.USERBLOCK = re.sub(FINDUSERNAME, editor.firstName, tempCSS.TIMESEARCHBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERID, editor.username, editor.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERNAME, editor.firstName, editor.USERBLOCK)
                editor.USERBLOCK = re.sub(FINDUSERNODESIZE, str(editor.iconSize), editor.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERNODECOLOR, editor.nodeColorText, editor.USERBLOCK)
                editor.USERBLOCK = re.sub(FINDUSERNODESHAPE, editor.nodeShapeText, editor.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERNAME, editor.firstName, editor.USERBLOCK)
                editor.USERBLOCK = re.sub(FINDUSERWAYWIDTH, str(editor.lineWidth), editor.USERBLOCK )
                editor.USERBLOCK  = re.sub(FINDUSERWAYCOLOR, editor.lineColorText, editor.USERBLOCK )
                editor.USERBLOCK  = re.sub(FINDTIMESEARCH, main.search_dates, editor.USERBLOCK )
                main.FINSHEDUSERBLOCK  += str(editor.USERBLOCK)
        else:
            for editor in main.addEditors:
                
                if main.editor_UID_toggled:
                    editor.USERBLOCK = re.sub(FINDUSERNAME, editor.firstName, tempCSS.TOGGLEDUSERBLOCK)
                else:
                    editor.USERBLOCK = re.sub(FINDUSERNAME, editor.firstName, tempCSS.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERID, editor.username, editor.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERNAME, editor.firstName, editor.USERBLOCK)
                editor.USERBLOCK = re.sub(FINDUSERNODESIZE, str(editor.iconSize), editor.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERNODECOLOR, editor.nodeColorText, editor.USERBLOCK)

                editor.USERBLOCK = re.sub(FINDUSERNODESHAPE, editor.nodeShapeText, editor.USERBLOCK)
                editor.USERBLOCK= re.sub(FINDUSERNAME, editor.firstName, editor.USERBLOCK)
                editor.USERBLOCK = re.sub(FINDUSERWAYWIDTH, str(editor.lineWidth), editor.USERBLOCK )
                editor.USERBLOCK  = re.sub(FINDUSERWAYCOLOR, editor.lineColorText, editor.USERBLOCK )
                main.FINSHEDUSERBLOCK  += str(editor.USERBLOCK)
                
        # 'Do the same for the static CSS blocks only once to enter all Team (unuploaded) Highlight settings'
        staticBlock=tempCSS.STATICBLOCK

        newSTATICBLOCK = re.sub(FINDNOTUPNODESIZE, str(main.unup_node_size), staticBlock)
        newSTATICBLOCK = re.sub(FINDNOTUPNODECOLOR,main.unup_node_color_text, newSTATICBLOCK)
        newSTATICBLOCK = re.sub(FINDNOTUPNODESHAPE, main.unup_node_shape, newSTATICBLOCK)
        newSTATICBLOCK = re.sub(FINDNOTUPWAYCOLOR, main.unup_line_color_text, newSTATICBLOCK)
        newSTATICBLOCK = re.sub(FINDNOTUPWAYWIDTH, str(main.unup_line_width), newSTATICBLOCK)
        newSTATICBLOCK = re.sub(FINDTITLE, main.TITLE, newSTATICBLOCK)
        
        # 'glue the fisihed userblock to the static block on the end'
        
        main.BLOCK = main.FINSHEDUSERBLOCK + newSTATICBLOCK
        
        # 'define the export file location & name'
        
        file = main.output_file_dir+("/")+(main.FILENAME)
        # 'write out the finished MapCSS file to the chosen directory'
        
        with open(file, 'w')as CSS:
            CSS.writelines (main.BLOCK)
        main.BLOCK = ""
        newSTATICBLOCK=""
        main.FINSHEDUSERBLOCK =""
        for i in main.addEditors:
            i.USERBLOCK = ""