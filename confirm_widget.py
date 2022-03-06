from PyQt5.QtWidgets import *

def confirmationWidget(main,title,text):
    main.confirmWidget = QMessageBox()
    main.confirmWidget.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    main.confirmWidget.setGeometry(500,500,500,500)
    main.confirmWidget.setWindowTitle(title)
    main.confirmWidget.setText(text)
    main.confirmWidget.show()
    returnValue = main.confirmWidget.exec()
    if returnValue == QMessageBox.Ok:
        main.confirmWidget.close()
        return(True)  
    elif returnValue == QMessageBox.Cancel:
        main.confirmWidget.close()
        return(False)


