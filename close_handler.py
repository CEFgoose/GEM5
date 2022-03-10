from export_functions import *

def export_unaltered_file(main):
    for editor in main.currentEditorsOrdered:
        editor.hidden=False
    main.time_search_active=False
    export_clicked(main,'close event')