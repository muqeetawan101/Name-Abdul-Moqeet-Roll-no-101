import os
import sys
import json
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication, QWidget, QMainWindow, QStackedWidget,
    QLabel, QLineEdit, QPushButton, QFrame, QVBoxLayout,
    QHBoxLayout, QToolButton, QListWidget, QListWidgetItem,
    QTableWidget, QTableWidgetItem, QTabWidget, QComboBox,
    QGridLayout, QSizePolicy, QScrollArea, QMessageBox, QInputDialog,
    QDialog
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtGui, QtWidgets

# ─────────────────────────────────────────────
#  QT DESIGNER GENERATED UI CLASSES
#  (compiled from add_new_case.ui, client_pannel.ui, create_user.ui,
#   delete_confirmation.ui, delete_user.ui via pyuic5)
# ─────────────────────────────────────────────

class Ui_FileNewCaseForm(object):
    def setupUi(self, FileNewCaseForm):
        FileNewCaseForm.setObjectName("FileNewCaseForm")
        FileNewCaseForm.resize(375, 760)
        FileNewCaseForm.setStyleSheet("QWidget#FileNewCaseForm {\n"
"    background-color: #0d1117;\n"
"}\n"
"QLabel {\n"
"    color: #e6e8eb;\n"
"}")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(FileNewCaseForm)
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.setSpacing(0)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.headerFrame = QtWidgets.QFrame(FileNewCaseForm)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 56))
        self.headerFrame.setStyleSheet("QFrame#headerFrame {\n"
"    background-color: #111827;\n"
"    border-bottom: 1px solid #1f2937;\n"
"}")
        self.headerFrame.setObjectName("headerFrame")
        self.headerLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        self.headerLayout.setContentsMargins(16, -1, 16, -1)
        self.headerLayout.setObjectName("headerLayout")
        self.btnMenu = QtWidgets.QToolButton(self.headerFrame)
        self.btnMenu.setStyleSheet("QToolButton {\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.btnMenu.setObjectName("btnMenu")
        self.headerLayout.addWidget(self.btnMenu)
        self.lblHeaderTitle = QtWidgets.QLabel(self.headerFrame)
        self.lblHeaderTitle.setStyleSheet("color:#ffffff; font-size:15px; font-weight:600; margin-left:6px;")
        self.lblHeaderTitle.setObjectName("lblHeaderTitle")
        self.headerLayout.addWidget(self.lblHeaderTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        self.btnUserAvatar = QtWidgets.QToolButton(self.headerFrame)
        self.btnUserAvatar.setStyleSheet("QToolButton {\n"
"    color: #ffffff;\n"
"    background-color: #1f2937;\n"
"    border-radius: 14px;\n"
"    min-width: 28px;\n"
"    min-height: 28px;\n"
"}")
        self.btnUserAvatar.setObjectName("btnUserAvatar")
        self.headerLayout.addWidget(self.btnUserAvatar)
        self.mainVerticalLayout.addWidget(self.headerFrame)
        self.formScrollArea = QtWidgets.QScrollArea(FileNewCaseForm)
        self.formScrollArea.setWidgetResizable(True)
        self.formScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.formScrollArea.setStyleSheet("QScrollArea {\n"
"    border: none;\n"
"    background: transparent;\n"
"}")
        self.formScrollArea.setObjectName("formScrollArea")
        self.formScrollContents = QtWidgets.QWidget()
        self.formScrollContents.setGeometry(QtCore.QRect(0, 0, 375, 700))
        self.formScrollContents.setObjectName("formScrollContents")
        self.formScrollLayout = QtWidgets.QVBoxLayout(self.formScrollContents)
        self.formScrollLayout.setContentsMargins(16, 16, 16, 16)
        self.formScrollLayout.setSpacing(14)
        self.formScrollLayout.setObjectName("formScrollLayout")
        self.formCardFrame = QtWidgets.QFrame(self.formScrollContents)
        self.formCardFrame.setStyleSheet("QFrame#formCardFrame {\n"
"    background-color: #ffffff;\n"
"    border-radius: 14px;\n"
"}")
        self.formCardFrame.setObjectName("formCardFrame")
        self.formCardLayout = QtWidgets.QVBoxLayout(self.formCardFrame)
        self.formCardLayout.setContentsMargins(20, 20, 20, 20)
        self.formCardLayout.setSpacing(10)
        self.formCardLayout.setObjectName("formCardLayout")
        self.lblNewCaseSubmissionsHeading = QtWidgets.QLabel(self.formCardFrame)
        self.lblNewCaseSubmissionsHeading.setStyleSheet("color:#d4a843; font-size:17px; font-weight:700;")
        self.lblNewCaseSubmissionsHeading.setObjectName("lblNewCaseSubmissionsHeading")
        self.formCardLayout.addWidget(self.lblNewCaseSubmissionsHeading)
        self.lblFormSubtitle = QtWidgets.QLabel(self.formCardFrame)
        self.lblFormSubtitle.setWordWrap(True)
        self.lblFormSubtitle.setStyleSheet("color:#6b7280; font-size:12px; margin-bottom:8px;")
        self.lblFormSubtitle.setObjectName("lblFormSubtitle")
        self.formCardLayout.addWidget(self.lblFormSubtitle)
        self.lblCaseTitle = QtWidgets.QLabel(self.formCardFrame)
        self.lblCaseTitle.setStyleSheet("color:#374151; font-size:12px; font-weight:700;")
        self.lblCaseTitle.setObjectName("lblCaseTitle")
        self.formCardLayout.addWidget(self.lblCaseTitle)
        self.txtCaseTitle = QtWidgets.QLineEdit(self.formCardFrame)
        self.txtCaseTitle.setMinimumSize(QtCore.QSize(0, 40))
        self.txtCaseTitle.setStyleSheet("QLineEdit {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    color: #1a1a1a;\n"
"    font-size: 13px;\n"
"}")
        self.txtCaseTitle.setObjectName("txtCaseTitle")
        self.formCardLayout.addWidget(self.txtCaseTitle)
        self.lblClientNameId = QtWidgets.QLabel(self.formCardFrame)
        self.lblClientNameId.setStyleSheet("color:#374151; font-size:12px; font-weight:700; margin-top:4px;")
        self.lblClientNameId.setObjectName("lblClientNameId")
        self.formCardLayout.addWidget(self.lblClientNameId)
        self.clientNameInputFrame = QtWidgets.QFrame(self.formCardFrame)
        self.clientNameInputFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.clientNameInputFrame.setStyleSheet("QFrame#clientNameInputFrame {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"}")
        self.clientNameInputFrame.setObjectName("clientNameInputFrame")
        self.clientNameInputLayout = QtWidgets.QHBoxLayout(self.clientNameInputFrame)
        self.clientNameInputLayout.setContentsMargins(10, 0, 10, 0)
        self.clientNameInputLayout.setSpacing(6)
        self.clientNameInputLayout.setObjectName("clientNameInputLayout")
        self.iconClientName = QtWidgets.QLabel(self.clientNameInputFrame)
        self.iconClientName.setStyleSheet("background: transparent; color:#16a085; font-size:12px;")
        self.iconClientName.setObjectName("iconClientName")
        self.clientNameInputLayout.addWidget(self.iconClientName)
        self.txtClientName = QtWidgets.QLineEdit(self.clientNameInputFrame)
        self.txtClientName.setStyleSheet("QLineEdit {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #16a085;\n"
"    font-size: 13px;\n"
"}")
        self.txtClientName.setObjectName("txtClientName")
        self.clientNameInputLayout.addWidget(self.txtClientName)
        self.formCardLayout.addWidget(self.clientNameInputFrame)
        self.lblCategory = QtWidgets.QLabel(self.formCardFrame)
        self.lblCategory.setStyleSheet("color:#374151; font-size:12px; font-weight:700; margin-top:4px;")
        self.lblCategory.setObjectName("lblCategory")
        self.formCardLayout.addWidget(self.lblCategory)
        self.comboCategory = QtWidgets.QComboBox(self.formCardFrame)
        self.comboCategory.setMinimumSize(QtCore.QSize(0, 40))
        self.comboCategory.setStyleSheet("QComboBox {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    color: #5b6472;\n"
"    font-size: 13px;\n"
"}")
        self.comboCategory.setObjectName("comboCategory")
        self.comboCategory.addItem("")
        self.comboCategory.addItem("")
        self.comboCategory.addItem("")
        self.comboCategory.addItem("")
        self.comboCategory.addItem("")
        self.formCardLayout.addWidget(self.comboCategory)
        self.lblPriorityLevel = QtWidgets.QLabel(self.formCardFrame)
        self.lblPriorityLevel.setStyleSheet("color:#374151; font-size:12px; font-weight:700; margin-top:4px;")
        self.lblPriorityLevel.setObjectName("lblPriorityLevel")
        self.formCardLayout.addWidget(self.lblPriorityLevel)
        self.comboPriorityLevel = QtWidgets.QComboBox(self.formCardFrame)
        self.comboPriorityLevel.setMinimumSize(QtCore.QSize(0, 40))
        self.comboPriorityLevel.setStyleSheet("QComboBox {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"    padding: 8px 10px;\n"
"    color: #374151;\n"
"    font-size: 13px;\n"
"}")
        self.comboPriorityLevel.setObjectName("comboPriorityLevel")
        self.comboPriorityLevel.addItem("")
        self.comboPriorityLevel.addItem("")
        self.comboPriorityLevel.addItem("")
        self.formCardLayout.addWidget(self.comboPriorityLevel)
        self.lblCaseDescription = QtWidgets.QLabel(self.formCardFrame)
        self.lblCaseDescription.setStyleSheet("color:#374151; font-size:12px; font-weight:700; margin-top:4px;")
        self.lblCaseDescription.setObjectName("lblCaseDescription")
        self.formCardLayout.addWidget(self.lblCaseDescription)
        self.txtCaseDescription = QtWidgets.QTextEdit(self.formCardFrame)
        self.txtCaseDescription.setMinimumSize(QtCore.QSize(0, 110))
        self.txtCaseDescription.setStyleSheet("QTextEdit {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: #222222;\n"
"    font-size: 13px;\n"
"}")
        self.txtCaseDescription.setObjectName("txtCaseDescription")
        self.formCardLayout.addWidget(self.txtCaseDescription)
        self.formScrollLayout.addWidget(self.formCardFrame)
        self.btnSubmitCase = QtWidgets.QPushButton(self.formScrollContents)
        self.btnSubmitCase.setMinimumSize(QtCore.QSize(0, 48))
        self.btnSubmitCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSubmitCase.setStyleSheet("QPushButton#btnSubmitCase {\n"
"    background-color: #11162a;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-weight: 700;\n"
"    font-size: 13px;\n"
"}\n"
"QPushButton#btnSubmitCase:hover {\n"
"    background-color: #1a2138;\n"
"}\n"
"QPushButton#btnSubmitCase:pressed {\n"
"    background-color: #0a0d1a;\n"
"}")
        self.btnSubmitCase.setObjectName("btnSubmitCase")
        self.formScrollLayout.addWidget(self.btnSubmitCase)
        self.btnCancel = QtWidgets.QPushButton(self.formScrollContents)
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 48))
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("QPushButton#btnCancel {\n"
"    background-color: #ffffff;\n"
"    color: #11162a;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 10px;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #f3f4f6;\n"
"}")
        self.btnCancel.setObjectName("btnCancel")
        self.formScrollLayout.addWidget(self.btnCancel)
        self.formScrollArea.setWidget(self.formScrollContents)
        self.mainVerticalLayout.addWidget(self.formScrollArea)

        self.retranslateUi(FileNewCaseForm)
        QtCore.QMetaObject.connectSlotsByName(FileNewCaseForm)

    def retranslateUi(self, FileNewCaseForm):
        _translate = QtCore.QCoreApplication.translate
        FileNewCaseForm.setWindowTitle(_translate("FileNewCaseForm", "File New Case"))
        self.btnMenu.setText(_translate("FileNewCaseForm", "≡"))
        self.lblHeaderTitle.setText(_translate("FileNewCaseForm", "File New Case"))
        self.btnUserAvatar.setText(_translate("FileNewCaseForm", "👤"))
        self.lblNewCaseSubmissionsHeading.setText(_translate("FileNewCaseForm", "New Case Submissions"))
        self.lblFormSubtitle.setText(_translate("FileNewCaseForm", "Please fill in the legal documentation details below to register a new case in the system."))
        self.lblCaseTitle.setText(_translate("FileNewCaseForm", "Case Title"))
        self.txtCaseTitle.setPlaceholderText(_translate("FileNewCaseForm", "e.g., State vs. Peterson (Civil)"))
        self.lblClientNameId.setText(_translate("FileNewCaseForm", "Client Name / ID"))
        self.iconClientName.setText(_translate("FileNewCaseForm", "👤"))
        self.txtClientName.setPlaceholderText(_translate("FileNewCaseForm", "Search or Enter Client Name"))
        self.lblCategory.setText(_translate("FileNewCaseForm", "Category"))
        self.comboCategory.setItemText(0, _translate("FileNewCaseForm", "Select Category"))
        self.comboCategory.setItemText(1, _translate("FileNewCaseForm", "Civil"))
        self.comboCategory.setItemText(2, _translate("FileNewCaseForm", "Criminal"))
        self.comboCategory.setItemText(3, _translate("FileNewCaseForm", "Family"))
        self.comboCategory.setItemText(4, _translate("FileNewCaseForm", "Corporate"))
        self.lblPriorityLevel.setText(_translate("FileNewCaseForm", "Priority Level"))
        self.comboPriorityLevel.setItemText(0, _translate("FileNewCaseForm", "Low"))
        self.comboPriorityLevel.setItemText(1, _translate("FileNewCaseForm", "Medium"))
        self.comboPriorityLevel.setItemText(2, _translate("FileNewCaseForm", "High"))
        self.lblCaseDescription.setText(_translate("FileNewCaseForm", "Case Description"))
        self.txtCaseDescription.setPlaceholderText(_translate("FileNewCaseForm", "Enter detailed case narrative, primary claims, and initial evidence summary..."))
        self.btnSubmitCase.setText(_translate("FileNewCaseForm", "Submit Case"))
        self.btnCancel.setText(_translate("FileNewCaseForm", "Cancel"))


class Ui_ClientDashboardPage(object):
    def setupUi(self, ClientDashboardPage):
        ClientDashboardPage.setObjectName("ClientDashboardPage")
        ClientDashboardPage.resize(1100, 700)
        ClientDashboardPage.setStyleSheet("QWidget#ClientDashboardPage {\n"
"    background-color: #0a0c12;\n"
"}\n"
"QLabel {\n"
"    color: #e6e8eb;\n"
"}")
        self.rootLayout = QtWidgets.QHBoxLayout(ClientDashboardPage)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")
        self.sidebarFrame = QtWidgets.QFrame(ClientDashboardPage)
        self.sidebarFrame.setMinimumSize(QtCore.QSize(200, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebarFrame.setStyleSheet("QFrame#sidebarFrame {\n"
"    background-color: #12141c;\n"
"    border-right: 1px solid #1f2230;\n"
"}")
        self.sidebarFrame.setObjectName("sidebarFrame")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setContentsMargins(18, 22, 18, 22)
        self.sidebarLayout.setSpacing(6)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.btnUserAvatar = QtWidgets.QToolButton(self.sidebarFrame)
        self.btnUserAvatar.setMinimumSize(QtCore.QSize(40, 40))
        self.btnUserAvatar.setStyleSheet("QToolButton {\n"
"    color: #ffffff;\n"
"    background-color: #232634;\n"
"    border-radius: 20px;\n"
"    font-size: 16px;\n"
"    margin-bottom: 6px;\n"
"}")
        self.btnUserAvatar.setObjectName("btnUserAvatar")
        self.sidebarLayout.addWidget(self.btnUserAvatar)
        self.lblWelcomeBackTitle = QtWidgets.QLabel(self.sidebarFrame)
        self.lblWelcomeBackTitle.setStyleSheet("color:#ffffff; font-size:15px; font-weight:700;")
        self.lblWelcomeBackTitle.setObjectName("lblWelcomeBackTitle")
        self.sidebarLayout.addWidget(self.lblWelcomeBackTitle)
        self.lblWelcomeBackSubtitle = QtWidgets.QLabel(self.sidebarFrame)
        self.lblWelcomeBackSubtitle.setStyleSheet("color:#7c8794; font-size:11px; margin-bottom:16px;")
        self.lblWelcomeBackSubtitle.setObjectName("lblWelcomeBackSubtitle")
        self.sidebarLayout.addWidget(self.lblWelcomeBackSubtitle)
        self.btnNavDashboard = QtWidgets.QPushButton(self.sidebarFrame)
        self.btnNavDashboard.setMinimumSize(QtCore.QSize(0, 38))
        self.btnNavDashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavDashboard.setStyleSheet("QPushButton#btnNavDashboard {\n"
"    background-color: #232842;\n"
"    color: #ffffff;\n"
"    text-align: left;\n"
"    padding-left: 12px;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}")
        self.btnNavDashboard.setObjectName("btnNavDashboard")
        self.sidebarLayout.addWidget(self.btnNavDashboard)
        self.btnNavCases = QtWidgets.QPushButton(self.sidebarFrame)
        self.btnNavCases.setMinimumSize(QtCore.QSize(0, 38))
        self.btnNavCases.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavCases.setStyleSheet("QPushButton#btnNavCases {\n"
"    background-color: transparent;\n"
"    color: #9aa1ac;\n"
"    text-align: left;\n"
"    padding-left: 12px;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"QPushButton#btnNavCases:hover {\n"
"    background-color: #1a1d28;\n"
"}")
        self.btnNavCases.setObjectName("btnNavCases")
        self.sidebarLayout.addWidget(self.btnNavCases)
        self.btnNavDocuments = QtWidgets.QPushButton(self.sidebarFrame)
        self.btnNavDocuments.setMinimumSize(QtCore.QSize(0, 38))
        self.btnNavDocuments.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavDocuments.setStyleSheet("QPushButton#btnNavDocuments {\n"
"    background-color: transparent;\n"
"    color: #9aa1ac;\n"
"    text-align: left;\n"
"    padding-left: 12px;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"QPushButton#btnNavDocuments:hover {\n"
"    background-color: #1a1d28;\n"
"}")
        self.btnNavDocuments.setObjectName("btnNavDocuments")
        self.sidebarLayout.addWidget(self.btnNavDocuments)
        self.btnNavMessages = QtWidgets.QPushButton(self.sidebarFrame)
        self.btnNavMessages.setMinimumSize(QtCore.QSize(0, 38))
        self.btnNavMessages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavMessages.setStyleSheet("QPushButton#btnNavMessages {\n"
"    background-color: transparent;\n"
"    color: #9aa1ac;\n"
"    text-align: left;\n"
"    padding-left: 12px;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-size: 13px;\n"
"}\n"
"QPushButton#btnNavMessages:hover {\n"
"    background-color: #1a1d28;\n"
"}")
        self.btnNavMessages.setObjectName("btnNavMessages")
        self.sidebarLayout.addWidget(self.btnNavMessages)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.rootLayout.addWidget(self.sidebarFrame)
        self.mainContentFrame = QtWidgets.QFrame(ClientDashboardPage)
        self.mainContentFrame.setStyleSheet("QFrame#mainContentFrame {\n"
"    background-color: #0a0c12;\n"
"    border: 1px solid #3d3460;\n"
"    border-radius: 16px;\n"
"}")
        self.mainContentFrame.setObjectName("mainContentFrame")
        self.mainContentLayout = QtWidgets.QVBoxLayout(self.mainContentFrame)
        self.mainContentLayout.setContentsMargins(28, 20, 28, 24)
        self.mainContentLayout.setSpacing(20)
        self.mainContentLayout.setObjectName("mainContentLayout")
        self.topBarFrame = QtWidgets.QFrame(self.mainContentFrame)
        self.topBarFrame.setObjectName("topBarFrame")
        self.topBarLayout = QtWidgets.QHBoxLayout(self.topBarFrame)
        self.topBarLayout.setContentsMargins(0, 0, 0, 0)
        self.topBarLayout.setObjectName("topBarLayout")
        self.lblWelcomeUser = QtWidgets.QLabel(self.topBarFrame)
        self.lblWelcomeUser.setStyleSheet("color:#d4a843; font-size:14px; font-weight:600;")
        self.lblWelcomeUser.setObjectName("lblWelcomeUser")
        self.topBarLayout.addWidget(self.lblWelcomeUser)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topBarLayout.addItem(spacerItem1)
        self.btnLogout = QtWidgets.QPushButton(self.topBarFrame)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet("QPushButton#btnLogout {\n"
"    background-color: transparent;\n"
"    color: #9aa1ac;\n"
"    border: none;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton#btnLogout:hover {\n"
"    color: #ffffff;\n"
"}")
        self.btnLogout.setObjectName("btnLogout")
        self.topBarLayout.addWidget(self.btnLogout)
        self.mainContentLayout.addWidget(self.topBarFrame)
        self.lblClientOverviewHeading = QtWidgets.QLabel(self.mainContentFrame)
        self.lblClientOverviewHeading.setStyleSheet("color:#ffffff; font-size:24px; font-weight:700;")
        self.lblClientOverviewHeading.setObjectName("lblClientOverviewHeading")
        self.mainContentLayout.addWidget(self.lblClientOverviewHeading)
        self.lblClientOverviewSubtitle = QtWidgets.QLabel(self.mainContentFrame)
        self.lblClientOverviewSubtitle.setWordWrap(True)
        self.lblClientOverviewSubtitle.setStyleSheet("color:#8b95a3; font-size:13px; margin-bottom:6px;")
        self.lblClientOverviewSubtitle.setObjectName("lblClientOverviewSubtitle")
        self.mainContentLayout.addWidget(self.lblClientOverviewSubtitle)
        self.cardsRowFrame = QtWidgets.QFrame(self.mainContentFrame)
        self.cardsRowFrame.setObjectName("cardsRowFrame")
        self.cardsRowLayout = QtWidgets.QHBoxLayout(self.cardsRowFrame)
        self.cardsRowLayout.setContentsMargins(0, 0, 0, 0)
        self.cardsRowLayout.setSpacing(16)
        self.cardsRowLayout.setObjectName("cardsRowLayout")
        self.cardViewCases = QtWidgets.QFrame(self.cardsRowFrame)
        self.cardViewCases.setStyleSheet("QFrame#cardViewCases {\n"
"    background-color: #fdfcf9;\n"
"    border-radius: 14px;\n"
"}")
        self.cardViewCases.setObjectName("cardViewCases")
        self.cardViewCasesLayout = QtWidgets.QVBoxLayout(self.cardViewCases)
        self.cardViewCasesLayout.setContentsMargins(20, 20, 20, 20)
        self.cardViewCasesLayout.setSpacing(8)
        self.cardViewCasesLayout.setObjectName("cardViewCasesLayout")
        self.iconViewCases = QtWidgets.QLabel(self.cardViewCases)
        self.iconViewCases.setMinimumSize(QtCore.QSize(40, 40))
        self.iconViewCases.setMaximumSize(QtCore.QSize(40, 40))
        self.iconViewCases.setAlignment(QtCore.Qt.AlignCenter)
        self.iconViewCases.setStyleSheet("background-color:#1a1d28; color:#ffffff; border-radius:10px; font-size:16px; margin-bottom:6px;")
        self.iconViewCases.setObjectName("iconViewCases")
        self.cardViewCasesLayout.addWidget(self.iconViewCases)
        self.lblViewCasesTitle = QtWidgets.QLabel(self.cardViewCases)
        self.lblViewCasesTitle.setStyleSheet("color:#15171c; font-size:16px; font-weight:700;")
        self.lblViewCasesTitle.setObjectName("lblViewCasesTitle")
        self.cardViewCasesLayout.addWidget(self.lblViewCasesTitle)
        self.lblViewCasesDesc = QtWidgets.QLabel(self.cardViewCases)
        self.lblViewCasesDesc.setWordWrap(True)
        self.lblViewCasesDesc.setStyleSheet("color:#6b7280; font-size:12px;")
        self.lblViewCasesDesc.setObjectName("lblViewCasesDesc")
        self.cardViewCasesLayout.addWidget(self.lblViewCasesDesc)
        spacerItem2 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.cardViewCasesLayout.addItem(spacerItem2)
        self.btnBrowseFiles = QtWidgets.QPushButton(self.cardViewCases)
        self.btnBrowseFiles.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBrowseFiles.setStyleSheet("QPushButton#btnBrowseFiles {\n"
"    background-color: transparent;\n"
"    color: #16a085;\n"
"    border: none;\n"
"    text-align: left;\n"
"    font-weight: 600;\n"
"    font-size: 12px;\n"
"    padding: 0px;\n"
"}")
        self.btnBrowseFiles.setObjectName("btnBrowseFiles")
        self.cardViewCasesLayout.addWidget(self.btnBrowseFiles)
        self.cardsRowLayout.addWidget(self.cardViewCases)
        self.cardTrackCase = QtWidgets.QFrame(self.cardsRowFrame)
        self.cardTrackCase.setStyleSheet("QFrame#cardTrackCase {\n"
"    background-color: #fdfcf9;\n"
"    border-radius: 14px;\n"
"}")
        self.cardTrackCase.setObjectName("cardTrackCase")
        self.cardTrackCaseLayout = QtWidgets.QVBoxLayout(self.cardTrackCase)
        self.cardTrackCaseLayout.setContentsMargins(20, 20, 20, 20)
        self.cardTrackCaseLayout.setSpacing(8)
        self.cardTrackCaseLayout.setObjectName("cardTrackCaseLayout")
        self.iconTrackCase = QtWidgets.QLabel(self.cardTrackCase)
        self.iconTrackCase.setMinimumSize(QtCore.QSize(40, 40))
        self.iconTrackCase.setMaximumSize(QtCore.QSize(40, 40))
        self.iconTrackCase.setAlignment(QtCore.Qt.AlignCenter)
        self.iconTrackCase.setStyleSheet("background-color:#1a1d28; color:#ffffff; border-radius:10px; font-size:16px; margin-bottom:6px;")
        self.iconTrackCase.setObjectName("iconTrackCase")
        self.cardTrackCaseLayout.addWidget(self.iconTrackCase)
        self.lblTrackCaseTitle = QtWidgets.QLabel(self.cardTrackCase)
        self.lblTrackCaseTitle.setStyleSheet("color:#15171c; font-size:16px; font-weight:700;")
        self.lblTrackCaseTitle.setObjectName("lblTrackCaseTitle")
        self.cardTrackCaseLayout.addWidget(self.lblTrackCaseTitle)
        self.lblTrackCaseDesc = QtWidgets.QLabel(self.cardTrackCase)
        self.lblTrackCaseDesc.setWordWrap(True)
        self.lblTrackCaseDesc.setStyleSheet("color:#6b7280; font-size:12px;")
        self.lblTrackCaseDesc.setObjectName("lblTrackCaseDesc")
        self.cardTrackCaseLayout.addWidget(self.lblTrackCaseDesc)
        spacerItem3 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.cardTrackCaseLayout.addItem(spacerItem3)
        self.btnViewRoadmap = QtWidgets.QPushButton(self.cardTrackCase)
        self.btnViewRoadmap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnViewRoadmap.setStyleSheet("QPushButton#btnViewRoadmap {\n"
"    background-color: transparent;\n"
"    color: #16a085;\n"
"    border: none;\n"
"    text-align: left;\n"
"    font-weight: 600;\n"
"    font-size: 12px;\n"
"    padding: 0px;\n"
"}")
        self.btnViewRoadmap.setObjectName("btnViewRoadmap")
        self.cardTrackCaseLayout.addWidget(self.btnViewRoadmap)
        self.cardsRowLayout.addWidget(self.cardTrackCase)
        self.rightColumnFrame = QtWidgets.QFrame(self.cardsRowFrame)
        self.rightColumnFrame.setObjectName("rightColumnFrame")
        self.rightColumnLayout = QtWidgets.QVBoxLayout(self.rightColumnFrame)
        self.rightColumnLayout.setContentsMargins(0, 0, 0, 0)
        self.rightColumnLayout.setSpacing(14)
        self.rightColumnLayout.setObjectName("rightColumnLayout")
        self.cardCaseStatus = QtWidgets.QFrame(self.rightColumnFrame)
        self.cardCaseStatus.setStyleSheet("QFrame#cardCaseStatus {\n"
"    background-color: #fdfcf9;\n"
"    border-radius: 14px;\n"
"}")
        self.cardCaseStatus.setObjectName("cardCaseStatus")
        self.cardCaseStatusLayout = QtWidgets.QVBoxLayout(self.cardCaseStatus)
        self.cardCaseStatusLayout.setContentsMargins(18, 16, 18, 16)
        self.cardCaseStatusLayout.setSpacing(8)
        self.cardCaseStatusLayout.setObjectName("cardCaseStatusLayout")
        self.cardCaseStatusHeaderRow = QtWidgets.QFrame(self.cardCaseStatus)
        self.cardCaseStatusHeaderRow.setObjectName("cardCaseStatusHeaderRow")
        self.cardCaseStatusHeaderRowLayout = QtWidgets.QHBoxLayout(self.cardCaseStatusHeaderRow)
        self.cardCaseStatusHeaderRowLayout.setContentsMargins(0, 0, 0, 0)
        self.cardCaseStatusHeaderRowLayout.setObjectName("cardCaseStatusHeaderRowLayout")
        self.lblCaseStatusHeader = QtWidgets.QLabel(self.cardCaseStatusHeaderRow)
        self.lblCaseStatusHeader.setStyleSheet("color:#6b7280; font-size:11px; font-weight:700; letter-spacing:1px;")
        self.lblCaseStatusHeader.setObjectName("lblCaseStatusHeader")
        self.cardCaseStatusHeaderRowLayout.addWidget(self.lblCaseStatusHeader)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cardCaseStatusHeaderRowLayout.addItem(spacerItem4)
        self.btnCaseStatusInfo = QtWidgets.QToolButton(self.cardCaseStatusHeaderRow)
        self.btnCaseStatusInfo.setStyleSheet("QToolButton { background: transparent; border: none; color: #9aa1ac; }")
        self.btnCaseStatusInfo.setObjectName("btnCaseStatusInfo")
        self.cardCaseStatusHeaderRowLayout.addWidget(self.btnCaseStatusInfo)
        self.cardCaseStatusLayout.addWidget(self.cardCaseStatusHeaderRow)
        self.cardCaseStatusNameRow = QtWidgets.QFrame(self.cardCaseStatus)
        self.cardCaseStatusNameRow.setObjectName("cardCaseStatusNameRow")
        self.cardCaseStatusNameRowLayout = QtWidgets.QHBoxLayout(self.cardCaseStatusNameRow)
        self.cardCaseStatusNameRowLayout.setContentsMargins(0, 0, 0, 0)
        self.cardCaseStatusNameRowLayout.setObjectName("cardCaseStatusNameRowLayout")
        self.lblCaseName = QtWidgets.QLabel(self.cardCaseStatusNameRow)
        self.lblCaseName.setStyleSheet("color:#15171c; font-size:13px; font-weight:700;")
        self.lblCaseName.setObjectName("lblCaseName")
        self.cardCaseStatusNameRowLayout.addWidget(self.lblCaseName)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.cardCaseStatusNameRowLayout.addItem(spacerItem5)
        self.badgeInProgress = QtWidgets.QLabel(self.cardCaseStatusNameRow)
        self.badgeInProgress.setStyleSheet("background-color:#fdecd2; color:#c9821f; font-size:10px; font-weight:700; border-radius:8px; padding:2px 8px;")
        self.badgeInProgress.setObjectName("badgeInProgress")
        self.cardCaseStatusNameRowLayout.addWidget(self.badgeInProgress)
        self.cardCaseStatusLayout.addWidget(self.cardCaseStatusNameRow)
        self.progressCaseStatus = QtWidgets.QProgressBar(self.cardCaseStatus)
        self.progressCaseStatus.setMinimumSize(QtCore.QSize(0, 8))
        self.progressCaseStatus.setMaximumSize(QtCore.QSize(16777215, 8))
        self.progressCaseStatus.setProperty("value", 55)
        self.progressCaseStatus.setTextVisible(False)
        self.progressCaseStatus.setStyleSheet("QProgressBar {\n"
"    background-color: #e9e6df;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #e8954f;\n"
"    border-radius: 4px;\n"
"}")
        self.progressCaseStatus.setObjectName("progressCaseStatus")
        self.cardCaseStatusLayout.addWidget(self.progressCaseStatus)
        self.lblNextUpdate = QtWidgets.QLabel(self.cardCaseStatus)
        self.lblNextUpdate.setStyleSheet("color:#8b8478; font-size:10px; margin-top:2px;")
        self.lblNextUpdate.setObjectName("lblNextUpdate")
        self.cardCaseStatusLayout.addWidget(self.lblNextUpdate)
        self.rightColumnLayout.addWidget(self.cardCaseStatus)
        self.cardLegalConsultation = QtWidgets.QFrame(self.rightColumnFrame)
        self.cardLegalConsultation.setStyleSheet("QFrame#cardLegalConsultation {\n"
"    background-color: #1b2a52;\n"
"    border-radius: 14px;\n"
"}")
        self.cardLegalConsultation.setObjectName("cardLegalConsultation")
        self.cardLegalConsultationLayout = QtWidgets.QVBoxLayout(self.cardLegalConsultation)
        self.cardLegalConsultationLayout.setContentsMargins(18, 16, 18, 16)
        self.cardLegalConsultationLayout.setSpacing(8)
        self.cardLegalConsultationLayout.setObjectName("cardLegalConsultationLayout")
        self.lblLegalConsultationTitle = QtWidgets.QLabel(self.cardLegalConsultation)
        self.lblLegalConsultationTitle.setStyleSheet("color:#ffffff; font-size:14px; font-weight:700;")
        self.lblLegalConsultationTitle.setObjectName("lblLegalConsultationTitle")
        self.cardLegalConsultationLayout.addWidget(self.lblLegalConsultationTitle)
        self.lblLegalConsultationDesc = QtWidgets.QLabel(self.cardLegalConsultation)
        self.lblLegalConsultationDesc.setWordWrap(True)
        self.lblLegalConsultationDesc.setStyleSheet("color:#aab3c5; font-size:11px;")
        self.lblLegalConsultationDesc.setObjectName("lblLegalConsultationDesc")
        self.cardLegalConsultationLayout.addWidget(self.lblLegalConsultationDesc)
        self.btnJoinMeeting = QtWidgets.QPushButton(self.cardLegalConsultation)
        self.btnJoinMeeting.setMinimumSize(QtCore.QSize(0, 34))
        self.btnJoinMeeting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnJoinMeeting.setStyleSheet("QPushButton#btnJoinMeeting {\n"
"    background-color: #e8954f;\n"
"    color: #1b2a52;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: 700;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton#btnJoinMeeting:hover {\n"
"    background-color: #f0a564;\n"
"}")
        self.btnJoinMeeting.setObjectName("btnJoinMeeting")
        self.cardLegalConsultationLayout.addWidget(self.btnJoinMeeting)
        self.rightColumnLayout.addWidget(self.cardLegalConsultation)
        self.cardsRowLayout.addWidget(self.rightColumnFrame)
        self.mainContentLayout.addWidget(self.cardsRowFrame)
        self.recentDocsHeaderFrame = QtWidgets.QFrame(self.mainContentFrame)
        self.recentDocsHeaderFrame.setObjectName("recentDocsHeaderFrame")
        self.recentDocsHeaderLayout = QtWidgets.QHBoxLayout(self.recentDocsHeaderFrame)
        self.recentDocsHeaderLayout.setContentsMargins(0, 10, 0, 0)
        self.recentDocsHeaderLayout.setObjectName("recentDocsHeaderLayout")
        self.lblRecentDocuments = QtWidgets.QLabel(self.recentDocsHeaderFrame)
        self.lblRecentDocuments.setStyleSheet("color:#ffffff; font-size:18px; font-weight:700;")
        self.lblRecentDocuments.setObjectName("lblRecentDocuments")
        self.recentDocsHeaderLayout.addWidget(self.lblRecentDocuments)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recentDocsHeaderLayout.addItem(spacerItem6)
        self.btnViewAllVault = QtWidgets.QPushButton(self.recentDocsHeaderFrame)
        self.btnViewAllVault.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnViewAllVault.setStyleSheet("QPushButton#btnViewAllVault {\n"
"    background-color: transparent;\n"
"    color: #9aa1ac;\n"
"    border: none;\n"
"    font-size: 12px;\n"
"}\n"
"QPushButton#btnViewAllVault:hover {\n"
"    color: #ffffff;\n"
"}")
        self.btnViewAllVault.setObjectName("btnViewAllVault")
        self.recentDocsHeaderLayout.addWidget(self.btnViewAllVault)
        self.mainContentLayout.addWidget(self.recentDocsHeaderFrame)
        self.documentRowFrame = QtWidgets.QFrame(self.mainContentFrame)
        self.documentRowFrame.setStyleSheet("QFrame#documentRowFrame {\n"
"    background-color: #12141c;\n"
"    border-radius: 12px;\n"
"}")
        self.documentRowFrame.setObjectName("documentRowFrame")
        self.documentRowLayout = QtWidgets.QHBoxLayout(self.documentRowFrame)
        self.documentRowLayout.setContentsMargins(16, 12, 16, 12)
        self.documentRowLayout.setSpacing(12)
        self.documentRowLayout.setObjectName("documentRowLayout")
        self.iconDocumentPdf = QtWidgets.QLabel(self.documentRowFrame)
        self.iconDocumentPdf.setMinimumSize(QtCore.QSize(36, 36))
        self.iconDocumentPdf.setMaximumSize(QtCore.QSize(36, 36))
        self.iconDocumentPdf.setAlignment(QtCore.Qt.AlignCenter)
        self.iconDocumentPdf.setStyleSheet("background-color:#3a1f24; color:#e0556b; border-radius:8px; font-size:15px;")
        self.iconDocumentPdf.setObjectName("iconDocumentPdf")
        self.documentRowLayout.addWidget(self.iconDocumentPdf)
        self.documentInfoFrame = QtWidgets.QFrame(self.documentRowFrame)
        self.documentInfoFrame.setObjectName("documentInfoFrame")
        self.documentInfoLayout = QtWidgets.QVBoxLayout(self.documentInfoFrame)
        self.documentInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.documentInfoLayout.setSpacing(2)
        self.documentInfoLayout.setObjectName("documentInfoLayout")
        self.lblDocName = QtWidgets.QLabel(self.documentInfoFrame)
        self.lblDocName.setStyleSheet("color:#ffffff; font-size:13px; font-weight:600;")
        self.lblDocName.setObjectName("lblDocName")
        self.documentInfoLayout.addWidget(self.lblDocName)
        self.lblDocMeta = QtWidgets.QLabel(self.documentInfoFrame)
        self.lblDocMeta.setStyleSheet("color:#7c8794; font-size:11px;")
        self.lblDocMeta.setObjectName("lblDocMeta")
        self.documentInfoLayout.addWidget(self.lblDocMeta)
        self.documentRowLayout.addWidget(self.documentInfoFrame)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.documentRowLayout.addItem(spacerItem7)
        self.mainContentLayout.addWidget(self.documentRowFrame)
        self.rootLayout.addWidget(self.mainContentFrame)

        self.retranslateUi(ClientDashboardPage)
        QtCore.QMetaObject.connectSlotsByName(ClientDashboardPage)

    def retranslateUi(self, ClientDashboardPage):
        _translate = QtCore.QCoreApplication.translate
        ClientDashboardPage.setWindowTitle(_translate("ClientDashboardPage", "Client Dashboard"))
        self.btnUserAvatar.setText(_translate("ClientDashboardPage", "👤"))
        self.lblWelcomeBackTitle.setText(_translate("ClientDashboardPage", "Welcome Back"))
        self.lblWelcomeBackSubtitle.setText(_translate("ClientDashboardPage", "Legal Professional"))
        self.btnNavDashboard.setText(_translate("ClientDashboardPage", "■  Dashboard"))
        self.btnNavCases.setText(_translate("ClientDashboardPage", "📁  Cases"))
        self.btnNavDocuments.setText(_translate("ClientDashboardPage", "📄  Documents"))
        self.btnNavMessages.setText(_translate("ClientDashboardPage", "✉  Messages"))
        self.lblWelcomeUser.setText(_translate("ClientDashboardPage", "Welcome, Jonathan Sterling"))
        self.btnLogout.setText(_translate("ClientDashboardPage", "Logout  ↹"))
        self.lblClientOverviewHeading.setText(_translate("ClientDashboardPage", "Client Overview"))
        self.lblClientOverviewSubtitle.setText(_translate("ClientDashboardPage", "Access your ongoing legal matters, track real-time progress, and review shared documentation within our secure vault."))
        self.iconViewCases.setText(_translate("ClientDashboardPage", "📁"))
        self.lblViewCasesTitle.setText(_translate("ClientDashboardPage", "View Cases"))
        self.lblViewCasesDesc.setText(_translate("ClientDashboardPage", "Access your full portfolio of active and archived legal matters."))
        self.btnBrowseFiles.setText(_translate("ClientDashboardPage", "Browse Files  →"))
        self.iconTrackCase.setText(_translate("ClientDashboardPage", "📍"))
        self.lblTrackCaseTitle.setText(_translate("ClientDashboardPage", "Track Case"))
        self.lblTrackCaseDesc.setText(_translate("ClientDashboardPage", "Real-time status updates and upcoming hearing schedules."))
        self.btnViewRoadmap.setText(_translate("ClientDashboardPage", "View Roadmap  →"))
        self.lblCaseStatusHeader.setText(_translate("ClientDashboardPage", "CASE STATUS"))
        self.btnCaseStatusInfo.setText(_translate("ClientDashboardPage", "ⓘ"))
        self.lblCaseName.setText(_translate("ClientDashboardPage", "Sterling vs. Apex Corp"))
        self.badgeInProgress.setText(_translate("ClientDashboardPage", "In Progress"))
        self.lblNextUpdate.setText(_translate("ClientDashboardPage", "Next Update: Tomorrow, 10:00 AM"))
        self.lblLegalConsultationTitle.setText(_translate("ClientDashboardPage", "Legal Consultation"))
        self.lblLegalConsultationDesc.setText(_translate("ClientDashboardPage", "You have an upcoming briefing with Senior Counsel at 2 PM."))
        self.btnJoinMeeting.setText(_translate("ClientDashboardPage", "Join Meeting"))
        self.lblRecentDocuments.setText(_translate("ClientDashboardPage", "Recent Documents"))
        self.btnViewAllVault.setText(_translate("ClientDashboardPage", "View All Vault  →"))
        self.iconDocumentPdf.setText(_translate("ClientDashboardPage", "📄"))
        self.lblDocName.setText(_translate("ClientDashboardPage", "Affidavit_Signed_v2.pdf"))
        self.lblDocMeta.setText(_translate("ClientDashboardPage", "Uploaded 2 hours ago • 4.3 MB"))


class Ui_CreateUserDialog(object):
    def setupUi(self, CreateUserDialog):
        CreateUserDialog.setObjectName("CreateUserDialog")
        CreateUserDialog.resize(900, 600)
        CreateUserDialog.setStyleSheet("\n"
"    QDialog {\n"
"      background-color: #0d1b2a;\n"
"    }\n"
"   ")
        self.sidebar = QtWidgets.QWidget(CreateUserDialog)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 180, 600))
        self.sidebar.setStyleSheet("\n"
"     QWidget { background-color: #0a1628; }\n"
"     QLabel#appTitle { color: #ffffff; font-size: 14px; font-weight: bold; padding: 20px 16px 8px 16px; }\n"
"     QPushButton {\n"
"       color: #8899aa;\n"
"       background: transparent;\n"
"       border: none;\n"
"       text-align: left;\n"
"       padding: 10px 16px;\n"
"       font-size: 13px;\n"
"     }\n"
"     QPushButton:hover { color: #ffffff; background-color: #132040; }\n"
"     QPushButton#activeNav {\n"
"       color: #ffffff;\n"
"       background-color: #1a2f50;\n"
"       border-left: 3px solid #e63946;\n"
"     }\n"
"    ")
        self.sidebar.setObjectName("sidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebarLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarLayout.setSpacing(0)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.appTitle = QtWidgets.QLabel(self.sidebar)
        self.appTitle.setObjectName("appTitle")
        self.sidebarLayout.addWidget(self.appTitle)
        self.navAssignJudge = QtWidgets.QPushButton(self.sidebar)
        self.navAssignJudge.setObjectName("navAssignJudge")
        self.sidebarLayout.addWidget(self.navAssignJudge)
        self.navAssignLawyer = QtWidgets.QPushButton(self.sidebar)
        self.navAssignLawyer.setObjectName("navAssignLawyer")
        self.sidebarLayout.addWidget(self.navAssignLawyer)
        self.navCreateUser = QtWidgets.QPushButton(self.sidebar)
        self.navCreateUser.setObjectName("navCreateUser")
        self.sidebarLayout.addWidget(self.navCreateUser)
        self.navViewUsers = QtWidgets.QPushButton(self.sidebar)
        self.navViewUsers.setObjectName("navViewUsers")
        self.sidebarLayout.addWidget(self.navViewUsers)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.mainContent = QtWidgets.QWidget(CreateUserDialog)
        self.mainContent.setGeometry(QtCore.QRect(180, 0, 720, 600))
        self.mainContent.setStyleSheet("QWidget { background-color: #0d1b2a; }")
        self.mainContent.setObjectName("mainContent")
        self.mainLayout = QtWidgets.QVBoxLayout(self.mainContent)
        self.mainLayout.setContentsMargins(40, 30, 40, 30)
        self.mainLayout.setSpacing(16)
        self.mainLayout.setObjectName("mainLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pageHeader = QtWidgets.QLabel(self.mainContent)
        self.pageHeader.setStyleSheet("color: #ffffff; font-size: 18px; font-weight: bold;")
        self.pageHeader.setObjectName("pageHeader")
        self.hboxlayout.addWidget(self.pageHeader)
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.systemLabel = QtWidgets.QLabel(self.mainContent)
        self.systemLabel.setStyleSheet("color: #8899aa; font-size: 12px;")
        self.systemLabel.setObjectName("systemLabel")
        self.hboxlayout.addWidget(self.systemLabel)
        self.mainLayout.addLayout(self.hboxlayout)
        self.formCard = QtWidgets.QFrame(self.mainContent)
        self.formCard.setStyleSheet("\n"
"        QFrame {\n"
"          background-color: #132040;\n"
"          border-radius: 10px;\n"
"          padding: 24px;\n"
"        }\n"
"       ")
        self.formCard.setObjectName("formCard")
        self.formCardLayout = QtWidgets.QVBoxLayout(self.formCard)
        self.formCardLayout.setContentsMargins(24, 24, 24, 24)
        self.formCardLayout.setSpacing(16)
        self.formCardLayout.setObjectName("formCardLayout")
        self.formTitle = QtWidgets.QLabel(self.formCard)
        self.formTitle.setStyleSheet("color: #ffffff; font-size: 20px; font-weight: bold;")
        self.formTitle.setObjectName("formTitle")
        self.formCardLayout.addWidget(self.formTitle)
        self.formSubtitle = QtWidgets.QLabel(self.formCard)
        self.formSubtitle.setStyleSheet("color: #8899aa; font-size: 12px;")
        self.formSubtitle.setObjectName("formSubtitle")
        self.formCardLayout.addWidget(self.formSubtitle)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setSpacing(16)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.labelUsername = QtWidgets.QLabel(self.formCard)
        self.labelUsername.setStyleSheet("color: #aabbcc; font-size: 12px;")
        self.labelUsername.setObjectName("labelUsername")
        self.vboxlayout.addWidget(self.labelUsername)
        self.inputUsername = QtWidgets.QLineEdit(self.formCard)
        self.inputUsername.setStyleSheet("\n"
"               QLineEdit {\n"
"                 background-color: #1e3050;\n"
"                 color: #ffffff;\n"
"                 border: 1px solid #2a4060;\n"
"                 border-radius: 6px;\n"
"                 padding: 8px 12px;\n"
"                 font-size: 13px;\n"
"               }\n"
"               QLineEdit:focus { border-color: #4a90d9; }\n"
"              ")
        self.inputUsername.setObjectName("inputUsername")
        self.vboxlayout.addWidget(self.inputUsername)
        self.hboxlayout1.addLayout(self.vboxlayout)
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.labelRole = QtWidgets.QLabel(self.formCard)
        self.labelRole.setStyleSheet("color: #aabbcc; font-size: 12px;")
        self.labelRole.setObjectName("labelRole")
        self.vboxlayout1.addWidget(self.labelRole)
        self.comboRole = QtWidgets.QComboBox(self.formCard)
        self.comboRole.setStyleSheet("\n"
"               QComboBox {\n"
"                 background-color: #1e3050;\n"
"                 color: #ffffff;\n"
"                 border: 1px solid #2a4060;\n"
"                 border-radius: 6px;\n"
"                 padding: 8px 12px;\n"
"                 font-size: 13px;\n"
"                 min-width: 160px;\n"
"               }\n"
"               QComboBox::drop-down { border: none; }\n"
"               QComboBox QAbstractItemView {\n"
"                 background-color: #1e3050;\n"
"                 color: #ffffff;\n"
"                 selection-background-color: #2a4060;\n"
"               }\n"
"              ")
        self.comboRole.setObjectName("comboRole")
        self.comboRole.addItem("")
        self.comboRole.addItem("")
        self.comboRole.addItem("")
        self.comboRole.addItem("")
        self.vboxlayout1.addWidget(self.comboRole)
        self.hboxlayout1.addLayout(self.vboxlayout1)
        self.formCardLayout.addLayout(self.hboxlayout1)
        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.labelFullName = QtWidgets.QLabel(self.formCard)
        self.labelFullName.setStyleSheet("color: #aabbcc; font-size: 12px;")
        self.labelFullName.setObjectName("labelFullName")
        self.vboxlayout2.addWidget(self.labelFullName)
        self.inputFullName = QtWidgets.QLineEdit(self.formCard)
        self.inputFullName.setStyleSheet("\n"
"             QLineEdit {\n"
"               background-color: #1e3050;\n"
"               color: #ffffff;\n"
"               border: 1px solid #2a4060;\n"
"               border-radius: 6px;\n"
"               padding: 8px 12px;\n"
"               font-size: 13px;\n"
"             }\n"
"             QLineEdit:focus { border-color: #4a90d9; }\n"
"            ")
        self.inputFullName.setObjectName("inputFullName")
        self.vboxlayout2.addWidget(self.inputFullName)
        self.formCardLayout.addLayout(self.vboxlayout2)
        self.vboxlayout3 = QtWidgets.QVBoxLayout()
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.labelPassword = QtWidgets.QLabel(self.formCard)
        self.labelPassword.setStyleSheet("color: #aabbcc; font-size: 12px;")
        self.labelPassword.setObjectName("labelPassword")
        self.vboxlayout3.addWidget(self.labelPassword)
        self.inputPassword = QtWidgets.QLineEdit(self.formCard)
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setStyleSheet("\n"
"             QLineEdit {\n"
"               background-color: #1e3050;\n"
"               color: #ffffff;\n"
"               border: 1px solid #2a4060;\n"
"               border-radius: 6px;\n"
"               padding: 8px 12px;\n"
"               font-size: 13px;\n"
"             }\n"
"             QLineEdit:focus { border-color: #4a90d9; }\n"
"            ")
        self.inputPassword.setObjectName("inputPassword")
        self.vboxlayout3.addWidget(self.inputPassword)
        self.formCardLayout.addLayout(self.vboxlayout3)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setSpacing(12)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.btnCreateUser = QtWidgets.QPushButton(self.formCard)
        self.btnCreateUser.setStyleSheet("\n"
"             QPushButton {\n"
"               background-color: #1a3a6e;\n"
"               color: #ffffff;\n"
"               border: none;\n"
"               border-radius: 6px;\n"
"               padding: 10px 28px;\n"
"               font-size: 13px;\n"
"               font-weight: bold;\n"
"               min-width: 120px;\n"
"             }\n"
"             QPushButton:hover { background-color: #224a8a; }\n"
"             QPushButton:pressed { background-color: #122a52; }\n"
"            ")
        self.btnCreateUser.setObjectName("btnCreateUser")
        self.hboxlayout2.addWidget(self.btnCreateUser)
        self.btnCancel = QtWidgets.QPushButton(self.formCard)
        self.btnCancel.setStyleSheet("\n"
"             QPushButton {\n"
"               background-color: transparent;\n"
"               color: #8899aa;\n"
"               border: 1px solid #2a4060;\n"
"               border-radius: 6px;\n"
"               padding: 10px 28px;\n"
"               font-size: 13px;\n"
"             }\n"
"             QPushButton:hover { color: #ffffff; border-color: #4a6080; }\n"
"            ")
        self.btnCancel.setObjectName("btnCancel")
        self.hboxlayout2.addWidget(self.btnCancel)
        spacerItem2 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem2)
        self.formCardLayout.addLayout(self.hboxlayout2)
        self.mainLayout.addWidget(self.formCard)
        spacerItem3 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem3)

        self.retranslateUi(CreateUserDialog)
        self.btnCancel.clicked.connect(CreateUserDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CreateUserDialog)

    def retranslateUi(self, CreateUserDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateUserDialog.setWindowTitle(_translate("CreateUserDialog", "Create New User"))
        self.appTitle.setText(_translate("CreateUserDialog", "Admin Panel"))
        self.navAssignJudge.setText(_translate("CreateUserDialog", "  Assign Judge"))
        self.navAssignLawyer.setText(_translate("CreateUserDialog", "  Assign Lawyer"))
        self.navCreateUser.setText(_translate("CreateUserDialog", "  Create User"))
        self.navViewUsers.setText(_translate("CreateUserDialog", "  View Users"))
        self.pageHeader.setText(_translate("CreateUserDialog", "Legal Management"))
        self.systemLabel.setText(_translate("CreateUserDialog", "System Admin"))
        self.formTitle.setText(_translate("CreateUserDialog", "Create New User"))
        self.formSubtitle.setText(_translate("CreateUserDialog", "Register a new profile to the legal database ecosystem."))
        self.labelUsername.setText(_translate("CreateUserDialog", "Username"))
        self.inputUsername.setPlaceholderText(_translate("CreateUserDialog", "e.g., john_doe_legal"))
        self.labelRole.setText(_translate("CreateUserDialog", "Role"))
        self.comboRole.setItemText(0, _translate("CreateUserDialog", "Judge"))
        self.comboRole.setItemText(1, _translate("CreateUserDialog", "Lawyer"))
        self.comboRole.setItemText(2, _translate("CreateUserDialog", "Client"))
        self.comboRole.setItemText(3, _translate("CreateUserDialog", "Admin"))
        self.labelFullName.setText(_translate("CreateUserDialog", "Full Name / Display Name"))
        self.inputFullName.setPlaceholderText(_translate("CreateUserDialog", "Full display name"))
        self.labelPassword.setText(_translate("CreateUserDialog", "Password"))
        self.inputPassword.setPlaceholderText(_translate("CreateUserDialog", "Enter password"))
        self.btnCreateUser.setText(_translate("CreateUserDialog", "Create User"))
        self.btnCancel.setText(_translate("CreateUserDialog", "Cancel"))


class Ui_DeleteConfirmationDialog(object):
    def setupUi(self, DeleteConfirmationDialog):
        DeleteConfirmationDialog.setObjectName("DeleteConfirmationDialog")
        DeleteConfirmationDialog.resize(340, 220)
        DeleteConfirmationDialog.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.FramelessWindowHint)
        DeleteConfirmationDialog.setStyleSheet("\n"
"    QDialog {\n"
"      background-color: #ffffff;\n"
"      border-radius: 12px;\n"
"    }\n"
"   ")
        self.mainLayout = QtWidgets.QVBoxLayout(DeleteConfirmationDialog)
        self.mainLayout.setContentsMargins(32, 32, 32, 28)
        self.mainLayout.setSpacing(12)
        self.mainLayout.setObjectName("mainLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.iconLabel = QtWidgets.QLabel(DeleteConfirmationDialog)
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setStyleSheet("\n"
"         QLabel {\n"
"           background-color: #ffe5e5;\n"
"           color: #e63946;\n"
"           font-size: 24px;\n"
"           border-radius: 28px;\n"
"           min-width: 56px;\n"
"           max-width: 56px;\n"
"           min-height: 56px;\n"
"           max-height: 56px;\n"
"           qproperty-alignment: AlignCenter;\n"
"         }\n"
"        ")
        self.iconLabel.setObjectName("iconLabel")
        self.hboxlayout.addWidget(self.iconLabel)
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.mainLayout.addLayout(self.hboxlayout)
        self.titleLabel = QtWidgets.QLabel(DeleteConfirmationDialog)
        self.titleLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.titleLabel.setStyleSheet("\n"
"       color: #111827;\n"
"       font-size: 18px;\n"
"       font-weight: bold;\n"
"      ")
        self.titleLabel.setObjectName("titleLabel")
        self.mainLayout.addWidget(self.titleLabel)
        self.subtitleLabel = QtWidgets.QLabel(DeleteConfirmationDialog)
        self.subtitleLabel.setAlignment(QtCore.Qt.AlignHCenter)
        self.subtitleLabel.setWordWrap(True)
        self.subtitleLabel.setStyleSheet("\n"
"       color: #6b7280;\n"
"       font-size: 13px;\n"
"       line-height: 1.4;\n"
"      ")
        self.subtitleLabel.setObjectName("subtitleLabel")
        self.mainLayout.addWidget(self.subtitleLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem2)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setSpacing(12)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.btnCancel = QtWidgets.QPushButton(DeleteConfirmationDialog)
        self.btnCancel.setStyleSheet("\n"
"         QPushButton {\n"
"           background-color: #ffffff;\n"
"           color: #374151;\n"
"           border: 1px solid #d1d5db;\n"
"           border-radius: 8px;\n"
"           padding: 10px 0px;\n"
"           font-size: 13px;\n"
"           font-weight: 500;\n"
"         }\n"
"         QPushButton:hover {\n"
"           background-color: #f9fafb;\n"
"         }\n"
"        ")
        self.btnCancel.setObjectName("btnCancel")
        self.hboxlayout1.addWidget(self.btnCancel)
        self.btnConfirm = QtWidgets.QPushButton(DeleteConfirmationDialog)
        self.btnConfirm.setStyleSheet("\n"
"         QPushButton {\n"
"           background-color: #e63946;\n"
"           color: #ffffff;\n"
"           border: none;\n"
"           border-radius: 8px;\n"
"           padding: 10px 0px;\n"
"           font-size: 13px;\n"
"           font-weight: bold;\n"
"         }\n"
"         QPushButton:hover { background-color: #c1121f; }\n"
"         QPushButton:pressed { background-color: #a00f1a; }\n"
"        ")
        self.btnConfirm.setObjectName("btnConfirm")
        self.hboxlayout1.addWidget(self.btnConfirm)
        self.mainLayout.addLayout(self.hboxlayout1)

        self.retranslateUi(DeleteConfirmationDialog)
        self.btnCancel.clicked.connect(DeleteConfirmationDialog.reject) # type: ignore
        self.btnConfirm.clicked.connect(DeleteConfirmationDialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DeleteConfirmationDialog)

    def retranslateUi(self, DeleteConfirmationDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteConfirmationDialog.setWindowTitle(_translate("DeleteConfirmationDialog", "Confirm Deletion"))
        self.iconLabel.setText(_translate("DeleteConfirmationDialog", "🗑"))
        self.titleLabel.setText(_translate("DeleteConfirmationDialog", "Are you sure?"))
        self.subtitleLabel.setText(_translate("DeleteConfirmationDialog", "This will permanently delete the selected user. This action cannot be undone."))
        self.btnCancel.setText(_translate("DeleteConfirmationDialog", "Cancel"))
        self.btnConfirm.setText(_translate("DeleteConfirmationDialog", "Confirm"))


class Ui_DeleteUserDialog(object):
    def setupUi(self, DeleteUserDialog):
        DeleteUserDialog.setObjectName("DeleteUserDialog")
        DeleteUserDialog.resize(900, 600)
        DeleteUserDialog.setStyleSheet("\n"
"    QDialog { background-color: #0d1b2a; }\n"
"   ")
        self.sidebar = QtWidgets.QWidget(DeleteUserDialog)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 180, 600))
        self.sidebar.setStyleSheet("\n"
"     QWidget { background-color: #0a1628; }\n"
"     QLabel#appTitle { color: #ffffff; font-size: 14px; font-weight: bold; padding: 20px 16px 8px 16px; }\n"
"     QPushButton {\n"
"       color: #8899aa;\n"
"       background: transparent;\n"
"       border: none;\n"
"       text-align: left;\n"
"       padding: 10px 16px;\n"
"       font-size: 13px;\n"
"     }\n"
"     QPushButton:hover { color: #ffffff; background-color: #132040; }\n"
"     QPushButton#activeNav {\n"
"       color: #ffffff;\n"
"       background-color: #1a2f50;\n"
"       border-left: 3px solid #e63946;\n"
"     }\n"
"    ")
        self.sidebar.setObjectName("sidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebarLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarLayout.setSpacing(0)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.appTitle = QtWidgets.QLabel(self.sidebar)
        self.appTitle.setObjectName("appTitle")
        self.sidebarLayout.addWidget(self.appTitle)
        self.navAssignJudge = QtWidgets.QPushButton(self.sidebar)
        self.navAssignJudge.setObjectName("navAssignJudge")
        self.sidebarLayout.addWidget(self.navAssignJudge)
        self.navAssignLawyer = QtWidgets.QPushButton(self.sidebar)
        self.navAssignLawyer.setObjectName("navAssignLawyer")
        self.sidebarLayout.addWidget(self.navAssignLawyer)
        self.navCreateUser = QtWidgets.QPushButton(self.sidebar)
        self.navCreateUser.setObjectName("navCreateUser")
        self.sidebarLayout.addWidget(self.navCreateUser)
        self.navViewUsers = QtWidgets.QPushButton(self.sidebar)
        self.navViewUsers.setObjectName("navViewUsers")
        self.sidebarLayout.addWidget(self.navViewUsers)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.mainContent = QtWidgets.QWidget(DeleteUserDialog)
        self.mainContent.setGeometry(QtCore.QRect(180, 0, 720, 600))
        self.mainContent.setStyleSheet("QWidget { background-color: #0d1b2a; }")
        self.mainContent.setObjectName("mainContent")
        self.mainLayout = QtWidgets.QVBoxLayout(self.mainContent)
        self.mainLayout.setContentsMargins(40, 30, 40, 30)
        self.mainLayout.setSpacing(16)
        self.mainLayout.setObjectName("mainLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.pageHeader = QtWidgets.QLabel(self.mainContent)
        self.pageHeader.setStyleSheet("color: #ffffff; font-size: 18px; font-weight: bold;")
        self.pageHeader.setObjectName("pageHeader")
        self.hboxlayout.addWidget(self.pageHeader)
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.adminLabel = QtWidgets.QLabel(self.mainContent)
        self.adminLabel.setStyleSheet("color: #8899aa; font-size: 12px;")
        self.adminLabel.setObjectName("adminLabel")
        self.hboxlayout.addWidget(self.adminLabel)
        self.mainLayout.addLayout(self.hboxlayout)
        self.formCard = QtWidgets.QFrame(self.mainContent)
        self.formCard.setStyleSheet("\n"
"        QFrame {\n"
"          background-color: #132040;\n"
"          border-radius: 10px;\n"
"        }\n"
"       ")
        self.formCard.setObjectName("formCard")
        self.formCardLayout = QtWidgets.QVBoxLayout(self.formCard)
        self.formCardLayout.setContentsMargins(28, 28, 28, 28)
        self.formCardLayout.setSpacing(16)
        self.formCardLayout.setObjectName("formCardLayout")
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setSpacing(14)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.deleteIconLabel = QtWidgets.QLabel(self.formCard)
        self.deleteIconLabel.setStyleSheet("\n"
"             QLabel {\n"
"               background-color: #3a1a1a;\n"
"               color: #e63946;\n"
"               font-size: 22px;\n"
"               border-radius: 24px;\n"
"               min-width: 48px;\n"
"               max-width: 48px;\n"
"               min-height: 48px;\n"
"               max-height: 48px;\n"
"               qproperty-alignment: AlignCenter;\n"
"             }\n"
"            ")
        self.deleteIconLabel.setObjectName("deleteIconLabel")
        self.hboxlayout1.addWidget(self.deleteIconLabel)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setSpacing(2)
        self.vboxlayout.setObjectName("vboxlayout")
        self.formTitle = QtWidgets.QLabel(self.formCard)
        self.formTitle.setStyleSheet("color: #ffffff; font-size: 18px; font-weight: bold;")
        self.formTitle.setObjectName("formTitle")
        self.vboxlayout.addWidget(self.formTitle)
        self.formSubtitle = QtWidgets.QLabel(self.formCard)
        self.formSubtitle.setStyleSheet("color: #8899aa; font-size: 12px;")
        self.formSubtitle.setObjectName("formSubtitle")
        self.vboxlayout.addWidget(self.formSubtitle)
        self.hboxlayout1.addLayout(self.vboxlayout)
        spacerItem2 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.formCardLayout.addLayout(self.hboxlayout1)
        self.separator = QtWidgets.QFrame(self.formCard)
        self.separator.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setStyleSheet("color: #1e3050;")
        self.separator.setObjectName("separator")
        self.formCardLayout.addWidget(self.separator)
        self.labelSelectUsername = QtWidgets.QLabel(self.formCard)
        self.labelSelectUsername.setStyleSheet("color: #aabbcc; font-size: 12px;")
        self.labelSelectUsername.setObjectName("labelSelectUsername")
        self.formCardLayout.addWidget(self.labelSelectUsername)
        self.inputSearchUsername = QtWidgets.QLineEdit(self.formCard)
        self.inputSearchUsername.setStyleSheet("\n"
"           QLineEdit {\n"
"             background-color: #1e3050;\n"
"             color: #ffffff;\n"
"             border: 1px solid #2a4060;\n"
"             border-radius: 6px;\n"
"             padding: 8px 12px;\n"
"             font-size: 13px;\n"
"           }\n"
"           QLineEdit:focus { border-color: #4a90d9; }\n"
"          ")
        self.inputSearchUsername.setObjectName("inputSearchUsername")
        self.formCardLayout.addWidget(self.inputSearchUsername)
        self.roleLabel = QtWidgets.QLabel(self.formCard)
        self.roleLabel.setStyleSheet("\n"
"           QLabel {\n"
"             background-color: #1a3050;\n"
"             color: #4db8ff;\n"
"             border: 1px solid #2a5080;\n"
"             border-radius: 4px;\n"
"             padding: 4px 10px;\n"
"             font-size: 11px;\n"
"             font-weight: bold;\n"
"             max-width: 110px;\n"
"           }\n"
"          ")
        self.roleLabel.setObjectName("roleLabel")
        self.formCardLayout.addWidget(self.roleLabel)
        self.dangerBox = QtWidgets.QFrame(self.formCard)
        self.dangerBox.setStyleSheet("\n"
"           QFrame {\n"
"             background-color: #2a1a0a;\n"
"             border: 1px solid #c97a00;\n"
"             border-left: 4px solid #e69900;\n"
"             border-radius: 6px;\n"
"           }\n"
"          ")
        self.dangerBox.setObjectName("dangerBox")
        self.dangerLayout = QtWidgets.QHBoxLayout(self.dangerBox)
        self.dangerLayout.setContentsMargins(12, 10, 12, 10)
        self.dangerLayout.setSpacing(10)
        self.dangerLayout.setObjectName("dangerLayout")
        self.dangerIcon = QtWidgets.QLabel(self.dangerBox)
        self.dangerIcon.setStyleSheet("color: #e69900; font-size: 16px;")
        self.dangerIcon.setObjectName("dangerIcon")
        self.dangerLayout.addWidget(self.dangerIcon)
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.dangerTitle = QtWidgets.QLabel(self.dangerBox)
        self.dangerTitle.setStyleSheet("color: #e69900; font-size: 11px; font-weight: bold;")
        self.dangerTitle.setObjectName("dangerTitle")
        self.vboxlayout1.addWidget(self.dangerTitle)
        self.dangerText = QtWidgets.QLabel(self.dangerBox)
        self.dangerText.setWordWrap(True)
        self.dangerText.setStyleSheet("color: #cc9944; font-size: 12px;")
        self.dangerText.setObjectName("dangerText")
        self.vboxlayout1.addWidget(self.dangerText)
        self.dangerLayout.addLayout(self.vboxlayout1)
        self.formCardLayout.addWidget(self.dangerBox)
        self.checkConfirm = QtWidgets.QCheckBox(self.formCard)
        self.checkConfirm.setStyleSheet("\n"
"           QCheckBox {\n"
"             color: #8899aa;\n"
"             font-size: 12px;\n"
"           }\n"
"           QCheckBox::indicator {\n"
"             width: 16px;\n"
"             height: 16px;\n"
"             border: 1px solid #3a5070;\n"
"             border-radius: 3px;\n"
"             background-color: #1e3050;\n"
"           }\n"
"           QCheckBox::indicator:checked {\n"
"             background-color: #e63946;\n"
"             border-color: #e63946;\n"
"           }\n"
"          ")
        self.checkConfirm.setObjectName("checkConfirm")
        self.formCardLayout.addWidget(self.checkConfirm)
        self.vboxlayout2 = QtWidgets.QVBoxLayout()
        self.vboxlayout2.setSpacing(10)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.btnDeleteUser = QtWidgets.QPushButton(self.formCard)
        self.btnDeleteUser.setEnabled(False)
        self.btnDeleteUser.setStyleSheet("\n"
"             QPushButton {\n"
"               background-color: #6b2030;\n"
"               color: #cc8899;\n"
"               border: none;\n"
"               border-radius: 6px;\n"
"               padding: 11px;\n"
"               font-size: 13px;\n"
"               font-weight: bold;\n"
"             }\n"
"             QPushButton:enabled {\n"
"               background-color: #e63946;\n"
"               color: #ffffff;\n"
"             }\n"
"             QPushButton:enabled:hover { background-color: #c1121f; }\n"
"             QPushButton:enabled:pressed { background-color: #a00f1a; }\n"
"            ")
        self.btnDeleteUser.setObjectName("btnDeleteUser")
        self.vboxlayout2.addWidget(self.btnDeleteUser)
        self.btnCancel = QtWidgets.QPushButton(self.formCard)
        self.btnCancel.setStyleSheet("\n"
"             QPushButton {\n"
"               background-color: transparent;\n"
"               color: #8899aa;\n"
"               border: 1px solid #2a4060;\n"
"               border-radius: 6px;\n"
"               padding: 10px;\n"
"               font-size: 13px;\n"
"             }\n"
"             QPushButton:hover { color: #ffffff; border-color: #4a6080; }\n"
"            ")
        self.btnCancel.setObjectName("btnCancel")
        self.vboxlayout2.addWidget(self.btnCancel)
        self.formCardLayout.addLayout(self.vboxlayout2)
        self.mainLayout.addWidget(self.formCard)
        spacerItem3 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainLayout.addItem(spacerItem3)

        self.retranslateUi(DeleteUserDialog)
        self.btnCancel.clicked.connect(DeleteUserDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DeleteUserDialog)

    def retranslateUi(self, DeleteUserDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteUserDialog.setWindowTitle(_translate("DeleteUserDialog", "Delete User"))
        self.appTitle.setText(_translate("DeleteUserDialog", "Admin Panel"))
        self.navAssignJudge.setText(_translate("DeleteUserDialog", "  Assign Judge"))
        self.navAssignLawyer.setText(_translate("DeleteUserDialog", "  Assign Lawyer"))
        self.navCreateUser.setText(_translate("DeleteUserDialog", "  Create User"))
        self.navViewUsers.setText(_translate("DeleteUserDialog", "  View Users"))
        self.pageHeader.setText(_translate("DeleteUserDialog", "Legal Management"))
        self.adminLabel.setText(_translate("DeleteUserDialog", "Admin Administrator"))
        self.deleteIconLabel.setText(_translate("DeleteUserDialog", "🗑"))
        self.formTitle.setText(_translate("DeleteUserDialog", "Delete User"))
        self.formSubtitle.setText(_translate("DeleteUserDialog", "Permanent account termination from the system"))
        self.labelSelectUsername.setText(_translate("DeleteUserDialog", "Select Username"))
        self.inputSearchUsername.setPlaceholderText(_translate("DeleteUserDialog", "🔍  john_doe_legal"))
        self.roleLabel.setText(_translate("DeleteUserDialog", "  State Lawyer"))
        self.dangerIcon.setText(_translate("DeleteUserDialog", "⚠"))
        self.dangerTitle.setText(_translate("DeleteUserDialog", "DANGER ZONE"))
        self.dangerText.setText(_translate("DeleteUserDialog", "This action cannot be undone. All associated case files, logs, and judicial appointments for this user will be orphaned or archived."))
        self.checkConfirm.setText(_translate("DeleteUserDialog", "I confirm that I want to delete this user and all associated data."))
        self.btnDeleteUser.setText(_translate("DeleteUserDialog", "🗑  Delete User"))
        self.btnCancel.setText(_translate("DeleteUserDialog", "Cancel"))


class Ui_LogoutConfirmDialog(object):
    """logout_confirmation.ui – small modal confirming a logout action."""

    def setupUi(self, LogoutConfirmDialog):
        LogoutConfirmDialog.setObjectName("LogoutConfirmDialog")
        LogoutConfirmDialog.resize(340, 230)
        LogoutConfirmDialog.setWindowTitle("Log Out")
        LogoutConfirmDialog.setStyleSheet(
            "background-color: #ffffff;\n"
            "font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QVBoxLayout(LogoutConfirmDialog)
        self.rootLayout.setContentsMargins(26, 24, 26, 0)
        self.rootLayout.setObjectName("rootLayout")

        self.lblIcon = QtWidgets.QLabel("⏻")
        self.lblIcon.setMinimumSize(QtCore.QSize(46, 46))
        self.lblIcon.setMaximumSize(QtCore.QSize(46, 46))
        self.lblIcon.setStyleSheet(
            "background-color: #eef1f8;\n"
            "border-radius: 23px;\n"
            "color: #0c1230;\n"
            "font-size: 18px;"
        )
        self.lblIcon.setAlignment(QtCore.Qt.AlignCenter)

        self.iconCenterLayout = QtWidgets.QHBoxLayout()
        self.iconCenterLayout.setObjectName("iconCenterLayout")
        self.iconCenterLayout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.iconCenterLayout.addWidget(self.lblIcon)
        self.iconCenterLayout.addItem(
            QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.rootLayout.addLayout(self.iconCenterLayout)

        self.rootLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblTitle = QtWidgets.QLabel("Log Out?")
        self.lblTitle.setStyleSheet("color: #0c1230; font-size: 17px; font-weight: bold;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.rootLayout.addWidget(self.lblTitle)

        self.lblMessage = QtWidgets.QLabel(
            "You will need to log in again to access your legal files and secure account."
        )
        self.lblMessage.setStyleSheet("color: #9aa3b5; font-size: 11px;")
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setWordWrap(True)
        self.rootLayout.addWidget(self.lblMessage)

        self.rootLayout.addItem(
            QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.buttonRowLayout = QtWidgets.QHBoxLayout()
        self.buttonRowLayout.setObjectName("buttonRowLayout")
        self.btnCancel = QtWidgets.QPushButton("Cancel")
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 40))
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet(
            "QPushButton { background-color: #ffffff; color: #0c1230; border: 1px solid #e2e5ee; "
            "border-radius: 6px; font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #f7f8fc; }"
        )
        self.buttonRowLayout.addWidget(self.btnCancel)

        self.btnLogOut = QtWidgets.QPushButton("Log Out")
        self.btnLogOut.setMinimumSize(QtCore.QSize(0, 40))
        self.btnLogOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogOut.setStyleSheet(
            "QPushButton { background-color: #0c1230; color: #ffffff; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.buttonRowLayout.addWidget(self.btnLogOut)
        self.rootLayout.addLayout(self.buttonRowLayout)

        self.rootLayout.addItem(
            QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.footerBar = QtWidgets.QFrame()
        self.footerBar.setMinimumSize(QtCore.QSize(0, 26))
        self.footerBar.setStyleSheet("background-color: #0c1230;")
        self.footerBarLayout = QtWidgets.QVBoxLayout(self.footerBar)
        self.footerBarLayout.setContentsMargins(0, 4, 0, 4)
        self.footerBarLayout.setObjectName("footerBarLayout")
        self.lblFooterNote = QtWidgets.QLabel("SECURE LEGALLINK PROTOCOL ACTIVE")
        self.lblFooterNote.setStyleSheet("color: #6b7390; font-size: 8px; font-weight: bold;")
        self.lblFooterNote.setAlignment(QtCore.Qt.AlignCenter)
        self.footerBarLayout.addWidget(self.lblFooterNote)
        self.rootLayout.addWidget(self.footerBar)

        # btnCancel -> reject() / btnLogOut -> accept(), wired in the .ui file itself.
        self.btnCancel.clicked.connect(LogoutConfirmDialog.reject)
        self.btnLogOut.clicked.connect(LogoutConfirmDialog.accept)


# ─────────────────────────────────────────────
#  UI CLASSES FROM .UI FILES (converted to Python)
# ─────────────────────────────────────────────

class Ui_AllCasesWindow(object):
    """View_cases.ui – Admin "All Cases" table screen."""

    def setupUi(self, AllCasesWindow):
        AllCasesWindow.setObjectName("AllCasesWindow")
        AllCasesWindow.resize(1200, 720)
        AllCasesWindow.setStyleSheet(
            "background-color: #eef1f8; font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QHBoxLayout(AllCasesWindow)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")

        # Sidebar
        self.sidebarFrame = QtWidgets.QFrame(AllCasesWindow)
        self.sidebarFrame.setMinimumSize(QtCore.QSize(220, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.sidebarFrame.setStyleSheet("background-color: #0c1230;")
        self.sidebarFrame.setObjectName("sidebarFrame")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setContentsMargins(16, 20, 16, 16)
        self.sidebarLayout.setObjectName("sidebarLayout")

        self.lblBrand = QtWidgets.QLabel("Court Admin", self.sidebarFrame)
        self.lblBrand.setStyleSheet("color: #f0b429; font-size: 16px; font-weight: bold;")
        self.sidebarLayout.addWidget(self.lblBrand)
        self.lblBrandSub = QtWidgets.QLabel("Admin Dashboard", self.sidebarFrame)
        self.lblBrandSub.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.sidebarLayout.addWidget(self.lblBrandSub)
        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))

        _nav_style_normal = ("QPushButton { color: #c7cbe0; background-color: transparent; "
                              "border: none; text-align: left; padding-left: 8px; font-size: 13px; "
                              "border-radius: 6px; } QPushButton:hover { background-color: #1a2247; }")
        _nav_style_active = ("QPushButton { color: #0c1230; background-color: #f0b429; border: none; "
                              "text-align: left; padding-left: 8px; font-size: 13px; font-weight: bold; "
                              "border-radius: 6px; }")

        self.btnNavDashboard = QtWidgets.QPushButton("  Dashboard", self.sidebarFrame)
        self.btnNavDashboard.setMinimumHeight(38)
        self.btnNavDashboard.setStyleSheet(_nav_style_normal)
        self.sidebarLayout.addWidget(self.btnNavDashboard)

        self.btnNavCases = QtWidgets.QPushButton("  Case Records", self.sidebarFrame)
        self.btnNavCases.setMinimumHeight(38)
        self.btnNavCases.setStyleSheet(_nav_style_active)
        self.sidebarLayout.addWidget(self.btnNavCases)

        self.btnNavAddCase = QtWidgets.QPushButton("  Add New Case", self.sidebarFrame)
        self.btnNavAddCase.setMinimumHeight(38)
        self.btnNavAddCase.setStyleSheet(_nav_style_normal)
        self.sidebarLayout.addWidget(self.btnNavAddCase)

        self.btnNavHearings = QtWidgets.QPushButton("  Manage Hearings", self.sidebarFrame)
        self.btnNavHearings.setMinimumHeight(38)
        self.btnNavHearings.setStyleSheet(_nav_style_normal)
        self.sidebarLayout.addWidget(self.btnNavHearings)

        self.btnNavUsers = QtWidgets.QPushButton("  Manage Users", self.sidebarFrame)
        self.btnNavUsers.setMinimumHeight(38)
        self.btnNavUsers.setStyleSheet(_nav_style_normal)
        self.sidebarLayout.addWidget(self.btnNavUsers)

        self.btnNavReports = QtWidgets.QPushButton("  Reports", self.sidebarFrame)
        self.btnNavReports.setMinimumHeight(38)
        self.btnNavReports.setStyleSheet(_nav_style_normal)
        self.sidebarLayout.addWidget(self.btnNavReports)

        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.btnCreateNewCase = QtWidgets.QPushButton("+ Create New Case", self.sidebarFrame)
        self.btnCreateNewCase.setMinimumHeight(42)
        self.btnCreateNewCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCreateNewCase.setStyleSheet(
            "QPushButton { background-color: #f0b429; color: #0c1230; border-radius: 6px; "
            "font-weight: bold; font-size: 13px; } QPushButton:hover { background-color: #ffce4d; }"
        )
        self.sidebarLayout.addWidget(self.btnCreateNewCase)
        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))

        self.btnLogout = QtWidgets.QPushButton("Sign Out", self.sidebarFrame)
        self.btnLogout.setMinimumHeight(36)
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet(
            "QPushButton { color: #c7cbe0; background-color: transparent; "
            "border: 1px solid #3a4566; border-radius: 6px; font-size: 13px; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.sidebarLayout.addWidget(self.btnLogout)
        self.rootLayout.addWidget(self.sidebarFrame)

        # Main content
        self.mainContent = QtWidgets.QWidget(AllCasesWindow)
        self.contentLayout = QtWidgets.QVBoxLayout(self.mainContent)
        self.contentLayout.setContentsMargins(28, 22, 28, 22)
        self.contentLayout.setObjectName("contentLayout")

        # Top bar
        self.topBarLayout = QtWidgets.QHBoxLayout()
        self.lblPageTitle = QtWidgets.QLabel("All Case Records")
        self.lblPageTitle.setStyleSheet("color: #1b2240; font-size: 18px; font-weight: bold;")
        self.topBarLayout.addWidget(self.lblPageTitle)
        self.topBarLayout.addStretch()
        self.contentLayout.addLayout(self.topBarLayout)

        # Search bar
        self.searchBarLayout = QtWidgets.QHBoxLayout()
        self.searchInput = QtWidgets.QLineEdit()
        self.searchInput.setMinimumHeight(36)
        self.searchInput.setStyleSheet(
            "QLineEdit { background-color: #ffffff; border: 1px solid #d6dae6; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.searchInput.setPlaceholderText("Search by case ID or title...")
        self.searchBarLayout.addWidget(self.searchInput)

        self.btnFilters = QtWidgets.QPushButton("Filters")
        self.btnFilters.setMinimumSize(QtCore.QSize(90, 36))
        self.btnFilters.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFilters.setStyleSheet(
            "QPushButton { background-color: #ffffff; border: 1px solid #d6dae6; "
            "border-radius: 6px; font-size: 12px; } QPushButton:hover { background-color: #f3f5fa; }"
        )
        self.searchBarLayout.addWidget(self.btnFilters)

        self.btnExportPdf = QtWidgets.QPushButton("Export PDF")
        self.btnExportPdf.setMinimumSize(QtCore.QSize(110, 36))
        self.btnExportPdf.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExportPdf.setStyleSheet(
            "QPushButton { background-color: #f0b429; color: #0c1230; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } QPushButton:hover { background-color: #ffce4d; }"
        )
        self.searchBarLayout.addWidget(self.btnExportPdf)
        self.contentLayout.addLayout(self.searchBarLayout)

        # Table
        self.tableCases = QtWidgets.QTableWidget()
        self.tableCases.setColumnCount(5)
        self.tableCases.setHorizontalHeaderLabels(
            ["Case ID", "Title / Parties", "Status", "Case Type", "Action"]
        )
        self.tableCases.setStyleSheet(
            "QTableWidget { background-color: #ffffff; border: 1px solid #e2e5ee; "
            "border-radius: 8px; gridline-color: #eef0f6; font-size: 12px; } "
            "QHeaderView::section { background-color: #f7f8fc; color: #6b7390; "
            "padding: 8px; border: none; font-weight: bold; }"
        )
        self.tableCases.setAlternatingRowColors(True)
        self.tableCases.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableCases.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableCases.horizontalHeader().setStretchLastSection(True)
        self.contentLayout.addWidget(self.tableCases)

        # Pagination row
        self.paginationLayout = QtWidgets.QHBoxLayout()
        self.lblResultsCount = QtWidgets.QLabel("Showing results")
        self.lblResultsCount.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.paginationLayout.addWidget(self.lblResultsCount)
        self.paginationLayout.addStretch()
        self.btnPrevPage = QtWidgets.QPushButton("‹")
        self.btnPrevPage.setMinimumSize(32, 28)
        self.paginationLayout.addWidget(self.btnPrevPage)
        self.btnNextPage = QtWidgets.QPushButton("›")
        self.btnNextPage.setMinimumSize(32, 28)
        self.paginationLayout.addWidget(self.btnNextPage)
        self.contentLayout.addLayout(self.paginationLayout)

        # Summary cards
        self.summaryCardsLayout = QtWidgets.QHBoxLayout()

        self.cardActiveCases = QtWidgets.QFrame()
        self.cardActiveCases.setMinimumHeight(90)
        self.cardActiveCases.setStyleSheet("background-color: #0c1230; border-radius: 8px;")
        _acl = QtWidgets.QVBoxLayout(self.cardActiveCases)
        self.lblActiveCasesValue = QtWidgets.QLabel("0")
        self.lblActiveCasesValue.setStyleSheet("color: #f0b429; font-size: 26px; font-weight: bold;")
        _acl.addWidget(self.lblActiveCasesValue)
        self.lblActiveCasesCaption = QtWidgets.QLabel("Active Cases")
        self.lblActiveCasesCaption.setStyleSheet("color: #c7cbe0; font-size: 11px;")
        _acl.addWidget(self.lblActiveCasesCaption)
        self.summaryCardsLayout.addWidget(self.cardActiveCases)

        self.cardPendingHearings = QtWidgets.QFrame()
        self.cardPendingHearings.setMinimumHeight(90)
        self.cardPendingHearings.setStyleSheet(
            "background-color: #ffffff; border: 1px solid #e2e5ee; border-radius: 8px;"
        )
        _phl = QtWidgets.QVBoxLayout(self.cardPendingHearings)
        self.lblPendingHearingsValue = QtWidgets.QLabel("0")
        self.lblPendingHearingsValue.setStyleSheet("color: #e0524a; font-size: 26px; font-weight: bold;")
        _phl.addWidget(self.lblPendingHearingsValue)
        self.lblPendingHearingsCaption = QtWidgets.QLabel("Pending Hearings")
        self.lblPendingHearingsCaption.setStyleSheet("color: #6b7390; font-size: 11px;")
        _phl.addWidget(self.lblPendingHearingsCaption)
        self.summaryCardsLayout.addWidget(self.cardPendingHearings)

        self.cardResolutionRate = QtWidgets.QFrame()
        self.cardResolutionRate.setMinimumHeight(90)
        self.cardResolutionRate.setStyleSheet(
            "background-color: #ffffff; border: 1px solid #e2e5ee; border-radius: 8px;"
        )
        _rrl = QtWidgets.QVBoxLayout(self.cardResolutionRate)
        self.lblResolutionRateValue = QtWidgets.QLabel("—")
        self.lblResolutionRateValue.setStyleSheet("color: #2fae66; font-size: 26px; font-weight: bold;")
        _rrl.addWidget(self.lblResolutionRateValue)
        self.lblResolutionRateCaption = QtWidgets.QLabel("Resolution Rate")
        self.lblResolutionRateCaption.setStyleSheet("color: #6b7390; font-size: 11px;")
        _rrl.addWidget(self.lblResolutionRateCaption)
        self.summaryCardsLayout.addWidget(self.cardResolutionRate)

        self.contentLayout.addLayout(self.summaryCardsLayout)
        self.rootLayout.addWidget(self.mainContent)


class Ui_AllUsersWindow(object):
    """View_users.ui – Admin "All Users" table screen."""

    def setupUi(self, AllUsersWindow):
        AllUsersWindow.setObjectName("AllUsersWindow")
        AllUsersWindow.resize(1200, 720)
        AllUsersWindow.setStyleSheet(
            "background-color: #0c1230; font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QHBoxLayout(AllUsersWindow)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)

        # Sidebar
        self.sidebarFrame = QtWidgets.QFrame(AllUsersWindow)
        self.sidebarFrame.setMinimumSize(QtCore.QSize(200, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebarFrame.setStyleSheet(
            "background-color: #0a0f29; border-right: 1px solid #1f2750;"
        )
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setContentsMargins(14, 18, 14, 16)

        self.lblBrand = QtWidgets.QLabel("Admin Panel", self.sidebarFrame)
        self.lblBrand.setStyleSheet("color: #ffffff; font-size: 15px; font-weight: bold;")
        self.sidebarLayout.addWidget(self.lblBrand)
        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))

        _ns = ("QPushButton { color: #8b93b0; background-color: transparent; border: none; "
               "text-align: left; padding-left: 6px; font-size: 12px; border-radius: 6px; } "
               "QPushButton:hover { background-color: #161d40; }")
        _as = ("QPushButton { color: #f0b429; background-color: #161d40; border: none; "
               "text-align: left; padding-left: 6px; font-size: 12px; font-weight: bold; border-radius: 6px; }")

        self.btnNavGood = QtWidgets.QPushButton("  Overview", self.sidebarFrame)
        self.btnNavGood.setMinimumHeight(34)
        self.btnNavGood.setStyleSheet(_ns)
        self.sidebarLayout.addWidget(self.btnNavGood)

        self.btnNavCaseLog = QtWidgets.QPushButton("  Case Log", self.sidebarFrame)
        self.btnNavCaseLog.setMinimumHeight(34)
        self.btnNavCaseLog.setStyleSheet(_ns)
        self.sidebarLayout.addWidget(self.btnNavCaseLog)

        self.btnNavLawyers = QtWidgets.QPushButton("  Manage Lawyers", self.sidebarFrame)
        self.btnNavLawyers.setMinimumHeight(34)
        self.btnNavLawyers.setStyleSheet(_ns)
        self.sidebarLayout.addWidget(self.btnNavLawyers)

        self.btnNavUsers = QtWidgets.QPushButton("  Manage Users", self.sidebarFrame)
        self.btnNavUsers.setMinimumHeight(34)
        self.btnNavUsers.setStyleSheet(_as)
        self.sidebarLayout.addWidget(self.btnNavUsers)

        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.lblAdminName = QtWidgets.QLabel("A. Rahman", self.sidebarFrame)
        self.lblAdminName.setStyleSheet("color: #ffffff; font-size: 12px; font-weight: bold;")
        self.sidebarLayout.addWidget(self.lblAdminName)
        self.lblAdminRole = QtWidgets.QLabel("Administrator", self.sidebarFrame)
        self.lblAdminRole.setStyleSheet("color: #6b7390; font-size: 10px;")
        self.sidebarLayout.addWidget(self.lblAdminRole)
        self.rootLayout.addWidget(self.sidebarFrame)

        # Main content
        self.mainContent = QtWidgets.QWidget(AllUsersWindow)
        self.contentLayout = QtWidgets.QVBoxLayout(self.mainContent)
        self.contentLayout.setContentsMargins(26, 20, 26, 20)

        # Top bar
        self.topBarLayout = QtWidgets.QHBoxLayout()
        self.lblPageTitle = QtWidgets.QLabel("Legal Management")
        self.lblPageTitle.setStyleSheet("color: #ffffff; font-size: 13px; font-weight: bold;")
        self.topBarLayout.addWidget(self.lblPageTitle)
        self.topBarLayout.addStretch()
        self.btnNotifications = QtWidgets.QPushButton("🔔")
        self.btnNotifications.setMinimumSize(28, 28)
        self.btnNotifications.setStyleSheet(
            "QPushButton { color: #c7cbe0; background-color: transparent; border: none; font-size: 12px; }"
        )
        self.topBarLayout.addWidget(self.btnNotifications)
        self.contentLayout.addLayout(self.topBarLayout)

        # Panel frame
        self.panelFrame = QtWidgets.QFrame()
        self.panelFrame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        self.panelLayout = QtWidgets.QVBoxLayout(self.panelFrame)
        self.panelLayout.setContentsMargins(20, 18, 20, 18)

        self.panelHeaderLayout = QtWidgets.QHBoxLayout()
        self.lblAllUsers = QtWidgets.QLabel("All Users")
        self.lblAllUsers.setStyleSheet("color: #0c1230; font-size: 18px; font-weight: bold;")
        self.panelHeaderLayout.addWidget(self.lblAllUsers)
        self.panelHeaderLayout.addStretch()
        self.searchInput = QtWidgets.QLineEdit()
        self.searchInput.setMinimumSize(QtCore.QSize(220, 32))
        self.searchInput.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 8px; font-size: 12px; }"
        )
        self.searchInput.setPlaceholderText("Search by name or role...")
        self.panelHeaderLayout.addWidget(self.searchInput)
        self.panelLayout.addLayout(self.panelHeaderLayout)

        self.tableUsers = QtWidgets.QTableWidget()
        self.tableUsers.setColumnCount(4)
        self.tableUsers.setHorizontalHeaderLabels(["Name", "Role", "Status", "Actions"])
        self.tableUsers.setStyleSheet(
            "QTableWidget { border: none; font-size: 12px; gridline-color: #eef0f6; } "
            "QHeaderView::section { background-color: #ffffff; color: #6b7390; padding: 6px; "
            "border: none; border-bottom: 1px solid #eef0f6; font-weight: bold; }"
        )
        self.tableUsers.setAlternatingRowColors(True)
        self.tableUsers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableUsers.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableUsers.horizontalHeader().setStretchLastSection(True)
        self.panelLayout.addWidget(self.tableUsers)
        self.contentLayout.addWidget(self.panelFrame)

        # Bottom info cards
        self.bottomCardsLayout = QtWidgets.QHBoxLayout()
        _card_style = "background-color: #11173a; border-radius: 8px;"
        for attr, title, desc in [
            ("cardCourtAccess", "Court Access",
             "Manage privileges and assigned courts per user role."),
            ("cardAuditLog", "Audit Log",
             "Review the history of account creation, password resets and role changes."),
            ("cardSupportHub", "Support Hub",
             "Contact administrators for account issues or access requests."),
        ]:
            card = QtWidgets.QFrame()
            card.setMinimumHeight(90)
            card.setStyleSheet(_card_style)
            cl = QtWidgets.QVBoxLayout(card)
            t = QtWidgets.QLabel(title)
            t.setStyleSheet("color: #f0b429; font-size: 12px; font-weight: bold;")
            cl.addWidget(t)
            d = QtWidgets.QLabel(desc)
            d.setStyleSheet("color: #8b93b0; font-size: 10px;")
            d.setWordWrap(True)
            cl.addWidget(d)
            setattr(self, attr, card)
            self.bottomCardsLayout.addWidget(card)
        self.contentLayout.addLayout(self.bottomCardsLayout)
        self.rootLayout.addWidget(self.mainContent)


class Ui_TrackCaseLawyerWidget(object):
    """track_case_lawyer_.ui – Lawyer's Track Case mini-panel."""

    def setupUi(self, TrackCaseLawyerWidget):
        TrackCaseLawyerWidget.setObjectName("TrackCaseLawyerWidget")
        TrackCaseLawyerWidget.resize(420, 320)
        TrackCaseLawyerWidget.setStyleSheet(
            "background-color: #0c1230; font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QVBoxLayout(TrackCaseLawyerWidget)
        self.rootLayout.setContentsMargins(16, 14, 16, 16)

        # Header row
        self.headerLayout = QtWidgets.QHBoxLayout()
        self.btnMenu = QtWidgets.QPushButton("☰")
        self.btnMenu.setMinimumSize(26, 26)
        self.btnMenu.setStyleSheet(
            "color: #ffffff; background-color: transparent; border: none; font-size: 16px;"
        )
        self.headerLayout.addWidget(self.btnMenu)
        self.lblPageTitle = QtWidgets.QLabel("Track Case")
        self.lblPageTitle.setStyleSheet("color: #f0b429; font-size: 15px; font-weight: bold;")
        self.headerLayout.addWidget(self.lblPageTitle)
        self.headerLayout.addStretch()
        self.btnInfo = QtWidgets.QPushButton("i")
        self.btnInfo.setMinimumSize(26, 26)
        self.btnInfo.setMaximumSize(26, 26)
        self.btnInfo.setStyleSheet(
            "QPushButton { color: #0c1230; background-color: #ffffff; "
            "border-radius: 13px; font-size: 11px; font-weight: bold; }"
        )
        self.headerLayout.addWidget(self.btnInfo)
        self.rootLayout.addLayout(self.headerLayout)

        # Card
        self.cardFrame = QtWidgets.QFrame()
        self.cardFrame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        self.cardLayout = QtWidgets.QVBoxLayout(self.cardFrame)
        self.cardLayout.setContentsMargins(20, 22, 20, 22)

        self.lblFieldLabel = QtWidgets.QLabel("CASE ID OR TITLE")
        self.lblFieldLabel.setStyleSheet("color: #6b7390; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblFieldLabel)

        self.txtTrackCaseId = QtWidgets.QLineEdit()
        self.txtTrackCaseId.setMinimumHeight(38)
        self.txtTrackCaseId.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtTrackCaseId.setPlaceholderText("e.g. LC-2024-8902")
        self.cardLayout.addWidget(self.txtTrackCaseId)
        self.cardLayout.addStretch()

        self.btnTrackCase = QtWidgets.QPushButton("⚲  TRACK CASE")
        self.btnTrackCase.setMinimumHeight(42)
        self.btnTrackCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTrackCase.setStyleSheet(
            "QPushButton { background-color: #0c1230; color: #f0b429; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.cardLayout.addWidget(self.btnTrackCase)
        self.rootLayout.addWidget(self.cardFrame)


class Ui_TrackMyCasesClientWindow(object):
    """track_my_cases__client_pannel_.ui – Client "Track My Case" full screen."""

    def setupUi(self, TrackMyCasesClientWindow):
        TrackMyCasesClientWindow.setObjectName("TrackMyCasesClientWindow")
        TrackMyCasesClientWindow.resize(1200, 760)
        TrackMyCasesClientWindow.setStyleSheet(
            "background-color: #0c1230; font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QHBoxLayout(TrackMyCasesClientWindow)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)

        # Sidebar
        self.sidebarFrame = QtWidgets.QFrame(TrackMyCasesClientWindow)
        self.sidebarFrame.setMinimumSize(QtCore.QSize(190, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(190, 16777215))
        self.sidebarFrame.setStyleSheet(
            "background-color: #0a0f29; border-right: 1px solid #1f2750;"
        )
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setContentsMargins(14, 18, 14, 16)

        self.lblBrand = QtWidgets.QLabel("Client Portal", self.sidebarFrame)
        self.lblBrand.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold;")
        self.sidebarLayout.addWidget(self.lblBrand)
        self.lblBrandSub = QtWidgets.QLabel("Case Overview", self.sidebarFrame)
        self.lblBrandSub.setStyleSheet("color: #6b7390; font-size: 10px;")
        self.sidebarLayout.addWidget(self.lblBrandSub)
        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed))

        _ns = ("QPushButton { color: #8b93b0; background-color: transparent; border: none; "
               "text-align: left; padding-left: 6px; font-size: 12px; border-radius: 6px; } "
               "QPushButton:hover { background-color: #161d40; }")
        _as = ("QPushButton { color: #f0b429; background-color: #161d40; border: none; "
               "text-align: left; padding-left: 6px; font-size: 12px; font-weight: bold; border-radius: 6px; }")

        self.btnNavMyCases = QtWidgets.QPushButton("  My Cases", self.sidebarFrame)
        self.btnNavMyCases.setMinimumHeight(34)
        self.btnNavMyCases.setStyleSheet(_ns)
        self.sidebarLayout.addWidget(self.btnNavMyCases)

        self.btnNavTrackCase = QtWidgets.QPushButton("  Track My Case", self.sidebarFrame)
        self.btnNavTrackCase.setMinimumHeight(34)
        self.btnNavTrackCase.setStyleSheet(_as)
        self.sidebarLayout.addWidget(self.btnNavTrackCase)

        self.sidebarLayout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.btnLogout = QtWidgets.QPushButton("  Logout", self.sidebarFrame)
        self.btnLogout.setMinimumHeight(34)
        self.btnLogout.setStyleSheet(_ns)
        self.sidebarLayout.addWidget(self.btnLogout)
        self.rootLayout.addWidget(self.sidebarFrame)

        # Main content
        self.mainContent = QtWidgets.QWidget(TrackMyCasesClientWindow)
        self.contentLayout = QtWidgets.QVBoxLayout(self.mainContent)
        self.contentLayout.setContentsMargins(26, 18, 26, 18)

        # Top bar
        self.topBarLayout = QtWidgets.QHBoxLayout()
        self.lblPageTitle = QtWidgets.QLabel("Track My Case")
        self.lblPageTitle.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold;")
        self.topBarLayout.addWidget(self.lblPageTitle)
        self.topBarLayout.addStretch()
        self.lblWelcomeBack = QtWidgets.QLabel("Welcome back,")
        self.lblWelcomeBack.setStyleSheet("color: #6b7390; font-size: 10px;")
        self.topBarLayout.addWidget(self.lblWelcomeBack)
        self.lblClientName = QtWidgets.QLabel("Client")
        self.lblClientName.setStyleSheet("color: #ffffff; font-size: 12px; font-weight: bold;")
        self.topBarLayout.addWidget(self.lblClientName)
        self.contentLayout.addLayout(self.topBarLayout)

        # Locate panel
        self.locatePanelFrame = QtWidgets.QFrame()
        self.locatePanelFrame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        self.locatePanelLayout = QtWidgets.QVBoxLayout(self.locatePanelFrame)
        self.locatePanelLayout.setContentsMargins(24, 20, 24, 20)

        self.lblLocateTitle = QtWidgets.QLabel("Locate Your Case")
        self.lblLocateTitle.setStyleSheet("color: #e0524a; font-size: 16px; font-weight: bold;")
        self.lblLocateTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.locatePanelLayout.addWidget(self.lblLocateTitle)

        self.lblLocateDesc = QtWidgets.QLabel(
            "Enter your Case Reference ID or Title to retrieve the latest "
            "status updates and hearing schedules."
        )
        self.lblLocateDesc.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.lblLocateDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLocateDesc.setWordWrap(True)
        self.locatePanelLayout.addWidget(self.lblLocateDesc)

        self.locateRowLayout = QtWidgets.QHBoxLayout()
        self.txtCaseRef = QtWidgets.QLineEdit()
        self.txtCaseRef.setMinimumHeight(38)
        self.txtCaseRef.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtCaseRef.setPlaceholderText("e.g. CAS-2024-8902 or case title")
        self.locateRowLayout.addWidget(self.txtCaseRef)

        self.btnTrack = QtWidgets.QPushButton("TRACK")
        self.btnTrack.setMinimumSize(QtCore.QSize(110, 38))
        self.btnTrack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTrack.setStyleSheet(
            "QPushButton { background-color: #0c1230; color: #ffffff; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.locateRowLayout.addWidget(self.btnTrack)
        self.locatePanelLayout.addLayout(self.locateRowLayout)
        self.contentLayout.addWidget(self.locatePanelFrame)

        # Case detail frame
        self.caseDetailFrame = QtWidgets.QFrame()
        self.caseDetailFrame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        self.caseDetailLayout = QtWidgets.QVBoxLayout(self.caseDetailFrame)
        self.caseDetailLayout.setContentsMargins(24, 20, 24, 20)

        self.caseHeaderLayout = QtWidgets.QHBoxLayout()
        self.lblCaseTitle = QtWidgets.QLabel("—")
        self.lblCaseTitle.setStyleSheet("color: #0c1230; font-size: 15px; font-weight: bold;")
        self.caseHeaderLayout.addWidget(self.lblCaseTitle)
        self.caseHeaderLayout.addStretch()
        self.lblStatusBadge = QtWidgets.QLabel("—")
        self.lblStatusBadge.setStyleSheet(
            "background-color: #e3f7ea; color: #2fae66; border-radius: 10px; "
            "padding: 4px 10px; font-size: 10px; font-weight: bold;"
        )
        self.caseHeaderLayout.addWidget(self.lblStatusBadge)
        self.caseDetailLayout.addLayout(self.caseHeaderLayout)

        self.lblCourtName = QtWidgets.QLabel("—")
        self.lblCourtName.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.caseDetailLayout.addWidget(self.lblCourtName)

        # Info row: judge / counsel / next hearing / time remaining
        self.caseInfoLayout = QtWidgets.QHBoxLayout()
        for cap_attr, val_attr, cap_text, val_text in [
            ("lblPresidingJudgeCaption", "lblPresidingJudgeValue", "PRESIDING JUDGE", "—"),
            ("lblOpposingCounselCaption", "lblOpposingCounselValue", "OPPOSING COUNSEL", "—"),
            ("lblNextHearingCaption", "lblNextHearingValue", "NEXT HEARING", "—"),
            ("lblTimeRemainingCaption", "lblTimeRemainingValue", "TIME REMAINING", "—"),
        ]:
            col = QtWidgets.QVBoxLayout()
            cap = QtWidgets.QLabel(cap_text)
            cap.setStyleSheet("color: #9aa3b5; font-size: 10px;")
            col.addWidget(cap)
            val = QtWidgets.QLabel(val_text)
            val.setStyleSheet("color: #0c1230; font-size: 12px; font-weight: bold;")
            col.addWidget(val)
            self.caseInfoLayout.addLayout(col)
            setattr(self, cap_attr, cap)
            setattr(self, val_attr, val)
        self.caseDetailLayout.addLayout(self.caseInfoLayout)

        # Milestone heading
        self.lblTimelineHeading = QtWidgets.QLabel("CASE MILESTONE PROGRESS")
        self.lblTimelineHeading.setStyleSheet("color: #0c1230; font-size: 12px; font-weight: bold;")
        self.caseDetailLayout.addWidget(self.lblTimelineHeading)

        # Milestone timeline
        self.timelineFrame = QtWidgets.QFrame()
        self.timelineLayout = QtWidgets.QVBoxLayout(self.timelineFrame)
        self._milestones = []
        for dot_color, title_text, desc_text in [
            ("#2fae66", "Initial Filing", "Complaint and summons served to all parties."),
            ("#2fae66", "Case Review & Scheduling", "Case reviewed and confirmed for hearing."),
            ("#f0b429", "Hearing Scheduled", "Documentation for recent submissions pending."),
            ("#c7cbe0", "Order Issued", ""),
        ]:
            row = QtWidgets.QHBoxLayout()
            dot = QtWidgets.QLabel("●")
            dot.setStyleSheet(f"color: {dot_color}; font-size: 14px;")
            row.addWidget(dot)
            txt_col = QtWidgets.QVBoxLayout()
            t = QtWidgets.QLabel(title_text)
            t.setStyleSheet("color: #0c1230; font-size: 12px; font-weight: bold;")
            txt_col.addWidget(t)
            if desc_text:
                d = QtWidgets.QLabel(desc_text)
                d.setStyleSheet("color: #9aa3b5; font-size: 10px;")
                txt_col.addWidget(d)
            row.addLayout(txt_col)
            self.timelineLayout.addLayout(row)
        self.caseDetailLayout.addWidget(self.timelineFrame)

        # Next action frame
        self.nextActionFrame = QtWidgets.QFrame()
        self.nextActionFrame.setStyleSheet("background-color: #fff8e6; border-radius: 8px;")
        _nal = QtWidgets.QVBoxLayout(self.nextActionFrame)
        _nal.setContentsMargins(14, 10, 14, 10)
        self.lblNextActionTitle = QtWidgets.QLabel("Next Action Required")
        self.lblNextActionTitle.setStyleSheet("color: #b8860b; font-size: 11px; font-weight: bold;")
        _nal.addWidget(self.lblNextActionTitle)
        self.lblNextActionDesc = QtWidgets.QLabel(
            "Please review and sign the mediation disclosure statement sent to your counsel inbox."
        )
        self.lblNextActionDesc.setStyleSheet("color: #6b7390; font-size: 10px;")
        self.lblNextActionDesc.setWordWrap(True)
        _nal.addWidget(self.lblNextActionDesc)
        self.caseDetailLayout.addWidget(self.nextActionFrame)
        self.contentLayout.addWidget(self.caseDetailFrame)
        self.rootLayout.addWidget(self.mainContent)


class Ui_ResetPasswordWindow(object):
    """reset_password.ui – mobile-style Reset Password screen."""

    def setupUi(self, ResetPasswordWindow):
        ResetPasswordWindow.setObjectName("ResetPasswordWindow")
        ResetPasswordWindow.resize(360, 520)
        ResetPasswordWindow.setWindowTitle("Legal Management - Reset Password")
        ResetPasswordWindow.setStyleSheet(
            "background-color: #0c1230;\n"
            "font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QVBoxLayout(ResetPasswordWindow)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")

        # Header
        self.headerLayout = QtWidgets.QHBoxLayout()
        self.headerLayout.setContentsMargins(14, 12, 14, 12)
        self.headerLayout.setObjectName("headerLayout")
        self.btnMenu = QtWidgets.QPushButton("☰")
        self.btnMenu.setMinimumSize(QtCore.QSize(24, 24))
        self.btnMenu.setStyleSheet(
            "color: #ffffff; background-color: transparent; border: none; font-size: 15px;"
        )
        self.headerLayout.addWidget(self.btnMenu)
        self.lblHeaderTitle = QtWidgets.QLabel("Legal Management")
        self.lblHeaderTitle.setStyleSheet(
            "color: #ffffff; font-size: 13px; font-weight: bold;"
        )
        self.headerLayout.addWidget(self.lblHeaderTitle)
        self.headerLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.btnLogoutIcon = QtWidgets.QPushButton("⏻")
        self.btnLogoutIcon.setMinimumSize(QtCore.QSize(24, 24))
        self.btnLogoutIcon.setStyleSheet(
            "color: #8b93b0; background-color: transparent; border: none; font-size: 13px;"
        )
        self.headerLayout.addWidget(self.btnLogoutIcon)
        self.rootLayout.addLayout(self.headerLayout)

        # Body / card
        self.bodyLayout = QtWidgets.QVBoxLayout()
        self.bodyLayout.setContentsMargins(20, 10, 20, 10)
        self.bodyLayout.setObjectName("bodyLayout")

        self.cardFrame = QtWidgets.QFrame()
        self.cardFrame.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px;"
        )
        self.cardLayout = QtWidgets.QVBoxLayout(self.cardFrame)
        self.cardLayout.setContentsMargins(22, 22, 22, 22)
        self.cardLayout.setObjectName("cardLayout")

        self.lblTitle = QtWidgets.QLabel("Reset Password")
        self.lblTitle.setStyleSheet("color: #0c1230; font-size: 17px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblTitle)

        self.lblSubtitle = QtWidgets.QLabel(
            "Ensure security by using a complex password for legal portal access."
        )
        self.lblSubtitle.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.lblSubtitle.setWordWrap(True)
        self.cardLayout.addWidget(self.lblSubtitle)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblUsernameCaption = QtWidgets.QLabel("USERNAME")
        self.lblUsernameCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblUsernameCaption)

        self.txtUsername = QtWidgets.QLineEdit()
        self.txtUsername.setMinimumSize(QtCore.QSize(0, 36))
        self.txtUsername.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtUsername.setPlaceholderText("Search user...")
        self.cardLayout.addWidget(self.txtUsername)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblNewPasswordCaption = QtWidgets.QLabel("NEW PASSWORD")
        self.lblNewPasswordCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblNewPasswordCaption)

        self.newPasswordRowLayout = QtWidgets.QHBoxLayout()
        self.newPasswordRowLayout.setObjectName("newPasswordRowLayout")
        self.txtNewPassword = QtWidgets.QLineEdit()
        self.txtNewPassword.setMinimumSize(QtCore.QSize(0, 36))
        self.txtNewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtNewPassword.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtNewPassword.setPlaceholderText("••••••••")
        self.newPasswordRowLayout.addWidget(self.txtNewPassword)
        self.btnToggleNewPassword = QtWidgets.QPushButton("👁")
        self.btnToggleNewPassword.setMinimumSize(QtCore.QSize(30, 30))
        self.btnToggleNewPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnToggleNewPassword.setCheckable(True)
        self.btnToggleNewPassword.setStyleSheet(
            "color: #6b7390; background-color: transparent; border: none; font-size: 13px;"
        )
        self.newPasswordRowLayout.addWidget(self.btnToggleNewPassword)
        self.cardLayout.addLayout(self.newPasswordRowLayout)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblConfirmPasswordCaption = QtWidgets.QLabel("CONFIRM PASSWORD")
        self.lblConfirmPasswordCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblConfirmPasswordCaption)

        self.confirmPasswordRowLayout = QtWidgets.QHBoxLayout()
        self.confirmPasswordRowLayout.setObjectName("confirmPasswordRowLayout")
        self.txtConfirmPassword = QtWidgets.QLineEdit()
        self.txtConfirmPassword.setMinimumSize(QtCore.QSize(0, 36))
        self.txtConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtConfirmPassword.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtConfirmPassword.setPlaceholderText("••••••••")
        self.confirmPasswordRowLayout.addWidget(self.txtConfirmPassword)
        self.btnToggleConfirmPassword = QtWidgets.QPushButton("👁")
        self.btnToggleConfirmPassword.setMinimumSize(QtCore.QSize(30, 30))
        self.btnToggleConfirmPassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnToggleConfirmPassword.setCheckable(True)
        self.btnToggleConfirmPassword.setStyleSheet(
            "color: #6b7390; background-color: transparent; border: none; font-size: 13px;"
        )
        self.confirmPasswordRowLayout.addWidget(self.btnToggleConfirmPassword)
        self.cardLayout.addLayout(self.confirmPasswordRowLayout)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.btnUpdatePassword = QtWidgets.QPushButton("UPDATE PASSWORD")
        self.btnUpdatePassword.setMinimumSize(QtCore.QSize(0, 40))
        self.btnUpdatePassword.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnUpdatePassword.setStyleSheet(
            "QPushButton { background-color: #0c1230; color: #f0b429; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.cardLayout.addWidget(self.btnUpdatePassword)

        self.btnCancel = QtWidgets.QPushButton("CANCEL")
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 40))
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet(
            "QPushButton { background-color: #ffffff; color: #e0524a; border: 1px solid #e2e5ee; "
            "border-radius: 6px; font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #f7f8fc; }"
        )
        self.cardLayout.addWidget(self.btnCancel)

        self.bodyLayout.addWidget(self.cardFrame)
        self.rootLayout.addLayout(self.bodyLayout)

        self.rootLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        # Bottom nav bar
        self.bottomNavFrame = QtWidgets.QFrame()
        self.bottomNavFrame.setMinimumSize(QtCore.QSize(0, 56))
        self.bottomNavFrame.setStyleSheet(
            "background-color: #0a0f29; border-top: 1px solid #1f2750;"
        )
        self.bottomNavLayout = QtWidgets.QHBoxLayout(self.bottomNavFrame)
        self.bottomNavLayout.setContentsMargins(10, 0, 10, 0)
        self.bottomNavLayout.setObjectName("bottomNavLayout")

        self.btnNavJudges = QtWidgets.QPushButton("⚖\nJudges")
        self.btnNavJudges.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavJudges.setStyleSheet(
            "color: #8b93b0; background-color: transparent; border: none; font-size: 10px;"
        )
        self.bottomNavLayout.addWidget(self.btnNavJudges)

        self.btnNavLawyers = QtWidgets.QPushButton("💼\nLawyers")
        self.btnNavLawyers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavLawyers.setStyleSheet(
            "color: #8b93b0; background-color: transparent; border: none; font-size: 10px;"
        )
        self.bottomNavLayout.addWidget(self.btnNavLawyers)

        self.btnNavNewUser = QtWidgets.QPushButton("👤\nNew User")
        self.btnNavNewUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavNewUser.setStyleSheet(
            "color: #f0b429; background-color: transparent; border: none; "
            "font-size: 10px; font-weight: bold;"
        )
        self.bottomNavLayout.addWidget(self.btnNavNewUser)

        self.btnNavUsers = QtWidgets.QPushButton("👥\nUsers")
        self.btnNavUsers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavUsers.setStyleSheet(
            "color: #8b93b0; background-color: transparent; border: none; font-size: 10px;"
        )
        self.bottomNavLayout.addWidget(self.btnNavUsers)

        self.rootLayout.addWidget(self.bottomNavFrame)


class Ui_ScheduleHearingWindow(object):
    """schedule_hearing.ui – mobile-style Schedule Hearing screen."""

    def setupUi(self, ScheduleHearingWindow):
        ScheduleHearingWindow.setObjectName("ScheduleHearingWindow")
        ScheduleHearingWindow.resize(360, 560)
        ScheduleHearingWindow.setWindowTitle("Schedule Hearing")
        ScheduleHearingWindow.setStyleSheet(
            "background-color: #0c1230;\n"
            "font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QVBoxLayout(ScheduleHearingWindow)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")

        # Header
        self.headerLayout = QtWidgets.QHBoxLayout()
        self.headerLayout.setContentsMargins(14, 12, 14, 12)
        self.headerLayout.setObjectName("headerLayout")
        self.btnMenu = QtWidgets.QPushButton("☰")
        self.btnMenu.setMinimumSize(QtCore.QSize(24, 24))
        self.btnMenu.setStyleSheet(
            "color: #ffffff; background-color: transparent; border: none; font-size: 15px;"
        )
        self.headerLayout.addWidget(self.btnMenu)
        self.lblHeaderTitle = QtWidgets.QLabel("Schedule Hearing")
        self.lblHeaderTitle.setStyleSheet(
            "color: #ffffff; font-size: 13px; font-weight: bold;"
        )
        self.headerLayout.addWidget(self.lblHeaderTitle)
        self.headerLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.btnInfo = QtWidgets.QPushButton("i")
        self.btnInfo.setMinimumSize(QtCore.QSize(26, 26))
        self.btnInfo.setMaximumSize(QtCore.QSize(26, 26))
        self.btnInfo.setStyleSheet(
            "QPushButton { color: #ffffff; background-color: #1a2247; "
            "border-radius: 13px; font-size: 11px; font-weight: bold; }"
        )
        self.headerLayout.addWidget(self.btnInfo)
        self.rootLayout.addLayout(self.headerLayout)

        # Body / card
        self.bodyLayout = QtWidgets.QVBoxLayout()
        self.bodyLayout.setContentsMargins(20, 4, 20, 16)
        self.bodyLayout.setObjectName("bodyLayout")

        self.cardFrame = QtWidgets.QFrame()
        self.cardFrame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")
        self.cardLayout = QtWidgets.QVBoxLayout(self.cardFrame)
        self.cardLayout.setContentsMargins(20, 20, 20, 20)
        self.cardLayout.setObjectName("cardLayout")

        self.lblCaseFieldCaption = QtWidgets.QLabel("CASE ID & TITLE")
        self.lblCaseFieldCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblCaseFieldCaption)

        self.cmbActiveCase = QtWidgets.QComboBox()
        self.cmbActiveCase.setMinimumSize(QtCore.QSize(0, 36))
        self.cmbActiveCase.setStyleSheet(
            "QComboBox { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; color: #b8860b; }"
        )
        self.cardLayout.addWidget(self.cmbActiveCase)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblHearingDateCaption = QtWidgets.QLabel("HEARING DATE")
        self.lblHearingDateCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblHearingDateCaption)

        self.dateHearing = QtWidgets.QDateEdit()
        self.dateHearing.setMinimumSize(QtCore.QSize(0, 36))
        self.dateHearing.setStyleSheet(
            "QDateEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.dateHearing.setDisplayFormat("dd/MM/yyyy")
        self.dateHearing.setCalendarPopup(True)
        self.dateHearing.setDate(QtCore.QDate.currentDate())
        self.cardLayout.addWidget(self.dateHearing)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblTimeSlotCaption = QtWidgets.QLabel("TIME SLOT")
        self.lblTimeSlotCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblTimeSlotCaption)

        self.timeHearingSlot = QtWidgets.QTimeEdit()
        self.timeHearingSlot.setMinimumSize(QtCore.QSize(0, 36))
        self.timeHearingSlot.setStyleSheet(
            "QTimeEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.timeHearingSlot.setDisplayFormat("hh:mm AP")
        self.timeHearingSlot.setTime(QtCore.QTime.currentTime())
        self.cardLayout.addWidget(self.timeHearingSlot)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblLocationCaption = QtWidgets.QLabel("COURTROOM / VIRTUAL LINK")
        self.lblLocationCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblLocationCaption)

        self.txtCourtroomOrLink = QtWidgets.QLineEdit()
        self.txtCourtroomOrLink.setMinimumSize(QtCore.QSize(0, 36))
        self.txtCourtroomOrLink.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtCourtroomOrLink.setPlaceholderText("e.g. Chamber 4B or Zoom ID")
        self.cardLayout.addWidget(self.txtCourtroomOrLink)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.lblRemarksCaption = QtWidgets.QLabel("JUDICIAL REMARKS")
        self.lblRemarksCaption.setStyleSheet("color: #e0524a; font-size: 10px; font-weight: bold;")
        self.cardLayout.addWidget(self.lblRemarksCaption)

        self.txtJudicialRemarks = QtWidgets.QTextEdit()
        self.txtJudicialRemarks.setMinimumSize(QtCore.QSize(0, 70))
        self.txtJudicialRemarks.setStyleSheet(
            "QTextEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding: 8px; font-size: 12px; }"
        )
        self.txtJudicialRemarks.setPlaceholderText(
            "Enter session notes or specific instructions for the registry..."
        )
        self.cardLayout.addWidget(self.txtJudicialRemarks)

        self.cardLayout.addItem(
            QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        self.btnScheduleHearing = QtWidgets.QPushButton("Schedule Hearing")
        self.btnScheduleHearing.setMinimumSize(QtCore.QSize(0, 40))
        self.btnScheduleHearing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnScheduleHearing.setStyleSheet(
            "QPushButton { background-color: #0c1230; color: #ffffff; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.cardLayout.addWidget(self.btnScheduleHearing)

        self.btnCancel = QtWidgets.QPushButton("Cancel")
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 40))
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet(
            "QPushButton { background-color: #ffffff; color: #e0524a; border: 1px solid #e2e5ee; "
            "border-radius: 6px; font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #f7f8fc; }"
        )
        self.cardLayout.addWidget(self.btnCancel)

        self.bodyLayout.addWidget(self.cardFrame)
        self.rootLayout.addLayout(self.bodyLayout)


class Ui_SearchCaseWindow(object):
    """search_case.ui – Admin "Search Case" screen with sidebar."""

    def setupUi(self, SearchCaseWindow):
        SearchCaseWindow.setObjectName("SearchCaseWindow")
        SearchCaseWindow.resize(1200, 720)
        SearchCaseWindow.setWindowTitle("LexSecure CCMS - Search Case")
        SearchCaseWindow.setStyleSheet(
            "background-color: #eef1f8;\n"
            "font-family: 'Inter';"
        )
        self.rootLayout = QtWidgets.QHBoxLayout(SearchCaseWindow)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")

        # Sidebar
        self.sidebarFrame = QtWidgets.QFrame()
        self.sidebarFrame.setMinimumSize(QtCore.QSize(200, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebarFrame.setStyleSheet("background-color: #0c1230;")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setContentsMargins(14, 18, 14, 16)
        self.sidebarLayout.setObjectName("sidebarLayout")

        self.lblBrand = QtWidgets.QLabel("Court Admin")
        self.lblBrand.setStyleSheet("color: #f0b429; font-size: 15px; font-weight: bold;")
        self.sidebarLayout.addWidget(self.lblBrand)

        self.lblBrandSub = QtWidgets.QLabel("Admin Dashboard")
        self.lblBrandSub.setStyleSheet("color: #6b7390; font-size: 10px;")
        self.sidebarLayout.addWidget(self.lblBrandSub)

        self.sidebarLayout.addItem(
            QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        )

        _nav_normal = (
            "QPushButton { color: #c7cbe0; background-color: transparent; border: none; "
            "text-align: left; padding-left: 8px; font-size: 12px; border-radius: 6px; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        _nav_active = (
            "QPushButton { color: #0c1230; background-color: #f0b429; border: none; "
            "text-align: left; padding-left: 8px; font-size: 12px; font-weight: bold; "
            "border-radius: 6px; }"
        )

        self.btnNavDashboard = QtWidgets.QPushButton("  Dashboard")
        self.btnNavDashboard.setMinimumSize(QtCore.QSize(0, 34))
        self.btnNavDashboard.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavDashboard.setStyleSheet(_nav_normal)
        self.sidebarLayout.addWidget(self.btnNavDashboard)

        self.btnNavSearchCase = QtWidgets.QPushButton("  Search Case")
        self.btnNavSearchCase.setMinimumSize(QtCore.QSize(0, 34))
        self.btnNavSearchCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavSearchCase.setStyleSheet(_nav_active)
        self.sidebarLayout.addWidget(self.btnNavSearchCase)

        self.btnNavAllCases = QtWidgets.QPushButton("  All Cases")
        self.btnNavAllCases.setMinimumSize(QtCore.QSize(0, 34))
        self.btnNavAllCases.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavAllCases.setStyleSheet(_nav_normal)
        self.sidebarLayout.addWidget(self.btnNavAllCases)

        self.btnNavHearings = QtWidgets.QPushButton("  Manage Hearings")
        self.btnNavHearings.setMinimumSize(QtCore.QSize(0, 34))
        self.btnNavHearings.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavHearings.setStyleSheet(_nav_normal)
        self.sidebarLayout.addWidget(self.btnNavHearings)

        self.btnNavUsers = QtWidgets.QPushButton("  Manage Users")
        self.btnNavUsers.setMinimumSize(QtCore.QSize(0, 34))
        self.btnNavUsers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavUsers.setStyleSheet(_nav_normal)
        self.sidebarLayout.addWidget(self.btnNavUsers)

        self.sidebarLayout.addItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        )

        self.btnLogout = QtWidgets.QPushButton("Sign Out")
        self.btnLogout.setMinimumSize(QtCore.QSize(0, 34))
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet(
            "QPushButton { color: #c7cbe0; background-color: transparent; border: 1px solid #3a4566; "
            "border-radius: 6px; font-size: 12px; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.sidebarLayout.addWidget(self.btnLogout)
        self.rootLayout.addWidget(self.sidebarFrame)

        # Main content
        self.mainContent = QtWidgets.QWidget()
        self.contentLayout = QtWidgets.QVBoxLayout(self.mainContent)
        self.contentLayout.setContentsMargins(28, 20, 28, 20)
        self.contentLayout.setObjectName("contentLayout")

        # Top bar
        self.topBarLayout = QtWidgets.QHBoxLayout()
        self.lblBrandTop = QtWidgets.QLabel("LexSecure CCMS")
        self.lblBrandTop.setStyleSheet("color: #0c1230; font-size: 13px; font-weight: bold;")
        self.topBarLayout.addWidget(self.lblBrandTop)
        self.topBarLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.btnNotifications = QtWidgets.QPushButton("notifications")
        self.btnNotifications.setStyleSheet(
            "color:#6b7390; background: transparent; border:none; font-size:11px;"
        )
        self.topBarLayout.addWidget(self.btnNotifications)
        self.btnSettings = QtWidgets.QPushButton("settings")
        self.btnSettings.setStyleSheet(
            "color:#6b7390; background: transparent; border:none; font-size:11px;"
        )
        self.topBarLayout.addWidget(self.btnSettings)
        self.btnHelp = QtWidgets.QPushButton("help")
        self.btnHelp.setStyleSheet(
            "color:#6b7390; background: transparent; border:none; font-size:11px;"
        )
        self.topBarLayout.addWidget(self.btnHelp)
        self.contentLayout.addLayout(self.topBarLayout)

        self.lblPageTitle = QtWidgets.QLabel("Search Case")
        self.lblPageTitle.setStyleSheet("color: #0c1230; font-size: 22px; font-weight: bold;")
        self.contentLayout.addWidget(self.lblPageTitle)

        self.lblPageSubtitle = QtWidgets.QLabel(
            "Browse and manage the centralized judicial repository"
        )
        self.lblPageSubtitle.setStyleSheet("color: #6b7390; font-size: 12px;")
        self.contentLayout.addWidget(self.lblPageSubtitle)

        # Search panel
        self.searchPanelFrame = QtWidgets.QFrame()
        self.searchPanelFrame.setStyleSheet(
            "background-color: #ffffff; border-radius: 10px; border: 1px solid #e2e5ee;"
        )
        self.searchPanelLayout = QtWidgets.QVBoxLayout(self.searchPanelFrame)
        self.searchPanelLayout.setContentsMargins(20, 18, 20, 18)
        self.searchPanelLayout.setObjectName("searchPanelLayout")

        self.lblSearchByLabel = QtWidgets.QLabel("SEARCH BY CASE ID OR PARTY NAME")
        self.lblSearchByLabel.setStyleSheet("color: #6b7390; font-size: 11px; font-weight: bold;")
        self.searchPanelLayout.addWidget(self.lblSearchByLabel)

        self.searchRowLayout = QtWidgets.QHBoxLayout()
        self.searchRowLayout.setObjectName("searchRowLayout")
        self.txtCaseQuery = QtWidgets.QLineEdit()
        self.txtCaseQuery.setMinimumSize(QtCore.QSize(0, 38))
        self.txtCaseQuery.setStyleSheet(
            "QLineEdit { background-color: #f5f6fa; border: 1px solid #e2e5ee; "
            "border-radius: 6px; padding-left: 10px; font-size: 12px; }"
        )
        self.txtCaseQuery.setPlaceholderText("e.g. Case ID, LC_2024_XXX or party name")
        self.searchRowLayout.addWidget(self.txtCaseQuery)
        self.btnSearchCase = QtWidgets.QPushButton("Search  →")
        self.btnSearchCase.setMinimumSize(QtCore.QSize(150, 38))
        self.btnSearchCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSearchCase.setStyleSheet(
            "QPushButton { background-color: #0c1230; color: #ffffff; border-radius: 6px; "
            "font-size: 12px; font-weight: bold; } "
            "QPushButton:hover { background-color: #1a2247; }"
        )
        self.searchRowLayout.addWidget(self.btnSearchCase)
        self.searchPanelLayout.addLayout(self.searchRowLayout)

        self.filterRowLayout = QtWidgets.QHBoxLayout()
        self.filterRowLayout.setObjectName("filterRowLayout")
        self.lblSearchInLabel = QtWidgets.QLabel("SEARCH IN:")
        self.lblSearchInLabel.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.filterRowLayout.addWidget(self.lblSearchInLabel)

        _filter_style = (
            "QPushButton { background-color: #eef1f8; color: #0c1230; border-radius: 14px; "
            "font-size: 11px; } QPushButton:checked { background-color: #0c1230; color: #ffffff; }"
        )

        self.btnFilterAll = QtWidgets.QPushButton("All")
        self.btnFilterAll.setMinimumSize(QtCore.QSize(70, 28))
        self.btnFilterAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFilterAll.setCheckable(True)
        self.btnFilterAll.setChecked(True)
        self.btnFilterAll.setStyleSheet(_filter_style)
        self.filterRowLayout.addWidget(self.btnFilterAll)

        self.btnFilterCivil = QtWidgets.QPushButton("Civil")
        self.btnFilterCivil.setMinimumSize(QtCore.QSize(70, 28))
        self.btnFilterCivil.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFilterCivil.setCheckable(True)
        self.btnFilterCivil.setStyleSheet(_filter_style)
        self.filterRowLayout.addWidget(self.btnFilterCivil)

        self.btnFilterCriminal = QtWidgets.QPushButton("Criminal")
        self.btnFilterCriminal.setMinimumSize(QtCore.QSize(80, 28))
        self.btnFilterCriminal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnFilterCriminal.setCheckable(True)
        self.btnFilterCriminal.setStyleSheet(_filter_style)
        self.filterRowLayout.addWidget(self.btnFilterCriminal)

        self.filterRowLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.searchPanelLayout.addLayout(self.filterRowLayout)
        self.contentLayout.addWidget(self.searchPanelFrame)

        # "Ready to search" placeholder
        self.resultsPlaceholderFrame = QtWidgets.QFrame()
        self.resultsPlaceholderLayout = QtWidgets.QVBoxLayout(self.resultsPlaceholderFrame)
        self.resultsPlaceholderLayout.setObjectName("resultsPlaceholderLayout")

        self.lblResultsIcon = QtWidgets.QLabel("🔍")
        self.lblResultsIcon.setStyleSheet("color: #c7cbe0; font-size: 30px;")
        self.lblResultsIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsPlaceholderLayout.addWidget(self.lblResultsIcon)

        self.lblReadyToSearch = QtWidgets.QLabel("Ready to Search")
        self.lblReadyToSearch.setStyleSheet("color: #0c1230; font-size: 14px; font-weight: bold;")
        self.lblReadyToSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.resultsPlaceholderLayout.addWidget(self.lblReadyToSearch)

        self.lblReadyToSearchDesc = QtWidgets.QLabel(
            "Enter a case number or party name to retrieve filings and case details."
        )
        self.lblReadyToSearchDesc.setStyleSheet("color: #6b7390; font-size: 11px;")
        self.lblReadyToSearchDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblReadyToSearchDesc.setWordWrap(True)
        self.resultsPlaceholderLayout.addWidget(self.lblReadyToSearchDesc)

        self.contentLayout.addWidget(self.resultsPlaceholderFrame)

        # Results table (hidden until a search is performed)
        self.tableSearchResults = QtWidgets.QTableWidget()
        self.tableSearchResults.setVisible(False)
        self.tableSearchResults.setColumnCount(4)
        self.tableSearchResults.setHorizontalHeaderLabels(
            ["Case ID", "Title / Parties", "Status", "Action"]
        )
        self.tableSearchResults.setStyleSheet(
            "QTableWidget { background-color: #ffffff; border: 1px solid #e2e5ee; "
            "border-radius: 8px; font-size: 12px; } "
            "QHeaderView::section { background-color: #f7f8fc; color: #6b7390; "
            "padding: 8px; border: none; font-weight: bold; }"
        )
        self.tableSearchResults.setAlternatingRowColors(True)
        self.tableSearchResults.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableSearchResults.horizontalHeader().setStretchLastSection(True)
        self.contentLayout.addWidget(self.tableSearchResults)

        self.rootLayout.addWidget(self.mainContent)


class Ui_MyCasesPage(object):
    """my_cases__client_pannel_.ui – Client "My Cases" screen.

    The .ui file ships with three hardcoded sample case cards (Doe vs. State,
    Global Logistics, Residential Lease). Here the static shell (sidebar, top
    bar, stats row, section header, scroll area) is built exactly as designed,
    while caseListLayout is left empty so MyCasesWidget can populate it with
    real case cards for the logged-in client at runtime.
    """

    def setupUi(self, MyCasesPage):
        MyCasesPage.setObjectName("MyCasesPage")
        MyCasesPage.resize(1024, 680)
        MyCasesPage.setWindowTitle("My Cases - Client Portal")
        MyCasesPage.setStyleSheet(
            "QWidget#MyCasesPage {\n"
            "    background-color: #0b0f17;\n"
            "}\n"
            "QLabel {\n"
            "    color: #e6e8eb;\n"
            "}"
        )
        self.rootLayout = QtWidgets.QHBoxLayout(MyCasesPage)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setObjectName("rootLayout")

        # ── Sidebar ──
        self.sidebarFrame = QtWidgets.QFrame()
        self.sidebarFrame.setMinimumSize(QtCore.QSize(220, 0))
        self.sidebarFrame.setMaximumSize(QtCore.QSize(220, 16777215))
        self.sidebarFrame.setStyleSheet(
            "QFrame#sidebarFrame {\n"
            "    background-color: #0e1420;\n"
            "    border-right: 1px solid #1c2230;\n"
            "}"
        )
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setSpacing(4)
        self.sidebarLayout.setContentsMargins(18, 20, 18, 20)
        self.sidebarLayout.setObjectName("sidebarLayout")

        self.lblLogoTitle = QtWidgets.QLabel("Client Portal")
        self.lblLogoTitle.setStyleSheet("color:#ffffff; font-size:16px; font-weight:700;")
        self.sidebarLayout.addWidget(self.lblLogoTitle)

        self.lblLogoSubtitle = QtWidgets.QLabel("CASE VIEWER")
        self.lblLogoSubtitle.setStyleSheet(
            "color:#5b6472; font-size:10px; font-weight:600; letter-spacing:1px; margin-bottom:18px;"
        )
        self.sidebarLayout.addWidget(self.lblLogoSubtitle)

        self.btnNavMyCases = QtWidgets.QPushButton("📁  My Cases")
        self.btnNavMyCases.setMinimumSize(QtCore.QSize(0, 40))
        self.btnNavMyCases.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavMyCases.setStyleSheet(
            "QPushButton#btnNavMyCases {\n"
            "    background-color: #1d2a52;\n"
            "    color: #ffffff;\n"
            "    text-align: left;\n"
            "    padding-left: 12px;\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    font-weight: 600;\n"
            "    font-size: 13px;\n"
            "}"
        )
        self.sidebarLayout.addWidget(self.btnNavMyCases)

        self.btnNavTrackCase = QtWidgets.QPushButton("🔍  Track My Case")
        self.btnNavTrackCase.setMinimumSize(QtCore.QSize(0, 40))
        self.btnNavTrackCase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnNavTrackCase.setStyleSheet(
            "QPushButton#btnNavTrackCase {\n"
            "    background-color: transparent;\n"
            "    color: #9aa1ac;\n"
            "    text-align: left;\n"
            "    padding-left: 12px;\n"
            "    border: none;\n"
            "    border-radius: 8px;\n"
            "    font-size: 13px;\n"
            "}\n"
            "QPushButton#btnNavTrackCase:hover {\n"
            "    background-color: #161d2b;\n"
            "}"
        )
        self.sidebarLayout.addWidget(self.btnNavTrackCase)

        self.sidebarLayout.addItem(
            QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        )

        self.userInfoFrame = QtWidgets.QFrame()
        self.userInfoLayout = QtWidgets.QHBoxLayout(self.userInfoFrame)
        self.userInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.userInfoLayout.setObjectName("userInfoLayout")
        self.lblUserName = QtWidgets.QLabel("John Doe")
        self.lblUserName.setStyleSheet("color:#d6d9de; font-size:13px;")
        self.userInfoLayout.addWidget(self.lblUserName)
        self.sidebarLayout.addWidget(self.userInfoFrame)

        self.btnLogout = QtWidgets.QPushButton("Logout")
        self.btnLogout.setMinimumSize(QtCore.QSize(0, 30))
        self.btnLogout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLogout.setStyleSheet(
            "QPushButton#btnLogout {\n"
            "    background-color: transparent;\n"
            "    color: #7c8794;\n"
            "    border: none;\n"
            "    text-align: left;\n"
            "    padding-left: 0px;\n"
            "    font-size: 12px;\n"
            "}"
        )
        self.sidebarLayout.addWidget(self.btnLogout)
        self.rootLayout.addWidget(self.sidebarFrame)

        # ── Main content ──
        self.mainContentFrame = QtWidgets.QFrame()
        self.mainContentLayout = QtWidgets.QVBoxLayout(self.mainContentFrame)
        self.mainContentLayout.setSpacing(18)
        self.mainContentLayout.setContentsMargins(28, 22, 28, 22)
        self.mainContentLayout.setObjectName("mainContentLayout")

        # Top bar
        self.topBarFrame = QtWidgets.QFrame()
        self.topBarLayout = QtWidgets.QHBoxLayout(self.topBarFrame)
        self.topBarLayout.setContentsMargins(0, 0, 0, 0)
        self.topBarLayout.setObjectName("topBarLayout")

        self.lblPageTitle = QtWidgets.QLabel("My Cases")
        self.lblPageTitle.setStyleSheet("color:#ffffff; font-size:20px; font-weight:700;")
        self.topBarLayout.addWidget(self.lblPageTitle)
        self.topBarLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )

        self.btnSearch = QtWidgets.QToolButton()
        self.btnSearch.setText("🔍")
        self.btnSearch.setStyleSheet(
            "QToolButton {\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    color: #ffffff;\n"
            "    font-size: 16px;\n"
            "}"
        )
        self.topBarLayout.addWidget(self.btnSearch)

        self.btnNotifications = QtWidgets.QToolButton()
        self.btnNotifications.setText("🔔")
        self.btnNotifications.setStyleSheet(
            "QToolButton {\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    color: #ffffff;\n"
            "    font-size: 16px;\n"
            "    margin-left: 14px;\n"
            "}"
        )
        self.topBarLayout.addWidget(self.btnNotifications)

        self.btnUserAvatar = QtWidgets.QToolButton()
        self.btnUserAvatar.setText("JD")
        self.btnUserAvatar.setStyleSheet(
            "QToolButton {\n"
            "    color: #ffffff;\n"
            "    background-color: #1f2937;\n"
            "    border-radius: 16px;\n"
            "    min-width: 32px;\n"
            "    min-height: 32px;\n"
            "    margin-left: 14px;\n"
            "    font-weight: 600;\n"
            "    font-size: 11px;\n"
            "}"
        )
        self.topBarLayout.addWidget(self.btnUserAvatar)
        self.mainContentLayout.addWidget(self.topBarFrame)

        # Stats row
        self.statsRowFrame = QtWidgets.QFrame()
        self.statsRowLayout = QtWidgets.QHBoxLayout(self.statsRowFrame)
        self.statsRowLayout.setSpacing(14)
        self.statsRowLayout.setContentsMargins(0, 0, 0, 0)
        self.statsRowLayout.setObjectName("statsRowLayout")

        self.cardTotalCases = QtWidgets.QFrame()
        self.cardTotalCases.setStyleSheet(
            "QFrame#cardTotalCases {\n"
            "    background-color: #111827;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        _ctc = QtWidgets.QVBoxLayout(self.cardTotalCases)
        _ctc.setContentsMargins(16, 12, 16, 12)
        self.lblTotalCasesTitle = QtWidgets.QLabel("TOTAL CASES")
        self.lblTotalCasesTitle.setStyleSheet(
            "color:#8b95a3; font-size:11px; font-weight:600; letter-spacing:1px;"
        )
        _ctc.addWidget(self.lblTotalCasesTitle)
        self.lblTotalCasesValue = QtWidgets.QLabel("00")
        self.lblTotalCasesValue.setStyleSheet("color:#39c5cf; font-size:22px; font-weight:700;")
        _ctc.addWidget(self.lblTotalCasesValue)
        self.statsRowLayout.addWidget(self.cardTotalCases)

        self.cardActiveCases = QtWidgets.QFrame()
        self.cardActiveCases.setStyleSheet(
            "QFrame#cardActiveCases {\n"
            "    background-color: #111827;\n"
            "    border-radius: 10px;\n"
            "}"
        )
        _cac = QtWidgets.QVBoxLayout(self.cardActiveCases)
        _cac.setContentsMargins(16, 12, 16, 12)
        self.lblActiveCasesTitle = QtWidgets.QLabel("ACTIVE")
        self.lblActiveCasesTitle.setStyleSheet(
            "color:#8b95a3; font-size:11px; font-weight:600; letter-spacing:1px;"
        )
        _cac.addWidget(self.lblActiveCasesTitle)
        self.lblActiveCasesValue = QtWidgets.QLabel("00")
        self.lblActiveCasesValue.setStyleSheet("color:#f5a623; font-size:22px; font-weight:700;")
        _cac.addWidget(self.lblActiveCasesValue)
        self.statsRowLayout.addWidget(self.cardActiveCases)

        self.statsRowLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )
        self.mainContentLayout.addWidget(self.statsRowFrame)

        # Section header
        self.sectionHeaderFrame = QtWidgets.QFrame()
        self.sectionHeaderLayout = QtWidgets.QHBoxLayout(self.sectionHeaderFrame)
        self.sectionHeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.sectionHeaderLayout.setObjectName("sectionHeaderLayout")

        self.lblActiveCaseFiles = QtWidgets.QLabel("Active Case Files")
        self.lblActiveCaseFiles.setStyleSheet("color:#ffffff; font-size:15px; font-weight:700;")
        self.sectionHeaderLayout.addWidget(self.lblActiveCaseFiles)
        self.sectionHeaderLayout.addItem(
            QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        )

        self.btnFilter = QtWidgets.QToolButton()
        self.btnFilter.setText("▾ Filter")
        self.btnFilter.setStyleSheet(
            "QToolButton {\n"
            "    color: #9aa1ac;\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    font-size: 12px;\n"
            "}"
        )
        self.sectionHeaderLayout.addWidget(self.btnFilter)

        self.btnSort = QtWidgets.QToolButton()
        self.btnSort.setText("⇕ Sort")
        self.btnSort.setStyleSheet(
            "QToolButton {\n"
            "    color: #9aa1ac;\n"
            "    background: transparent;\n"
            "    border: none;\n"
            "    font-size: 12px;\n"
            "    margin-left: 12px;\n"
            "}"
        )
        self.sectionHeaderLayout.addWidget(self.btnSort)
        self.mainContentLayout.addWidget(self.sectionHeaderFrame)

        # Scrollable case list (populated dynamically at runtime)
        self.caseListScrollArea = QtWidgets.QScrollArea()
        self.caseListScrollArea.setWidgetResizable(True)
        self.caseListScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.caseListScrollArea.setStyleSheet(
            "QScrollArea {\n"
            "    border: none;\n"
            "    background: transparent;\n"
            "}"
        )
        self.caseListScrollContents = QtWidgets.QWidget()
        self.caseListLayout = QtWidgets.QVBoxLayout(self.caseListScrollContents)
        self.caseListLayout.setSpacing(12)
        self.caseListLayout.setContentsMargins(0, 0, 0, 0)
        self.caseListLayout.setObjectName("caseListLayout")
        self.caseListScrollArea.setWidget(self.caseListScrollContents)
        self.mainContentLayout.addWidget(self.caseListScrollArea)

        # Empty-state placeholder (shown when the client has no cases)
        self.lblEmptyState = QtWidgets.QLabel("No cases on file yet.")
        self.lblEmptyState.setStyleSheet("color:#5b6472; font-size:13px;")
        self.lblEmptyState.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEmptyState.setVisible(False)
        self.caseListLayout.addWidget(self.lblEmptyState)

        self.rootLayout.addWidget(self.mainContentFrame)


# ─────────────────────────────────────────────
#  STORAGE  (from Final_code.py)
# ─────────────────────────────────────────────

DATA_FOLDER = "data"

FILES = {
    "cases":         "cases.json",
    "hearings":      "hearings.json",
    "firs":          "firs.json",
    "orders":        "orders.json",
    "users":         "users.json",
    "timeline":      "timeline.json",
    "audit":         "audit.json",
    "notifications": "notifications.json",
}


def init_storage():
    os.makedirs(DATA_FOLDER, exist_ok=True)
    for f in FILES.values():
        path = os.path.join(DATA_FOLDER, f)
        if not os.path.exists(path):
            with open(path, "w") as fp:
                json.dump([], fp)


def load_data(name):
    with open(os.path.join(DATA_FOLDER, FILES[name]), "r") as f:
        return json.load(f)


def save_data(name, data):
    with open(os.path.join(DATA_FOLDER, FILES[name]), "w") as f:
        json.dump(data, f, indent=4)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ─────────────────────────────────────────────
#  BUSINESS LOGIC  (from Final_code.py)
# ─────────────────────────────────────────────

def initialize_default_admin():
    users = load_data("users")
    if not any(u.get("username") == "admin" for u in users):
        users.append({"username": "admin", "password": "admin123", "role": "Admin"})
        save_data("users", users)


def login(username, password):
    for u in load_data("users"):
        if u["username"] == username and u["password"] == password:
            return u
    return None


def add_timeline(case_id, event):
    t = load_data("timeline")
    t.append({"case_id": case_id, "event": event, "date": now()})
    save_data("timeline", t)


def add_audit(user, action):
    a = load_data("audit")
    a.append({"user": user, "action": action, "date": now()})
    save_data("audit", a)


def create_user(username, password, role):
    users = load_data("users")
    users.append({"username": username, "password": password, "role": role})
    save_data("users", users)


def delete_user(username):
    users = [u for u in load_data("users") if u["username"] != username]
    save_data("users", users)


def reset_password(username, new_password):
    users = load_data("users")
    for u in users:
        if u["username"] == username:
            u["password"] = new_password
    save_data("users", users)


def add_case(title, description, category, priority, client):
    cases = load_data("cases")
    cid = max((c["id"] for c in cases), default=0) + 1
    case = {
        "id": cid, "title": title, "description": description,
        "category": category, "priority": priority, "status": "Filed",
        "judge": "", "lawyer": "", "client": client, "filing_date": now(),
    }
    cases.append(case)
    save_data("cases", cases)
    add_timeline(cid, "Case Filed")
    return cid


def assign_judge(case_id, judge_name):
    cases = load_data("cases")
    for c in cases:
        if c["id"] == case_id:
            c["judge"] = judge_name
            add_timeline(case_id, f"Judge Assigned: {judge_name}")
    save_data("cases", cases)


def assign_lawyer(case_id, lawyer_name):
    cases = load_data("cases")
    for c in cases:
        if c["id"] == case_id:
            c["lawyer"] = lawyer_name
            add_timeline(case_id, f"Lawyer Assigned: {lawyer_name}")
    save_data("cases", cases)


def schedule_hearing(case_id, date, time, courtroom, remarks):
    hearings = load_data("hearings")
    hearings.append({"case_id": case_id, "date": date, "time": time,
                     "courtroom": courtroom, "remarks": remarks})
    save_data("hearings", hearings)
    add_timeline(case_id, "Hearing Scheduled")


def issue_order(case_id, order_text):
    orders = load_data("orders")
    orders.append({"case_id": case_id, "order": order_text, "date": now()})
    save_data("orders", orders)
    add_timeline(case_id, "Order Issued")


# ─────────────────────────────────────────────
#  SHARED STYLE HELPERS
# ─────────────────────────────────────────────

DARK_BG     = "#0c1230"
CARD_BG     = "#131a3d"
BORDER_COL  = "#232b55"
ACCENT      = "#f0b429"
TEXT_MAIN   = "#e6e8f0"
TEXT_MUTED  = "#9aa3bd"
LIGHT_BG    = "#eef1f8"


def h_sep():
    """Thin horizontal divider line."""
    f = QFrame()
    f.setFrameShape(QFrame.HLine)
    f.setStyleSheet(f"color: {BORDER_COL};")
    return f


def styled_btn(text, primary=True):
    b = QPushButton(text)
    if primary:
        b.setStyleSheet(
            f"QPushButton{{background:{ACCENT};color:{DARK_BG};border-radius:6px;"
            f"padding:10px 20px;font-weight:bold;}}"
            f"QPushButton:hover{{background:#ffce4d;}}"
        )
    else:
        b.setStyleSheet(
            f"QPushButton{{background:transparent;color:{TEXT_MAIN};"
            f"border:1px solid #2c3566;border-radius:6px;padding:10px 20px;}}"
            f"QPushButton:hover{{background:#1a2247;}}"
        )
    return b


# ─────────────────────────────────────────────
#  WINDOW 1 – WELCOME  (Welcome.ui)
# ─────────────────────────────────────────────

class Ui_IssueOrderForm(object):
    def setupUi(self, IssueOrderForm):
        IssueOrderForm.setObjectName("IssueOrderForm")
        IssueOrderForm.resize(375, 720)
        IssueOrderForm.setStyleSheet("QWidget#IssueOrderForm {\n"
"    background-color: #0d1117;\n"
"}\n"
"QLabel {\n"
"    color: #e6e8eb;\n"
"}")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(IssueOrderForm)
        self.mainVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVerticalLayout.setSpacing(0)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.headerFrame = QtWidgets.QFrame(IssueOrderForm)
        self.headerFrame.setMinimumSize(QtCore.QSize(0, 56))
        self.headerFrame.setStyleSheet("QFrame#headerFrame {\n"
"    background-color: #111827;\n"
"    border-bottom: 1px solid #1f2937;\n"
"}")
        self.headerFrame.setObjectName("headerFrame")
        self.headerLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        self.headerLayout.setContentsMargins(16, -1, 16, -1)
        self.headerLayout.setObjectName("headerLayout")
        self.btnMenu = QtWidgets.QToolButton(self.headerFrame)
        self.btnMenu.setStyleSheet("QToolButton {\n"
"    color: #ffffff;\n"
"    font-size: 20px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.btnMenu.setObjectName("btnMenu")
        self.headerLayout.addWidget(self.btnMenu)
        self.lblHeaderTitle = QtWidgets.QLabel(self.headerFrame)
        self.lblHeaderTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeaderTitle.setStyleSheet("color:#ffffff; font-size:15px; font-weight:600;")
        self.lblHeaderTitle.setObjectName("lblHeaderTitle")
        self.headerLayout.addWidget(self.lblHeaderTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        self.btnUserAvatar = QtWidgets.QToolButton(self.headerFrame)
        self.btnUserAvatar.setStyleSheet("QToolButton {\n"
"    color: #ffffff;\n"
"    background-color: #1f2937;\n"
"    border-radius: 14px;\n"
"    min-width: 28px;\n"
"    min-height: 28px;\n"
"}")
        self.btnUserAvatar.setObjectName("btnUserAvatar")
        self.headerLayout.addWidget(self.btnUserAvatar)
        self.mainVerticalLayout.addWidget(self.headerFrame)
        self.statsRowFrame = QtWidgets.QFrame(IssueOrderForm)
        self.statsRowFrame.setObjectName("statsRowFrame")
        self.statsRowLayout = QtWidgets.QHBoxLayout(self.statsRowFrame)
        self.statsRowLayout.setContentsMargins(16, 16, 16, -1)
        self.statsRowLayout.setSpacing(12)
        self.statsRowLayout.setObjectName("statsRowLayout")
        self.cardDrafts = QtWidgets.QFrame(self.statsRowFrame)
        self.cardDrafts.setStyleSheet("QFrame#cardDrafts {\n"
"    background-color: #111827;\n"
"    border-radius: 10px;\n"
"}")
        self.cardDrafts.setObjectName("cardDrafts")
        self.cardDraftsLayout = QtWidgets.QVBoxLayout(self.cardDrafts)
        self.cardDraftsLayout.setContentsMargins(14, 10, 14, 10)
        self.cardDraftsLayout.setObjectName("cardDraftsLayout")
        self.lblDraftsTitle = QtWidgets.QLabel(self.cardDrafts)
        self.lblDraftsTitle.setStyleSheet("color:#8b95a3; font-size:11px; font-weight:600; letter-spacing:1px;")
        self.lblDraftsTitle.setObjectName("lblDraftsTitle")
        self.cardDraftsLayout.addWidget(self.lblDraftsTitle)
        self.lblDraftsValue = QtWidgets.QLabel(self.cardDrafts)
        self.lblDraftsValue.setStyleSheet("color:#ffffff; font-size:16px; font-weight:700;")
        self.lblDraftsValue.setObjectName("lblDraftsValue")
        self.cardDraftsLayout.addWidget(self.lblDraftsValue)
        self.statsRowLayout.addWidget(self.cardDrafts)
        self.cardCourtroom = QtWidgets.QFrame(self.statsRowFrame)
        self.cardCourtroom.setStyleSheet("QFrame#cardCourtroom {\n"
"    background-color: #111827;\n"
"    border-radius: 10px;\n"
"}")
        self.cardCourtroom.setObjectName("cardCourtroom")
        self.cardCourtroomLayout = QtWidgets.QVBoxLayout(self.cardCourtroom)
        self.cardCourtroomLayout.setContentsMargins(14, 10, 14, 10)
        self.cardCourtroomLayout.setObjectName("cardCourtroomLayout")
        self.lblCourtroomTitle = QtWidgets.QLabel(self.cardCourtroom)
        self.lblCourtroomTitle.setStyleSheet("color:#8b95a3; font-size:11px; font-weight:600; letter-spacing:1px;")
        self.lblCourtroomTitle.setObjectName("lblCourtroomTitle")
        self.cardCourtroomLayout.addWidget(self.lblCourtroomTitle)
        self.lblCourtroomValue = QtWidgets.QLabel(self.cardCourtroom)
        self.lblCourtroomValue.setStyleSheet("color:#ffffff; font-size:16px; font-weight:700;")
        self.lblCourtroomValue.setObjectName("lblCourtroomValue")
        self.cardCourtroomLayout.addWidget(self.lblCourtroomValue)
        self.statsRowLayout.addWidget(self.cardCourtroom)
        self.mainVerticalLayout.addWidget(self.statsRowFrame)
        self.lblOrderDetailsHeading = QtWidgets.QLabel(IssueOrderForm)
        self.lblOrderDetailsHeading.setStyleSheet("color:#ffffff; font-size:18px; font-weight:700; margin-left:16px; margin-top:20px; margin-bottom:10px;")
        self.lblOrderDetailsHeading.setObjectName("lblOrderDetailsHeading")
        self.mainVerticalLayout.addWidget(self.lblOrderDetailsHeading)
        self.formCardFrame = QtWidgets.QFrame(IssueOrderForm)
        self.formCardFrame.setStyleSheet("QFrame#formCardFrame {\n"
"    background-color: #ffffff;\n"
"    border-radius: 14px;\n"
"}")
        self.formCardFrame.setObjectName("formCardFrame")
        self.formCardLayout = QtWidgets.QVBoxLayout(self.formCardFrame)
        self.formCardLayout.setContentsMargins(18, 18, 18, 18)
        self.formCardLayout.setSpacing(10)
        self.formCardLayout.setObjectName("formCardLayout")
        self.lblCaseReference = QtWidgets.QLabel(self.formCardFrame)
        self.lblCaseReference.setStyleSheet("color:#5b6472; font-size:12px; font-weight:600;")
        self.lblCaseReference.setObjectName("lblCaseReference")
        self.formCardLayout.addWidget(self.lblCaseReference)
        self.comboCaseReference = QtWidgets.QComboBox(self.formCardFrame)
        self.comboCaseReference.setMinimumSize(QtCore.QSize(0, 40))
        self.comboCaseReference.setStyleSheet("QComboBox {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: #9aa1ac;\n"
"}")
        self.comboCaseReference.setObjectName("comboCaseReference")
        self.comboCaseReference.addItem("")
        self.formCardLayout.addWidget(self.comboCaseReference)
        self.lblOrderText = QtWidgets.QLabel(self.formCardFrame)
        self.lblOrderText.setStyleSheet("color:#5b6472; font-size:12px; font-weight:600; margin-top:8px;")
        self.lblOrderText.setObjectName("lblOrderText")
        self.formCardLayout.addWidget(self.lblOrderText)
        self.txtOrderInstructions = QtWidgets.QTextEdit(self.formCardFrame)
        self.txtOrderInstructions.setMinimumSize(QtCore.QSize(0, 130))
        self.txtOrderInstructions.setStyleSheet("QTextEdit {\n"
"    background-color: #f3f4f6;\n"
"    border: 1px solid #d8dce1;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: #222222;\n"
"    font-size: 13px;\n"
"}")
        self.txtOrderInstructions.setObjectName("txtOrderInstructions")
        self.formCardLayout.addWidget(self.txtOrderInstructions)
        self.mainVerticalLayout.addWidget(self.formCardFrame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.mainVerticalLayout.addItem(spacerItem1)
        self.btnIssueOrder = QtWidgets.QPushButton(IssueOrderForm)
        self.btnIssueOrder.setMinimumSize(QtCore.QSize(0, 48))
        self.btnIssueOrder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnIssueOrder.setStyleSheet("QPushButton#btnIssueOrder {\n"
"    background-color: #1d2a52;\n"
"    color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    font-weight: 700;\n"
"    font-size: 13px;\n"
"    margin-left: 16px;\n"
"    margin-right: 16px;\n"
"}\n"
"QPushButton#btnIssueOrder:hover {\n"
"    background-color: #243161;\n"
"}\n"
"QPushButton#btnIssueOrder:pressed {\n"
"    background-color: #16204a;\n"
"}")
        self.btnIssueOrder.setObjectName("btnIssueOrder")
        self.mainVerticalLayout.addWidget(self.btnIssueOrder)
        self.btnCancel = QtWidgets.QPushButton(IssueOrderForm)
        self.btnCancel.setMinimumSize(QtCore.QSize(0, 48))
        self.btnCancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancel.setStyleSheet("QPushButton#btnCancel {\n"
"    background-color: transparent;\n"
"    color: #7c8794;\n"
"    border: 1px solid #1f2937;\n"
"    border-radius: 10px;\n"
"    font-size: 13px;\n"
"    margin-left: 16px;\n"
"    margin-right: 16px;\n"
"    margin-top: 8px;\n"
"    margin-bottom: 16px;\n"
"}\n"
"QPushButton#btnCancel:hover {\n"
"    background-color: #161d2b;\n"
"}")
        self.btnCancel.setObjectName("btnCancel")
        self.mainVerticalLayout.addWidget(self.btnCancel)

        self.retranslateUi(IssueOrderForm)
        QtCore.QMetaObject.connectSlotsByName(IssueOrderForm)

    def retranslateUi(self, IssueOrderForm):
        _translate = QtCore.QCoreApplication.translate
        IssueOrderForm.setWindowTitle(_translate("IssueOrderForm", "Issue Order"))
        self.btnMenu.setText(_translate("IssueOrderForm", "≡"))
        self.lblHeaderTitle.setText(_translate("IssueOrderForm", "Issue Order"))
        self.btnUserAvatar.setText(_translate("IssueOrderForm", "👤"))
        self.lblDraftsTitle.setText(_translate("IssueOrderForm", "DRAFTS"))
        self.lblDraftsValue.setText(_translate("IssueOrderForm", "12 Pending"))
        self.lblCourtroomTitle.setText(_translate("IssueOrderForm", "COURTROOM"))
        self.lblCourtroomValue.setText(_translate("IssueOrderForm", "Room 4B"))
        self.lblOrderDetailsHeading.setText(_translate("IssueOrderForm", "Order Details"))
        self.lblCaseReference.setText(_translate("IssueOrderForm", "Select Case Reference"))
        self.comboCaseReference.setItemText(0, _translate("IssueOrderForm", "Choose a case..."))
        self.lblOrderText.setText(_translate("IssueOrderForm", "Judicial Instruction / Order Text"))
        self.txtOrderInstructions.setPlaceholderText(_translate("IssueOrderForm", "Type the final ruling or interim order instructions here..."))
        self.btnIssueOrder.setText(_translate("IssueOrderForm", "➤  Issue Order"))
        self.btnCancel.setText(_translate("IssueOrderForm", "Cancel"))


class Ui_JudgePanelWidget(object):
    def setupUi(self, JudgePanelWidget):
        JudgePanelWidget.setObjectName("JudgePanelWidget")
        JudgePanelWidget.resize(1280, 760)
        JudgePanelWidget.setStyleSheet("QWidget#JudgePanelWidget {\n"
"    background-color: #0c0f1a;\n"
"    color: #e6e8f0;\n"
"    font-family: \'Inter\';\n"
"}\n"
"QFrame#frameSidebar {\n"
"    background-color: #11141f;\n"
"    border-right: 1px solid #232737;\n"
"}\n"
"QLabel#labelWelcomeBack {\n"
"    color: #9aa3bd;\n"
"    font-size: 11px;\n"
"}\n"
"QLabel#labelLegalProfessional {\n"
"    color: #f0b429;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QToolButton.sidebarItem {\n"
"    background: transparent;\n"
"    color: #9aa3bd;\n"
"    text-align: left;\n"
"    padding: 10px 14px;\n"
"    font-size: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton#navDashboardBtn {\n"
"    background-color: #1c2030;\n"
"    color: #ffffff;\n"
"    text-align: left;\n"
"    padding: 10px 14px;\n"
"    font-size: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton#btnLogout {\n"
"    background: transparent;\n"
"    color: #9aa3bd;\n"
"    text-align: left;\n"
"    padding: 10px 14px;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel#labelPageWelcome {\n"
"    color: #f0b429;\n"
"    font-size: 20px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnDateBadge {\n"
"    background-color: #1c2030;\n"
"    color: #e6e8f0;\n"
"    border-radius: 14px;\n"
"    padding: 6px 16px;\n"
"    font-size: 11px;\n"
"}\n"
"QFrame#frameOverviewCard {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#labelOverviewTitle {\n"
"    color: #0c1230;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel.overviewFieldLabel {\n"
"    color: #6c7aa0;\n"
"    font-size: 11px;\n"
"}\n"
"QLabel#labelUpcomingHearingsValue, QLabel#labelRecentOrdersValue {\n"
"    color: #0c1230;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"}\n"
"QFrame#frameCourtSession {\n"
"    background-color: #16223d;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #233156;\n"
"}\n"
"QLabel#labelCourtSessionTitle {\n"
"    color: #f0b429;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelCourtSessionBody {\n"
"    color: #c7cee6;\n"
"    font-size: 11px;\n"
"}\n"
"QLabel#labelCriticalActionsHeader {\n"
"    color: #f0b429;\n"
"    font-size: 11px;\n"
"    font-weight: 700;\n"
"}\n"
"QFrame.actionCard {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel.actionCardTitle {\n"
"    color: #0c1230;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel.actionCardDesc {\n"
"    color: #6c7aa0;\n"
"    font-size: 10px;\n"
"}\n"
"QFrame#frameRecentActivity {\n"
"    background-color: #11141f;\n"
"    border: 1px solid #232737;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#labelRecentActivityTitle {\n"
"    color: #ffffff;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelSeeAllActivity {\n"
"    color: #f0b429;\n"
"    font-size: 11px;\n"
"}\n"
"QLabel.activityItemTitle {\n"
"    color: #e6e8f0;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel.activityItemTime {\n"
"    color: #6c7aa0;\n"
"    font-size: 10px;\n"
"}\n"
"QFrame#frameSecureLink {\n"
"    background-color: #16223d;\n"
"    border: 1px solid #233156;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#labelSecureLinkTitle {\n"
"    color: #ffffff;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelSecureLinkBody {\n"
"    color: #c7cee6;\n"
"    font-size: 11px;\n"
"}\n"
"QPushButton#btnSecurityProtocolDetails {\n"
"    background-color: #ffffff;\n"
"    color: #0c1230;\n"
"    border-radius: 6px;\n"
"    padding: 8px 14px;\n"
"    font-weight: 600;\n"
"    font-size: 11px;\n"
"}\n"
"")
        self.rootLayout = QtWidgets.QHBoxLayout(JudgePanelWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")
        self.frameSidebar = QtWidgets.QFrame(JudgePanelWidget)
        self.frameSidebar.setMinimumWidth(200)
        self.frameSidebar.setMaximumWidth(200)
        self.frameSidebar.setObjectName("frameSidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.frameSidebar)
        self.sidebarLayout.setContentsMargins(16, 20, 16, 20)
        self.sidebarLayout.setSpacing(4)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.labelWelcomeBack = QtWidgets.QLabel(self.frameSidebar)
        self.labelWelcomeBack.setObjectName("labelWelcomeBack")
        self.sidebarLayout.addWidget(self.labelWelcomeBack)
        self.labelLegalProfessional = QtWidgets.QLabel(self.frameSidebar)
        self.labelLegalProfessional.setObjectName("labelLegalProfessional")
        self.sidebarLayout.addWidget(self.labelLegalProfessional)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.navDashboardBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navDashboardBtn.setObjectName("navDashboardBtn")
        self.sidebarLayout.addWidget(self.navDashboardBtn)
        self.navCasesBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navCasesBtn.setObjectName("navCasesBtn")
        self.sidebarLayout.addWidget(self.navCasesBtn)
        self.navDocumentsBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navDocumentsBtn.setObjectName("navDocumentsBtn")
        self.sidebarLayout.addWidget(self.navDocumentsBtn)
        self.navMessagesBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navMessagesBtn.setObjectName("navMessagesBtn")
        self.sidebarLayout.addWidget(self.navMessagesBtn)
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem1)
        self.btnLogout = QtWidgets.QToolButton(self.frameSidebar)
        self.btnLogout.setObjectName("btnLogout")
        self.sidebarLayout.addWidget(self.btnLogout)
        self.rootLayout.addWidget(self.frameSidebar)
        self.contentLayout = QtWidgets.QVBoxLayout()
        self.contentLayout.setContentsMargins(28, 22, 28, 22)
        self.contentLayout.setSpacing(18)
        self.contentLayout.setObjectName("contentLayout")
        self.headerRowLayout = QtWidgets.QHBoxLayout()
        self.headerRowLayout.setObjectName("headerRowLayout")
        self.labelPageWelcome = QtWidgets.QLabel(JudgePanelWidget)
        self.labelPageWelcome.setObjectName("labelPageWelcome")
        self.headerRowLayout.addWidget(self.labelPageWelcome)
        spacerItem2 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerRowLayout.addItem(spacerItem2)
        self.btnDateBadge = QtWidgets.QPushButton(JudgePanelWidget)
        self.btnDateBadge.setObjectName("btnDateBadge")
        self.headerRowLayout.addWidget(self.btnDateBadge)
        self.btnUserAvatar = QtWidgets.QToolButton(JudgePanelWidget)
        self.btnUserAvatar.setObjectName("btnUserAvatar")
        self.headerRowLayout.addWidget(self.btnUserAvatar)
        self.contentLayout.addLayout(self.headerRowLayout)
        self.overviewRowLayout = QtWidgets.QHBoxLayout()
        self.overviewRowLayout.setSpacing(16)
        self.overviewRowLayout.setObjectName("overviewRowLayout")
        self.frameOverviewCard = QtWidgets.QFrame(JudgePanelWidget)
        self.frameOverviewCard.setObjectName("frameOverviewCard")
        self.overviewCardLayout = QtWidgets.QVBoxLayout(self.frameOverviewCard)
        self.overviewCardLayout.setContentsMargins(18, 16, 18, 16)
        self.overviewCardLayout.setObjectName("overviewCardLayout")
        self.labelOverviewTitle = QtWidgets.QLabel(self.frameOverviewCard)
        self.labelOverviewTitle.setObjectName("labelOverviewTitle")
        self.overviewCardLayout.addWidget(self.labelOverviewTitle)
        self.upcomingHearingsRowLayout = QtWidgets.QHBoxLayout()
        self.upcomingHearingsRowLayout.setObjectName("upcomingHearingsRowLayout")
        self.labelUpcomingHearingsLabel = QtWidgets.QLabel(self.frameOverviewCard)
        self.labelUpcomingHearingsLabel.setObjectName("labelUpcomingHearingsLabel")
        self.upcomingHearingsRowLayout.addWidget(self.labelUpcomingHearingsLabel)
        spacerItem3 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upcomingHearingsRowLayout.addItem(spacerItem3)
        self.labelUpcomingHearingsValue = QtWidgets.QLabel(self.frameOverviewCard)
        self.labelUpcomingHearingsValue.setObjectName("labelUpcomingHearingsValue")
        self.upcomingHearingsRowLayout.addWidget(self.labelUpcomingHearingsValue)
        self.overviewCardLayout.addLayout(self.upcomingHearingsRowLayout)
        self.recentOrdersRowLayout = QtWidgets.QHBoxLayout()
        self.recentOrdersRowLayout.setObjectName("recentOrdersRowLayout")
        self.labelRecentOrdersLabel = QtWidgets.QLabel(self.frameOverviewCard)
        self.labelRecentOrdersLabel.setObjectName("labelRecentOrdersLabel")
        self.recentOrdersRowLayout.addWidget(self.labelRecentOrdersLabel)
        spacerItem4 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recentOrdersRowLayout.addItem(spacerItem4)
        self.labelRecentOrdersValue = QtWidgets.QLabel(self.frameOverviewCard)
        self.labelRecentOrdersValue.setObjectName("labelRecentOrdersValue")
        self.recentOrdersRowLayout.addWidget(self.labelRecentOrdersValue)
        self.overviewCardLayout.addLayout(self.recentOrdersRowLayout)
        self.overviewRowLayout.addWidget(self.frameOverviewCard)
        self.frameCourtSession = QtWidgets.QFrame(JudgePanelWidget)
        self.frameCourtSession.setObjectName("frameCourtSession")
        self.courtSessionLayout = QtWidgets.QVBoxLayout(self.frameCourtSession)
        self.courtSessionLayout.setContentsMargins(18, 16, 18, 16)
        self.courtSessionLayout.setObjectName("courtSessionLayout")
        self.labelCourtSessionTitle = QtWidgets.QLabel(self.frameCourtSession)
        self.labelCourtSessionTitle.setObjectName("labelCourtSessionTitle")
        self.courtSessionLayout.addWidget(self.labelCourtSessionTitle)
        self.labelCourtSessionBody = QtWidgets.QLabel(self.frameCourtSession)
        self.labelCourtSessionBody.setWordWrap(True)
        self.labelCourtSessionBody.setObjectName("labelCourtSessionBody")
        self.courtSessionLayout.addWidget(self.labelCourtSessionBody)
        self.overviewRowLayout.addWidget(self.frameCourtSession)
        self.contentLayout.addLayout(self.overviewRowLayout)
        self.labelCriticalActionsHeader = QtWidgets.QLabel(JudgePanelWidget)
        self.labelCriticalActionsHeader.setObjectName("labelCriticalActionsHeader")
        self.contentLayout.addWidget(self.labelCriticalActionsHeader)
        self.actionsRowLayout = QtWidgets.QHBoxLayout()
        self.actionsRowLayout.setSpacing(16)
        self.actionsRowLayout.setObjectName("actionsRowLayout")
        self.cardViewCases = QtWidgets.QFrame(JudgePanelWidget)
        self.cardViewCases.setStyleSheet("background-color:#ffffff;border-radius:10px;")
        self.cardViewCases.setObjectName("cardViewCases")
        self.cardViewCasesLayout = QtWidgets.QVBoxLayout(self.cardViewCases)
        self.cardViewCasesLayout.setContentsMargins(16, 14, 16, 14)
        self.cardViewCasesLayout.setObjectName("cardViewCasesLayout")
        self.iconViewCases = QtWidgets.QLabel(self.cardViewCases)
        self.iconViewCases.setObjectName("iconViewCases")
        self.cardViewCasesLayout.addWidget(self.iconViewCases)
        self.labelViewCasesTitle = QtWidgets.QLabel(self.cardViewCases)
        self.labelViewCasesTitle.setObjectName("labelViewCasesTitle")
        self.cardViewCasesLayout.addWidget(self.labelViewCasesTitle)
        self.labelViewCasesDesc = QtWidgets.QLabel(self.cardViewCases)
        self.labelViewCasesDesc.setWordWrap(True)
        self.labelViewCasesDesc.setObjectName("labelViewCasesDesc")
        self.cardViewCasesLayout.addWidget(self.labelViewCasesDesc)
        self.actionsRowLayout.addWidget(self.cardViewCases)
        self.cardScheduleHearing = QtWidgets.QFrame(JudgePanelWidget)
        self.cardScheduleHearing.setStyleSheet("background-color:#ffffff;border-radius:10px;")
        self.cardScheduleHearing.setObjectName("cardScheduleHearing")
        self.cardScheduleHearingLayout = QtWidgets.QVBoxLayout(self.cardScheduleHearing)
        self.cardScheduleHearingLayout.setContentsMargins(16, 14, 16, 14)
        self.cardScheduleHearingLayout.setObjectName("cardScheduleHearingLayout")
        self.iconScheduleHearing = QtWidgets.QLabel(self.cardScheduleHearing)
        self.iconScheduleHearing.setObjectName("iconScheduleHearing")
        self.cardScheduleHearingLayout.addWidget(self.iconScheduleHearing)
        self.labelScheduleHearingTitle = QtWidgets.QLabel(self.cardScheduleHearing)
        self.labelScheduleHearingTitle.setObjectName("labelScheduleHearingTitle")
        self.cardScheduleHearingLayout.addWidget(self.labelScheduleHearingTitle)
        self.labelScheduleHearingDesc = QtWidgets.QLabel(self.cardScheduleHearing)
        self.labelScheduleHearingDesc.setWordWrap(True)
        self.labelScheduleHearingDesc.setObjectName("labelScheduleHearingDesc")
        self.cardScheduleHearingLayout.addWidget(self.labelScheduleHearingDesc)
        self.actionsRowLayout.addWidget(self.cardScheduleHearing)
        self.cardIssueOrder = QtWidgets.QFrame(JudgePanelWidget)
        self.cardIssueOrder.setStyleSheet("background-color:#ffffff;border-radius:10px;")
        self.cardIssueOrder.setObjectName("cardIssueOrder")
        self.cardIssueOrderLayout = QtWidgets.QVBoxLayout(self.cardIssueOrder)
        self.cardIssueOrderLayout.setContentsMargins(16, 14, 16, 14)
        self.cardIssueOrderLayout.setObjectName("cardIssueOrderLayout")
        self.iconIssueOrder = QtWidgets.QLabel(self.cardIssueOrder)
        self.iconIssueOrder.setObjectName("iconIssueOrder")
        self.cardIssueOrderLayout.addWidget(self.iconIssueOrder)
        self.labelIssueOrderTitle = QtWidgets.QLabel(self.cardIssueOrder)
        self.labelIssueOrderTitle.setObjectName("labelIssueOrderTitle")
        self.cardIssueOrderLayout.addWidget(self.labelIssueOrderTitle)
        self.labelIssueOrderDesc = QtWidgets.QLabel(self.cardIssueOrder)
        self.labelIssueOrderDesc.setWordWrap(True)
        self.labelIssueOrderDesc.setObjectName("labelIssueOrderDesc")
        self.cardIssueOrderLayout.addWidget(self.labelIssueOrderDesc)
        self.actionsRowLayout.addWidget(self.cardIssueOrder)
        self.cardCaseDetails = QtWidgets.QFrame(JudgePanelWidget)
        self.cardCaseDetails.setStyleSheet("background-color:#ffffff;border-radius:10px;")
        self.cardCaseDetails.setObjectName("cardCaseDetails")
        self.cardCaseDetailsLayout = QtWidgets.QVBoxLayout(self.cardCaseDetails)
        self.cardCaseDetailsLayout.setContentsMargins(16, 14, 16, 14)
        self.cardCaseDetailsLayout.setObjectName("cardCaseDetailsLayout")
        self.iconCaseDetails = QtWidgets.QLabel(self.cardCaseDetails)
        self.iconCaseDetails.setObjectName("iconCaseDetails")
        self.cardCaseDetailsLayout.addWidget(self.iconCaseDetails)
        self.labelCaseDetailsTitle = QtWidgets.QLabel(self.cardCaseDetails)
        self.labelCaseDetailsTitle.setObjectName("labelCaseDetailsTitle")
        self.cardCaseDetailsLayout.addWidget(self.labelCaseDetailsTitle)
        self.labelCaseDetailsDesc = QtWidgets.QLabel(self.cardCaseDetails)
        self.labelCaseDetailsDesc.setWordWrap(True)
        self.labelCaseDetailsDesc.setObjectName("labelCaseDetailsDesc")
        self.cardCaseDetailsLayout.addWidget(self.labelCaseDetailsDesc)
        self.actionsRowLayout.addWidget(self.cardCaseDetails)
        self.contentLayout.addLayout(self.actionsRowLayout)
        self.bottomRowLayout = QtWidgets.QHBoxLayout()
        self.bottomRowLayout.setSpacing(16)
        self.bottomRowLayout.setObjectName("bottomRowLayout")
        self.frameRecentActivity = QtWidgets.QFrame(JudgePanelWidget)
        self.frameRecentActivity.setObjectName("frameRecentActivity")
        self.recentActivityLayout = QtWidgets.QVBoxLayout(self.frameRecentActivity)
        self.recentActivityLayout.setContentsMargins(18, 16, 18, 16)
        self.recentActivityLayout.setObjectName("recentActivityLayout")
        self.recentActivityHeaderLayout = QtWidgets.QHBoxLayout()
        self.recentActivityHeaderLayout.setObjectName("recentActivityHeaderLayout")
        self.labelRecentActivityTitle = QtWidgets.QLabel(self.frameRecentActivity)
        self.labelRecentActivityTitle.setObjectName("labelRecentActivityTitle")
        self.recentActivityHeaderLayout.addWidget(self.labelRecentActivityTitle)
        spacerItem5 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recentActivityHeaderLayout.addItem(spacerItem5)
        self.labelSeeAllActivity = QtWidgets.QLabel(self.frameRecentActivity)
        self.labelSeeAllActivity.setObjectName("labelSeeAllActivity")
        self.recentActivityHeaderLayout.addWidget(self.labelSeeAllActivity)
        self.recentActivityLayout.addLayout(self.recentActivityHeaderLayout)
        self.listRecentActivity = QtWidgets.QListWidget(self.frameRecentActivity)
        self.listRecentActivity.setObjectName("listRecentActivity")
        item = QtWidgets.QListWidgetItem()
        self.listRecentActivity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listRecentActivity.addItem(item)
        self.recentActivityLayout.addWidget(self.listRecentActivity)
        self.bottomRowLayout.addWidget(self.frameRecentActivity)
        self.frameSecureLink = QtWidgets.QFrame(JudgePanelWidget)
        self.frameSecureLink.setMinimumWidth(280)
        self.frameSecureLink.setMaximumWidth(280)
        self.frameSecureLink.setObjectName("frameSecureLink")
        self.secureLinkLayout = QtWidgets.QVBoxLayout(self.frameSecureLink)
        self.secureLinkLayout.setContentsMargins(18, 16, 18, 16)
        self.secureLinkLayout.setObjectName("secureLinkLayout")
        self.labelSecureLinkTitle = QtWidgets.QLabel(self.frameSecureLink)
        self.labelSecureLinkTitle.setObjectName("labelSecureLinkTitle")
        self.secureLinkLayout.addWidget(self.labelSecureLinkTitle)
        self.labelSecureLinkBody = QtWidgets.QLabel(self.frameSecureLink)
        self.labelSecureLinkBody.setWordWrap(True)
        self.labelSecureLinkBody.setObjectName("labelSecureLinkBody")
        self.secureLinkLayout.addWidget(self.labelSecureLinkBody)
        self.btnSecurityProtocolDetails = QtWidgets.QPushButton(self.frameSecureLink)
        self.btnSecurityProtocolDetails.setObjectName("btnSecurityProtocolDetails")
        self.secureLinkLayout.addWidget(self.btnSecurityProtocolDetails)
        self.bottomRowLayout.addWidget(self.frameSecureLink)
        self.contentLayout.addLayout(self.bottomRowLayout)
        self.rootLayout.addLayout(self.contentLayout)

        self.retranslateUi(JudgePanelWidget)
        QtCore.QMetaObject.connectSlotsByName(JudgePanelWidget)

    def retranslateUi(self, JudgePanelWidget):
        _translate = QtCore.QCoreApplication.translate
        JudgePanelWidget.setWindowTitle(_translate("JudgePanelWidget", "Judge Dashboard"))
        self.labelWelcomeBack.setText(_translate("JudgePanelWidget", "Welcome Back"))
        self.labelLegalProfessional.setText(_translate("JudgePanelWidget", "Legal Professional"))
        self.navDashboardBtn.setText(_translate("JudgePanelWidget", "Dashboard"))
        self.navCasesBtn.setText(_translate("JudgePanelWidget", "Cases"))
        self.navDocumentsBtn.setText(_translate("JudgePanelWidget", "Documents"))
        self.navMessagesBtn.setText(_translate("JudgePanelWidget", "Messages"))
        self.btnLogout.setText(_translate("JudgePanelWidget", "Logout"))
        self.labelPageWelcome.setText(_translate("JudgePanelWidget", "Welcome, Judge Alexander"))
        self.btnDateBadge.setText(_translate("JudgePanelWidget", "📅 Oct 24, 2023"))
        self.btnUserAvatar.setText(_translate("JudgePanelWidget", "👤"))
        self.labelOverviewTitle.setText(_translate("JudgePanelWidget", "Today\'s Overview"))
        self.labelUpcomingHearingsLabel.setText(_translate("JudgePanelWidget", "Upcoming Hearings"))
        self.labelUpcomingHearingsValue.setText(_translate("JudgePanelWidget", "5"))
        self.labelRecentOrdersLabel.setText(_translate("JudgePanelWidget", "Recent Orders"))
        self.labelRecentOrdersValue.setText(_translate("JudgePanelWidget", "2"))
        self.labelCourtSessionTitle.setText(_translate("JudgePanelWidget", "Court in Session"))
        self.labelCourtSessionBody.setText(_translate("JudgePanelWidget", "The 4th Circuit digital portal is active. You have 3 pending decisions requiring signature before 5:00 PM."))
        self.labelCriticalActionsHeader.setText(_translate("JudgePanelWidget", "CRITICAL ACTIONS"))
        self.iconViewCases.setText(_translate("JudgePanelWidget", "📁"))
        self.labelViewCasesTitle.setText(_translate("JudgePanelWidget", "View Cases"))
        self.labelViewCasesDesc.setText(_translate("JudgePanelWidget", "Review active litigation dockets."))
        self.iconScheduleHearing.setText(_translate("JudgePanelWidget", "📅"))
        self.labelScheduleHearingTitle.setText(_translate("JudgePanelWidget", "Schedule Hearing"))
        self.labelScheduleHearingDesc.setText(_translate("JudgePanelWidget", "Coordinate session availability."))
        self.iconIssueOrder.setText(_translate("JudgePanelWidget", "📝"))
        self.labelIssueOrderTitle.setText(_translate("JudgePanelWidget", "Issue Order"))
        self.labelIssueOrderDesc.setText(_translate("JudgePanelWidget", "Draft and sign judicial directives."))
        self.iconCaseDetails.setText(_translate("JudgePanelWidget", "🔎"))
        self.labelCaseDetailsTitle.setText(_translate("JudgePanelWidget", "Case Details"))
        self.labelCaseDetailsDesc.setText(_translate("JudgePanelWidget", "Deep dive into specific files."))
        self.labelRecentActivityTitle.setText(_translate("JudgePanelWidget", "Recent Activity"))
        self.labelSeeAllActivity.setText(_translate("JudgePanelWidget", "See all activity"))
        __sortingEnabled = self.listRecentActivity.isSortingEnabled()
        self.listRecentActivity.setSortingEnabled(False)
        item = self.listRecentActivity.item(0)
        item.setText(_translate("JudgePanelWidget", "Order signed: Case #4421-B\n"
"9 hours ago"))
        item = self.listRecentActivity.item(1)
        item.setText(_translate("JudgePanelWidget", "Hearing rescheduled: Doe vs. Global Corp\n"
"Yesterday at 4:15 PM"))
        self.listRecentActivity.setSortingEnabled(__sortingEnabled)
        self.labelSecureLinkTitle.setText(_translate("JudgePanelWidget", "🛡  Secure Link Active"))
        self.labelSecureLinkBody.setText(_translate("JudgePanelWidget", "Your session is protected by end-to-end encryption and 2FA protocols."))
        self.btnSecurityProtocolDetails.setText(_translate("JudgePanelWidget", "Security Protocol Details"))


class Ui_LawyerPanelWidget(object):
    def setupUi(self, LawyerPanelWidget):
        LawyerPanelWidget.setObjectName("LawyerPanelWidget")
        LawyerPanelWidget.resize(1280, 760)
        LawyerPanelWidget.setStyleSheet("QWidget#LawyerPanelWidget {\n"
"    background-color: #0c0f1a;\n"
"    color: #e6e8f0;\n"
"    font-family: \'Inter\';\n"
"    border: 2px solid #5b46e0;\n"
"    border-radius: 10px;\n"
"}\n"
"QFrame#frameSidebar {\n"
"    background-color: #11141f;\n"
"    border-right: 1px solid #232737;\n"
"}\n"
"QLabel#labelWelcomeBack {\n"
"    color: #9aa3bd;\n"
"    font-size: 11px;\n"
"}\n"
"QLabel#labelLegalProfessional {\n"
"    color: #f0b429;\n"
"    font-size: 12px;\n"
"    font-weight: 700;\n"
"}\n"
"QToolButton.sidebarItem {\n"
"    background: transparent;\n"
"    color: #9aa3bd;\n"
"    text-align: left;\n"
"    padding: 10px 14px;\n"
"    font-size: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton#navDashboardBtn {\n"
"    background-color: #1c2030;\n"
"    color: #ffffff;\n"
"    text-align: left;\n"
"    padding: 10px 14px;\n"
"    font-size: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"QToolButton#btnLogout {\n"
"    background: transparent;\n"
"    color: #9aa3bd;\n"
"    text-align: left;\n"
"    padding: 10px 14px;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel#labelPageWelcome {\n"
"    color: #ffffff;\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelSystemStatus {\n"
"    color: #6c7aa0;\n"
"    font-size: 10px;\n"
"}\n"
"QLabel#labelSystemStatusActive {\n"
"    color: #22c55e;\n"
"    font-size: 10px;\n"
"    font-weight: 700;\n"
"}\n"
"QPushButton#btnLogoutTop {\n"
"    background-color: #2b59ff;\n"
"    color: #ffffff;\n"
"    border-radius: 14px;\n"
"    padding: 6px 18px;\n"
"    font-size: 11px;\n"
"    font-weight: 600;\n"
"}\n"
"QFrame#frameMyCasesCard {\n"
"    background-color: #ffffff;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel#labelMyCasesTitle {\n"
"    color: #0c1230;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelMyCasesSubtitle {\n"
"    color: #6c7aa0;\n"
"    font-size: 10px;\n"
"}\n"
"QLabel#labelMyCasesValue {\n"
"    color: #2b59ff;\n"
"    font-size: 36px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelViewAll {\n"
"    color: #2b59ff;\n"
"    font-size: 11px;\n"
"    font-weight: 600;\n"
"}\n"
"QFrame#frameDocketOverview {\n"
"    background-color: #161a2c;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #232737;\n"
"}\n"
"QLabel#labelDocketOverviewTitle {\n"
"    color: #ffffff;\n"
"    font-size: 15px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel#labelDocketOverviewBody {\n"
"    color: #b7bedd;\n"
"    font-size: 12px;\n"
"}\n"
"QLabel#labelQuickActionsHeader {\n"
"    color: #ffffff;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"QFrame.quickActionCard {\n"
"    background-color: #161a2c;\n"
"    border: 1px solid #232737;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel.quickActionIconCircle {\n"
"    background-color: #1f2438;\n"
"    border-radius: 20px;\n"
"    font-size: 16px;\n"
"}\n"
"QLabel.quickActionTitle {\n"
"    color: #ffffff;\n"
"    font-size: 13px;\n"
"    font-weight: 700;\n"
"}\n"
"QLabel.quickActionDesc {\n"
"    color: #8a92ab;\n"
"    font-size: 10px;\n"
"}\n"
"QLabel#iconFileCase {\n"
"    color: #2b59ff;\n"
"}\n"
"QLabel#iconSearchCase {\n"
"    color: #f0b429;\n"
"}\n"
"QLabel#iconTrackCase {\n"
"    color: #22c55e;\n"
"}\n"
"")
        self.rootLayout = QtWidgets.QHBoxLayout(LawyerPanelWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")
        self.frameSidebar = QtWidgets.QFrame(LawyerPanelWidget)
        self.frameSidebar.setMinimumWidth(200)
        self.frameSidebar.setMaximumWidth(200)
        self.frameSidebar.setObjectName("frameSidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.frameSidebar)
        self.sidebarLayout.setContentsMargins(16, 20, 16, 20)
        self.sidebarLayout.setSpacing(4)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.labelWelcomeBack = QtWidgets.QLabel(self.frameSidebar)
        self.labelWelcomeBack.setObjectName("labelWelcomeBack")
        self.sidebarLayout.addWidget(self.labelWelcomeBack)
        self.labelLegalProfessional = QtWidgets.QLabel(self.frameSidebar)
        self.labelLegalProfessional.setObjectName("labelLegalProfessional")
        self.sidebarLayout.addWidget(self.labelLegalProfessional)
        spacerItem = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.navDashboardBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navDashboardBtn.setObjectName("navDashboardBtn")
        self.sidebarLayout.addWidget(self.navDashboardBtn)
        self.navCasesBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navCasesBtn.setObjectName("navCasesBtn")
        self.sidebarLayout.addWidget(self.navCasesBtn)
        self.navDocumentsBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navDocumentsBtn.setObjectName("navDocumentsBtn")
        self.sidebarLayout.addWidget(self.navDocumentsBtn)
        self.navMessagesBtn = QtWidgets.QToolButton(self.frameSidebar)
        self.navMessagesBtn.setObjectName("navMessagesBtn")
        self.sidebarLayout.addWidget(self.navMessagesBtn)
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem1)
        self.btnLogout = QtWidgets.QToolButton(self.frameSidebar)
        self.btnLogout.setObjectName("btnLogout")
        self.sidebarLayout.addWidget(self.btnLogout)
        self.rootLayout.addWidget(self.frameSidebar)
        self.contentLayout = QtWidgets.QVBoxLayout()
        self.contentLayout.setContentsMargins(28, 22, 28, 22)
        self.contentLayout.setSpacing(18)
        self.contentLayout.setObjectName("contentLayout")
        self.headerRowLayout = QtWidgets.QHBoxLayout()
        self.headerRowLayout.setObjectName("headerRowLayout")
        self.labelPageWelcome = QtWidgets.QLabel(LawyerPanelWidget)
        self.labelPageWelcome.setObjectName("labelPageWelcome")
        self.headerRowLayout.addWidget(self.labelPageWelcome)
        spacerItem2 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerRowLayout.addItem(spacerItem2)
        self.labelSystemStatus = QtWidgets.QLabel(LawyerPanelWidget)
        self.labelSystemStatus.setObjectName("labelSystemStatus")
        self.headerRowLayout.addWidget(self.labelSystemStatus)
        self.labelSystemStatusActive = QtWidgets.QLabel(LawyerPanelWidget)
        self.labelSystemStatusActive.setObjectName("labelSystemStatusActive")
        self.headerRowLayout.addWidget(self.labelSystemStatusActive)
        self.btnLogoutTop = QtWidgets.QPushButton(LawyerPanelWidget)
        self.btnLogoutTop.setObjectName("btnLogoutTop")
        self.headerRowLayout.addWidget(self.btnLogoutTop)
        self.contentLayout.addLayout(self.headerRowLayout)
        self.overviewRowLayout = QtWidgets.QHBoxLayout()
        self.overviewRowLayout.setSpacing(16)
        self.overviewRowLayout.setObjectName("overviewRowLayout")
        self.frameMyCasesCard = QtWidgets.QFrame(LawyerPanelWidget)
        self.frameMyCasesCard.setMinimumWidth(260)
        self.frameMyCasesCard.setMaximumWidth(260)
        self.frameMyCasesCard.setObjectName("frameMyCasesCard")
        self.myCasesCardLayout = QtWidgets.QVBoxLayout(self.frameMyCasesCard)
        self.myCasesCardLayout.setContentsMargins(18, 16, 18, 16)
        self.myCasesCardLayout.setObjectName("myCasesCardLayout")
        self.myCasesTitleRowLayout = QtWidgets.QHBoxLayout()
        self.myCasesTitleRowLayout.setObjectName("myCasesTitleRowLayout")
        self.labelMyCasesTitle = QtWidgets.QLabel(self.frameMyCasesCard)
        self.labelMyCasesTitle.setObjectName("labelMyCasesTitle")
        self.myCasesTitleRowLayout.addWidget(self.labelMyCasesTitle)
        spacerItem3 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.myCasesTitleRowLayout.addItem(spacerItem3)
        self.iconMyCasesFolder = QtWidgets.QLabel(self.frameMyCasesCard)
        self.iconMyCasesFolder.setObjectName("iconMyCasesFolder")
        self.myCasesTitleRowLayout.addWidget(self.iconMyCasesFolder)
        self.myCasesCardLayout.addLayout(self.myCasesTitleRowLayout)
        self.labelMyCasesSubtitle = QtWidgets.QLabel(self.frameMyCasesCard)
        self.labelMyCasesSubtitle.setObjectName("labelMyCasesSubtitle")
        self.myCasesCardLayout.addWidget(self.labelMyCasesSubtitle)
        self.labelMyCasesValue = QtWidgets.QLabel(self.frameMyCasesCard)
        self.labelMyCasesValue.setObjectName("labelMyCasesValue")
        self.myCasesCardLayout.addWidget(self.labelMyCasesValue)
        self.labelViewAll = QtWidgets.QLabel(self.frameMyCasesCard)
        self.labelViewAll.setObjectName("labelViewAll")
        self.myCasesCardLayout.addWidget(self.labelViewAll)
        self.overviewRowLayout.addWidget(self.frameMyCasesCard)
        self.frameDocketOverview = QtWidgets.QFrame(LawyerPanelWidget)
        self.frameDocketOverview.setObjectName("frameDocketOverview")
        self.docketOverviewLayout = QtWidgets.QVBoxLayout(self.frameDocketOverview)
        self.docketOverviewLayout.setContentsMargins(20, 18, 20, 18)
        self.docketOverviewLayout.setObjectName("docketOverviewLayout")
        self.labelDocketOverviewTitle = QtWidgets.QLabel(self.frameDocketOverview)
        self.labelDocketOverviewTitle.setObjectName("labelDocketOverviewTitle")
        self.docketOverviewLayout.addWidget(self.labelDocketOverviewTitle)
        self.labelDocketOverviewBody = QtWidgets.QLabel(self.frameDocketOverview)
        self.labelDocketOverviewBody.setWordWrap(True)
        self.labelDocketOverviewBody.setObjectName("labelDocketOverviewBody")
        self.docketOverviewLayout.addWidget(self.labelDocketOverviewBody)
        self.overviewRowLayout.addWidget(self.frameDocketOverview)
        self.contentLayout.addLayout(self.overviewRowLayout)
        self.labelQuickActionsHeader = QtWidgets.QLabel(LawyerPanelWidget)
        self.labelQuickActionsHeader.setObjectName("labelQuickActionsHeader")
        self.contentLayout.addWidget(self.labelQuickActionsHeader)
        self.quickActionsRowLayout = QtWidgets.QHBoxLayout()
        self.quickActionsRowLayout.setSpacing(16)
        self.quickActionsRowLayout.setObjectName("quickActionsRowLayout")
        self.cardFileCase = QtWidgets.QFrame(LawyerPanelWidget)
        self.cardFileCase.setStyleSheet("background-color:#161a2c;border:1px solid #232737;border-radius:10px;")
        self.cardFileCase.setObjectName("cardFileCase")
        self.cardFileCaseLayout = QtWidgets.QVBoxLayout(self.cardFileCase)
        self.cardFileCaseLayout.setContentsMargins(16, 16, 16, 16)
        self.cardFileCaseLayout.setObjectName("cardFileCaseLayout")
        self.iconFileCase = QtWidgets.QLabel(self.cardFileCase)
        self.iconFileCase.setObjectName("iconFileCase")
        self.cardFileCaseLayout.addWidget(self.iconFileCase)
        self.labelFileCaseTitle = QtWidgets.QLabel(self.cardFileCase)
        self.labelFileCaseTitle.setObjectName("labelFileCaseTitle")
        self.cardFileCaseLayout.addWidget(self.labelFileCaseTitle)
        self.labelFileCaseDesc = QtWidgets.QLabel(self.cardFileCase)
        self.labelFileCaseDesc.setWordWrap(True)
        self.labelFileCaseDesc.setObjectName("labelFileCaseDesc")
        self.cardFileCaseLayout.addWidget(self.labelFileCaseDesc)
        self.quickActionsRowLayout.addWidget(self.cardFileCase)
        self.cardSearchCase = QtWidgets.QFrame(LawyerPanelWidget)
        self.cardSearchCase.setStyleSheet("background-color:#161a2c;border:1px solid #232737;border-radius:10px;")
        self.cardSearchCase.setObjectName("cardSearchCase")
        self.cardSearchCaseLayout = QtWidgets.QVBoxLayout(self.cardSearchCase)
        self.cardSearchCaseLayout.setContentsMargins(16, 16, 16, 16)
        self.cardSearchCaseLayout.setObjectName("cardSearchCaseLayout")
        self.iconSearchCase = QtWidgets.QLabel(self.cardSearchCase)
        self.iconSearchCase.setObjectName("iconSearchCase")
        self.cardSearchCaseLayout.addWidget(self.iconSearchCase)
        self.labelSearchCaseTitle = QtWidgets.QLabel(self.cardSearchCase)
        self.labelSearchCaseTitle.setObjectName("labelSearchCaseTitle")
        self.cardSearchCaseLayout.addWidget(self.labelSearchCaseTitle)
        self.labelSearchCaseDesc = QtWidgets.QLabel(self.cardSearchCase)
        self.labelSearchCaseDesc.setWordWrap(True)
        self.labelSearchCaseDesc.setObjectName("labelSearchCaseDesc")
        self.cardSearchCaseLayout.addWidget(self.labelSearchCaseDesc)
        self.quickActionsRowLayout.addWidget(self.cardSearchCase)
        self.cardTrackCase = QtWidgets.QFrame(LawyerPanelWidget)
        self.cardTrackCase.setStyleSheet("background-color:#161a2c;border:1px solid #232737;border-radius:10px;")
        self.cardTrackCase.setObjectName("cardTrackCase")
        self.cardTrackCaseLayout = QtWidgets.QVBoxLayout(self.cardTrackCase)
        self.cardTrackCaseLayout.setContentsMargins(16, 16, 16, 16)
        self.cardTrackCaseLayout.setObjectName("cardTrackCaseLayout")
        self.iconTrackCase = QtWidgets.QLabel(self.cardTrackCase)
        self.iconTrackCase.setObjectName("iconTrackCase")
        self.cardTrackCaseLayout.addWidget(self.iconTrackCase)
        self.labelTrackCaseTitle = QtWidgets.QLabel(self.cardTrackCase)
        self.labelTrackCaseTitle.setObjectName("labelTrackCaseTitle")
        self.cardTrackCaseLayout.addWidget(self.labelTrackCaseTitle)
        self.labelTrackCaseDesc = QtWidgets.QLabel(self.cardTrackCase)
        self.labelTrackCaseDesc.setWordWrap(True)
        self.labelTrackCaseDesc.setObjectName("labelTrackCaseDesc")
        self.cardTrackCaseLayout.addWidget(self.labelTrackCaseDesc)
        self.quickActionsRowLayout.addWidget(self.cardTrackCase)
        self.contentLayout.addLayout(self.quickActionsRowLayout)
        spacerItem4 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.contentLayout.addItem(spacerItem4)
        self.rootLayout.addLayout(self.contentLayout)

        self.retranslateUi(LawyerPanelWidget)
        QtCore.QMetaObject.connectSlotsByName(LawyerPanelWidget)

    def retranslateUi(self, LawyerPanelWidget):
        _translate = QtCore.QCoreApplication.translate
        LawyerPanelWidget.setWindowTitle(_translate("LawyerPanelWidget", "Lawyer Dashboard"))
        self.labelWelcomeBack.setText(_translate("LawyerPanelWidget", "Welcome Back"))
        self.labelLegalProfessional.setText(_translate("LawyerPanelWidget", "Legal Professional"))
        self.navDashboardBtn.setText(_translate("LawyerPanelWidget", "Dashboard"))
        self.navCasesBtn.setText(_translate("LawyerPanelWidget", "Cases"))
        self.navDocumentsBtn.setText(_translate("LawyerPanelWidget", "Documents"))
        self.navMessagesBtn.setText(_translate("LawyerPanelWidget", "Messages"))
        self.btnLogout.setText(_translate("LawyerPanelWidget", "Logout"))
        self.labelPageWelcome.setText(_translate("LawyerPanelWidget", "Welcome, Lawyer Alexander"))
        self.labelSystemStatus.setText(_translate("LawyerPanelWidget", "SYSTEM STATUS:"))
        self.labelSystemStatusActive.setText(_translate("LawyerPanelWidget", "ACTIVE"))
        self.btnLogoutTop.setText(_translate("LawyerPanelWidget", "Logout"))
        self.labelMyCasesTitle.setText(_translate("LawyerPanelWidget", "My Cases"))
        self.iconMyCasesFolder.setText(_translate("LawyerPanelWidget", "📁"))
        self.labelMyCasesSubtitle.setText(_translate("LawyerPanelWidget", "Total active case files"))
        self.labelMyCasesValue.setText(_translate("LawyerPanelWidget", "12"))
        self.labelViewAll.setText(_translate("LawyerPanelWidget", "View All →"))
        self.labelDocketOverviewTitle.setText(_translate("LawyerPanelWidget", "Docket Overview"))
        self.labelDocketOverviewBody.setText(_translate("LawyerPanelWidget", "You have 5 hearings scheduled for today and 2 pending document approvals. Your efficiency score is up by 12% this month."))
        self.labelQuickActionsHeader.setText(_translate("LawyerPanelWidget", "Quick Actions"))
        self.iconFileCase.setText(_translate("LawyerPanelWidget", "⊕"))
        self.labelFileCaseTitle.setText(_translate("LawyerPanelWidget", "File Case"))
        self.labelFileCaseDesc.setText(_translate("LawyerPanelWidget", "Initiate a new legal proceeding."))
        self.iconSearchCase.setText(_translate("LawyerPanelWidget", "🔍"))
        self.labelSearchCaseTitle.setText(_translate("LawyerPanelWidget", "Search Case"))
        self.labelSearchCaseDesc.setText(_translate("LawyerPanelWidget", "Find existing records in the archive."))
        self.iconTrackCase.setText(_translate("LawyerPanelWidget", "📍"))
        self.labelTrackCaseTitle.setText(_translate("LawyerPanelWidget", "Track Case"))
        self.labelTrackCaseDesc.setText(_translate("LawyerPanelWidget", "Real-time status of active dockets."))


class Ui_ReportsWidget(object):
    def setupUi(self, ReportsWidget):
        ReportsWidget.setObjectName("ReportsWidget")
        ReportsWidget.resize(1280, 800)
        ReportsWidget.setStyleSheet("\n"
"    QWidget#ReportsWidget {\n"
"        background-color: #0f1b2d;\n"
"        color: #ffffff;\n"
"        font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    }\n"
"    QWidget#sidebar {\n"
"        background-color: #0d1727;\n"
"        border-right: 1px solid #1e2d42;\n"
"        min-width: 200px;\n"
"        max-width: 200px;\n"
"    }\n"
"    QLabel#appTitle {\n"
"        color: #4fa3e0;\n"
"        font-size: 14px;\n"
"        font-weight: bold;\n"
"        padding: 16px 12px 8px 12px;\n"
"    }\n"
"    QLabel#sidebarUserRole {\n"
"        color: #8fa8c8;\n"
"        font-size: 10px;\n"
"        padding: 2px 12px 10px 12px;\n"
"    }\n"
"    QPushButton#sidebarBtn {\n"
"        background-color: transparent;\n"
"        color: #8fa8c8;\n"
"        border: none;\n"
"        text-align: left;\n"
"        padding: 8px 16px;\n"
"        font-size: 12px;\n"
"    }\n"
"    QPushButton#sidebarBtn:hover {\n"
"        background-color: #1a2d45;\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton#sidebarBtnActive {\n"
"        background-color: #1e3a5f;\n"
"        color: #4fa3e0;\n"
"        border-left: 3px solid #4fa3e0;\n"
"        border-right: none;\n"
"        border-top: none;\n"
"        border-bottom: none;\n"
"        text-align: left;\n"
"        padding: 8px 13px;\n"
"        font-size: 12px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QPushButton#createNewCaseBtn {\n"
"        background-color: #f5a623;\n"
"        color: #000000;\n"
"        border: none;\n"
"        border-radius: 4px;\n"
"        padding: 10px 14px;\n"
"        font-size: 12px;\n"
"        font-weight: bold;\n"
"        margin: 12px;\n"
"    }\n"
"    QPushButton#createNewCaseBtn:hover {\n"
"        background-color: #e09518;\n"
"    }\n"
"    QWidget#topbar {\n"
"        background-color: #0f1b2d;\n"
"        border-bottom: 1px solid #1e2d42;\n"
"        min-height: 48px;\n"
"        max-height: 48px;\n"
"    }\n"
"    QLabel#topbarTitle {\n"
"        color: #ffffff;\n"
"        font-size: 13px;\n"
"        font-weight: bold;\n"
"        padding: 0px 8px;\n"
"    }\n"
"    QPushButton#topbarNavBtn {\n"
"        background-color: transparent;\n"
"        color: #8fa8c8;\n"
"        border: none;\n"
"        padding: 6px 10px;\n"
"        font-size: 12px;\n"
"    }\n"
"    QPushButton#topbarNavBtnActive {\n"
"        background-color: transparent;\n"
"        color: #4fa3e0;\n"
"        border-bottom: 2px solid #4fa3e0;\n"
"        border-top: none;\n"
"        border-left: none;\n"
"        border-right: none;\n"
"        padding: 6px 10px;\n"
"        font-size: 12px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QPushButton#topbarNavBtn:hover {\n"
"        color: #ffffff;\n"
"    }\n"
"    QPushButton#exportReportBtn {\n"
"        background-color: #1e3a5f;\n"
"        color: #4fa3e0;\n"
"        border: 1px solid #4fa3e0;\n"
"        border-radius: 4px;\n"
"        padding: 6px 14px;\n"
"        font-size: 12px;\n"
"    }\n"
"    QPushButton#exportReportBtn:hover {\n"
"        background-color: #254a78;\n"
"    }\n"
"    QWidget#contentArea {\n"
"        background-color: #0f1b2d;\n"
"        padding: 20px;\n"
"    }\n"
"    QLabel#pageTitle {\n"
"        color: #ffffff;\n"
"        font-size: 20px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QLabel#pageSubtitle {\n"
"        color: #6b8299;\n"
"        font-size: 11px;\n"
"    }\n"
"    QWidget#cardWidget {\n"
"        background-color: #13233a;\n"
"        border: 1px solid #1e2d42;\n"
"        border-radius: 6px;\n"
"    }\n"
"    QLabel#cardTitle {\n"
"        color: #8fa8c8;\n"
"        font-size: 12px;\n"
"        font-weight: bold;\n"
"        padding: 12px 14px 4px 14px;\n"
"    }\n"
"    QLabel#donutCenterNumber {\n"
"        color: #ffffff;\n"
"        font-size: 28px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QLabel#legendDot {\n"
"        min-width: 10px;\n"
"        max-width: 10px;\n"
"        min-height: 10px;\n"
"        max-height: 10px;\n"
"        border-radius: 5px;\n"
"    }\n"
"    QLabel#legendLabel {\n"
"        color: #8fa8c8;\n"
"        font-size: 11px;\n"
"    }\n"
"    QLabel#legendValue {\n"
"        color: #ffffff;\n"
"        font-size: 11px;\n"
"        font-weight: bold;\n"
"    }\n"
"    QLabel#trendBadgeExport {\n"
"        background-color: #1b3d5f;\n"
"        color: #4fa3e0;\n"
"        border-radius: 3px;\n"
"        padding: 2px 8px;\n"
"        font-size: 10px;\n"
"    }\n"
"    QWidget#tableHeaderWidget {\n"
"        background-color: #0d1727;\n"
"        border-radius: 0px;\n"
"    }\n"
"    QLabel#tableHeaderLabel {\n"
"        color: #6b8299;\n"
"        font-size: 10px;\n"
"        font-weight: bold;\n"
"        padding: 6px 10px;\n"
"    }\n"
"    QWidget#tableRowWidget {\n"
"        background-color: #13233a;\n"
"        border-bottom: 1px solid #1a2a3f;\n"
"    }\n"
"    QWidget#tableRowWidgetAlt {\n"
"        background-color: #0f1e30;\n"
"        border-bottom: 1px solid #1a2a3f;\n"
"    }\n"
"    QLabel#tableCell {\n"
"        color: #c8d8e8;\n"
"        font-size: 11px;\n"
"        padding: 8px 10px;\n"
"    }\n"
"    QLabel#tableCellMono {\n"
"        color: #4fa3e0;\n"
"        font-size: 11px;\n"
"        font-family: \"Courier New\", monospace;\n"
"        padding: 8px 10px;\n"
"    }\n"
"    QLabel#statusBadgeGreen {\n"
"        background-color: #1a4a2e;\n"
"        color: #4ecb71;\n"
"        border-radius: 3px;\n"
"        padding: 2px 8px;\n"
"        font-size: 10px;\n"
"    }\n"
"    QLabel#statusBadgeBlue {\n"
"        background-color: #1b3d5f;\n"
"        color: #4fa3e0;\n"
"        border-radius: 3px;\n"
"        padding: 2px 8px;\n"
"        font-size: 10px;\n"
"    }\n"
"    QLabel#statusBadgeOrange {\n"
"        background-color: #4a2e10;\n"
"        color: #f5a623;\n"
"        border-radius: 3px;\n"
"        padding: 2px 8px;\n"
"        font-size: 10px;\n"
"    }\n"
"    QScrollBar:vertical {\n"
"        background-color: #0d1727;\n"
"        width: 6px;\n"
"        border-radius: 3px;\n"
"    }\n"
"    QScrollBar::handle:vertical {\n"
"        background-color: #2a4060;\n"
"        border-radius: 3px;\n"
"    }\n"
"   ")
        self.rootLayout = QtWidgets.QHBoxLayout(ReportsWidget)
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")
        self.sidebar = QtWidgets.QWidget(ReportsWidget)
        self.sidebar.setObjectName("sidebar")
        self.sidebarLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.sidebarLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarLayout.setSpacing(0)
        self.sidebarLayout.setObjectName("sidebarLayout")
        self.appTitle = QtWidgets.QLabel(self.sidebar)
        self.appTitle.setObjectName("appTitle")
        self.sidebarLayout.addWidget(self.appTitle)
        self.sidebarDivider1 = QtWidgets.QFrame(self.sidebar)
        self.sidebarDivider1.setFrameShape(QtWidgets.QFrame.HLine)
        self.sidebarDivider1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebarDivider1.setObjectName("sidebarDivider1")
        self.sidebarLayout.addWidget(self.sidebarDivider1)
        self.userInfoWidget = QtWidgets.QWidget(self.sidebar)
        self.userInfoWidget.setObjectName("userInfoWidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.userInfoWidget)
        self.vboxlayout.setContentsMargins(12, 10, 0, 0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.userName = QtWidgets.QLabel(self.userInfoWidget)
        self.userName.setObjectName("userName")
        self.vboxlayout.addWidget(self.userName)
        self.sidebarUserRole = QtWidgets.QLabel(self.userInfoWidget)
        self.sidebarUserRole.setObjectName("sidebarUserRole")
        self.vboxlayout.addWidget(self.sidebarUserRole)
        self.sidebarLayout.addWidget(self.userInfoWidget)
        self.sidebarDivider2 = QtWidgets.QFrame(self.sidebar)
        self.sidebarDivider2.setFrameShape(QtWidgets.QFrame.HLine)
        self.sidebarDivider2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sidebarDivider2.setObjectName("sidebarDivider2")
        self.sidebarLayout.addWidget(self.sidebarDivider2)
        self.navDashboard = QtWidgets.QPushButton(self.sidebar)
        self.navDashboard.setFlat(True)
        self.navDashboard.setObjectName("navDashboard")
        self.sidebarLayout.addWidget(self.navDashboard)
        self.navCases = QtWidgets.QPushButton(self.sidebar)
        self.navCases.setFlat(True)
        self.navCases.setObjectName("navCases")
        self.sidebarLayout.addWidget(self.navCases)
        self.navCalendar = QtWidgets.QPushButton(self.sidebar)
        self.navCalendar.setFlat(True)
        self.navCalendar.setObjectName("navCalendar")
        self.sidebarLayout.addWidget(self.navCalendar)
        self.navDocuments = QtWidgets.QPushButton(self.sidebar)
        self.navDocuments.setFlat(True)
        self.navDocuments.setObjectName("navDocuments")
        self.sidebarLayout.addWidget(self.navDocuments)
        self.navReports = QtWidgets.QPushButton(self.sidebar)
        self.navReports.setFlat(True)
        self.navReports.setObjectName("navReports")
        self.sidebarLayout.addWidget(self.navReports)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.sidebarLayout.addItem(spacerItem)
        self.createNewCaseBtn = QtWidgets.QPushButton(self.sidebar)
        self.createNewCaseBtn.setObjectName("createNewCaseBtn")
        self.sidebarLayout.addWidget(self.createNewCaseBtn)
        self.navSettings = QtWidgets.QPushButton(self.sidebar)
        self.navSettings.setFlat(True)
        self.navSettings.setObjectName("navSettings")
        self.sidebarLayout.addWidget(self.navSettings)
        self.navLogout = QtWidgets.QPushButton(self.sidebar)
        self.navLogout.setFlat(True)
        self.navLogout.setObjectName("navLogout")
        self.sidebarLayout.addWidget(self.navLogout)
        self.rootLayout.addWidget(self.sidebar)
        self.mainArea = QtWidgets.QWidget(ReportsWidget)
        self.mainArea.setObjectName("mainArea")
        self.mainAreaLayout = QtWidgets.QVBoxLayout(self.mainArea)
        self.mainAreaLayout.setContentsMargins(0, 0, 0, 0)
        self.mainAreaLayout.setSpacing(0)
        self.mainAreaLayout.setObjectName("mainAreaLayout")
        self.topbar = QtWidgets.QWidget(self.mainArea)
        self.topbar.setObjectName("topbar")
        self.topbarLayout = QtWidgets.QHBoxLayout(self.topbar)
        self.topbarLayout.setContentsMargins(16, 0, 16, 0)
        self.topbarLayout.setSpacing(4)
        self.topbarLayout.setObjectName("topbarLayout")
        self.topbarTitle = QtWidgets.QLabel(self.topbar)
        self.topbarTitle.setObjectName("topbarTitle")
        self.topbarLayout.addWidget(self.topbarTitle)
        self.topNavCases = QtWidgets.QPushButton(self.topbar)
        self.topNavCases.setFlat(True)
        self.topNavCases.setObjectName("topNavCases")
        self.topbarLayout.addWidget(self.topNavCases)
        self.topNavFilings = QtWidgets.QPushButton(self.topbar)
        self.topNavFilings.setFlat(True)
        self.topNavFilings.setObjectName("topNavFilings")
        self.topbarLayout.addWidget(self.topNavFilings)
        self.topNavReports = QtWidgets.QPushButton(self.topbar)
        self.topNavReports.setFlat(True)
        self.topNavReports.setObjectName("topNavReports")
        self.topbarLayout.addWidget(self.topNavReports)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.topbarLayout.addItem(spacerItem1)
        self.topbarIcons = QtWidgets.QLabel(self.topbar)
        self.topbarIcons.setObjectName("topbarIcons")
        self.topbarLayout.addWidget(self.topbarIcons)
        self.signOutBtn = QtWidgets.QPushButton(self.topbar)
        self.signOutBtn.setFlat(True)
        self.signOutBtn.setObjectName("signOutBtn")
        self.topbarLayout.addWidget(self.signOutBtn)
        self.mainAreaLayout.addWidget(self.topbar)
        self.contentScrollArea = QtWidgets.QScrollArea(self.mainArea)
        self.contentScrollArea.setWidgetResizable(True)
        self.contentScrollArea.setObjectName("contentScrollArea")
        self.contentArea = QtWidgets.QWidget()
        self.contentArea.setObjectName("contentArea")
        self.contentLayout = QtWidgets.QVBoxLayout(self.contentArea)
        self.contentLayout.setContentsMargins(24, 20, 24, 20)
        self.contentLayout.setSpacing(16)
        self.contentLayout.setObjectName("contentLayout")
        self.pageHeaderLayout = QtWidgets.QHBoxLayout()
        self.pageHeaderLayout.setSpacing(8)
        self.pageHeaderLayout.setObjectName("pageHeaderLayout")
        self.vboxlayout1 = QtWidgets.QVBoxLayout()
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.pageTitle = QtWidgets.QLabel(self.contentArea)
        self.pageTitle.setObjectName("pageTitle")
        self.vboxlayout1.addWidget(self.pageTitle)
        self.pageSubtitle = QtWidgets.QLabel(self.contentArea)
        self.pageSubtitle.setObjectName("pageSubtitle")
        self.vboxlayout1.addWidget(self.pageSubtitle)
        self.pageHeaderLayout.addLayout(self.vboxlayout1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pageHeaderLayout.addItem(spacerItem2)
        self.exportReportBtn = QtWidgets.QPushButton(self.contentArea)
        self.exportReportBtn.setObjectName("exportReportBtn")
        self.pageHeaderLayout.addWidget(self.exportReportBtn)
        self.contentLayout.addLayout(self.pageHeaderLayout)
        self.cardsRowLayout = QtWidgets.QHBoxLayout()
        self.cardsRowLayout.setSpacing(16)
        self.cardsRowLayout.setObjectName("cardsRowLayout")
        self.casesByStatusCard = QtWidgets.QWidget(self.contentArea)
        self.casesByStatusCard.setMinimumWidth(260)
        self.casesByStatusCard.setMaximumWidth(320)
        self.casesByStatusCard.setObjectName("casesByStatusCard")
        self.casesByStatusLayout = QtWidgets.QVBoxLayout(self.casesByStatusCard)
        self.casesByStatusLayout.setContentsMargins(14, 14, 14, 14)
        self.casesByStatusLayout.setSpacing(8)
        self.casesByStatusLayout.setObjectName("casesByStatusLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.casesByStatusTitle = QtWidgets.QLabel(self.casesByStatusCard)
        self.casesByStatusTitle.setObjectName("casesByStatusTitle")
        self.hboxlayout.addWidget(self.casesByStatusTitle)
        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.casesByStatusMenu = QtWidgets.QLabel(self.casesByStatusCard)
        self.casesByStatusMenu.setObjectName("casesByStatusMenu")
        self.hboxlayout.addWidget(self.casesByStatusMenu)
        self.casesByStatusLayout.addLayout(self.hboxlayout)
        self.donutChartPlaceholder = QtWidgets.QWidget(self.casesByStatusCard)
        self.donutChartPlaceholder.setMinimumHeight(150)
        self.donutChartPlaceholder.setMaximumHeight(160)
        self.donutChartPlaceholder.setObjectName("donutChartPlaceholder")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.donutChartPlaceholder)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.donutCenterNumber = QtWidgets.QLabel(self.donutChartPlaceholder)
        self.donutCenterNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.donutCenterNumber.setObjectName("donutCenterNumber")
        self.vboxlayout2.addWidget(self.donutCenterNumber)
        self.donutCenterLabel = QtWidgets.QLabel(self.donutChartPlaceholder)
        self.donutCenterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.donutCenterLabel.setObjectName("donutCenterLabel")
        self.vboxlayout2.addWidget(self.donutCenterLabel)
        self.casesByStatusLayout.addWidget(self.donutChartPlaceholder)
        self.legendLayout = QtWidgets.QVBoxLayout()
        self.legendLayout.setSpacing(6)
        self.legendLayout.setObjectName("legendLayout")
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.dotFiled = QtWidgets.QLabel(self.casesByStatusCard)
        self.dotFiled.setObjectName("dotFiled")
        self.hboxlayout1.addWidget(self.dotFiled)
        self.labelFiled = QtWidgets.QLabel(self.casesByStatusCard)
        self.labelFiled.setObjectName("labelFiled")
        self.hboxlayout1.addWidget(self.labelFiled)
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem4)
        self.valueFiled = QtWidgets.QLabel(self.casesByStatusCard)
        self.valueFiled.setObjectName("valueFiled")
        self.hboxlayout1.addWidget(self.valueFiled)
        self.legendLayout.addLayout(self.hboxlayout1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.dotClosed = QtWidgets.QLabel(self.casesByStatusCard)
        self.dotClosed.setObjectName("dotClosed")
        self.hboxlayout2.addWidget(self.dotClosed)
        self.labelClosed = QtWidgets.QLabel(self.casesByStatusCard)
        self.labelClosed.setObjectName("labelClosed")
        self.hboxlayout2.addWidget(self.labelClosed)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem5)
        self.valueClosed = QtWidgets.QLabel(self.casesByStatusCard)
        self.valueClosed.setObjectName("valueClosed")
        self.hboxlayout2.addWidget(self.valueClosed)
        self.legendLayout.addLayout(self.hboxlayout2)
        self.casesByStatusLayout.addLayout(self.legendLayout)
        self.cardsRowLayout.addWidget(self.casesByStatusCard)
        self.filingTrendsCard = QtWidgets.QWidget(self.contentArea)
        self.filingTrendsCard.setObjectName("filingTrendsCard")
        self.filingTrendsLayout = QtWidgets.QVBoxLayout(self.filingTrendsCard)
        self.filingTrendsLayout.setContentsMargins(14, 14, 14, 14)
        self.filingTrendsLayout.setSpacing(8)
        self.filingTrendsLayout.setObjectName("filingTrendsLayout")
        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.filingTrendsTitle = QtWidgets.QLabel(self.filingTrendsCard)
        self.filingTrendsTitle.setObjectName("filingTrendsTitle")
        self.hboxlayout3.addWidget(self.filingTrendsTitle)
        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem6)
        self.trendBadgeExport = QtWidgets.QLabel(self.filingTrendsCard)
        self.trendBadgeExport.setObjectName("trendBadgeExport")
        self.hboxlayout3.addWidget(self.trendBadgeExport)
        self.filingTrendsLayout.addLayout(self.hboxlayout3)
        self.barChartPlaceholder = QtWidgets.QWidget(self.filingTrendsCard)
        self.barChartPlaceholder.setMinimumHeight(180)
        self.barChartPlaceholder.setObjectName("barChartPlaceholder")
        self.hboxlayout4 = QtWidgets.QHBoxLayout(self.barChartPlaceholder)
        self.hboxlayout4.setContentsMargins(0, 8, 0, 0)
        self.hboxlayout4.setSpacing(4)
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.bar1 = QtWidgets.QLabel(self.barChartPlaceholder)
        self.bar1.setAlignment(QtCore.Qt.AlignBottom)
        self.bar1.setObjectName("bar1")
        self.hboxlayout4.addWidget(self.bar1)
        self.bar2 = QtWidgets.QLabel(self.barChartPlaceholder)
        self.bar2.setAlignment(QtCore.Qt.AlignBottom)
        self.bar2.setObjectName("bar2")
        self.hboxlayout4.addWidget(self.bar2)
        self.bar3 = QtWidgets.QLabel(self.barChartPlaceholder)
        self.bar3.setAlignment(QtCore.Qt.AlignBottom)
        self.bar3.setObjectName("bar3")
        self.hboxlayout4.addWidget(self.bar3)
        self.bar4 = QtWidgets.QLabel(self.barChartPlaceholder)
        self.bar4.setAlignment(QtCore.Qt.AlignBottom)
        self.bar4.setObjectName("bar4")
        self.hboxlayout4.addWidget(self.bar4)
        self.bar5 = QtWidgets.QLabel(self.barChartPlaceholder)
        self.bar5.setAlignment(QtCore.Qt.AlignBottom)
        self.bar5.setObjectName("bar5")
        self.hboxlayout4.addWidget(self.bar5)
        self.bar6 = QtWidgets.QLabel(self.barChartPlaceholder)
        self.bar6.setAlignment(QtCore.Qt.AlignBottom)
        self.bar6.setObjectName("bar6")
        self.hboxlayout4.addWidget(self.bar6)
        spacerItem7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem7)
        self.filingTrendsLayout.addWidget(self.barChartPlaceholder)
        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setSpacing(4)
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.xLabel1 = QtWidgets.QLabel(self.filingTrendsCard)
        self.xLabel1.setObjectName("xLabel1")
        self.hboxlayout5.addWidget(self.xLabel1)
        spacerItem8 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem8)
        self.xLabel2 = QtWidgets.QLabel(self.filingTrendsCard)
        self.xLabel2.setObjectName("xLabel2")
        self.hboxlayout5.addWidget(self.xLabel2)
        spacerItem9 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem9)
        self.xLabel3 = QtWidgets.QLabel(self.filingTrendsCard)
        self.xLabel3.setObjectName("xLabel3")
        self.hboxlayout5.addWidget(self.xLabel3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem10)
        self.filingTrendsLayout.addLayout(self.hboxlayout5)
        self.cardsRowLayout.addWidget(self.filingTrendsCard)
        self.contentLayout.addLayout(self.cardsRowLayout)
        self.activityLogsCard = QtWidgets.QWidget(self.contentArea)
        self.activityLogsCard.setObjectName("activityLogsCard")
        self.activityLogsLayout = QtWidgets.QVBoxLayout(self.activityLogsCard)
        self.activityLogsLayout.setContentsMargins(0, 0, 0, 0)
        self.activityLogsLayout.setSpacing(0)
        self.activityLogsLayout.setObjectName("activityLogsLayout")
        self.activityHeaderLayout = QtWidgets.QHBoxLayout()
        self.activityHeaderLayout.setContentsMargins(14, 12, 14, 12)
        self.activityHeaderLayout.setObjectName("activityHeaderLayout")
        self.activityLogsTitle = QtWidgets.QLabel(self.activityLogsCard)
        self.activityLogsTitle.setObjectName("activityLogsTitle")
        self.activityHeaderLayout.addWidget(self.activityLogsTitle)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.activityHeaderLayout.addItem(spacerItem11)
        self.activityFilterIcon = QtWidgets.QLabel(self.activityLogsCard)
        self.activityFilterIcon.setObjectName("activityFilterIcon")
        self.activityHeaderLayout.addWidget(self.activityFilterIcon)
        self.activityLogsLayout.addLayout(self.activityHeaderLayout)
        self.tableHeaderWidget = QtWidgets.QWidget(self.activityLogsCard)
        self.tableHeaderWidget.setObjectName("tableHeaderWidget")
        self.tableHeaderLayout = QtWidgets.QHBoxLayout(self.tableHeaderWidget)
        self.tableHeaderLayout.setContentsMargins(0, 0, 0, 0)
        self.tableHeaderLayout.setSpacing(0)
        self.tableHeaderLayout.setObjectName("tableHeaderLayout")
        self.thCaseNumber = QtWidgets.QLabel(self.tableHeaderWidget)
        self.thCaseNumber.setMinimumWidth(150)
        self.thCaseNumber.setObjectName("thCaseNumber")
        self.tableHeaderLayout.addWidget(self.thCaseNumber)
        self.thActivity = QtWidgets.QLabel(self.tableHeaderWidget)
        self.thActivity.setMinimumWidth(180)
        self.thActivity.setObjectName("thActivity")
        self.tableHeaderLayout.addWidget(self.thActivity)
        self.thDetails = QtWidgets.QLabel(self.tableHeaderWidget)
        self.thDetails.setMinimumWidth(180)
        self.thDetails.setObjectName("thDetails")
        self.tableHeaderLayout.addWidget(self.thDetails)
        self.thPerformedBy = QtWidgets.QLabel(self.tableHeaderWidget)
        self.thPerformedBy.setMinimumWidth(140)
        self.thPerformedBy.setObjectName("thPerformedBy")
        self.tableHeaderLayout.addWidget(self.thPerformedBy)
        self.thStatus = QtWidgets.QLabel(self.tableHeaderWidget)
        self.thStatus.setMinimumWidth(100)
        self.thStatus.setObjectName("thStatus")
        self.tableHeaderLayout.addWidget(self.thStatus)
        self.thTimestamp = QtWidgets.QLabel(self.tableHeaderWidget)
        self.thTimestamp.setMinimumWidth(120)
        self.thTimestamp.setObjectName("thTimestamp")
        self.tableHeaderLayout.addWidget(self.thTimestamp)
        self.activityLogsLayout.addWidget(self.tableHeaderWidget)
        self.tableRow1 = QtWidgets.QWidget(self.activityLogsCard)
        self.tableRow1.setObjectName("tableRow1")
        self.row1Layout = QtWidgets.QHBoxLayout(self.tableRow1)
        self.row1Layout.setContentsMargins(0, 0, 0, 0)
        self.row1Layout.setSpacing(0)
        self.row1Layout.setObjectName("row1Layout")
        self.r1CaseNum = QtWidgets.QLabel(self.tableRow1)
        self.r1CaseNum.setMinimumWidth(150)
        self.r1CaseNum.setObjectName("r1CaseNum")
        self.row1Layout.addWidget(self.r1CaseNum)
        self.r1Activity = QtWidgets.QLabel(self.tableRow1)
        self.r1Activity.setMinimumWidth(180)
        self.r1Activity.setObjectName("r1Activity")
        self.row1Layout.addWidget(self.r1Activity)
        self.r1Details = QtWidgets.QLabel(self.tableRow1)
        self.r1Details.setMinimumWidth(180)
        self.r1Details.setObjectName("r1Details")
        self.row1Layout.addWidget(self.r1Details)
        self.r1PerformedBy = QtWidgets.QLabel(self.tableRow1)
        self.r1PerformedBy.setMinimumWidth(140)
        self.r1PerformedBy.setObjectName("r1PerformedBy")
        self.row1Layout.addWidget(self.r1PerformedBy)
        self.r1Status = QtWidgets.QLabel(self.tableRow1)
        self.r1Status.setMinimumWidth(100)
        self.r1Status.setObjectName("r1Status")
        self.row1Layout.addWidget(self.r1Status)
        self.r1Timestamp = QtWidgets.QLabel(self.tableRow1)
        self.r1Timestamp.setMinimumWidth(120)
        self.r1Timestamp.setObjectName("r1Timestamp")
        self.row1Layout.addWidget(self.r1Timestamp)
        self.activityLogsLayout.addWidget(self.tableRow1)
        self.tableRow2 = QtWidgets.QWidget(self.activityLogsCard)
        self.tableRow2.setObjectName("tableRow2")
        self.row2Layout = QtWidgets.QHBoxLayout(self.tableRow2)
        self.row2Layout.setContentsMargins(0, 0, 0, 0)
        self.row2Layout.setSpacing(0)
        self.row2Layout.setObjectName("row2Layout")
        self.r2CaseNum = QtWidgets.QLabel(self.tableRow2)
        self.r2CaseNum.setMinimumWidth(150)
        self.r2CaseNum.setObjectName("r2CaseNum")
        self.row2Layout.addWidget(self.r2CaseNum)
        self.r2Activity = QtWidgets.QLabel(self.tableRow2)
        self.r2Activity.setMinimumWidth(180)
        self.r2Activity.setObjectName("r2Activity")
        self.row2Layout.addWidget(self.r2Activity)
        self.r2Details = QtWidgets.QLabel(self.tableRow2)
        self.r2Details.setMinimumWidth(180)
        self.r2Details.setObjectName("r2Details")
        self.row2Layout.addWidget(self.r2Details)
        self.r2PerformedBy = QtWidgets.QLabel(self.tableRow2)
        self.r2PerformedBy.setMinimumWidth(140)
        self.r2PerformedBy.setObjectName("r2PerformedBy")
        self.row2Layout.addWidget(self.r2PerformedBy)
        self.r2Status = QtWidgets.QLabel(self.tableRow2)
        self.r2Status.setMinimumWidth(100)
        self.r2Status.setObjectName("r2Status")
        self.row2Layout.addWidget(self.r2Status)
        self.r2Timestamp = QtWidgets.QLabel(self.tableRow2)
        self.r2Timestamp.setMinimumWidth(120)
        self.r2Timestamp.setObjectName("r2Timestamp")
        self.row2Layout.addWidget(self.r2Timestamp)
        self.activityLogsLayout.addWidget(self.tableRow2)
        self.tableRow3 = QtWidgets.QWidget(self.activityLogsCard)
        self.tableRow3.setObjectName("tableRow3")
        self.row3Layout = QtWidgets.QHBoxLayout(self.tableRow3)
        self.row3Layout.setContentsMargins(0, 0, 0, 0)
        self.row3Layout.setSpacing(0)
        self.row3Layout.setObjectName("row3Layout")
        self.r3CaseNum = QtWidgets.QLabel(self.tableRow3)
        self.r3CaseNum.setMinimumWidth(150)
        self.r3CaseNum.setObjectName("r3CaseNum")
        self.row3Layout.addWidget(self.r3CaseNum)
        self.r3Activity = QtWidgets.QLabel(self.tableRow3)
        self.r3Activity.setMinimumWidth(180)
        self.r3Activity.setObjectName("r3Activity")
        self.row3Layout.addWidget(self.r3Activity)
        self.r3Details = QtWidgets.QLabel(self.tableRow3)
        self.r3Details.setMinimumWidth(180)
        self.r3Details.setObjectName("r3Details")
        self.row3Layout.addWidget(self.r3Details)
        self.r3PerformedBy = QtWidgets.QLabel(self.tableRow3)
        self.r3PerformedBy.setMinimumWidth(140)
        self.r3PerformedBy.setObjectName("r3PerformedBy")
        self.row3Layout.addWidget(self.r3PerformedBy)
        self.r3Status = QtWidgets.QLabel(self.tableRow3)
        self.r3Status.setMinimumWidth(100)
        self.r3Status.setObjectName("r3Status")
        self.row3Layout.addWidget(self.r3Status)
        self.r3Timestamp = QtWidgets.QLabel(self.tableRow3)
        self.r3Timestamp.setMinimumWidth(120)
        self.r3Timestamp.setObjectName("r3Timestamp")
        self.row3Layout.addWidget(self.r3Timestamp)
        self.activityLogsLayout.addWidget(self.tableRow3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.activityLogsLayout.addItem(spacerItem12)
        self.contentLayout.addWidget(self.activityLogsCard)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.contentLayout.addItem(spacerItem13)
        self.contentScrollArea.setWidget(self.contentArea)
        self.mainAreaLayout.addWidget(self.contentScrollArea)
        self.rootLayout.addWidget(self.mainArea)

        self.retranslateUi(ReportsWidget)
        QtCore.QMetaObject.connectSlotsByName(ReportsWidget)

    def retranslateUi(self, ReportsWidget):
        _translate = QtCore.QCoreApplication.translate
        ReportsWidget.setWindowTitle(_translate("ReportsWidget", "LexSecure CCMS - Reports"))
        self.appTitle.setText(_translate("ReportsWidget", "LexSecure CCMS"))
        self.sidebarDivider1.setStyleSheet(_translate("ReportsWidget", "color: #1e2d42;"))
        self.userName.setText(_translate("ReportsWidget", "Court Admin"))
        self.userName.setStyleSheet(_translate("ReportsWidget", "color: #ffffff; font-size: 12px; font-weight: bold;"))
        self.sidebarUserRole.setText(_translate("ReportsWidget", "Court Admin"))
        self.sidebarDivider2.setStyleSheet(_translate("ReportsWidget", "color: #1e2d42;"))
        self.navDashboard.setText(_translate("ReportsWidget", "Dashboard"))
        self.navCases.setText(_translate("ReportsWidget", "Case Search"))
        self.navCalendar.setText(_translate("ReportsWidget", "Calendar"))
        self.navDocuments.setText(_translate("ReportsWidget", "E-Filing"))
        self.navReports.setText(_translate("ReportsWidget", "Reports"))
        self.createNewCaseBtn.setText(_translate("ReportsWidget", "+ Create New Case"))
        self.navSettings.setText(_translate("ReportsWidget", "Settings"))
        self.navLogout.setText(_translate("ReportsWidget", "Logout"))
        self.topbarTitle.setText(_translate("ReportsWidget", "LexSecure CCMS"))
        self.topNavCases.setText(_translate("ReportsWidget", "Cases"))
        self.topNavFilings.setText(_translate("ReportsWidget", "Filings"))
        self.topNavReports.setText(_translate("ReportsWidget", "Reports"))
        self.topbarIcons.setText(_translate("ReportsWidget", "🔔  ⚙  👤"))
        self.topbarIcons.setStyleSheet(_translate("ReportsWidget", "color: #8fa8c8; font-size: 14px; padding: 0 8px;"))
        self.signOutBtn.setText(_translate("ReportsWidget", "Sign Out"))
        self.signOutBtn.setStyleSheet(_translate("ReportsWidget", "background-color: transparent; color: #8fa8c8; border: 1px solid #2a4060; border-radius: 4px; padding: 4px 12px; font-size: 11px;"))
        self.contentScrollArea.setStyleSheet(_translate("ReportsWidget", "QScrollArea { border: none; background-color: #0f1b2d; }"))
        self.pageTitle.setText(_translate("ReportsWidget", "Reports"))
        self.pageSubtitle.setText(_translate("ReportsWidget", "Generate and view detailed case management activity reports."))
        self.exportReportBtn.setText(_translate("ReportsWidget", "⬇ Export Report"))
        self.casesByStatusTitle.setText(_translate("ReportsWidget", "Cases by Status"))
        self.casesByStatusTitle.setStyleSheet(_translate("ReportsWidget", "color: #8fa8c8; font-size: 12px; font-weight: bold; padding: 0;"))
        self.casesByStatusMenu.setText(_translate("ReportsWidget", "⋮"))
        self.casesByStatusMenu.setStyleSheet(_translate("ReportsWidget", "color: #6b8299; font-size: 16px;"))
        self.donutChartPlaceholder.setStyleSheet(_translate("ReportsWidget", "\n"
"                   QWidget#donutChartPlaceholder {\n"
"                       border-radius: 75px;\n"
"                       background-color: transparent;\n"
"                   }\n"
"                  "))
        self.donutCenterNumber.setText(_translate("ReportsWidget", "6"))
        self.donutCenterNumber.setStyleSheet(_translate("ReportsWidget", "color: #ffffff; font-size: 32px; font-weight: bold;"))
        self.donutCenterLabel.setText(_translate("ReportsWidget", "Total Cases"))
        self.donutCenterLabel.setStyleSheet(_translate("ReportsWidget", "color: #6b8299; font-size: 10px;"))
        self.dotFiled.setText(_translate("ReportsWidget", " "))
        self.dotFiled.setStyleSheet(_translate("ReportsWidget", "background-color: #4fa3e0; border-radius: 5px; min-width:10px; max-width:10px; min-height:10px; max-height:10px;"))
        self.labelFiled.setText(_translate("ReportsWidget", "Filed"))
        self.valueFiled.setText(_translate("ReportsWidget", "4"))
        self.dotClosed.setText(_translate("ReportsWidget", " "))
        self.dotClosed.setStyleSheet(_translate("ReportsWidget", "background-color: #4ecb71; border-radius: 5px; min-width:10px; max-width:10px; min-height:10px; max-height:10px;"))
        self.labelClosed.setText(_translate("ReportsWidget", "Closed"))
        self.valueClosed.setText(_translate("ReportsWidget", "2"))
        self.filingTrendsTitle.setText(_translate("ReportsWidget", "Filing Trends"))
        self.filingTrendsTitle.setStyleSheet(_translate("ReportsWidget", "color: #8fa8c8; font-size: 12px; font-weight: bold;"))
        self.trendBadgeExport.setText(_translate("ReportsWidget", "Last 30 days"))
        self.trendBadgeExport.setStyleSheet(_translate("ReportsWidget", "background-color: #1b3d5f; color: #4fa3e0; border-radius: 3px; padding: 2px 8px; font-size: 10px;"))
        self.barChartPlaceholder.setStyleSheet(_translate("ReportsWidget", "background-color: transparent;"))
        self.bar1.setText(_translate("ReportsWidget", " "))
        self.bar1.setStyleSheet(_translate("ReportsWidget", "background-color:#2a4060; border-radius:2px; min-width:18px; max-width:18px; min-height:60px;"))
        self.bar2.setText(_translate("ReportsWidget", " "))
        self.bar2.setStyleSheet(_translate("ReportsWidget", "background-color:#2a4060; border-radius:2px; min-width:18px; max-width:18px; min-height:40px;"))
        self.bar3.setText(_translate("ReportsWidget", " "))
        self.bar3.setStyleSheet(_translate("ReportsWidget", "background-color:#2a4060; border-radius:2px; min-width:18px; max-width:18px; min-height:100px;"))
        self.bar4.setText(_translate("ReportsWidget", " "))
        self.bar4.setStyleSheet(_translate("ReportsWidget", "background-color:#4fa3e0; border-radius:2px; min-width:18px; max-width:18px; min-height:150px;"))
        self.bar5.setText(_translate("ReportsWidget", " "))
        self.bar5.setStyleSheet(_translate("ReportsWidget", "background-color:#2a4060; border-radius:2px; min-width:18px; max-width:18px; min-height:80px;"))
        self.bar6.setText(_translate("ReportsWidget", " "))
        self.bar6.setStyleSheet(_translate("ReportsWidget", "background-color:#2a4060; border-radius:2px; min-width:18px; max-width:18px; min-height:50px;"))
        self.xLabel1.setText(_translate("ReportsWidget", "Jan 24"))
        self.xLabel1.setStyleSheet(_translate("ReportsWidget", "color:#6b8299; font-size:9px;"))
        self.xLabel2.setText(_translate("ReportsWidget", "Feb 24"))
        self.xLabel2.setStyleSheet(_translate("ReportsWidget", "color:#6b8299; font-size:9px;"))
        self.xLabel3.setText(_translate("ReportsWidget", "Mar 24"))
        self.xLabel3.setStyleSheet(_translate("ReportsWidget", "color:#6b8299; font-size:9px;"))
        self.activityLogsTitle.setText(_translate("ReportsWidget", "Recent Activity Logs"))
        self.activityLogsTitle.setStyleSheet(_translate("ReportsWidget", "color: #ffffff; font-size: 13px; font-weight: bold;"))
        self.activityFilterIcon.setText(_translate("ReportsWidget", "▼  🔍"))
        self.activityFilterIcon.setStyleSheet(_translate("ReportsWidget", "color: #8fa8c8; font-size: 12px;"))
        self.tableHeaderWidget.setStyleSheet(_translate("ReportsWidget", "background-color: #0d1727; border-top: 1px solid #1e2d42; border-bottom: 1px solid #1e2d42;"))
        self.thCaseNumber.setText(_translate("ReportsWidget", "CASE NUMBER"))
        self.thActivity.setText(_translate("ReportsWidget", "ACTIVITY"))
        self.thDetails.setText(_translate("ReportsWidget", "DETAILS"))
        self.thPerformedBy.setText(_translate("ReportsWidget", "PERFORMED BY"))
        self.thStatus.setText(_translate("ReportsWidget", "STATUS"))
        self.thTimestamp.setText(_translate("ReportsWidget", "TIMESTAMP"))
        self.r1CaseNum.setText(_translate("ReportsWidget", "CVS-2024-0001"))
        self.r1Activity.setText(_translate("ReportsWidget", "Order Signed"))
        self.r1Details.setText(_translate("ReportsWidget", "Judge A. Hill in 41 vs..."))
        self.r1PerformedBy.setText(_translate("ReportsWidget", "Court Admin"))
        self.r1Status.setText(_translate("ReportsWidget", "Completed"))
        self.r1Status.setStyleSheet(_translate("ReportsWidget", "background-color: #1a4a2e; color: #4ecb71; border-radius: 3px; padding: 2px 8px; font-size: 10px; margin: 8px 4px;"))
        self.r1Timestamp.setText(_translate("ReportsWidget", "6/24 1:02 AM"))
        self.r2CaseNum.setText(_translate("ReportsWidget", "CVS-2024-0002"))
        self.r2Activity.setText(_translate("ReportsWidget", "Initial Filing Received"))
        self.r2Details.setText(_translate("ReportsWidget", "Nala Mike v. Mike"))
        self.r2PerformedBy.setText(_translate("ReportsWidget", "System Admin"))
        self.r2Status.setText(_translate("ReportsWidget", "Info Only"))
        self.r2Status.setStyleSheet(_translate("ReportsWidget", "background-color: #1b3d5f; color: #4fa3e0; border-radius: 3px; padding: 2px 8px; font-size: 10px; margin: 8px 4px;"))
        self.r2Timestamp.setText(_translate("ReportsWidget", "Yesterday"))
        self.r3CaseNum.setText(_translate("ReportsWidget", "FMS-2024-1533"))
        self.r3Activity.setText(_translate("ReportsWidget", "Case Created"))
        self.r3Details.setText(_translate("ReportsWidget", "–"))
        self.r3PerformedBy.setText(_translate("ReportsWidget", "System Admin"))
        self.r3Status.setText(_translate("ReportsWidget", "Pending"))
        self.r3Status.setStyleSheet(_translate("ReportsWidget", "background-color: #4a2e10; color: #f5a623; border-radius: 3px; padding: 2px 8px; font-size: 10px; margin: 8px 4px;"))
        self.r3Timestamp.setText(_translate("ReportsWidget", "Yesterday"))


class WelcomeWindow(QWidget):
    def __init__(self, on_login, on_exit):
        super().__init__()
        self.setWindowTitle("Court Case Management System")
        self.resize(900, 600)
        self.setStyleSheet(f"background-color:{DARK_BG};")

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)

        root.addStretch(2)

        # Logo
        logo = QLabel("⚖")
        logo.setFixedSize(90, 90)
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet(
            "background-color:rgba(240,180,41,30);border-radius:45px;"
            f"color:{ACCENT};font-size:36px;font-weight:bold;"
        )
        logo_row = QHBoxLayout()
        logo_row.addStretch()
        logo_row.addWidget(logo)
        logo_row.addStretch()
        root.addLayout(logo_row)

        root.addSpacing(16)

        # Title
        title = QLabel("Court Case Management System")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(f"color:#ffffff;font-size:28px;font-weight:bold;")
        root.addWidget(title)

        # Subtitle
        sub = QLabel("A digital platform for managing court cases, filings, hearings and documents.")
        sub.setAlignment(Qt.AlignCenter)
        sub.setWordWrap(True)
        sub.setStyleSheet(f"color:{TEXT_MUTED};font-size:13px;")
        root.addWidget(sub)

        root.addStretch(1)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_login = QPushButton("Login")
        btn_login.setMinimumSize(140, 42)
        btn_login.setCursor(Qt.PointingHandCursor)
        btn_login.setStyleSheet(
            f"QPushButton{{background:{ACCENT};color:{DARK_BG};border-radius:6px;"
            f"font-weight:bold;font-size:14px;}}"
            f"QPushButton:hover{{background:#ffce4d;}}"
        )
        btn_exit = QPushButton("Exit")
        btn_exit.setMinimumSize(100, 42)
        btn_exit.setCursor(Qt.PointingHandCursor)
        btn_exit.setStyleSheet(
            f"QPushButton{{background:transparent;color:#ffffff;"
            f"border:1px solid #3a4566;border-radius:6px;font-size:14px;}}"
            f"QPushButton:hover{{background:#1a2247;}}"
        )
        btn_row.addWidget(btn_login)
        btn_row.addSpacing(12)
        btn_row.addWidget(btn_exit)
        btn_row.addStretch()
        root.addLayout(btn_row)

        root.addStretch(2)

        btn_login.clicked.connect(on_login)
        btn_exit.clicked.connect(on_exit)


# ─────────────────────────────────────────────
#  WINDOW 2 – LOGIN  (login.ui)
# ─────────────────────────────────────────────

class LoginWindow(QWidget):
    def __init__(self, on_success, on_back=None):
        super().__init__()
        self.on_success = on_success
        self.setWindowTitle("LexSecure CCMS - Login")
        self.resize(420, 520)
        self.setStyleSheet(f"background-color:{DARK_BG};font-family:'Inter';")

        root = QVBoxLayout(self)
        root.setContentsMargins(40, 50, 40, 30)

        # Logo centred
        logo = QLabel("⚖")
        logo.setFixedSize(56, 56)
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet(
            "background-color:rgba(240,180,41,30);border-radius:28px;"
            f"color:{ACCENT};font-size:22px;font-weight:bold;"
        )
        row = QHBoxLayout()
        row.addStretch()
        row.addWidget(logo)
        row.addStretch()
        root.addLayout(row)

        brand = QLabel("LexSecure CCMS")
        brand.setAlignment(Qt.AlignCenter)
        brand.setStyleSheet("color:#ffffff;font-size:18px;font-weight:bold;")
        root.addWidget(brand)
        root.addSpacing(20)

        # Card frame
        card = QFrame()
        card.setStyleSheet(
            f"background-color:#11173a;border-radius:10px;border:1px solid #1f2750;"
        )
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 22, 24, 22)

        lbl_title = QLabel("Login")
        lbl_title.setStyleSheet("color:#ffffff;font-size:16px;font-weight:bold;")
        card_layout.addWidget(lbl_title)

        lbl_sub = QLabel("Enter your credentials to access your secure legal workspace.")
        lbl_sub.setWordWrap(True)
        lbl_sub.setStyleSheet(f"color:#8b93b0;font-size:11px;")
        card_layout.addWidget(lbl_sub)
        card_layout.addSpacing(14)

        # Username
        card_layout.addWidget(self._field_label("USERNAME"))
        self.txt_username = QLineEdit()
        self.txt_username.setPlaceholderText("your_username")
        self.txt_username.setMinimumHeight(38)
        self.txt_username.setStyleSheet(
            f"QLineEdit{{background:{DARK_BG};color:#ffffff;border:1px solid #2a3360;"
            f"border-radius:6px;padding-left:10px;font-size:12px;}}"
        )
        card_layout.addWidget(self.txt_username)
        card_layout.addSpacing(10)

        # Password
        card_layout.addWidget(self._field_label("PASSWORD"))
        pw_row = QHBoxLayout()
        self.txt_password = QLineEdit()
        self.txt_password.setPlaceholderText("••••••••")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setMinimumHeight(38)
        self.txt_password.setStyleSheet(
            f"QLineEdit{{background:{DARK_BG};color:#ffffff;border:1px solid #2a3360;"
            f"border-radius:6px;padding-left:10px;font-size:12px;}}"
        )
        btn_toggle = QPushButton("👁")
        btn_toggle.setFixedSize(30, 30)
        btn_toggle.setCheckable(True)
        btn_toggle.setCursor(Qt.PointingHandCursor)
        btn_toggle.setStyleSheet(
            f"color:#8b93b0;background:transparent;border:none;font-size:13px;"
        )
        btn_toggle.toggled.connect(
            lambda on: self.txt_password.setEchoMode(
                QLineEdit.Normal if on else QLineEdit.Password
            )
        )
        pw_row.addWidget(self.txt_password)
        pw_row.addWidget(btn_toggle)
        card_layout.addLayout(pw_row)
        card_layout.addSpacing(16)

        # Login button
        self.lbl_error = QLabel("")
        self.lbl_error.setStyleSheet("color:#ff6b6b;font-size:11px;")
        self.lbl_error.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(self.lbl_error)

        btn_login = QPushButton("Login  →")
        btn_login.setMinimumHeight(42)
        btn_login.setCursor(Qt.PointingHandCursor)
        btn_login.setStyleSheet(
            f"QPushButton{{background:{ACCENT};color:{DARK_BG};border-radius:6px;"
            f"font-size:13px;font-weight:bold;}}"
            f"QPushButton:hover{{background:#ffce4d;}}"
        )
        btn_login.clicked.connect(self._do_login)
        card_layout.addWidget(btn_login)

        lbl_footer = QLabel("Secured Legal Sync Protocol Active")
        lbl_footer.setAlignment(Qt.AlignCenter)
        lbl_footer.setStyleSheet("color:#5a6280;font-size:9px;")
        card_layout.addWidget(lbl_footer)

        root.addWidget(card)
        root.addSpacing(14)

        # Footer links
        foot_row = QHBoxLayout()
        btn_forgot = QPushButton("Forgot password?")
        btn_forgot.setStyleSheet(
            "color:#8b93b0;background:transparent;border:none;font-size:11px;"
        )
        btn_forgot.setCursor(Qt.PointingHandCursor)
        btn_forgot.clicked.connect(self._forgot_password)
        foot_row.addWidget(btn_forgot)
        foot_row.addStretch()
        root.addLayout(foot_row)

        # Allow Enter key
        self.txt_password.returnPressed.connect(self._do_login)
        self.txt_username.returnPressed.connect(self._do_login)

    def _field_label(self, text):
        lbl = QLabel(text)
        lbl.setStyleSheet("color:#c7cbe0;font-size:10px;font-weight:bold;")
        return lbl

    def _do_login(self):
        user = login(self.txt_username.text().strip(), self.txt_password.text())
        if user:
            self.lbl_error.setText("")
            self.on_success(user)
        else:
            self.lbl_error.setText("Invalid username or password.")

    def _forgot_password(self):
        QMessageBox.information(self, "Forgot Password",
                                "Please contact your system administrator to reset your password.")


# ─────────────────────────────────────────────
#  SHARED SIDEBAR helper
# ─────────────────────────────────────────────

def make_sidebar(nav_items, on_new_case=None):
    """
    Returns (sidebar_frame, dict_of_buttons).
    nav_items: list of (label, key_str)
    """
    frame = QFrame()
    frame.setFixedWidth(220)
    frame.setStyleSheet(f"QFrame{{background:{DARK_BG};}}")
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(16, 20, 16, 20)
    layout.setSpacing(6)

    brand = QLabel("Court Admin")
    brand.setStyleSheet("color:#ffffff;font-size:14px;font-weight:700;")
    layout.addWidget(brand)
    layout.addSpacing(4)

    buttons = {}
    for label, key in nav_items:
        btn = QToolButton()
        btn.setText(label)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn.setMinimumHeight(36)
        btn.setStyleSheet(
            "QToolButton{background:transparent;color:#b7bedd;text-align:left;"
            "padding:8px 14px;font-size:12px;border-radius:6px;border:none;}"
            "QToolButton:hover{background:#1a2247;color:#ffffff;}"
        )
        layout.addWidget(btn)
        buttons[key] = btn

    layout.addStretch()

    if on_new_case:
        btn_new = QToolButton()
        btn_new.setText("+ New Case")
        btn_new.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn_new.setMinimumHeight(38)
        btn_new.setStyleSheet(
            f"QToolButton{{background:{ACCENT};color:{DARK_BG};font-weight:700;"
            f"border-radius:6px;padding:10px;border:none;}}"
            f"QToolButton:hover{{background:#ffce4d;}}"
        )
        btn_new.clicked.connect(on_new_case)
        layout.addWidget(btn_new)
        buttons["new_case"] = btn_new

    return frame, buttons


# ─────────────────────────────────────────────
#  ADMIN DASHBOARD  (admin_dashboard.ui)
# ─────────────────────────────────────────────

class AdminDashboardWidget(QWidget):
    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setStyleSheet(f"background:{LIGHT_BG};color:#1b2240;font-family:'Inter';")
        self._build_ui()

    def _build_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Sidebar
        nav_items = [
            ("Dashboard", "dashboard"), ("Cases", "cases"),
            ("Judges", "judges"), ("Lawyers", "lawyers"),
            ("Users", "users"), ("Settings", "settings"),
        ]
        sidebar, btns = make_sidebar(nav_items, on_new_case=self._new_case)
        btns["dashboard"].clicked.connect(lambda: self.app.show_admin_dashboard())
        btns["cases"].clicked.connect(lambda: self.app.show_admin_panel())
        btns["judges"].clicked.connect(lambda: self.app.show_assign_judge())
        btns["lawyers"].clicked.connect(lambda: self.app.show_assign_lawyer())
        btns["users"].clicked.connect(lambda: self.app.show_admin_panel())
        root.addWidget(sidebar)

        # Main column
        main_col = QVBoxLayout()
        main_col.setSpacing(0)

        # Topbar
        topbar = QFrame()
        topbar.setStyleSheet("background:#ffffff;border-bottom:1px solid #dfe3ee;")
        tb_layout = QHBoxLayout(topbar)
        tb_layout.setContentsMargins(24, 12, 24, 12)
        lbl_brand = QLabel("LexSecure CCMS")
        lbl_brand.setStyleSheet("color:#0c1230;font-size:16px;font-weight:700;")
        tb_layout.addWidget(lbl_brand)
        tb_layout.addStretch()
        search = QLineEdit()
        search.setPlaceholderText("Search cases, users...")
        search.setFixedWidth(240)
        search.setStyleSheet(
            "background:#f5f6fa;border:1px solid #dfe3ee;border-radius:8px;"
            "padding:6px 12px;font-size:12px;"
        )
        tb_layout.addWidget(search)
        tb_layout.addSpacing(12)
        btn_notif = QToolButton()
        btn_notif.setText("🔔")
        btn_notif.setStyleSheet("border:none;font-size:16px;")
        tb_layout.addWidget(btn_notif)
        btn_avatar = QToolButton()
        btn_avatar.setText("👤")
        btn_avatar.setStyleSheet("border:none;font-size:16px;")
        btn_avatar.clicked.connect(lambda: self.app.confirm_logout(self))
        tb_layout.addWidget(btn_avatar)
        main_col.addWidget(topbar)

        # Content
        content = QVBoxLayout()
        content.setContentsMargins(24, 20, 24, 20)
        content.setSpacing(16)

        lbl_title = QLabel("Dashboard")
        lbl_title.setStyleSheet("color:#1b2240;font-size:20px;font-weight:700;")
        content.addWidget(lbl_title)

        # Stat cards row
        stat_row = QHBoxLayout()
        stat_row.setSpacing(16)
        cases = load_data("cases")
        stat_counts = {
            "Total Cases": (str(len(cases)), "#0c1230"),
            "Open Cases":  (str(sum(1 for c in cases if c["status"] == "Filed")), "#2563eb"),
            "Closed Cases":(str(sum(1 for c in cases if c["status"] == "Closed")), "#16a34a"),
            "Pending Review":(str(sum(1 for c in cases if c["status"] not in ("Filed","Closed"))), "#d97706"),
        }
        for label, (val, color) in stat_counts.items():
            card = QFrame()
            card.setStyleSheet("background:#ffffff;border:1px solid #dfe3ee;border-radius:10px;")
            cl = QVBoxLayout(card)
            cl.setContentsMargins(16, 14, 16, 14)
            v = QLabel(val)
            v.setStyleSheet(f"color:{color};font-size:24px;font-weight:700;")
            cl.addWidget(v)
            l2 = QLabel(label)
            l2.setStyleSheet("color:#8a92ab;font-size:11px;font-weight:600;")
            cl.addWidget(l2)
            stat_row.addWidget(card)
        content.addLayout(stat_row)

        # Middle row: Activity + Docket
        mid_row = QHBoxLayout()
        mid_row.setSpacing(16)

        activity_card = QFrame()
        activity_card.setStyleSheet(
            "background:#ffffff;border:1px solid #dfe3ee;border-radius:10px;"
        )
        ac_layout = QVBoxLayout(activity_card)
        ac_layout.setContentsMargins(18, 16, 18, 16)
        ac_title = QLabel("Recent Case Activity")
        ac_title.setStyleSheet("color:#1b2240;font-size:14px;font-weight:700;")
        ac_layout.addWidget(ac_title)
        self.list_activity = QListWidget()
        self.list_activity.setStyleSheet(
            "background:transparent;border:none;color:#1b2240;font-size:12px;"
        )
        self._refresh_activity()
        ac_layout.addWidget(self.list_activity)
        mid_row.addWidget(activity_card)

        docket_card = QFrame()
        docket_card.setFixedWidth(260)
        docket_card.setStyleSheet(
            "background:#ffffff;border:1px solid #dfe3ee;border-radius:10px;"
        )
        dc_layout = QVBoxLayout(docket_card)
        dc_layout.setContentsMargins(18, 16, 18, 16)
        dc_title = QLabel("Docket Summary")
        dc_title.setStyleSheet("color:#1b2240;font-size:14px;font-weight:700;")
        dc_layout.addWidget(dc_title)
        self.list_docket = QListWidget()
        self.list_docket.setStyleSheet(
            "background:transparent;border:none;color:#1b2240;font-size:12px;"
        )
        self._refresh_docket()
        dc_layout.addWidget(self.list_docket)
        mid_row.addWidget(docket_card)
        content.addLayout(mid_row)

        # Alert banner
        alert = QFrame()
        alert.setStyleSheet(
            "background:#fef3e8;border:1px solid #f3d9b1;border-radius:10px;"
        )
        al = QVBoxLayout(alert)
        al.setContentsMargins(16, 12, 16, 12)
        al_title = QLabel("⚠ System Integrity Alert")
        al_title.setStyleSheet("color:#b45309;font-size:12px;font-weight:700;")
        al.addWidget(al_title)
        al_body = QLabel(
            "A scheduled maintenance window is planned. "
            "Some services may be temporarily unavailable."
        )
        al_body.setWordWrap(True)
        al_body.setStyleSheet("color:#92651b;font-size:11px;")
        al.addWidget(al_body)
        content.addWidget(alert)
        content.addStretch()

        main_col.addLayout(content)
        root.addLayout(main_col)

    def _refresh_activity(self):
        self.list_activity.clear()
        timeline = load_data("timeline")
        for entry in reversed(timeline[-10:]):
            self.list_activity.addItem(
                f"{entry['event']}  —  Case #{entry['case_id']}  ({entry['date']})"
            )

    def _refresh_docket(self):
        self.list_docket.clear()
        cases = load_data("cases")
        from collections import Counter
        counts = Counter(c["status"] for c in cases)
        for status, count in counts.items():
            self.list_docket.addItem(f"{status}: {count}")

    def showEvent(self, event):
        self._refresh_activity()
        self._refresh_docket()
        super().showEvent(event)

    def _new_case(self):
        self.app.show_add_case()


# ─────────────────────────────────────────────
#  ADMIN PANEL  (admin_panel.ui)
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
#  DELETE CONFIRMATION  (delete_confirmation.ui)
# ─────────────────────────────────────────────

class DeleteConfirmationDialog(QDialog, Ui_DeleteConfirmationDialog):
    """Generic 'Are you sure?' dialog. Cancel/Confirm are auto-wired to
    reject()/accept() via the .ui file's own <connections> block."""

    def __init__(self, parent=None, title="Are you sure?",
                 subtitle="This will permanently delete the selected item. "
                           "This action cannot be undone."):
        super().__init__(parent)
        self.setupUi(self)
        self.titleLabel.setText(title)
        self.subtitleLabel.setText(subtitle)


# ─────────────────────────────────────────────
#  LOGOUT CONFIRMATION  (logout_confirmation.ui)
# ─────────────────────────────────────────────

class LogoutConfirmDialog(QDialog, Ui_LogoutConfirmDialog):
    """'Log Out?' dialog. Cancel/Log Out are auto-wired to reject()/accept()
    via the .ui file's own <connections> block."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


# ─────────────────────────────────────────────
#  CREATE USER  (create_user.ui)
# ─────────────────────────────────────────────

class CreateUserDialog(QDialog, Ui_CreateUserDialog):
    def __init__(self, app_controller, parent=None):
        super().__init__(parent)
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnCreateUser.clicked.connect(self._submit)
        # btnCancel -> reject() is wired in the .ui file itself.

        # Sidebar nav shortcuts: close this dialog and jump to the
        # corresponding admin screen.
        self.navAssignJudge.clicked.connect(lambda: self._jump(self.app.show_assign_judge))
        self.navAssignLawyer.clicked.connect(lambda: self._jump(self.app.show_assign_lawyer))
        self.navViewUsers.clicked.connect(lambda: self._jump(self.app.show_admin_panel))
        # navCreateUser is the active page already – no-op.

    def _jump(self, callback):
        self.reject()
        callback()

    def _submit(self):
        username = self.inputUsername.text().strip()
        password = self.inputPassword.text().strip()
        role = self.comboRole.currentText().strip()

        if not username or not password:
            QMessageBox.warning(self, "Validation", "Username and password are required.")
            return
        if any(u["username"] == username for u in load_data("users")):
            QMessageBox.warning(self, "Validation", f"User '{username}' already exists.")
            return

        create_user(username, password, role)
        if self.app.current_user:
            add_audit(self.app.current_user["username"], f"Created user '{username}' ({role})")
        QMessageBox.information(self, "Success", f"User '{username}' created.")
        self.accept()


# ─────────────────────────────────────────────
#  DELETE USER  (delete_user.ui)
# ─────────────────────────────────────────────

class DeleteUserDialog(QDialog, Ui_DeleteUserDialog):
    def __init__(self, app_controller, parent=None):
        super().__init__(parent)
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.checkConfirm.stateChanged.connect(
            lambda state: self.btnDeleteUser.setEnabled(bool(state))
        )
        self.btnDeleteUser.clicked.connect(self._submit)
        # btnCancel -> reject() is wired in the .ui file itself.

        self.navAssignJudge.clicked.connect(lambda: self._jump(self.app.show_assign_judge))
        self.navAssignLawyer.clicked.connect(lambda: self._jump(self.app.show_assign_lawyer))
        self.navCreateUser.clicked.connect(self._jump_create_user)
        # navViewUsers is the active page already – no-op.

    def _jump(self, callback):
        self.reject()
        callback()

    def _jump_create_user(self):
        self.reject()
        dlg = CreateUserDialog(self.app, parent=self.app)
        dlg.exec_()

    def _submit(self):
        username = self.inputSearchUsername.text().strip()
        if not username:
            QMessageBox.warning(self, "Validation", "Enter a username to delete.")
            return
        if not any(u["username"] == username for u in load_data("users")):
            QMessageBox.warning(self, "Validation", f"User '{username}' not found.")
            return

        confirm = DeleteConfirmationDialog(
            self,
            title="Delete this user?",
            subtitle=f"This will permanently delete '{username}' and all associated data. "
                     f"This action cannot be undone.",
        )
        if confirm.exec_() == QDialog.Accepted:
            delete_user(username)
            if self.app.current_user:
                add_audit(self.app.current_user["username"], f"Deleted user '{username}'")
            QMessageBox.information(self, "Success", f"User '{username}' deleted.")
            self.accept()


class AdminPanelWidget(QWidget):
    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setStyleSheet(f"background:{LIGHT_BG};color:#1b2240;font-family:'Inter';")
        self._build_ui()

    def _build_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        nav_items = [
            ("Dashboard", "dashboard"), ("Cases", "cases"),
            ("Judges", "judges"), ("Lawyers", "lawyers"),
            ("Users", "users"), ("Settings", "settings"),
        ]
        sidebar, btns = make_sidebar(nav_items, on_new_case=self._new_case)
        btns["dashboard"].clicked.connect(lambda: self.app.show_admin_dashboard())
        btns["cases"].clicked.connect(lambda: self.app.show_admin_panel())
        btns["judges"].clicked.connect(lambda: self.app.show_assign_judge())
        btns["lawyers"].clicked.connect(lambda: self.app.show_assign_lawyer())
        root.addWidget(sidebar)

        content = QVBoxLayout()
        content.setContentsMargins(28, 24, 28, 24)
        content.setSpacing(18)

        # Welcome row
        top_row = QHBoxLayout()
        self.lbl_welcome = QLabel("Welcome, Admin")
        self.lbl_welcome.setStyleSheet("color:#1b2240;font-size:22px;font-weight:700;")
        top_row.addWidget(self.lbl_welcome)
        top_row.addStretch()
        search = QLineEdit()
        search.setPlaceholderText("Search anything...")
        search.setFixedWidth(260)
        search.setStyleSheet(
            "background:#ffffff;border:1px solid #dfe3ee;border-radius:8px;padding:8px 14px;"
        )
        top_row.addWidget(search)
        content.addLayout(top_row)

        # Action grid – maps exactly to admin_panel.ui cards
        actions = [
            ("📊", "Dashboard",      self.app.show_admin_dashboard),
            ("📁", "Add Case",       self.app.show_add_case),
            ("🔍", "Search Case",    self._search_case),
            ("📋", "View Cases",     self.app.show_view_cases),
            ("⚖️", "Assign Judge",   self.app.show_assign_judge),
            ("👨‍⚖️","Add Lawyer",    self.app.show_assign_lawyer),
            ("➕", "Create User",    self._create_user),
            ("👥", "View Users",     self._view_users),
            ("🗑️", "Delete User",   self._delete_user),
            ("🔑", "Reset Password", self._reset_password),
        ]

        grid = QGridLayout()
        grid.setHorizontalSpacing(16)
        grid.setVerticalSpacing(16)

        for idx, (icon, label, callback) in enumerate(actions):
            row, col = divmod(idx, 3)
            card = QFrame()
            card.setStyleSheet(
                "background:#ffffff;border:1px solid #dfe3ee;border-radius:10px;"
            )
            card.setCursor(Qt.PointingHandCursor)
            cl = QVBoxLayout(card)
            cl.setContentsMargins(16, 16, 16, 16)
            icon_lbl = QLabel(icon)
            icon_lbl.setStyleSheet("font-size:22px;")
            cl.addWidget(icon_lbl)
            txt_lbl = QLabel(label)
            txt_lbl.setStyleSheet("color:#1b2240;font-size:13px;font-weight:700;")
            cl.addWidget(txt_lbl)
            # Make the whole card clickable (mouse events on the icon/label
            # children bubble up to the frame when they're left unhandled).
            card.mousePressEvent = lambda event, cb=callback: cb()
            grid.addWidget(card, row, col)

        content.addLayout(grid)
        content.addStretch()
        root.addLayout(content)

    def _new_case(self):
        self.app.show_add_case()

    def _search_case(self):
        self.app.show_search_case()

    def _create_user(self):
        dlg = CreateUserDialog(self.app, parent=self)
        dlg.exec_()

    def _view_users(self):
        self.app.show_view_users()

    def _delete_user(self):
        dlg = DeleteUserDialog(self.app, parent=self)
        dlg.exec_()

    def _reset_password(self):
        self.app.show_reset_password()

    def showEvent(self, event):
        """Update welcome label with the logged-in user's name."""
        if self.app.current_user:
            self.lbl_welcome.setText(
                f"Welcome, {self.app.current_user.get('username', 'Admin')}"
            )
        super().showEvent(event)


# ─────────────────────────────────────────────
#  ADD CASE  (inline dialog-style screen)
# ─────────────────────────────────────────────

class AddCaseWidget(QWidget, Ui_FileNewCaseForm):
    """Loads file_new_case.ui (Qt Designer) and wires it to add_case() logic."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        # Top bar icon buttons – simple placeholders
        self.btnMenu.clicked.connect(self._cancel)
        self.btnUserAvatar.clicked.connect(self._show_profile)

        self.btnSubmitCase.clicked.connect(self._submit)
        self.btnCancel.clicked.connect(self._cancel)

    def _show_profile(self):
        user = self.app.current_user or {}
        QMessageBox.information(
            self, "Profile",
            f"Logged in as: {user.get('username', '-')}\nRole: {user.get('role', '-')}"
        )

    def refresh(self):
        """Call before showing this page so it starts from a clean slate."""
        self.comboCategory.setCurrentIndex(0)
        self.comboPriorityLevel.setCurrentIndex(0)
        self.txtCaseTitle.clear()
        self.txtClientName.clear()
        self.txtCaseDescription.clear()

    def _submit(self):
        title = self.txtCaseTitle.text().strip()
        description = self.txtCaseDescription.toPlainText().strip()
        category = self.comboCategory.currentText().strip()
        priority = self.comboPriorityLevel.currentText().strip()
        client = self.txtClientName.text().strip()

        if not title:
            QMessageBox.warning(self, "Validation", "Case title is required.")
            return
        if category in ("", "Select Category"):
            category = ""

        cid = add_case(title=title, description=description,
                        category=category, priority=priority, client=client)
        if self.app.current_user:
            add_audit(self.app.current_user["username"], f"Added case #{cid}")
        QMessageBox.information(self, "Success", f"Case #{cid} filed successfully.")
        self._return_to_caller()

    def _cancel(self):
        self._return_to_caller()

    def _return_to_caller(self):
        self.app.show_role_dashboard()


# ─────────────────────────────────────────────
#  ASSIGN JUDGE  (assign_judge.ui)
# ─────────────────────────────────────────────

class AssignJudgeWidget(QWidget):
    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setStyleSheet(
            f"QWidget#AssignJudgeWidget{{background:{DARK_BG};color:{TEXT_MAIN};font-family:'Inter';}}"
        )
        self.setObjectName("AssignJudgeWidget")
        self._build_ui()

    def _build_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(20)

        # Left column
        left = QVBoxLayout()
        left.setSpacing(12)

        breadcrumb = QLabel("Legal Management")
        breadcrumb.setStyleSheet(f"color:{ACCENT};font-size:12px;")
        left.addWidget(breadcrumb)

        page_title = QLabel("Assign Judge")
        page_title.setStyleSheet("color:#ffffff;font-size:22px;font-weight:600;")
        left.addWidget(page_title)

        subtitle = QLabel(
            "Allocate judicial authority to pending cases within the jurisdiction. "
            "Ensure all conflict-of-interest checks are completed before finalization."
        )
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet(f"color:{TEXT_MUTED};font-size:13px;")
        left.addWidget(subtitle)

        # Form card
        form_card = QFrame()
        form_card.setStyleSheet(
            f"background:{CARD_BG};border:1px solid {BORDER_COL};border-radius:10px;"
        )
        fc_layout = QVBoxLayout(form_card)
        fc_layout.setContentsMargins(20, 20, 20, 20)
        fc_layout.setSpacing(12)

        combo_row = QHBoxLayout()

        # Case combo
        case_col = QVBoxLayout()
        lbl_case = QLabel("CASE ID")
        lbl_case.setStyleSheet("color:#9aa3bd;font-size:11px;font-weight:600;")
        self.combo_case = QComboBox()
        self.combo_case.setStyleSheet(
            f"QComboBox{{background:{DARK_BG};border:1px solid #2c3566;"
            f"border-radius:6px;padding:6px 10px;color:#ffffff;}}"
        )
        case_col.addWidget(lbl_case)
        case_col.addWidget(self.combo_case)
        combo_row.addLayout(case_col)

        # Judge combo
        judge_col = QVBoxLayout()
        lbl_judge = QLabel("ASSIGN JUDGE")
        lbl_judge.setStyleSheet("color:#9aa3bd;font-size:11px;font-weight:600;")
        self.combo_judge = QComboBox()
        self.combo_judge.setStyleSheet(
            f"QComboBox{{background:{DARK_BG};border:1px solid #2c3566;"
            f"border-radius:6px;padding:6px 10px;color:#ffffff;}}"
        )
        judge_col.addWidget(lbl_judge)
        judge_col.addWidget(self.combo_judge)
        combo_row.addLayout(judge_col)
        fc_layout.addLayout(combo_row)

        # Current assignment info card
        info_card = QFrame()
        info_card.setStyleSheet(
            f"background:{DARK_BG};border:1px solid #2c3566;border-radius:8px;"
        )
        ic_l = QVBoxLayout(info_card)
        ic_l.setContentsMargins(14, 12, 14, 12)
        self.lbl_current_title = QLabel("Current Unassigned Cases")
        self.lbl_current_title.setStyleSheet("color:#ffffff;font-size:12px;font-weight:600;")
        ic_l.addWidget(self.lbl_current_title)
        self.lbl_current_judge = QLabel("Current Judge: None")
        self.lbl_current_judge.setStyleSheet(f"color:{TEXT_MUTED};font-size:12px;")
        ic_l.addWidget(self.lbl_current_judge)
        fc_layout.addWidget(info_card)

        # Update label when case changes
        self.combo_case.currentIndexChanged.connect(self._on_case_changed)

        # Buttons
        btn_row = QHBoxLayout()
        btn_assign = styled_btn("Assign Judge")
        btn_assign.clicked.connect(self._do_assign)
        btn_cancel = styled_btn("Cancel", primary=False)
        btn_cancel.clicked.connect(lambda: self.app.show_admin_panel())
        btn_row.addWidget(btn_assign)
        btn_row.addWidget(btn_cancel)
        btn_row.addStretch()
        fc_layout.addLayout(btn_row)

        left.addWidget(form_card)
        left.addStretch()
        root.addLayout(left)

        # Right column
        right = QVBoxLayout()
        right.setSpacing(16)

        # Workload card
        wl_card = QFrame()
        wl_card.setStyleSheet(
            f"background:{CARD_BG};border:1px solid {BORDER_COL};border-radius:10px;"
        )
        wl_l = QVBoxLayout(wl_card)
        wl_l.setContentsMargins(16, 16, 16, 16)
        wl_title = QLabel("Workload Overview")
        wl_title.setStyleSheet("color:#ffffff;font-size:14px;font-weight:600;")
        wl_l.addWidget(wl_title)
        unassigned_row = QHBoxLayout()
        unassigned_lbl = QLabel("Unassigned Cases")
        unassigned_lbl.setStyleSheet(f"color:{TEXT_MUTED};font-size:12px;")
        unassigned_row.addWidget(unassigned_lbl)
        self.lbl_unassigned_count = QLabel("0")
        self.lbl_unassigned_count.setStyleSheet(
            "color:#ff6b6b;font-weight:700;font-size:16px;"
        )
        unassigned_row.addWidget(self.lbl_unassigned_count)
        wl_l.addLayout(unassigned_row)
        wl_note = QLabel("Heavy sign-off review queue this week.")
        wl_note.setWordWrap(True)
        wl_note.setStyleSheet(f"color:{TEXT_MUTED};font-size:11px;")
        wl_l.addWidget(wl_note)
        right.addWidget(wl_card)

        # Available judges card
        judges_card = QFrame()
        judges_card.setStyleSheet(
            f"background:{CARD_BG};border:1px solid {BORDER_COL};border-radius:10px;"
        )
        jc_l = QVBoxLayout(judges_card)
        jc_l.setContentsMargins(16, 16, 16, 16)
        jc_title = QLabel("Available Judges")
        jc_title.setStyleSheet("color:#ffffff;font-size:14px;font-weight:600;")
        jc_l.addWidget(jc_title)
        self.list_judges = QListWidget()
        self.list_judges.setStyleSheet(
            f"background:transparent;border:none;color:{TEXT_MAIN};font-size:12px;"
        )
        jc_l.addWidget(self.list_judges)
        right.addWidget(judges_card)
        right.addStretch()
        root.addLayout(right)

    def showEvent(self, event):
        self._refresh()
        super().showEvent(event)

    def _refresh(self):
        self.combo_case.clear()
        self.combo_case.addItem("Select pending case...")
        cases = load_data("cases")
        unassigned = [c for c in cases if not c.get("judge")]
        self.lbl_unassigned_count.setText(str(len(unassigned)))
        for c in cases:
            self.combo_case.addItem(f"#{c['id']} – {c['title']}", c["id"])

        self.combo_judge.clear()
        self.combo_judge.addItem("Select a judge...")
        users = load_data("users")
        self.list_judges.clear()
        for u in users:
            if u["role"] == "Judge":
                self.combo_judge.addItem(u["username"])
                self.list_judges.addItem(f"Hon. {u['username']}")

    def _on_case_changed(self, idx):
        if idx <= 0:
            self.lbl_current_judge.setText("Current Judge: None")
            return
        case_id = self.combo_case.itemData(idx)
        for c in load_data("cases"):
            if c["id"] == case_id:
                self.lbl_current_judge.setText(
                    f"Current Judge: {c['judge'] or 'None'}"
                )

    def _do_assign(self):
        if self.combo_case.currentIndex() <= 0 or self.combo_judge.currentIndex() <= 0:
            QMessageBox.warning(self, "Validation", "Please select a case and a judge.")
            return
        case_id = self.combo_case.currentData()
        judge_name = self.combo_judge.currentText()
        assign_judge(case_id, judge_name)
        add_audit(self.app.current_user["username"],
                  f"Assigned judge {judge_name} to case #{case_id}")
        QMessageBox.information(self, "Success",
                                f"Judge '{judge_name}' assigned to case #{case_id}.")
        self._refresh()


# ─────────────────────────────────────────────
#  ASSIGN LAWYER  (assign_lawyer.ui)
# ─────────────────────────────────────────────

class AssignLawyerWidget(QWidget):
    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setStyleSheet(
            f"QWidget#AssignLawyerWidget{{background:{DARK_BG};color:{TEXT_MAIN};font-family:'Inter';}}"
        )
        self.setObjectName("AssignLawyerWidget")
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(10)

        breadcrumb = QLabel("Admin Panel  /  Legal Management")
        breadcrumb.setStyleSheet(f"color:{TEXT_MUTED};font-size:12px;")
        root.addWidget(breadcrumb)

        page_title = QLabel("Legal Representation Assignment")
        page_title.setStyleSheet("color:#ffffff;font-size:22px;font-weight:600;")
        root.addWidget(page_title)

        subtitle = QLabel(
            "Assign specialized legal counsel to active case files. "
            "Ensure all conflict checks are completed before submission."
        )
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet(f"color:{TEXT_MUTED};font-size:13px;")
        root.addWidget(subtitle)

        form_card = QFrame()
        form_card.setStyleSheet(
            f"background:{CARD_BG};border:1px solid {BORDER_COL};border-radius:10px;"
        )
        fc_l = QVBoxLayout(form_card)
        fc_l.setContentsMargins(24, 24, 24, 24)
        fc_l.setSpacing(18)

        # Case selection row
        case_row = QHBoxLayout()
        case_col = QVBoxLayout()
        lbl_case = QLabel("CASE SELECTION")
        lbl_case.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
        self.combo_case = QComboBox()
        self.combo_case.setStyleSheet(
            f"QComboBox{{background:{DARK_BG};border:1px solid #2c3566;"
            f"border-radius:6px;padding:6px 10px;color:#ffffff;}}"
        )
        self.combo_case.currentIndexChanged.connect(self._on_case_changed)
        case_col.addWidget(lbl_case)
        case_col.addWidget(self.combo_case)
        case_row.addLayout(case_col)

        meta_col = QVBoxLayout()
        self.lbl_case_id_tag = QLabel("CASE-ID    CR-2024-XXXX")
        self.lbl_case_id_tag.setStyleSheet(f"color:{TEXT_MUTED};font-size:11px;")
        self.lbl_case_date_tag = QLabel("FILED    --/--/----")
        self.lbl_case_date_tag.setStyleSheet(f"color:{TEXT_MUTED};font-size:11px;")
        meta_col.addWidget(self.lbl_case_id_tag)
        meta_col.addWidget(self.lbl_case_date_tag)
        case_row.addLayout(meta_col)
        fc_l.addLayout(case_row)

        # Lawyer selection row
        lawyer_row = QHBoxLayout()
        lawyer_col = QVBoxLayout()
        lbl_lawyer = QLabel("SELECT LAWYER")
        lbl_lawyer.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
        self.combo_lawyer = QComboBox()
        self.combo_lawyer.setStyleSheet(
            f"QComboBox{{background:{DARK_BG};border:1px solid #2c3566;"
            f"border-radius:6px;padding:6px 10px;color:#ffffff;}}"
        )
        self.combo_lawyer.currentIndexChanged.connect(self._on_lawyer_changed)
        lawyer_col.addWidget(lbl_lawyer)
        lawyer_col.addWidget(self.combo_lawyer)
        lawyer_row.addLayout(lawyer_col)

        lmeta_col = QVBoxLayout()
        self.lbl_spec = QLabel("SPECIALIZATION    --")
        self.lbl_spec.setStyleSheet(f"color:{TEXT_MUTED};font-size:11px;")
        self.lbl_lit = QLabel("LITIGATION    Branch 4")
        self.lbl_lit.setStyleSheet(f"color:{TEXT_MUTED};font-size:11px;")
        lmeta_col.addWidget(self.lbl_spec)
        lmeta_col.addWidget(self.lbl_lit)
        lawyer_row.addLayout(lmeta_col)
        fc_l.addLayout(lawyer_row)

        # Preview
        preview = QFrame()
        preview.setStyleSheet(
            f"background:{DARK_BG};border:1px solid #2c3566;border-radius:8px;"
        )
        pv_l = QVBoxLayout(preview)
        pv_l.setContentsMargins(16, 14, 16, 14)
        pv_title = QLabel("ASSIGNMENT PREVIEW")
        pv_title.setStyleSheet(f"color:{ACCENT};font-size:12px;font-weight:600;")
        pv_l.addWidget(pv_title)
        self.lbl_preview = QLabel("Select a case and lawyer above.")
        self.lbl_preview.setStyleSheet(f"color:{TEXT_MUTED};font-size:12px;")
        pv_l.addWidget(self.lbl_preview)
        fc_l.addWidget(preview)

        # Buttons
        btn_row = QHBoxLayout()
        btn_assign = styled_btn("Confirm and Assign Lawyer")
        btn_assign.clicked.connect(self._do_assign)
        btn_cancel = styled_btn("Cancel", primary=False)
        btn_cancel.clicked.connect(lambda: self.app.show_admin_panel())
        btn_row.addWidget(btn_assign)
        btn_row.addWidget(btn_cancel)
        fc_l.addLayout(btn_row)

        root.addWidget(form_card)
        root.addStretch()

    def showEvent(self, event):
        self._refresh()
        super().showEvent(event)

    def _refresh(self):
        self.combo_case.clear()
        self.combo_case.addItem("Select an active case...")
        for c in load_data("cases"):
            self.combo_case.addItem(f"#{c['id']} – {c['title']}", c["id"])

        self.combo_lawyer.clear()
        self.combo_lawyer.addItem("Choose lawyer to assign...")
        for u in load_data("users"):
            if u["role"] == "Lawyer":
                self.combo_lawyer.addItem(u["username"])

    def _on_case_changed(self, idx):
        if idx <= 0:
            self.lbl_case_id_tag.setText("CASE-ID    CR-2024-XXXX")
            self.lbl_case_date_tag.setText("FILED    --/--/----")
            return
        case_id = self.combo_case.itemData(idx)
        for c in load_data("cases"):
            if c["id"] == case_id:
                self.lbl_case_id_tag.setText(f"CASE-ID    #{c['id']}")
                self.lbl_case_date_tag.setText(f"FILED    {c['filing_date'][:10]}")
        self._update_preview()

    def _on_lawyer_changed(self, idx):
        if idx > 0:
            self.lbl_spec.setText(f"SPECIALIZATION    General")
        self._update_preview()

    def _update_preview(self):
        case_txt = self.combo_case.currentText() if self.combo_case.currentIndex() > 0 else "—"
        lawyer_txt = self.combo_lawyer.currentText() if self.combo_lawyer.currentIndex() > 0 else "—"
        self.lbl_preview.setText(f"Case: {case_txt}  →  Lawyer: {lawyer_txt}")

    def _do_assign(self):
        if self.combo_case.currentIndex() <= 0 or self.combo_lawyer.currentIndex() <= 0:
            QMessageBox.warning(self, "Validation", "Please select a case and a lawyer.")
            return
        case_id = self.combo_case.currentData()
        lawyer_name = self.combo_lawyer.currentText()
        assign_lawyer(case_id, lawyer_name)
        add_audit(self.app.current_user["username"],
                  f"Assigned lawyer {lawyer_name} to case #{case_id}")
        QMessageBox.information(self, "Success",
                                f"Lawyer '{lawyer_name}' assigned to case #{case_id}.")
        self._refresh()


# ─────────────────────────────────────────────
#  CASE DETAILS  (case_details.ui)
# ─────────────────────────────────────────────

class CaseDetailsWidget(QWidget):
    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self._case = None
        self.setStyleSheet(
            f"QWidget#CaseDetailsWidget{{background:{DARK_BG};color:{TEXT_MAIN};font-family:'Inter';}}"
        )
        self.setObjectName("CaseDetailsWidget")
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setSpacing(0)
        root.setContentsMargins(0, 0, 0, 0)

        # Header
        header_row = QHBoxLayout()
        header_row.setContentsMargins(16, 14, 16, 10)
        lbl_hdr = QLabel("Case Details")
        lbl_hdr.setStyleSheet("color:#ffffff;font-size:14px;font-weight:600;")
        header_row.addWidget(lbl_hdr)
        header_row.addStretch()
        btn_back = QPushButton("Back to Cases")
        btn_back.setStyleSheet(
            f"QPushButton{{background:transparent;color:{ACCENT};"
            f"border:1px solid #2c3566;border-radius:6px;padding:4px 10px;font-size:11px;}}"
        )
        btn_back.clicked.connect(lambda: self.app.show_admin_panel())
        header_row.addWidget(btn_back)
        root.addLayout(header_row)

        # Title block
        title_block = QVBoxLayout()
        title_block.setContentsMargins(16, 0, 16, 10)
        self.lbl_case_title = QLabel("Case Title")
        self.lbl_case_title.setStyleSheet(
            f"color:{ACCENT};font-size:18px;font-weight:700;"
        )
        title_block.addWidget(self.lbl_case_title)
        self.lbl_matter_num = QLabel("Matter #—")
        self.lbl_matter_num.setStyleSheet(f"color:{TEXT_MUTED};font-size:12px;")
        title_block.addWidget(self.lbl_matter_num)
        root.addLayout(title_block)

        # Case ID card
        id_card = QFrame()
        id_card.setStyleSheet(
            f"background:{CARD_BG};border:1px solid {BORDER_COL};border-radius:10px;"
        )
        ic_l = QVBoxLayout(id_card)
        ic_l.setContentsMargins(16, 14, 16, 14)
        ic_l.setSpacing(10)

        # Case ID + badge row
        id_row = QHBoxLayout()
        id_col = QVBoxLayout()
        id_fld = QLabel("CASE ID")
        id_fld.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
        id_col.addWidget(id_fld)
        self.lbl_case_id_val = QLabel("—")
        self.lbl_case_id_val.setStyleSheet("color:#ffffff;font-size:16px;font-weight:700;")
        id_col.addWidget(self.lbl_case_id_val)
        id_row.addLayout(id_col)
        id_row.addStretch()
        self.badge_status = QLabel("Active")
        self.badge_status.setStyleSheet(
            "background:#1f8a4c;color:#ffffff;font-size:10px;"
            "font-weight:600;border-radius:8px;padding:2px 10px;"
        )
        id_row.addWidget(self.badge_status)
        ic_l.addLayout(id_row)

        # Description
        desc_fld = QLabel("DESCRIPTION")
        desc_fld.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
        ic_l.addWidget(desc_fld)
        self.lbl_desc = QLabel("—")
        self.lbl_desc.setWordWrap(True)
        self.lbl_desc.setStyleSheet(f"color:{TEXT_MAIN};font-size:12px;")
        ic_l.addWidget(self.lbl_desc)

        # Category + Priority
        cat_pri_row = QHBoxLayout()
        for fld_lbl_name, attr in [("CATEGORY", "lbl_category"), ("PRIORITY", "lbl_priority")]:
            col = QVBoxLayout()
            fld = QLabel(fld_lbl_name)
            fld.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
            col.addWidget(fld)
            val = QLabel("—")
            val.setStyleSheet(f"color:{TEXT_MAIN};font-size:12px;")
            col.addWidget(val)
            setattr(self, attr, val)
            cat_pri_row.addLayout(col)
        ic_l.addLayout(cat_pri_row)

        # Judge + Lawyer
        jl_row = QHBoxLayout()
        for fld_lbl_name, attr in [("PRESIDING JUDGE", "lbl_judge"), ("LEAD LAWYER", "lbl_lawyer")]:
            col = QVBoxLayout()
            fld = QLabel(fld_lbl_name)
            fld.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
            col.addWidget(fld)
            val = QLabel("—")
            val.setStyleSheet(f"color:{TEXT_MAIN};font-size:12px;")
            col.addWidget(val)
            setattr(self, attr, val)
            jl_row.addLayout(col)
        ic_l.addLayout(jl_row)

        # Client + Filing Date
        cf_row = QHBoxLayout()
        for fld_lbl_name, attr in [("CLIENT", "lbl_client"), ("FILING DATE", "lbl_filing_date")]:
            col = QVBoxLayout()
            fld = QLabel(fld_lbl_name)
            fld.setStyleSheet("color:#6c7aa0;font-size:10px;font-weight:700;")
            col.addWidget(fld)
            val = QLabel("—")
            val.setStyleSheet(f"color:{TEXT_MAIN};font-size:12px;")
            col.addWidget(val)
            setattr(self, attr, val)
            cf_row.addLayout(col)
        ic_l.addLayout(cf_row)

        root.addWidget(id_card)

        # Tabs: Timeline / Hearings / Orders
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(
            f"QTabBar::tab{{background:transparent;color:{TEXT_MUTED};"
            f"padding:8px 14px;font-size:12px;}}"
            f"QTabBar::tab:selected{{color:{ACCENT};border-bottom:2px solid {ACCENT};}}"
            f"QTabWidget::pane{{border:none;background:{DARK_BG};}}"
        )

        # Timeline tab
        timeline_tab = QWidget()
        tl_l = QVBoxLayout(timeline_tab)
        self.list_timeline = QListWidget()
        self.list_timeline.setStyleSheet(
            f"background:transparent;border:none;color:{TEXT_MAIN};font-size:12px;"
        )
        tl_l.addWidget(self.list_timeline)
        self.tabs.addTab(timeline_tab, "Timeline")

        # Hearings tab
        hearings_tab = QWidget()
        hr_l = QVBoxLayout(hearings_tab)
        self.table_hearings = QTableWidget(0, 3)
        self.table_hearings.setHorizontalHeaderLabels(["Date", "Courtroom", "Remarks"])
        self.table_hearings.setStyleSheet(
            f"background:transparent;color:{TEXT_MAIN};font-size:12px;"
            f"gridline-color:{BORDER_COL};"
        )
        hr_l.addWidget(self.table_hearings)
        self.tabs.addTab(hearings_tab, "Hearings")

        # Orders tab
        orders_tab = QWidget()
        or_l = QVBoxLayout(orders_tab)
        self.list_orders = QListWidget()
        self.list_orders.setStyleSheet(
            f"background:transparent;border:none;color:{TEXT_MAIN};font-size:12px;"
        )
        or_l.addWidget(self.list_orders)
        self.tabs.addTab(orders_tab, "Orders")

        root.addWidget(self.tabs)

        # Bottom nav bar
        bottom_nav = QFrame()
        bottom_nav.setStyleSheet(
            f"background:{CARD_BG};border-top:1px solid {BORDER_COL};"
        )
        bn_l = QHBoxLayout(bottom_nav)
        bn_l.setContentsMargins(8, 8, 8, 8)
        for label, callback in [
            ("Judges", lambda: self.app.show_assign_judge()),
            ("Lawyers", lambda: self.app.show_assign_lawyer()),
            ("Cases", lambda: self.app.show_admin_panel()),
            ("Dashboard", lambda: self.app.show_role_dashboard()),
        ]:
            btn = QToolButton()
            btn.setText(label)
            btn.setStyleSheet(
                f"QToolButton{{background:transparent;color:{TEXT_MUTED};"
                f"font-size:10px;border:none;}}"
            )
            btn.clicked.connect(callback)
            bn_l.addWidget(btn)
        root.addWidget(bottom_nav)

    def load_case(self, case_id):
        cases = load_data("cases")
        case = next((c for c in cases if c["id"] == case_id), None)
        if not case:
            return
        self._case = case

        self.lbl_case_title.setText(case["title"])
        self.lbl_matter_num.setText(f"Matter #{case['id']}")
        self.lbl_case_id_val.setText(f"#{case['id']}")
        self.badge_status.setText(case["status"])
        self.lbl_desc.setText(case.get("description", "—"))
        self.lbl_category.setText(case.get("category", "—"))
        self.lbl_priority.setText(case.get("priority", "—"))
        self.lbl_judge.setText(case.get("judge") or "Unassigned")
        self.lbl_lawyer.setText(case.get("lawyer") or "Unassigned")
        self.lbl_client.setText(case.get("client", "—"))
        self.lbl_filing_date.setText(case.get("filing_date", "—")[:10])

        # Timeline
        self.list_timeline.clear()
        for t in load_data("timeline"):
            if t["case_id"] == case_id:
                self.list_timeline.addItem(f"{t['date']}  —  {t['event']}")

        # Hearings
        hearings = [h for h in load_data("hearings") if h["case_id"] == case_id]
        self.table_hearings.setRowCount(len(hearings))
        for row, h in enumerate(hearings):
            self.table_hearings.setItem(row, 0, QTableWidgetItem(h.get("date", "")))
            self.table_hearings.setItem(row, 1, QTableWidgetItem(h.get("courtroom", "")))
            self.table_hearings.setItem(row, 2, QTableWidgetItem(h.get("remarks", "")))

        # Orders
        self.list_orders.clear()
        for o in load_data("orders"):
            if o["case_id"] == case_id:
                self.list_orders.addItem(f"{o['date'][:10]}  —  {o['order']}")


# ─────────────────────────────────────────────
#  JUDGE PANEL  (re-uses existing screens)
# ─────────────────────────────────────────────

class IssueOrderDialog(QDialog, Ui_IssueOrderForm):
    """Loads issue_order__judge_.ui (Qt Designer) and wires it to issue_order() logic."""

    def __init__(self, app_controller, parent=None):
        super().__init__(parent)
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()
        self.refresh()

    def _wire_ui(self):
        self.btnIssueOrder.clicked.connect(self._submit)
        self.btnCancel.clicked.connect(self.reject)

    def refresh(self):
        cases = load_data("cases")
        self.comboCaseReference.clear()
        for c in cases:
            self.comboCaseReference.addItem(f"#{c['id']}  {c.get('title', '')}", c["id"])
        self.txtOrderInstructions.clear()

        drafts = sum(1 for c in cases if c.get("status") not in ("Closed",))
        self.lblDraftsValue.setText(str(drafts))
        hearings = load_data("hearings")
        self.lblCourtroomValue.setText(str(len(hearings)))

    def _submit(self):
        idx = self.comboCaseReference.currentIndex()
        if idx < 0:
            QMessageBox.warning(self, "Validation", "No case available to issue an order for.")
            return
        cid = self.comboCaseReference.currentData()
        order_text = self.txtOrderInstructions.toPlainText().strip()
        if not order_text:
            QMessageBox.warning(self, "Validation", "Order text is required.")
            return
        issue_order(cid, order_text)
        QMessageBox.information(self, "Success", "Order issued.")
        self.accept()


class JudgePanelWidget(QWidget, Ui_JudgePanelWidget):
    """Loads judge_panel.ui (Qt Designer) and wires it to app logic."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))

        self.navDashboardBtn.clicked.connect(lambda: None)  # already on dashboard
        self.navCasesBtn.clicked.connect(self._view_cases)
        self.navDocumentsBtn.clicked.connect(self._not_implemented)
        self.navMessagesBtn.clicked.connect(self._not_implemented)
        self.btnDateBadge.clicked.connect(lambda: None)
        self.btnUserAvatar.clicked.connect(self._show_profile)
        self.btnSecurityProtocolDetails.clicked.connect(self._not_implemented)

        for card, cb in [
            (self.cardViewCases, self._view_cases),
            (self.cardScheduleHearing, self._schedule_hearing),
            (self.cardIssueOrder, self._issue_order),
            (self.cardCaseDetails, self._view_case_details),
        ]:
            card.setCursor(Qt.PointingHandCursor)
            card.mousePressEvent = lambda event, cb=cb: cb()

    def refresh(self):
        cases = load_data("cases")
        hearings = load_data("hearings")
        self.labelUpcomingHearingsValue.setText(str(len(hearings)))
        orders = sum(1 for c in cases if c.get("status") == "Order Issued")
        self.labelRecentOrdersValue.setText(str(orders))

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)

    def _show_profile(self):
        user = self.app.current_user or {}
        QMessageBox.information(
            self, "Profile",
            f"Logged in as: {user.get('username', '-')}\nRole: {user.get('role', '-')}"
        )

    def _not_implemented(self):
        QMessageBox.information(self, "Coming Soon", "This feature is not yet available.")

    def _view_cases(self):
        self.app.show_view_cases()

    def _schedule_hearing(self):
        self.app.show_schedule_hearing()

    def _issue_order(self):
        dlg = IssueOrderDialog(self.app, self)
        dlg.exec_()

    def _view_case_details(self):
        cid, ok = QInputDialog.getInt(self, "Case Details", "Case ID:")
        if ok:
            self.app.show_case_details(cid)


# ─────────────────────────────────────────────
#  LAWYER PANEL
# ─────────────────────────────────────────────

class LawyerPanelWidget(QWidget, Ui_LawyerPanelWidget):
    """Loads lawyer_panel.ui (Qt Designer) and wires it to app logic."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))
        self.btnLogoutTop.clicked.connect(lambda: self.app.confirm_logout(self))

        self.navDashboardBtn.clicked.connect(lambda: None)  # already on dashboard
        self.navCasesBtn.clicked.connect(self._view_cases)
        self.navDocumentsBtn.clicked.connect(self._not_implemented)
        self.navMessagesBtn.clicked.connect(self._not_implemented)

        self.labelViewAll.setCursor(Qt.PointingHandCursor)
        self.labelViewAll.mousePressEvent = lambda event: self._view_cases()

        for card, cb in [
            (self.cardFileCase, self._file_case),
            (self.cardSearchCase, self._search_case),
            (self.cardTrackCase, self._track_case),
        ]:
            card.setCursor(Qt.PointingHandCursor)
            card.mousePressEvent = lambda event, cb=cb: cb()

    def refresh(self):
        username = (self.app.current_user or {}).get("username")
        my_cases = [c for c in load_data("cases") if c.get("client") == username] if username else []
        self.labelMyCasesValue.setText(str(len(my_cases)))

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)

    def _not_implemented(self):
        QMessageBox.information(self, "Coming Soon", "This feature is not yet available.")

    def _view_cases(self):
        self.app.show_view_cases()

    def _file_case(self):
        self.app.show_add_case()

    def _search_case(self):
        self.app.show_search_case()

    def _track_case(self):
        self.app.show_track_case_lawyer()
# ─────────────────────────────────────────────

class ClientPanelWidget(QWidget, Ui_ClientDashboardPage):
    """Loads client_pannel.ui (Qt Designer) and wires it to app logic."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))

        # Sidebar nav
        self.btnNavDashboard.clicked.connect(lambda: None)  # already on dashboard
        self.btnNavCases.clicked.connect(self._view_cases)
        self.btnNavDocuments.clicked.connect(self._not_implemented)
        self.btnNavMessages.clicked.connect(self._not_implemented)
        self.btnUserAvatar.clicked.connect(self._show_profile)

        # Action cards
        self.btnBrowseFiles.clicked.connect(self._view_cases)
        self.btnViewRoadmap.clicked.connect(self._track_case)
        self.btnCaseStatusInfo.clicked.connect(self._track_case)
        self.btnJoinMeeting.clicked.connect(self._not_implemented)
        self.btnViewAllVault.clicked.connect(self._not_implemented)

    def refresh(self):
        """Call before showing this page so it reflects the logged-in client."""
        user = self.app.current_user or {}
        username = user.get("username", "Client")
        self.lblWelcomeUser.setText(f"Welcome, {username}")

        my_cases = [c for c in load_data("cases") if c.get("client") == username]
        if my_cases:
            latest = my_cases[-1]
            self.lblCaseName.setText(f"{latest['title']} (#{latest['id']})")
            self.badgeInProgress.setText(latest.get("status", "Filed"))
        else:
            self.lblCaseName.setText("No cases on file")
            self.badgeInProgress.setText("—")

    def _show_profile(self):
        user = self.app.current_user or {}
        QMessageBox.information(
            self, "Profile",
            f"Logged in as: {user.get('username', '-')}\nRole: {user.get('role', '-')}"
        )

    def _not_implemented(self):
        QMessageBox.information(self, "Coming Soon", "This feature is not yet available.")

    def _view_cases(self):
        self.app.show_my_cases()

    def _track_case(self):
        self.app.show_track_case_client()


# ─────────────────────────────────────────────
#  MY CASES (CLIENT)  (my_cases__client_pannel_.ui)
# ─────────────────────────────────────────────

class MyCasesWidget(QWidget, Ui_MyCasesPage):
    """Client's full "My Cases" screen, wired from my_cases__client_pannel_.ui.

    The original .ui ships three hardcoded sample case cards; here the
    sidebar/top bar/stats shell is kept exactly as designed, while the case
    list itself is rebuilt from real data for the logged-in client each time
    the page is shown.
    """

    STATUS_BADGE_STYLES = {
        "Filed":       ("background-color:#3a2f1c; color:#f5a623;", "AWAITING DOCUMENTS"),
        "In Progress": ("background-color:#1d3b34; color:#3fcf8e;", "IN PROGRESS"),
        "Closed":      ("background-color:#23293a; color:#7c8794;", "CLOSED"),
    }

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))

        # Sidebar nav
        self.btnNavMyCases.clicked.connect(lambda: None)   # already on this page
        self.btnNavTrackCase.clicked.connect(self.app.show_track_case_client)

        # Top bar placeholders
        self.btnSearch.clicked.connect(self._not_implemented)
        self.btnNotifications.clicked.connect(self._not_implemented)
        self.btnUserAvatar.clicked.connect(self._show_profile)
        self.btnFilter.clicked.connect(self._not_implemented)
        self.btnSort.clicked.connect(self._not_implemented)

    def _not_implemented(self):
        QMessageBox.information(self, "Coming Soon", "This feature is not yet available.")

    def _show_profile(self):
        user = self.app.current_user or {}
        QMessageBox.information(
            self, "Profile",
            f"Logged in as: {user.get('username', '-')}\nRole: {user.get('role', '-')}"
        )

    def refresh(self):
        """Call before showing this page so it reflects the logged-in client."""
        user = self.app.current_user or {}
        username = user.get("username", "Client")
        self.lblUserName.setText(username)
        initials = "".join(part[0].upper() for part in username.split()[:2]) or "U"
        self.btnUserAvatar.setText(initials)

        cases = [c for c in load_data("cases") if c.get("client") == username]
        total = len(cases)
        active = sum(1 for c in cases if c.get("status") not in ("Closed",))
        self.lblTotalCasesValue.setText(f"{total:02d}")
        self.lblActiveCasesValue.setText(f"{active:02d}")

        self._populate_case_list(cases)

    def _clear_case_list(self):
        # Remove every card widget except the empty-state label, which is
        # kept around (hidden) so it doesn't need to be rebuilt each time.
        layout = self.caseListLayout
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget is not None and widget is not self.lblEmptyState:
                widget.setParent(None)

    def _populate_case_list(self, cases):
        self._clear_case_list()

        if not cases:
            self.lblEmptyState.setVisible(True)
            return
        self.lblEmptyState.setVisible(False)

        hearings = load_data("hearings")
        for c in cases:
            card = self._build_case_card(c, hearings)
            self.caseListLayout.addWidget(card)

    def _build_case_card(self, case, hearings):
        badge_style, default_label = self.STATUS_BADGE_STYLES.get(
            case.get("status", "Filed"), self.STATUS_BADGE_STYLES["Filed"]
        )
        badge_text = case.get("status", default_label).upper()

        card = QFrame()
        card.setStyleSheet(
            "QFrame{background-color:#111827;border-radius:12px;}"
        )
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(8)
        card_layout.setContentsMargins(18, 14, 18, 14)

        # Top row: title + status badge + priority badge
        top_row = QHBoxLayout()
        lbl_title = QLabel(f"{case.get('title', 'Untitled Case')}")
        lbl_title.setStyleSheet("color:#ffffff; font-size:15px; font-weight:700;")
        top_row.addWidget(lbl_title)

        badge_status = QLabel(badge_text)
        badge_status.setStyleSheet(
            f"{badge_style} font-size:10px; font-weight:700; border-radius:9px; padding:3px 9px; margin-left:10px;"
        )
        top_row.addWidget(badge_status)

        if case.get("priority") == "High":
            badge_priority = QLabel("HIGH PRIORITY")
            badge_priority.setStyleSheet(
                "background-color:#3a1f24; color:#f0556b; font-size:10px; "
                "font-weight:700; border-radius:9px; padding:3px 9px; margin-left:6px;"
            )
            top_row.addWidget(badge_priority)

        top_row.addStretch()
        card_layout.addLayout(top_row)

        # Mid row: next hearing + filing date
        mid_row = QHBoxLayout()
        case_hearings = [h for h in hearings if h.get("case_id") == case.get("id")]
        next_hearing_text = case_hearings[-1].get("date", "N/A") if case_hearings else "N/A"
        lbl_next_hearing = QLabel(f"Next Hearing: {next_hearing_text}")
        lbl_next_hearing.setStyleSheet("color:#9aa1ac; font-size:12px;")
        mid_row.addWidget(lbl_next_hearing)

        filing_date = case.get("filing_date", "")[:10] or "—"
        lbl_filing_date = QLabel(f"Filing Date: {filing_date}")
        lbl_filing_date.setStyleSheet("color:#9aa1ac; font-size:12px; margin-left:18px;")
        mid_row.addWidget(lbl_filing_date)

        mid_row.addStretch()
        card_layout.addLayout(mid_row)

        # Bottom row: view details button
        bottom_row = QHBoxLayout()
        bottom_row.addStretch()
        btn_view = QPushButton("VIEW DETAILS  →")
        btn_view.setCursor(Qt.PointingHandCursor)
        btn_view.setStyleSheet(
            "QPushButton{background-color:#1d2a52;color:#ffffff;border:none;"
            "border-radius:8px;padding:7px 14px;font-weight:600;font-size:11px;}"
            "QPushButton:hover{background-color:#243161;}"
        )
        cid = case["id"]
        btn_view.clicked.connect(lambda _, cid=cid: self.app.show_case_details(cid))
        bottom_row.addWidget(btn_view)
        card_layout.addLayout(bottom_row)

        return card

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  VIEW CASES WIDGET  (View_cases.ui)
# ─────────────────────────────────────────────

class ViewCasesWidget(QWidget, Ui_AllCasesWindow):
    """Full-screen All Cases table, wired from View_cases.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))
        self.btnNavDashboard.clicked.connect(self.app.show_role_dashboard)
        self.btnNavCases.clicked.connect(lambda: None)   # already on this page
        self.btnNavAddCase.clicked.connect(self.app.show_add_case)
        self.btnNavHearings.clicked.connect(lambda: None)
        self.btnNavUsers.clicked.connect(self.app.show_view_users)
        self.btnNavReports.clicked.connect(self.app.show_reports)
        self.btnCreateNewCase.clicked.connect(self.app.show_add_case)
        self.searchInput.textChanged.connect(self._on_search)
        self.btnFilters.clicked.connect(lambda: None)
        self.btnExportPdf.clicked.connect(lambda: QMessageBox.information(
            self, "Export", "PDF export is not yet implemented."))
        self.btnPrevPage.clicked.connect(lambda: None)
        self.btnNextPage.clicked.connect(lambda: None)

    def refresh(self):
        cases = load_data("cases")
        self._populate_table(cases)
        self.lblResultsCount.setText(f"Showing {len(cases)} case(s)")
        total = len(cases)
        closed = sum(1 for c in cases if c.get("status") == "Closed")
        hearings = load_data("hearings")
        pending_h = len(hearings)
        resolution = f"{int(closed / total * 100)}%" if total else "—"
        self.lblActiveCasesValue.setText(str(total))
        self.lblPendingHearingsValue.setText(str(pending_h))
        self.lblResolutionRateValue.setText(resolution)

    def _populate_table(self, cases):
        self.tableCases.setRowCount(len(cases))
        for row, c in enumerate(cases):
            self.tableCases.setItem(row, 0, QTableWidgetItem(f"#{c['id']}"))
            self.tableCases.setItem(row, 1, QTableWidgetItem(c.get("title", "")))
            self.tableCases.setItem(row, 2, QTableWidgetItem(c.get("status", "")))
            self.tableCases.setItem(row, 3, QTableWidgetItem(c.get("category", "")))
            btn = QPushButton("View")
            btn.setStyleSheet(
                "QPushButton{background:#0c1230;color:#f0b429;border-radius:4px;padding:4px 10px;}"
                "QPushButton:hover{background:#1a2247;}"
            )
            cid = c["id"]
            btn.clicked.connect(lambda _, cid=cid: self.app.show_case_details(cid))
            self.tableCases.setCellWidget(row, 4, btn)
        self.tableCases.resizeColumnsToContents()

    def _on_search(self, text):
        cases = load_data("cases")
        if text.strip():
            cases = [c for c in cases
                     if text.lower() in c.get("title", "").lower()
                     or text in str(c.get("id", ""))]
        self._populate_table(cases)
        self.lblResultsCount.setText(f"Showing {len(cases)} case(s)")

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  REPORTS WIDGET  (reports.ui)
# ─────────────────────────────────────────────

class ReportsWidget(QWidget, Ui_ReportsWidget):
    """Loads reports.ui (Qt Designer) and wires it to app logic."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.navLogout.clicked.connect(lambda: self.app.confirm_logout(self))
        self.signOutBtn.clicked.connect(lambda: self.app.confirm_logout(self))

        self.navDashboard.clicked.connect(self.app.show_role_dashboard)
        self.navCases.clicked.connect(self.app.show_view_cases)
        self.navReports.clicked.connect(lambda: None)   # already on this page
        self.createNewCaseBtn.clicked.connect(self.app.show_add_case)
        self.topNavCases.clicked.connect(self.app.show_view_cases)
        self.topNavReports.clicked.connect(lambda: None)  # already on this page

        for btn in (self.navCalendar, self.navDocuments, self.navSettings,
                    self.topNavFilings, self.exportReportBtn):
            btn.clicked.connect(self._not_implemented)

        for lbl in (self.casesByStatusMenu, self.trendBadgeExport, self.activityFilterIcon):
            lbl.setCursor(Qt.PointingHandCursor)
            lbl.mousePressEvent = lambda event: self._not_implemented()

    def refresh(self):
        cases = load_data("cases")
        total = len(cases)
        closed = sum(1 for c in cases if c.get("status") == "Closed")
        filed = total - closed
        self.donutCenterNumber.setText(str(total))
        self.valueFiled.setText(str(filed))
        self.valueClosed.setText(str(closed))

        audits = load_data("audit") or []
        rows = [self.tableRow1, self.tableRow2, self.tableRow3]
        fields = [
            (self.r1CaseNum, self.r1Activity, self.r1Details, self.r1PerformedBy, self.r1Status, self.r1Timestamp),
            (self.r2CaseNum, self.r2Activity, self.r2Details, self.r2PerformedBy, self.r2Status, self.r2Timestamp),
            (self.r3CaseNum, self.r3Activity, self.r3Details, self.r3PerformedBy, self.r3Status, self.r3Timestamp),
        ]
        recent = audits[-3:][::-1]
        for i, row_widget in enumerate(rows):
            if i < len(recent):
                entry = recent[i]
                case_num, activity_lbl, details_lbl, by_lbl, status_lbl, ts_lbl = fields[i]
                case_num.setText("—")
                activity_lbl.setText(entry.get("action", ""))
                details_lbl.setText(entry.get("action", ""))
                by_lbl.setText(entry.get("user", ""))
                status_lbl.setText("Logged")
                ts_lbl.setText(entry.get("date", ""))
                row_widget.setVisible(True)
            else:
                row_widget.setVisible(False)

    def _not_implemented(self):
        QMessageBox.information(self, "Coming Soon", "This feature is not yet available.")

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  VIEW USERS WIDGET  (View_users.ui)
# ─────────────────────────────────────────────

class ViewUsersWidget(QWidget, Ui_AllUsersWindow):
    """Full-screen All Users table, wired from View_users.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnNavGood.clicked.connect(self.app.show_role_dashboard)
        self.btnNavCaseLog.clicked.connect(self.app.show_view_cases)
        self.btnNavLawyers.clicked.connect(self.app.show_assign_lawyer)
        self.btnNavUsers.clicked.connect(lambda: None)   # already here
        self.searchInput.textChanged.connect(self._on_search)

    def refresh(self):
        users = load_data("users")
        # Update admin name from current user
        if self.app.current_user:
            self.lblAdminName.setText(self.app.current_user.get("username", "Admin"))
        self._populate_table(users)

    def _populate_table(self, users):
        self.tableUsers.setRowCount(len(users))
        for row, u in enumerate(users):
            self.tableUsers.setItem(row, 0, QTableWidgetItem(u.get("username", "")))
            self.tableUsers.setItem(row, 1, QTableWidgetItem(u.get("role", "")))
            self.tableUsers.setItem(row, 2, QTableWidgetItem("Active"))
            btn_row = QHBoxLayout()
            del_btn = QPushButton("Delete")
            del_btn.setStyleSheet(
                "QPushButton{background:#e63946;color:#fff;border-radius:4px;padding:4px 8px;}"
            )
            username = u["username"]
            del_btn.clicked.connect(lambda _, u=username: self._delete(u))
            container = QWidget()
            container.setLayout(btn_row)
            btn_row.addWidget(del_btn)
            btn_row.setContentsMargins(4, 2, 4, 2)
            self.tableUsers.setCellWidget(row, 3, container)
        self.tableUsers.resizeColumnsToContents()

    def _delete(self, username):
        confirm = DeleteConfirmationDialog(
            self,
            title=f"Delete '{username}'?",
            subtitle="This will permanently delete the user. This action cannot be undone.",
        )
        if confirm.exec_() == QDialog.Accepted:
            delete_user(username)
            if self.app.current_user:
                add_audit(self.app.current_user["username"], f"Deleted user '{username}'")
            self.refresh()

    def _on_search(self, text):
        users = load_data("users")
        if text.strip():
            t = text.lower()
            users = [u for u in users
                     if t in u.get("username", "").lower()
                     or t in u.get("role", "").lower()]
        self._populate_table(users)

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  TRACK CASE (LAWYER)  (track_case_lawyer_.ui)
# ─────────────────────────────────────────────

class TrackCaseLawyerWidget(QWidget, Ui_TrackCaseLawyerWidget):
    """Lawyer's Track Case panel, wired from track_case_lawyer_.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnMenu.clicked.connect(
            lambda: self.app.stack.setCurrentIndex(self.app.PAGE_LAWYER_PANEL)
        )
        self.btnTrackCase.clicked.connect(self._do_track)
        self.txtTrackCaseId.returnPressed.connect(self._do_track)

    def _do_track(self):
        text = self.txtTrackCaseId.text().strip()
        if not text:
            QMessageBox.warning(self, "Input Required", "Please enter a Case ID or title.")
            return
        cases = load_data("cases")
        # Try numeric ID first
        found = None
        if text.isdigit():
            cid = int(text)
            found = next((c for c in cases if c["id"] == cid), None)
        if not found:
            matches = [c for c in cases if text.lower() in c.get("title", "").lower()]
            if len(matches) == 1:
                found = matches[0]
            elif len(matches) > 1:
                msg = "\n".join(f"#{c['id']}  {c['title']}" for c in matches)
                QMessageBox.information(self, "Multiple Matches", f"Found multiple cases:\n{msg}")
                return
        if found:
            self.app.show_case_details(found["id"])
        else:
            QMessageBox.warning(self, "Not Found",
                                f"No case found for '{text}'. Please check the ID or title.")


# ─────────────────────────────────────────────
#  TRACK MY CASES (CLIENT)  (track_my_cases__client_pannel_.ui)
# ─────────────────────────────────────────────

class TrackMyCasesClientWidget(QWidget, Ui_TrackMyCasesClientWindow):
    """Client's Track My Case screen, wired from track_my_cases__client_pannel_.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))
        self.btnNavMyCases.clicked.connect(
            lambda: self.app.stack.setCurrentIndex(self.app.PAGE_CLIENT_PANEL)
        )
        self.btnNavTrackCase.clicked.connect(lambda: None)  # already here
        self.btnTrack.clicked.connect(self._do_track)
        self.txtCaseRef.returnPressed.connect(self._do_track)

    def refresh(self):
        user = self.app.current_user or {}
        username = user.get("username", "Client")
        self.lblClientName.setText(username)
        # Clear detail panel
        self.lblCaseTitle.setText("—")
        self.lblStatusBadge.setText("—")
        self.lblCourtName.setText("Enter your case ID above to view details.")
        self.lblPresidingJudgeValue.setText("—")
        self.lblOpposingCounselValue.setText("—")
        self.lblNextHearingValue.setText("—")
        self.lblTimeRemainingValue.setText("—")

    def _do_track(self):
        text = self.txtCaseRef.text().strip()
        if not text:
            QMessageBox.warning(self, "Input Required", "Please enter a Case Reference ID or title.")
            return
        user = self.app.current_user or {}
        username = user.get("username", "")
        cases = load_data("cases")
        # Filter to this client's cases
        my_cases = [c for c in cases if c.get("client") == username]

        found = None
        if text.isdigit():
            found = next((c for c in my_cases if c["id"] == int(text)), None)
        if not found:
            matches = [c for c in my_cases if text.lower() in c.get("title", "").lower()]
            if len(matches) == 1:
                found = matches[0]
            elif len(matches) > 1:
                found = matches[0]  # pick the latest match

        if found:
            self._display_case(found)
        else:
            QMessageBox.warning(self, "Not Found",
                                f"No case found for '{text}'. Please check your reference.")

    def _display_case(self, case):
        self.lblCaseTitle.setText(f"#{case['id']}: {case['title']}")
        status = case.get("status", "Filed")
        self.lblStatusBadge.setText(status.upper())
        self.lblCourtName.setText(
            f"Category: {case.get('category', '—')}  |  Priority: {case.get('priority', '—')}"
        )
        self.lblPresidingJudgeValue.setText(case.get("judge") or "Unassigned")
        self.lblOpposingCounselValue.setText(case.get("lawyer") or "Unassigned")

        hearings = [h for h in load_data("hearings") if h.get("case_id") == case["id"]]
        if hearings:
            next_h = hearings[-1]
            self.lblNextHearingValue.setText(next_h.get("date", "—"))
            self.lblTimeRemainingValue.setText(next_h.get("time", "—"))
        else:
            self.lblNextHearingValue.setText("—")
            self.lblTimeRemainingValue.setText("—")

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  RESET PASSWORD  (reset_password.ui)
# ─────────────────────────────────────────────

class ResetPasswordWidget(QWidget, Ui_ResetPasswordWindow):
    """Admin-facing Reset Password screen, wired from reset_password.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnMenu.clicked.connect(lambda: self.app.show_admin_panel())
        self.btnLogoutIcon.clicked.connect(lambda: self.app.confirm_logout(self))

        self.btnToggleNewPassword.toggled.connect(
            lambda on: self.txtNewPassword.setEchoMode(
                QLineEdit.Normal if on else QLineEdit.Password
            )
        )
        self.btnToggleConfirmPassword.toggled.connect(
            lambda on: self.txtConfirmPassword.setEchoMode(
                QLineEdit.Normal if on else QLineEdit.Password
            )
        )

        self.btnUpdatePassword.clicked.connect(self._do_update)
        self.btnCancel.clicked.connect(self._cancel)

        # Bottom nav shortcuts
        self.btnNavJudges.clicked.connect(self.app.show_assign_judge)
        self.btnNavLawyers.clicked.connect(self.app.show_assign_lawyer)
        self.btnNavNewUser.clicked.connect(self._jump_create_user)
        self.btnNavUsers.clicked.connect(self.app.show_view_users)

    def refresh(self):
        self.txtUsername.clear()
        self.txtNewPassword.clear()
        self.txtConfirmPassword.clear()
        self.btnToggleNewPassword.setChecked(False)
        self.btnToggleConfirmPassword.setChecked(False)

    def _jump_create_user(self):
        dlg = CreateUserDialog(self.app, parent=self)
        dlg.exec_()

    def _do_update(self):
        username = self.txtUsername.text().strip()
        new_pw = self.txtNewPassword.text()
        confirm_pw = self.txtConfirmPassword.text()

        if not username:
            QMessageBox.warning(self, "Validation", "Please enter the username.")
            return
        if not any(u["username"] == username for u in load_data("users")):
            QMessageBox.warning(self, "Validation", f"User '{username}' not found.")
            return
        if not new_pw or not confirm_pw:
            QMessageBox.warning(self, "Validation", "Please enter and confirm the new password.")
            return
        if new_pw != confirm_pw:
            QMessageBox.warning(self, "Validation", "Passwords do not match.")
            return

        reset_password(username, new_pw)
        if self.app.current_user:
            add_audit(self.app.current_user["username"], f"Reset password for '{username}'")
        QMessageBox.information(self, "Success", f"Password updated for '{username}'.")
        self._cancel()

    def _cancel(self):
        self.app.show_admin_panel()

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  SCHEDULE HEARING  (schedule_hearing.ui)
# ─────────────────────────────────────────────

class ScheduleHearingWidget(QWidget, Ui_ScheduleHearingWindow):
    """Judge-facing Schedule Hearing screen, wired from schedule_hearing.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnMenu.clicked.connect(
            lambda: self.app.stack.setCurrentIndex(self.app.PAGE_JUDGE_PANEL)
        )
        self.btnInfo.clicked.connect(
            lambda: QMessageBox.information(
                self, "Schedule Hearing",
                "Select an active case, pick a date and time, then provide "
                "the courtroom or virtual meeting link before confirming."
            )
        )
        self.btnScheduleHearing.clicked.connect(self._do_schedule)
        self.btnCancel.clicked.connect(self._cancel)

    def refresh(self):
        self.cmbActiveCase.clear()
        self.cmbActiveCase.addItem("Select an active case...")
        for c in load_data("cases"):
            self.cmbActiveCase.addItem(f"#{c['id']} – {c['title']}", c["id"])

        self.dateHearing.setDate(QtCore.QDate.currentDate())
        self.timeHearingSlot.setTime(QtCore.QTime.currentTime())
        self.txtCourtroomOrLink.clear()
        self.txtJudicialRemarks.clear()

    def _do_schedule(self):
        if self.cmbActiveCase.currentIndex() <= 0:
            QMessageBox.warning(self, "Validation", "Please select a case.")
            return
        courtroom = self.txtCourtroomOrLink.text().strip()
        if not courtroom:
            QMessageBox.warning(self, "Validation", "Please enter a courtroom or virtual link.")
            return

        case_id = self.cmbActiveCase.currentData()
        date_str = self.dateHearing.date().toString("yyyy-MM-dd")
        time_str = self.timeHearingSlot.time().toString("hh:mm AP")
        remarks = self.txtJudicialRemarks.toPlainText().strip()

        schedule_hearing(case_id, date_str, time_str, courtroom, remarks)
        if self.app.current_user:
            add_audit(self.app.current_user["username"],
                      f"Scheduled hearing for case #{case_id} on {date_str}")
        QMessageBox.information(self, "Success", f"Hearing scheduled for case #{case_id}.")
        self._cancel()

    def _cancel(self):
        self.app.stack.setCurrentIndex(self.app.PAGE_JUDGE_PANEL)

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  SEARCH CASE  (search_case.ui)
# ─────────────────────────────────────────────

class SearchCaseWidget(QWidget, Ui_SearchCaseWindow):
    """Admin-facing full Search Case screen, wired from search_case.ui."""

    def __init__(self, app_controller):
        super().__init__()
        self.app = app_controller
        self.setupUi(self)
        self._wire_ui()

    def _wire_ui(self):
        self.btnLogout.clicked.connect(lambda: self.app.confirm_logout(self))

        # Sidebar nav
        self.btnNavDashboard.clicked.connect(self.app.show_role_dashboard)
        self.btnNavSearchCase.clicked.connect(lambda: None)   # already on this page
        self.btnNavAllCases.clicked.connect(self.app.show_view_cases)
        self.btnNavHearings.clicked.connect(lambda: None)
        self.btnNavUsers.clicked.connect(self.app.show_view_users)

        # Top bar placeholders
        self.btnNotifications.clicked.connect(
            lambda: QMessageBox.information(self, "Notifications", "No new notifications.")
        )
        self.btnSettings.clicked.connect(
            lambda: QMessageBox.information(self, "Settings", "No settings available yet.")
        )
        self.btnHelp.clicked.connect(
            lambda: QMessageBox.information(self, "Help", "Search by case ID or party/title name.")
        )

        # Search + filters
        self.btnSearchCase.clicked.connect(self._do_search)
        self.txtCaseQuery.returnPressed.connect(self._do_search)
        self.btnFilterAll.clicked.connect(lambda: self._set_filter("All"))
        self.btnFilterCivil.clicked.connect(lambda: self._set_filter("Civil Law"))
        self.btnFilterCriminal.clicked.connect(lambda: self._set_filter("Criminal Law"))

    def refresh(self):
        self.txtCaseQuery.clear()
        self.btnFilterAll.setChecked(True)
        self.btnFilterCivil.setChecked(False)
        self.btnFilterCriminal.setChecked(False)
        self.tableSearchResults.setVisible(False)
        self.resultsPlaceholderFrame.setVisible(True)

    def _set_filter(self, category):
        self.btnFilterAll.setChecked(category == "All")
        self.btnFilterCivil.setChecked(category == "Civil Law")
        self.btnFilterCriminal.setChecked(category == "Criminal Law")
        if self.txtCaseQuery.text().strip() or category != "All":
            self._do_search()

    def _current_filter(self):
        if self.btnFilterCivil.isChecked():
            return "Civil Law"
        if self.btnFilterCriminal.isChecked():
            return "Criminal Law"
        return "All"

    def _do_search(self):
        query = self.txtCaseQuery.text().strip().lower()
        category = self._current_filter()

        cases = load_data("cases")
        results = []
        for c in cases:
            if category != "All" and c.get("category") != category:
                continue
            if query:
                haystack = f"{c.get('id')} {c.get('title','')} {c.get('client','')}".lower()
                if query not in haystack:
                    continue
            results.append(c)

        if not query and category == "All":
            # Nothing typed and no filter applied yet -> show the placeholder.
            self.tableSearchResults.setVisible(False)
            self.resultsPlaceholderFrame.setVisible(True)
            return

        self.resultsPlaceholderFrame.setVisible(False)
        self.tableSearchResults.setVisible(True)
        self._populate_table(results)

    def _populate_table(self, cases):
        self.tableSearchResults.setRowCount(len(cases))
        for row, c in enumerate(cases):
            self.tableSearchResults.setItem(row, 0, QTableWidgetItem(f"#{c['id']}"))
            self.tableSearchResults.setItem(row, 1, QTableWidgetItem(c.get("title", "")))
            self.tableSearchResults.setItem(row, 2, QTableWidgetItem(c.get("status", "")))
            btn = QPushButton("View")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(
                "QPushButton{background:#0c1230;color:#f0b429;border-radius:4px;padding:4px 10px;}"
                "QPushButton:hover{background:#1a2247;}"
            )
            cid = c["id"]
            btn.clicked.connect(lambda _, cid=cid: self.app.show_case_details(cid))
            self.tableSearchResults.setCellWidget(row, 3, btn)
        self.tableSearchResults.resizeColumnsToContents()

    def showEvent(self, event):
        self.refresh()
        super().showEvent(event)


# ─────────────────────────────────────────────
#  APP CONTROLLER  (main window / router)
# ─────────────────────────────────────────────

class AppController(QMainWindow):
    """Central QMainWindow that owns the QStackedWidget and routing."""

    # Page indices
    PAGE_WELCOME              = 0
    PAGE_LOGIN                = 1
    PAGE_ADMIN_DASHBOARD      = 2
    PAGE_ADMIN_PANEL          = 3
    PAGE_ASSIGN_JUDGE         = 4
    PAGE_ASSIGN_LAWYER        = 5
    PAGE_CASE_DETAILS         = 6
    PAGE_ADD_CASE             = 7
    PAGE_JUDGE_PANEL          = 8
    PAGE_LAWYER_PANEL         = 9
    PAGE_CLIENT_PANEL         = 10
    PAGE_VIEW_CASES           = 11
    PAGE_VIEW_USERS           = 12
    PAGE_TRACK_CASE_LAWYER    = 13
    PAGE_TRACK_CASE_CLIENT    = 14
    PAGE_RESET_PASSWORD       = 15
    PAGE_SCHEDULE_HEARING     = 16
    PAGE_SEARCH_CASE          = 17
    PAGE_MY_CASES             = 18
    PAGE_REPORTS              = 19

    def __init__(self):
        super().__init__()
        self.setWindowTitle("LexSecure CCMS")
        self.resize(1280, 800)
        self.current_user = None

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Build all screens
        self.w_welcome   = WelcomeWindow(
            on_login=self.show_login,
            on_exit=self.close,
        )
        self.w_login     = LoginWindow(on_success=self._on_login_success)
        self.w_admin_db  = AdminDashboardWidget(self)
        self.w_admin_pnl = AdminPanelWidget(self)
        self.w_assign_j  = AssignJudgeWidget(self)
        self.w_assign_l  = AssignLawyerWidget(self)
        self.w_case_det  = CaseDetailsWidget(self)
        self.w_add_case  = AddCaseWidget(self)
        self.w_judge     = JudgePanelWidget(self)
        self.w_lawyer    = LawyerPanelWidget(self)
        self.w_client    = ClientPanelWidget(self)
        # New screens from .ui files
        self.w_view_cases          = ViewCasesWidget(self)
        self.w_view_users          = ViewUsersWidget(self)
        self.w_track_case_lawyer   = TrackCaseLawyerWidget(self)
        self.w_track_case_client   = TrackMyCasesClientWidget(self)
        self.w_reset_password      = ResetPasswordWidget(self)
        self.w_schedule_hearing    = ScheduleHearingWidget(self)
        self.w_search_case         = SearchCaseWidget(self)
        self.w_my_cases            = MyCasesWidget(self)
        self.w_reports             = ReportsWidget(self)

        for w in [
            self.w_welcome, self.w_login, self.w_admin_db, self.w_admin_pnl,
            self.w_assign_j, self.w_assign_l, self.w_case_det, self.w_add_case,
            self.w_judge, self.w_lawyer, self.w_client,
            self.w_view_cases, self.w_view_users,
            self.w_track_case_lawyer, self.w_track_case_client,
            self.w_reset_password, self.w_schedule_hearing, self.w_search_case,
            self.w_my_cases, self.w_reports,
        ]:
            self.stack.addWidget(w)

        self.stack.setCurrentIndex(self.PAGE_WELCOME)

    # ── navigation helpers ──

    def show_login(self):
        self.stack.setCurrentIndex(self.PAGE_LOGIN)

    def show_admin_dashboard(self):
        self.stack.setCurrentIndex(self.PAGE_ADMIN_DASHBOARD)

    def show_role_dashboard(self):
        """Route back to whichever panel matches the logged-in user's role.

        Several screens (View Cases, Search Case, Reports, View Users) are
        shared between roles. Their 'Dashboard' nav buttons used to always
        call show_admin_dashboard(), so a Judge (or Lawyer/Client) who
        opened one of these from their own panel would get dumped into the
        Admin Dashboard instead of going back to their own panel.
        """
        role = (self.current_user or {}).get("role")
        if role == "Judge":
            self.stack.setCurrentIndex(self.PAGE_JUDGE_PANEL)
        elif role == "Lawyer":
            self.stack.setCurrentIndex(self.PAGE_LAWYER_PANEL)
        elif role == "Client":
            self.w_client.refresh()
            self.stack.setCurrentIndex(self.PAGE_CLIENT_PANEL)
        else:
            self.show_admin_dashboard()

    def show_admin_panel(self):
        self.stack.setCurrentIndex(self.PAGE_ADMIN_PANEL)

    def show_assign_judge(self):
        self.stack.setCurrentIndex(self.PAGE_ASSIGN_JUDGE)

    def show_assign_lawyer(self):
        self.stack.setCurrentIndex(self.PAGE_ASSIGN_LAWYER)

    def show_view_cases(self):
        self.w_view_cases.refresh()
        self.stack.setCurrentIndex(self.PAGE_VIEW_CASES)

    def show_view_users(self):
        self.w_view_users.refresh()
        self.stack.setCurrentIndex(self.PAGE_VIEW_USERS)

    def show_track_case_lawyer(self):
        self.stack.setCurrentIndex(self.PAGE_TRACK_CASE_LAWYER)

    def show_track_case_client(self):
        self.w_track_case_client.refresh()
        self.stack.setCurrentIndex(self.PAGE_TRACK_CASE_CLIENT)

    def show_reset_password(self):
        self.w_reset_password.refresh()
        self.stack.setCurrentIndex(self.PAGE_RESET_PASSWORD)

    def show_schedule_hearing(self):
        self.w_schedule_hearing.refresh()
        self.stack.setCurrentIndex(self.PAGE_SCHEDULE_HEARING)

    def show_search_case(self):
        self.w_search_case.refresh()
        self.stack.setCurrentIndex(self.PAGE_SEARCH_CASE)

    def show_my_cases(self):
        self.w_my_cases.refresh()
        self.stack.setCurrentIndex(self.PAGE_MY_CASES)

    def show_reports(self):
        self.w_reports.refresh()
        self.stack.setCurrentIndex(self.PAGE_REPORTS)

    def show_case_details(self, case_id):
        self.w_case_det.load_case(case_id)
        self.stack.setCurrentIndex(self.PAGE_CASE_DETAILS)

    def show_add_case(self):
        self.w_add_case.refresh()
        self.stack.setCurrentIndex(self.PAGE_ADD_CASE)

    def _on_login_success(self, user):
        self.current_user = user
        role = user["role"]
        if role == "Admin":
            self.show_admin_dashboard()
        elif role == "Judge":
            self.stack.setCurrentIndex(self.PAGE_JUDGE_PANEL)
        elif role == "Lawyer":
            self.stack.setCurrentIndex(self.PAGE_LAWYER_PANEL)
        elif role == "Client":
            self.w_client.refresh()
            self.stack.setCurrentIndex(self.PAGE_CLIENT_PANEL)

    def logout(self):
        self.current_user = None
        self.stack.setCurrentIndex(self.PAGE_WELCOME)

    def confirm_logout(self, parent=None):
        """Show the Log Out? confirmation dialog; only logs out if accepted."""
        dlg = LogoutConfirmDialog(parent or self)
        if dlg.exec_() == QDialog.Accepted:
            self.logout()


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

def main():
    init_storage()
    initialize_default_admin()

    app = QApplication(sys.argv)
    app.setFont(QFont("Inter", 10))

    window = AppController()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
