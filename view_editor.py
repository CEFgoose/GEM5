from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import *


def open_view_editor_widget(main):
    editor=main.selectedEditors[0]
    main.view_editor_widget=QWidget()
    main.view_editor_widget_layout=QGridLayout()
    main.view_editor_widget.setLayout(main.view_editor_widget_layout)

    main.widget_editor_name=QLabel()
    main.widget_editor_name.setText('Name: %s'%(editor.firstName))
    main.view_editor_widget_layout.addWidget(main.widget_editor_name,0,0)

    main.widget_editor_username=QLabel()
    main.widget_editor_username.setText('Username: %s'%(editor.username))
    main.view_editor_widget_layout.addWidget(main.widget_editor_username,0,1)

    main.widget_editor_line_width=QLabel()
    main.widget_editor_line_width.setText('Line Width: %s'%(editor.lineWidth))
    main.view_editor_widget_layout.addWidget(main.widget_editor_line_width,1,0)

    main.widget_editor_line_color=QLabel()
    main.widget_editor_line_color.setText('Line Color:')
    main.view_editor_widget_layout.addWidget(main.widget_editor_line_color,1,1)

    main.widget_editor_line_color_preview=QLabel()

    main.widget_editor_line_color_preview.setPixmap(editor.lineColorPixmap)
    main.view_editor_widget_layout.addWidget(main.widget_editor_line_color_preview,1,2)



    main.widget_editor_node_size=QLabel()
    main.widget_editor_node_size.setText('Node Size: %s'%(editor.iconSize))
    main.view_editor_widget_layout.addWidget(main.widget_editor_node_size,2,0)

    main.widget_editor_node_shape=QLabel()
    main.widget_editor_node_shape.setPixmap(editor.nodeShape)
    main.view_editor_widget_layout.addWidget(main.widget_editor_node_shape,2,1)

    main.view_editor_widget.show()