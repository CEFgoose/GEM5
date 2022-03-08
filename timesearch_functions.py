from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#---Open or close the calendar widget for time search date selection
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

#---toggles date selectcion mode between start/end dates
def set_date_select_mode(main,select):
    main.dateSelectMode=select
    print(main.dateSelectMode)

#---saves the selected date to the appropriate var(start or end date) and displays the date in the appropriate date field
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

#---grabs the correctly formatted search dates from start/end date fields and constructs search dates for mapcss export
def set_search_dates(main):
    if main.startDateField.text()!= "":
        if main.endDateField.text()!= "":
            main.search_dates  = ("%s/%s"%(main.startDateField.text(),main.endDateField.text()))
        else:
            main.search_dates = "%s/"%(main.startDateField.text())
    else:
        pass


#---clears the start and end dates foields when "clear" button bressed or time search toggled off
def clear_dates(main):
    main.startDateField.setText('')
    main.startDateField.repaint()   
    main.endDateField.setText('')
    main.endDateField.repaint()  
    main.endDateButton.setChecked(False)  
    main.startDateButton.setChecked(False)  
    main.dateSelectMode='start'

#---toggles the time search function on/off
def toggle_time_search(main,value):
    main.time_search_active=value
