# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TherapyPortalBiDWTi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

class TherapyPortal(object):
    def TherapyPortalUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(592, 451)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.line_x = QFrame(Form)
        self.line_x.setObjectName(u"line_x")
        self.line_x.setGeometry(QRect(0, 130, 591, 21))
        self.line_x.setFrameShape(QFrame.HLine)
        self.line_x.setFrameShadow(QFrame.Sunken)
        self.line_y = QFrame(Form)
        self.line_y.setObjectName(u"line_y")
        self.line_y.setGeometry(QRect(220, 0, 16, 431))
        self.line_y.setFrameShape(QFrame.VLine)
        self.line_y.setFrameShadow(QFrame.Sunken)
        self.frame_PatientDetails = QFrame(Form)
        self.frame_PatientDetails.setObjectName(u"frame_PatientDetails")
        self.frame_PatientDetails.setGeometry(QRect(0, 0, 231, 141))
        self.frame_PatientDetails.setFrameShape(QFrame.StyledPanel)
        self.frame_PatientDetails.setFrameShadow(QFrame.Raised)
        self.label_PatientID = QLabel(self.frame_PatientDetails)
        self.label_PatientID.setObjectName(u"label_PatientID")
        self.label_PatientID.setGeometry(QRect(10, 30, 81, 16))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_PatientID.setFont(font1)
        self.label_PatientGenderShow = QLabel(self.frame_PatientDetails)
        self.label_PatientGenderShow.setObjectName(u"label_PatientGenderShow")
        self.label_PatientGenderShow.setGeometry(QRect(90, 90, 131, 16))
        self.label_PatientGenderShow.setFont(font1)
        self.label_PatientAgeShow = QLabel(self.frame_PatientDetails)
        self.label_PatientAgeShow.setObjectName(u"label_PatientAgeShow")
        self.label_PatientAgeShow.setGeometry(QRect(90, 70, 131, 16))
        self.label_PatientAgeShow.setFont(font1)
        self.label_PatientName = QLabel(self.frame_PatientDetails)
        self.label_PatientName.setObjectName(u"label_PatientName")
        self.label_PatientName.setGeometry(QRect(10, 50, 81, 16))
        self.label_PatientName.setFont(font1)
        self.label_PatientGender = QLabel(self.frame_PatientDetails)
        self.label_PatientGender.setObjectName(u"label_PatientGender")
        self.label_PatientGender.setGeometry(QRect(10, 90, 81, 16))
        self.label_PatientGender.setFont(font1)
        self.label_PatientDetails = QLabel(self.frame_PatientDetails)
        self.label_PatientDetails.setObjectName(u"label_PatientDetails")
        self.label_PatientDetails.setGeometry(QRect(10, 10, 131, 16))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setUnderline(True)
        font2.setWeight(75)
        self.label_PatientDetails.setFont(font2)
        self.label_PatientNameShow = QLabel(self.frame_PatientDetails)
        self.label_PatientNameShow.setObjectName(u"label_PatientNameShow")
        self.label_PatientNameShow.setGeometry(QRect(90, 50, 131, 16))
        self.label_PatientNameShow.setFont(font1)
        self.label_PatientBloodGroup = QLabel(self.frame_PatientDetails)
        self.label_PatientBloodGroup.setObjectName(u"label_PatientBloodGroup")
        self.label_PatientBloodGroup.setGeometry(QRect(10, 110, 81, 16))
        self.label_PatientBloodGroup.setFont(font1)
        self.label_PatientIDShow = QLabel(self.frame_PatientDetails)
        self.label_PatientIDShow.setObjectName(u"label_PatientIDShow")
        self.label_PatientIDShow.setGeometry(QRect(90, 30, 131, 16))
        self.label_PatientIDShow.setFont(font1)
        self.label_PatientAge = QLabel(self.frame_PatientDetails)
        self.label_PatientAge.setObjectName(u"label_PatientAge")
        self.label_PatientAge.setGeometry(QRect(10, 70, 81, 16))
        self.label_PatientAge.setFont(font1)
        self.label_PatientBloodGroupShow = QLabel(self.frame_PatientDetails)
        self.label_PatientBloodGroupShow.setObjectName(u"label_PatientBloodGroupShow")
        self.label_PatientBloodGroupShow.setGeometry(QRect(90, 110, 131, 16))
        self.label_PatientBloodGroupShow.setFont(font1)
        self.frame_TherapyDetails = QFrame(Form)
        self.frame_TherapyDetails.setObjectName(u"frame_TherapyDetails")
        self.frame_TherapyDetails.setGeometry(QRect(280, 0, 271, 141))
        self.frame_TherapyDetails.setFrameShape(QFrame.StyledPanel)
        self.frame_TherapyDetails.setFrameShadow(QFrame.Raised)
        self.label_Data6 = QLabel(self.frame_TherapyDetails)
        self.label_Data6.setObjectName(u"label_Data6")
        self.label_Data6.setGeometry(QRect(180, 80, 41, 16))
        self.label_Data6.setFont(font1)
        self.label_Data5 = QLabel(self.frame_TherapyDetails)
        self.label_Data5.setObjectName(u"label_Data5")
        self.label_Data5.setGeometry(QRect(180, 60, 41, 16))
        self.label_Data5.setFont(font1)
        self.label_Data5Show = QLabel(self.frame_TherapyDetails)
        self.label_Data5Show.setObjectName(u"label_Data5Show")
        self.label_Data5Show.setGeometry(QRect(230, 60, 41, 16))
        self.label_Data5Show.setFont(font1)
        self.label_Data3Show = QLabel(self.frame_TherapyDetails)
        self.label_Data3Show.setObjectName(u"label_Data3Show")
        self.label_Data3Show.setGeometry(QRect(50, 80, 41, 16))
        self.label_Data3Show.setFont(font1)
        self.label_Data6Show = QLabel(self.frame_TherapyDetails)
        self.label_Data6Show.setObjectName(u"label_Data6Show")
        self.label_Data6Show.setGeometry(QRect(230, 80, 41, 16))
        self.label_Data6Show.setFont(font1)
        self.label_Data4Show = QLabel(self.frame_TherapyDetails)
        self.label_Data4Show.setObjectName(u"label_Data4Show")
        self.label_Data4Show.setGeometry(QRect(230, 40, 41, 16))
        self.label_Data4Show.setFont(font1)
        self.label_Data1Show = QLabel(self.frame_TherapyDetails)
        self.label_Data1Show.setObjectName(u"label_Data1Show")
        self.label_Data1Show.setGeometry(QRect(50, 40, 41, 16))
        self.label_Data1Show.setFont(font1)
        self.label_Data4 = QLabel(self.frame_TherapyDetails)
        self.label_Data4.setObjectName(u"label_Data4")
        self.label_Data4.setGeometry(QRect(180, 40, 41, 16))
        self.label_Data4.setFont(font1)
        self.label_Data1 = QLabel(self.frame_TherapyDetails)
        self.label_Data1.setObjectName(u"label_Data1")
        self.label_Data1.setGeometry(QRect(0, 40, 41, 16))
        self.label_Data1.setFont(font1)
        self.label_Data2Show = QLabel(self.frame_TherapyDetails)
        self.label_Data2Show.setObjectName(u"label_Data2Show")
        self.label_Data2Show.setGeometry(QRect(50, 60, 41, 16))
        self.label_Data2Show.setFont(font1)
        self.label_TherayDetails = QLabel(self.frame_TherapyDetails)
        self.label_TherayDetails.setObjectName(u"label_TherayDetails")
        self.label_TherayDetails.setGeometry(QRect(80, 10, 131, 16))
        self.label_TherayDetails.setFont(font2)
        self.label_Data3 = QLabel(self.frame_TherapyDetails)
        self.label_Data3.setObjectName(u"label_Data3")
        self.label_Data3.setGeometry(QRect(0, 80, 41, 16))
        self.label_Data3.setFont(font1)
        self.pushButton_Show3DVisualization = QPushButton(self.frame_TherapyDetails)
        self.pushButton_Show3DVisualization.setObjectName(u"pushButton_Show3DVisualization")
        self.pushButton_Show3DVisualization.setGeometry(QRect(80, 110, 121, 23))
        self.pushButton_Show3DVisualization.setFont(font1)
        self.label_Data2 = QLabel(self.frame_TherapyDetails)
        self.label_Data2.setObjectName(u"label_Data2")
        self.label_Data2.setGeometry(QRect(0, 60, 41, 16))
        self.label_Data2.setFont(font1)
        self.frame_3DVisualization = QFrame(Form)
        self.frame_3DVisualization.setObjectName(u"frame_3DVisualization")
        self.frame_3DVisualization.setGeometry(QRect(230, 140, 361, 281))
        self.frame_3DVisualization.setFrameShape(QFrame.StyledPanel)
        self.frame_3DVisualization.setFrameShadow(QFrame.Raised)
        self.label_15 = QLabel(self.frame_3DVisualization)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(130, 10, 131, 16))
        self.label_15.setFont(font2)
        self.frame_3DVisualizationSimulation = QFrame(self.frame_3DVisualization)
        self.frame_3DVisualizationSimulation.setObjectName(u"frame_3DVisualizationSimulation")
        self.frame_3DVisualizationSimulation.setGeometry(QRect(10, 30, 341, 231))
        self.frame_3DVisualizationSimulation.setMouseTracking(False)
        self.frame_3DVisualizationSimulation.setFrameShape(QFrame.StyledPanel)
        self.frame_3DVisualizationSimulation.setFrameShadow(QFrame.Raised)
        self.line_x1 = QFrame(Form)
        self.line_x1.setObjectName(u"line_x1")
        self.line_x1.setGeometry(QRect(0, 420, 591, 21))
        self.line_x1.setFrameShape(QFrame.HLine)
        self.line_x1.setFrameShadow(QFrame.Sunken)
        self.frame_TherapyController = QFrame(Form)
        self.frame_TherapyController.setObjectName(u"frame_TherapyController")
        self.frame_TherapyController.setGeometry(QRect(0, 140, 231, 281))
        self.frame_TherapyController.setFrameShape(QFrame.StyledPanel)
        self.frame_TherapyController.setFrameShadow(QFrame.Raised)
        self.label_TherapyController = QLabel(self.frame_TherapyController)
        self.label_TherapyController.setObjectName(u"label_TherapyController")
        self.label_TherapyController.setGeometry(QRect(10, 10, 161, 16))
        self.label_TherapyController.setFont(font2)
        self.label_TherapyStatusShow = QLabel(self.frame_TherapyController)
        self.label_TherapyStatusShow.setObjectName(u"label_TherapyStatusShow")
        self.label_TherapyStatusShow.setGeometry(QRect(100, 220, 121, 20))
        self.label_TherapyStatusShow.setFont(font1)
        self.label_SessionTime = QLabel(self.frame_TherapyController)
        self.label_SessionTime.setObjectName(u"label_SessionTime")
        self.label_SessionTime.setGeometry(QRect(10, 250, 81, 16))
        self.label_SessionTime.setFont(font1)
        self.label_Mode = QLabel(self.frame_TherapyController)
        self.label_Mode.setObjectName(u"label_Mode")
        self.label_Mode.setGeometry(QRect(10, 70, 81, 16))
        self.label_Mode.setFont(font1)
        self.label_Arm = QLabel(self.frame_TherapyController)
        self.label_Arm.setObjectName(u"label_Arm")
        self.label_Arm.setGeometry(QRect(10, 40, 81, 16))
        self.label_Arm.setFont(font1)
        self.pushButton_ConnectWithHardware = QPushButton(self.frame_TherapyController)
        self.pushButton_ConnectWithHardware.setObjectName(u"pushButton_ConnectWithHardware")
        self.pushButton_ConnectWithHardware.setGeometry(QRect(40, 130, 141, 23))
        self.pushButton_ConnectWithHardware.setFont(font1)
        self.label_TherapyStatus = QLabel(self.frame_TherapyController)
        self.label_TherapyStatus.setObjectName(u"label_TherapyStatus")
        self.label_TherapyStatus.setGeometry(QRect(10, 220, 81, 16))
        self.label_TherapyStatus.setFont(font1)
        self.comboBox_TherapyModeChoose = QComboBox(self.frame_TherapyController)
        self.comboBox_TherapyModeChoose.addItem("")
        self.comboBox_TherapyModeChoose.addItem("")
        self.comboBox_TherapyModeChoose.setObjectName(u"comboBox_TherapyModeChoose")
        self.comboBox_TherapyModeChoose.setGeometry(QRect(90, 70, 131, 22))
        self.comboBox_TherapyModeChoose.setFont(font1)
        self.pushButton_StopTherapy = QPushButton(self.frame_TherapyController)
        self.pushButton_StopTherapy.setObjectName(u"pushButton_StopTherapy")
        self.pushButton_StopTherapy.setGeometry(QRect(50, 190, 121, 23))
        self.pushButton_StopTherapy.setFont(font1)
        self.pushButton_StartTherapy = QPushButton(self.frame_TherapyController)
        self.pushButton_StartTherapy.setObjectName(u"pushButton_StartTherapy")
        self.pushButton_StartTherapy.setGeometry(QRect(50, 160, 121, 23))
        self.pushButton_StartTherapy.setFont(font1)
        self.comboBox_ArmChoose = QComboBox(self.frame_TherapyController)
        self.comboBox_ArmChoose.addItem("")
        self.comboBox_ArmChoose.addItem("")
        self.comboBox_ArmChoose.setObjectName(u"comboBox_ArmChoose")
        self.comboBox_ArmChoose.setGeometry(QRect(90, 40, 131, 22))
        self.comboBox_ArmChoose.setFont(font1)
        self.label_Type = QLabel(self.frame_TherapyController)
        self.label_Type.setObjectName(u"label_Type")
        self.label_Type.setGeometry(QRect(10, 100, 81, 16))
        self.label_Type.setFont(font1)
        self.comboBox_TherapyTypeChoose = QComboBox(self.frame_TherapyController)
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.addItem("")
        self.comboBox_TherapyTypeChoose.setObjectName(u"comboBox_TherapyTypeChoose")
        self.comboBox_TherapyTypeChoose.setGeometry(QRect(90, 100, 131, 22))
        self.comboBox_TherapyTypeChoose.setFont(font1)
        self.label_TherapyTimeShow = QLabel(self.frame_TherapyController)
        self.label_TherapyTimeShow.setObjectName(u"label_TherapyTimeShow")
        self.label_TherapyTimeShow.setGeometry(QRect(100, 250, 121, 20))
        self.label_TherapyTimeShow.setFont(font1)
        self.label_HardwareConnectionStatus = QLabel(Form)
        self.label_HardwareConnectionStatus.setObjectName(u"label_HardwareConnectionStatus")
        self.label_HardwareConnectionStatus.setGeometry(QRect(400, 430, 181, 20))
        self.label_HardwareConnectionStatus.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # TherapyPortalUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Therapy Portal", None))
        self.label_PatientID.setText(QCoreApplication.translate("Form", u"Patient ID :", None))
        self.label_PatientGenderShow.setText("")
        self.label_PatientAgeShow.setText("")
        self.label_PatientName.setText(QCoreApplication.translate("Form", u"Patient's Name :", None))
        self.label_PatientGender.setText(QCoreApplication.translate("Form", u"Gender :", None))
        self.label_PatientDetails.setText(QCoreApplication.translate("Form", u"Patient's Details", None))
        self.label_PatientNameShow.setText("")
        self.label_PatientBloodGroup.setText(QCoreApplication.translate("Form", u"Blood Group :", None))
        self.label_PatientIDShow.setText("")
        self.label_PatientAge.setText(QCoreApplication.translate("Form", u"Age :", None))
        self.label_PatientBloodGroupShow.setText("")
        self.label_Data6.setText(QCoreApplication.translate("Form", u"Data 6 :", None))
        self.label_Data5.setText(QCoreApplication.translate("Form", u"Data 5 :", None))
        self.label_Data5Show.setText("")
        self.label_Data3Show.setText("")
        self.label_Data6Show.setText("")
        self.label_Data4Show.setText("")
        self.label_Data1Show.setText("")
        self.label_Data4.setText(QCoreApplication.translate("Form", u"Data 4 :", None))
        self.label_Data1.setText(QCoreApplication.translate("Form", u"Data 1 :", None))
        self.label_Data2Show.setText("")
        self.label_TherayDetails.setText(QCoreApplication.translate("Form", u"Therapy Details", None))
        self.label_Data3.setText(QCoreApplication.translate("Form", u"Data 3 :", None))
        self.pushButton_Show3DVisualization.setText(QCoreApplication.translate("Form", u"Show 3D Visualization", None))
        self.label_Data2.setText(QCoreApplication.translate("Form", u"Data 2 :", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"3D Visualization", None))
        self.label_TherapyController.setText(QCoreApplication.translate("Form", u"Therapy Controller", None))
        self.label_TherapyStatusShow.setText("")
        self.label_SessionTime.setText(QCoreApplication.translate("Form", u"Session Time :", None))
        self.label_Mode.setText(QCoreApplication.translate("Form", u"Mode :", None))
        self.label_Arm.setText(QCoreApplication.translate("Form", u"Arm :", None))
        self.pushButton_ConnectWithHardware.setText(QCoreApplication.translate("Form", u"Connect with Hardware", None))
        self.label_TherapyStatus.setText(QCoreApplication.translate("Form", u"Therapy Status :", None))
        self.comboBox_TherapyModeChoose.setItemText(0, QCoreApplication.translate("Form", u"Active", None))
        self.comboBox_TherapyModeChoose.setItemText(1, QCoreApplication.translate("Form", u"Passive", None))

        self.pushButton_StopTherapy.setText(QCoreApplication.translate("Form", u"Stop Therapy", None))
        self.pushButton_StartTherapy.setText(QCoreApplication.translate("Form", u"Start Therapy", None))
        self.comboBox_ArmChoose.setItemText(0, QCoreApplication.translate("Form", u"Right", None))
        self.comboBox_ArmChoose.setItemText(1, QCoreApplication.translate("Form", u"Left", None))

        self.label_Type.setText(QCoreApplication.translate("Form", u"Type :", None))
        self.comboBox_TherapyTypeChoose.setItemText(0, QCoreApplication.translate("Form", u"Armpit stretch", None))
        self.comboBox_TherapyTypeChoose.setItemText(1, QCoreApplication.translate("Form", u"Finger walk", None))
        self.comboBox_TherapyTypeChoose.setItemText(2, QCoreApplication.translate("Form", u"Forward flexion", None))
        self.comboBox_TherapyTypeChoose.setItemText(3, QCoreApplication.translate("Form", u"Inward rotation", None))
        self.comboBox_TherapyTypeChoose.setItemText(4, QCoreApplication.translate("Form", u"Neck stretches", None))
        self.comboBox_TherapyTypeChoose.setItemText(5, QCoreApplication.translate("Form", u"Pendulum stretch", None))
        self.comboBox_TherapyTypeChoose.setItemText(6, QCoreApplication.translate("Form", u"Scapular Retractions", None))
        self.comboBox_TherapyTypeChoose.setItemText(7, QCoreApplication.translate("Form", u"Towel stretch", None))

        self.label_TherapyTimeShow.setText("")
        self.label_HardwareConnectionStatus.setText("")
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = TherapyPortal()
    ui.TherapyPortalUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())