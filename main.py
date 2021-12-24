from PyQt5 import QtWidgets
import sys
import re
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator, QRegExpValidator, QDoubleValidator

class Page1(QMainWindow):
    def __init__(self):
        super(Page1, self).__init__()
        loadUi("page1.ui",self)
        # this will only allow user to enter integers and nothing else
        object_for_ageValidator = QIntValidator()
        self.lineEdit_input_age.setValidator(object_for_ageValidator)
        
        #it will allow user to enter only alphabets in name
        object_for_nameValidator = QRegExpValidator(QRegExp("[A-Za-z ]+"))
        self.lineEdit_input_name.setValidator(object_for_nameValidator)
        
        
        #it will allow user to enter valid email IDs
        object_for_emailValidator = QRegExpValidator(QRegExp("[a-zA-Z0-9+_.-]+@[a-z]+[.a-z]{2,4}"))
        self.lineEdit_input_email_ID.setValidator(object_for_emailValidator)
        

        self.pushButton_next_page.clicked.connect(self.show_page2)
        
        
    def show_page2(self):
        """method to go to page2 
        """
        ##check if the fields are empty
        isTrue = self.check_if_empty()
        
        if isTrue:
            widget.setCurrentIndex(1)
        
    def show_specific_error_popup(self, y):
        """shows a warning window with a apecific message 
        """
        msg = QMessageBox()
        msg.setWindowTitle("Error popup")
        msg.setText(y)
        # add message box icon
        msg.setIcon(QMessageBox.Warning)
        msg.adjustSize()
        x = msg.exec_()       
        
        
    def show_error_popup(self):
        """shows a warning message 
        """
        msg = QMessageBox()
        msg.setWindowTitle("Error popup")
        msg.setText("Fields cannot be left empty !")
        # add message box icon
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()

    def check_email_ID(self, email_ID):
        """checks if the given email ID is according to regular expression of email ID
           returns False if it's not according to regex
           otherwise returns True
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email_ID)):
            return True
        return False
    
    def check_if_empty(self):
        """checks if input fields are empty , calls show_error_popup method if some field is empty
           checks if the age is in between [0, 150], calls show_error_popup with the given error
            
           if there are no errors, empty fields, this method returns True, else returns False
        """
        username = self.lineEdit_input_name.text()
        age = (self.lineEdit_input_age.text())
        email_ID = self.lineEdit_input_email_ID.text()
        radio_button_is_checked = self.radioButton_input_male.isChecked() or self.radioButton_input_female.isChecked() or self.radioButton_input_other.isChecked()
        if username and age and email_ID and radio_button_is_checked:
            # return True
            if int(age) < 0 or int(age) > 150:
                self.show_specific_error_popup("Age should be between 0 to 150")
                return False
            if not self.check_email_ID(email_ID):
                self.show_specific_error_popup("Invalid email ID")
                return False
        else:
            self.show_error_popup()
            return False
        return True
    
class Page2(QMainWindow):
    def __init__(self):
        super(Page2,self).__init__()
        loadUi("page2.ui", self)
        #it will allow user to enter only double type of cgpa
        object_for_cgpaValidator = QDoubleValidator()
        self.lineEdit_input_ug_cgpa.setValidator(object_for_cgpaValidator)
        self.lineEdit_input_pg_cgpa.setValidator(object_for_cgpaValidator)
        
        #it will allow user to only enter alphabets for institute name
        object_for_instituteValidator = QRegExpValidator(QRegExp("[A-Za-z ]+"))
        self.lineEdit_input_institution.setValidator(object_for_instituteValidator)
        
        # calls show_popup method to validate the input fields upon clicking Submit button
        isTrue = self.pushButton_submit.clicked.connect(self.check_if_empty)
        if isTrue:
            self.pushButton_submit.clicked.connect(self.show_popup)
        
        # calls resume opener method upon clicking push button with 📂 icon
        self.pushButton_folder.clicked.connect(self.resume_opener)
    
    def resume_opener(self):
        """Opens the file explorer of the system to find resume 
           prints the name of the file with location in lineEdit text box  
        """
        resume_file = QtWidgets.QFileDialog.getOpenFileName(None, 'Open your resume ', 'C:\\Users\\shree\\OneDrive\\Desktop') 
        self.lineEdit_input_resume.setText(resume_file[0])
        
    def show_popup(self):
        """this popup is called on click of pushbutton if all the fields are validated
           This pop up opens a small window to show Successful Submission 
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Pop up")
        msg.setText("Success! Your submission has been saved!")
        ##check if the fields are empty
        isTrue = self.check_if_empty()
        if isTrue:
            x = msg.exec_()
            
            
    def check_if_empty(self):
        """this method gets the fields like institution name, cgpa and other fields from Page2
           checks if any method is empty, there are empty, show_error_popup() method is called
           if there is any discrepency in the entered fields like if cgpa is not in between [0.0, 10,0],
            ->show_error_popup() with specific error message is called
           this method returns True if all the methods are validated
           otherwise returns False
        """
        institution = self.lineEdit_input_institution.text()
        ug_cgpa = (self.lineEdit_input_ug_cgpa.text())
        pg_cgpa = (self.lineEdit_input_pg_cgpa.text())
        ug_combobox = str(self.comboBox_input_UGCourse.currentText())
        pg_combobox = str(self.comboBox_input_PGCourse.currentText())
        resume = self.lineEdit_input_resume.text()
        combobox_isSelected = ug_combobox != "Select" and pg_combobox != "Select"
        valid_cgpa = True
        if institution and valid_cgpa and combobox_isSelected and resume:
            if (float(ug_cgpa) < 0.0 or float(ug_cgpa) > 10.0) or (float(pg_cgpa) < 0.0 or float(pg_cgpa) > 10.0):
                self.show_specific_error_popup("CGPA should be in the range of 0 to 10")
                valid_cgpa = False
                return False
        else:
            self.show_error_popup()
            return False
        return True    
        
    
    
    def show_error_popup(self):
        """shows warning message as a samll popup window 
        """
        msg = QMessageBox()
        msg.setWindowTitle("Error popup")
        msg.setText("Fields cannot be left empty !")
        # add message box icon
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()    

    def show_specific_error_popup(self, y):
        """shows a specific warning message as a small popup window 
        """
        msg = QMessageBox()
        msg.setWindowTitle("Error popup")
        msg.setText(y)
        # add message box icon
        msg.setIcon(QMessageBox.Warning)
        msg.adjustSize()
        x = msg.exec_()   

#stacking Page1 and Page2 and calling page1.ui in the beginning
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
page1 = Page1()
page2 = Page2()
widget.addWidget(page1)
widget.addWidget(page2)
widget.setCurrentIndex(0)
widget.show()

#window is not in full size, so set the size for the window
widget.setFixedWidth(1070)
widget.setFixedHeight(750)

app.exec_()