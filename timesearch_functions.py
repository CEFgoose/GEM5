from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def open_calendar(main):
    if main.calendarOpen == False:
        main.calendar = QCalendarWidget(main)
        main.openCalendarButton.setText("CLOSE CALENDAR")
        main.calendar.move(350, 400)
        main.calendar.resize(300, 200)
        main.calendar.setGridVisible(True)
        main.calendar.show()
        main.calendar.clicked.connect(lambda:set_date(main,main.calendar.selectedDate()))
        main.calendarOpen = True

    else:
        main.calendar.close()
        main.openCalendarButton.setText("OPEN CALENDAR")
        main.calendarOpen = False

def set_date_select_mode(main,select):
    main.dateSelectMode=select
    print(main.dateSelectMode)

def set_date(main,qDate):
    MONTH = qDate.month()
    DAY = qDate.day()
    if MONTH < 10:
        MONTH = "0%s"%(MONTH)
    if DAY < 10:
        DAY = "0%s"%(DAY)
    if main.dateSelectMode=='start':
        main.startDateField.setText('{0}-{1}-{2}'.format(qDate.year(), MONTH, DAY))
        main.startDateField.repaint()
    else:
        main.endDateField.setText('{0}-{1}-{2}'.format(qDate.year(), MONTH, DAY))
        main.endDateField.repaint()

def set_search_dates(main):
    if main.startDateField.text()!= "":
        if main.endDateField.text()!= "":
            main.search_dates  = ("%s/%s"%(main.startDateField.text(),main.endDateField.text()))
        else:
            main.search_dates = "%s/"%(main.startDateField.text())
    else:
        pass
    print(main.search_dates)

def clear_dates(main):
    main.startDateField.setText('')
    main.startDateField.repaint()   
    main.endDateField.setText('')
    main.endDateField.repaint()  
    main.endDateButton.setChecked(False)  
    main.startDateButton.setChecked(False)  
    main.dateSelectMode='start'


def toggle_time_search(main,value):
    main.time_search_active=value
    print(main.time_search_active)