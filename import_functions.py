from PyQt5.QtWidgets import *
from REGEXES import *
from editor_class import *
import re

def importCssFile(main):
    try:
        infile = QFileDialog.getOpenFileName(
            main, main.filters, main.output_file_dir, main.select_filters
        )
        infile = str(infile[0])
        with open(infile, "r+") as reader:
            infile_text = reader.read()
    except Exception as e:
        print(e)
    try:
        import_proceed(main,infile_text)
    except Exception as e:
        print(e)

def import_proceed(main, inCSS):
    parse_mapcss_text(main,str(inCSS))
    # construct_table(parsed_users)

def parse_mapcss_text(main, inCSS):
    original_text = str(inCSS)
    text_no_newline = original_text.replace("\n", " ")
    text_no_newline = re.sub(
        r"//.*?\n",
        "",
        re.sub(r"//.*?\\n", " ", re.sub(r"/\*.*?\*/", " ", text_no_newline)),
    )
    parse_team_from_mapcss(main,text_no_newline)
    parse_users_from_mapcss(main,str(original_text))
    parse_unuploaded_data_from_mapcss(main,original_text)

def parse_users_from_mapcss(main,mapcss_text):
    editor_info=mapcss_text.split('/* USER SEARCH SETTINGS */')
    editor_info=editor_info[1:]
    for editor in editor_info:
        editor=editor.replace('\n','')
        editor_first_name = re.findall(findFirstName, editor)
        editor_username = re.findall(findUsername, editor)
        editor_first_name=editor_first_name[0].split('")')[0].split('user_')[1]
        editor_username=editor_username[0].split('")')[0].split('user:')[1]
        editor_line_color= editor.split('casing-color: ')[1].split(";")[0]
        editor_line_width=editor.split('casing-width: ')[1].split(";")[0]
        editor_node_size=editor.split('symbol-size: ')[1].split(";")[0]
        editor_node_shape=editor.split('symbol-shape: ')[1].split(";")[0]
        editor_node_color=editor.split('symbol-stroke-color: ')[1].split(";")[0]
        editor=EDITOR(editor_first_name,editor_username,editor_line_color,editor_node_color,editor_node_size,editor_node_shape,editor_line_width)
        main.currentEditors[editor.username]=editor
    for editor in main.currentEditors.values():
        editor.construct_list_item(main)

def parse_team_from_mapcss(main,mapcss_text):
    title = re.findall(r"title: \"(.*?)\"", mapcss_text)
    teamname = title[0]
    main.teamNameField.setText(teamname)

def parse_unuploaded_data_from_mapcss(main,mapcss_text):
    unup_info=mapcss_text.split('/* MODIFIED BUT NOT UPLOADED LAYER STYLE */')[1]
    main.unup_node_shape=unup_info.split('symbol-shape: ')[1].split(';')[0]
    main.unup_node_color_ui=QColor(unup_info.split('symbol-stroke-color: ')[1].split(';')[0])
    main.unup_node_size=unup_info.split('symbol-size: ')[1].split(';')[0]
    main.unup_line_color_ui=QColor(unup_info.split('casing-color: ')[1].split(';')[0])
    main.unup_line_width=unup_info.split('casing-width: ')[1].split(';')[0]
    main.unupLineWidthSpinner.setValue(int(main.unup_line_width))
    main.unupNodeWidthSpinner.setValue(int(main.unup_node_size))
    main.unupLineColorpix.fill(main.unup_line_color_ui)
    main.unupLineColorPreview.setPixmap(main.unupLineColorpix)
    main.unupNodeColorpix.fill(main.unup_node_color_ui)
    main.unupNodeColorPreview.setPixmap(main.unupNodeColorpix)

    main.unupNodeShapePixmap = QPixmap(allShapes[main.unup_node_shape])
    main.unupNodeShapeMask = main.unupNodeShapePixmap.createMaskFromColor(QColor(BLACK), Qt.MaskInColor)
    main.unupNodeShapePixmap.fill(main.unup_node_color_ui)
    main.unupNodeShapePixmap.setMask(main.unupNodeShapeMask)
    main.unupNodeShapePixmap=main.unupNodeShapePixmap.scaled(20,20)
    main.unupNodeShapePreview.setPixmap(main.unupNodeShapePixmap)



            
