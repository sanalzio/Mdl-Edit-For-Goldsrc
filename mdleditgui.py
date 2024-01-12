# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mdleditnew.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 385)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mdledit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath.setGeometry(QtCore.QRect(30, 40, 471, 21))
        self.filepath.setObjectName("filepath")
        self.sfile = QtWidgets.QPushButton(self.centralwidget)
        self.sfile.setGeometry(QtCore.QRect(510, 38, 21, 23))
        self.sfile.setObjectName("sfile")
        self.kosol = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.kosol.setGeometry(QtCore.QRect(10, 210, 551, 151))
        self.kosol.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.kosol.setReadOnly(True)
        self.kosol.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.kosol.setObjectName("kosol")
        self.sekmeler = QtWidgets.QTabWidget(self.centralwidget)
        self.sekmeler.setGeometry(QtCore.QRect(0, 0, 571, 391))
        self.sekmeler.setObjectName("sekmeler")
        self.compmenu = QtWidgets.QWidget()
        self.compmenu.setObjectName("compmenu")
        self.compbutton = QtWidgets.QPushButton(self.compmenu)
        self.compbutton.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.compbutton.setObjectName("compbutton")
        self.sekmeler.addTab(self.compmenu, "")
        self.decompmenu = QtWidgets.QWidget()
        self.decompmenu.setObjectName("decompmenu")
        self.clqc = QtWidgets.QCheckBox(self.decompmenu)
        self.clqc.setEnabled(True)
        self.clqc.setGeometry(QtCore.QRect(25, 85, 101, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clqc.sizePolicy().hasHeightForWidth())
        self.clqc.setSizePolicy(sizePolicy)
        self.clqc.setMinimumSize(QtCore.QSize(0, 0))
        self.clqc.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.clqc.setFont(font)
        self.clqc.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.clqc.setIconSize(QtCore.QSize(16, 16))
        self.clqc.setTristate(False)
        self.clqc.setObjectName("clqc")
        self.decompbutton = QtWidgets.QPushButton(self.decompmenu)
        self.decompbutton.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.decompbutton.setObjectName("decompbutton")
        self.sekmeler.addTab(self.decompmenu, "")
        self.testmenu = QtWidgets.QWidget()
        self.testmenu.setObjectName("testmenu")
        self.testbtn = QtWidgets.QPushButton(self.testmenu)
        self.testbtn.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.testbtn.setObjectName("testbtn")
        self.sekmeler.addTab(self.testmenu, "")
        self.cutmenu = QtWidgets.QWidget()
        self.cutmenu.setObjectName("cutmenu")
        self.cutbutton = QtWidgets.QPushButton(self.cutmenu)
        self.cutbutton.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.cutbutton.setObjectName("cutbutton")
        self.ucgen = QtWidgets.QLabel(self.cutmenu)
        self.ucgen.setGeometry(QtCore.QRect(20, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ucgen.setFont(font)
        self.ucgen.setObjectName("ucgen")
        self.ucgengirdi = QtWidgets.QLineEdit(self.cutmenu)
        self.ucgengirdi.setGeometry(QtCore.QRect(115, 85, 101, 20))
        self.ucgengirdi.setObjectName("ucgengirdi")
        self.sekmeler.addTab(self.cutmenu, "")
        self.seqmenu = QtWidgets.QWidget()
        self.seqmenu.setObjectName("seqmenu")
        self.strtlabal = QtWidgets.QLabel(self.seqmenu)
        self.strtlabal.setGeometry(QtCore.QRect(330, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.strtlabal.setFont(font)
        self.strtlabal.setObjectName("strtlabal")
        self.endlabal = QtWidgets.QLabel(self.seqmenu)
        self.endlabal.setGeometry(QtCore.QRect(330, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.endlabal.setFont(font)
        self.endlabal.setObjectName("endlabal")
        self.strtspin = QtWidgets.QSpinBox(self.seqmenu)
        self.strtspin.setGeometry(QtCore.QRect(390, 90, 42, 22))
        self.strtspin.setObjectName("strtspin")
        self.endspin = QtWidgets.QSpinBox(self.seqmenu)
        self.endspin.setGeometry(QtCore.QRect(390, 120, 42, 22))
        self.endspin.setObjectName("endspin")
        self.frmc = QtWidgets.QLabel(self.seqmenu)
        self.frmc.setGeometry(QtCore.QRect(100, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frmc.setFont(font)
        self.frmc.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.frmc.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.frmc.setObjectName("frmc")
        self.aply = QtWidgets.QPushButton(self.seqmenu)
        self.aply.setGeometry(QtCore.QRect(340, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.aply.setFont(font)
        self.aply.setObjectName("aply")
        self.divisorlab = QtWidgets.QLabel(self.seqmenu)
        self.divisorlab.setGeometry(QtCore.QRect(120, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.divisorlab.setFont(font)
        self.divisorlab.setObjectName("divisorlab")
        self.divisorspin = QtWidgets.QSpinBox(self.seqmenu)
        self.divisorspin.setGeometry(QtCore.QRect(210, 130, 42, 22))
        self.divisorspin.setObjectName("divisorspin")
        self.cmpbtn = QtWidgets.QPushButton(self.seqmenu)
        self.cmpbtn.setGeometry(QtCore.QRect(140, 180, 75, 23))
        self.cmpbtn.setObjectName("cmpbtn")
        self.revbtn = QtWidgets.QPushButton(self.seqmenu)
        self.revbtn.setGeometry(QtCore.QRect(250, 220, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.revbtn.setFont(font)
        self.revbtn.setObjectName("revbtn")
        self.refbtn = QtWidgets.QPushButton(self.seqmenu)
        self.refbtn.setGeometry(QtCore.QRect(508, 40, 21, 23))
        self.refbtn.setObjectName("refbtn")
        self.sekmeler.addTab(self.seqmenu, "")
        self.exifmenu = QtWidgets.QWidget()
        self.exifmenu.setObjectName("exifmenu")
        self.triangles = QtWidgets.QLabel(self.exifmenu)
        self.triangles.setEnabled(True)
        self.triangles.setGeometry(QtCore.QRect(175, 60, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.triangles.setFont(font)
        self.triangles.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.triangles.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.triangles.setTextFormat(QtCore.Qt.AutoText)
        self.triangles.setWordWrap(False)
        self.triangles.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.triangles.setObjectName("triangles")
        self.verts = QtWidgets.QLabel(self.exifmenu)
        self.verts.setGeometry(QtCore.QRect(175, 100, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.verts.setFont(font)
        self.verts.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.verts.setWordWrap(False)
        self.verts.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.verts.setObjectName("verts")
        self.norms = QtWidgets.QLabel(self.exifmenu)
        self.norms.setGeometry(QtCore.QRect(175, 180, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.norms.setFont(font)
        self.norms.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.norms.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.norms.setObjectName("norms")
        self.mats = QtWidgets.QLabel(self.exifmenu)
        self.mats.setGeometry(QtCore.QRect(175, 220, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.mats.setFont(font)
        self.mats.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.mats.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.mats.setObjectName("mats")
        self.joints = QtWidgets.QLabel(self.exifmenu)
        self.joints.setGeometry(QtCore.QRect(175, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.joints.setFont(font)
        self.joints.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.joints.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.joints.setObjectName("joints")
        self.refbtn2 = QtWidgets.QPushButton(self.exifmenu)
        self.refbtn2.setGeometry(QtCore.QRect(508, 40, 21, 23))
        self.refbtn2.setObjectName("refbtn2")
        self.joints.raise_()
        self.mats.raise_()
        self.verts.raise_()
        self.norms.raise_()
        self.triangles.raise_()
        self.refbtn2.raise_()
        self.sekmeler.addTab(self.exifmenu, "")
        self.cfgmenu = QtWidgets.QWidget()
        self.cfgmenu.setObjectName("cfgmenu")
        self.sbs = QtWidgets.QCheckBox(self.cfgmenu)
        self.sbs.setGeometry(QtCore.QRect(25, 85, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sbs.setFont(font)
        self.sbs.setObjectName("sbs")
        self.stpath = QtWidgets.QLineEdit(self.cfgmenu)
        self.stpath.setGeometry(QtCore.QRect(150, 150, 351, 20))
        self.stpath.setObjectName("stpath")
        self.cslab = QtWidgets.QLabel(self.cfgmenu)
        self.cslab.setGeometry(QtCore.QRect(25, 150, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cslab.setFont(font)
        self.cslab.setObjectName("cslab")
        self.stfsel = QtWidgets.QPushButton(self.cfgmenu)
        self.stfsel.setGeometry(QtCore.QRect(510, 148, 21, 23))
        self.stfsel.setObjectName("stfsel")
        self.savebtn = QtWidgets.QPushButton(self.cfgmenu)
        self.savebtn.setGeometry(QtCore.QRect(485, 320, 75, 23))
        self.savebtn.setObjectName("savebtn")
        self.modlabel = QtWidgets.QLabel(self.cfgmenu)
        self.modlabel.setGeometry(QtCore.QRect(25, 230, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.modlabel.setFont(font)
        self.modlabel.setObjectName("modlabel")
        self.moddir = QtWidgets.QLineEdit(self.cfgmenu)
        self.moddir.setGeometry(QtCore.QRect(150, 230, 351, 20))
        self.moddir.setObjectName("moddir")
        self.smoddir = QtWidgets.QPushButton(self.cfgmenu)
        self.smoddir.setGeometry(QtCore.QRect(510, 228, 21, 23))
        self.smoddir.setObjectName("smoddir")
        self.shpath = QtWidgets.QLineEdit(self.cfgmenu)
        self.shpath.setGeometry(QtCore.QRect(130, 20, 371, 20))
        self.shpath.setObjectName("shpath")
        self.shsel = QtWidgets.QPushButton(self.cfgmenu)
        self.shsel.setGeometry(QtCore.QRect(510, 18, 21, 23))
        self.shsel.setObjectName("shsel")
        self.shlab = QtWidgets.QLabel(self.cfgmenu)
        self.shlab.setGeometry(QtCore.QRect(23, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.shlab.setFont(font)
        self.shlab.setObjectName("shlab")
        self.sekmeler.addTab(self.cfgmenu, "")
        self.sekmeler.raise_()
        self.filepath.raise_()
        self.sfile.raise_()
        self.kosol.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sekmeler.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MdlEdit"))
        self.sfile.setText(_translate("MainWindow", "..."))
        self.compbutton.setText(_translate("MainWindow", "Compile"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.compmenu), _translate("MainWindow", "Compile"))
        self.clqc.setText(_translate("MainWindow", "Clear .qc"))
        self.decompbutton.setText(_translate("MainWindow", "Decompile"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.decompmenu), _translate("MainWindow", "Decompile"))
        self.testbtn.setText(_translate("MainWindow", "Test in game"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.testmenu), _translate("MainWindow", "Test in game"))
        self.cutbutton.setText(_translate("MainWindow", "Cut Smd"))
        self.ucgen.setText(_translate("MainWindow", "Max Triangles"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.cutmenu), _translate("MainWindow", "SmdCut"))
        self.strtlabal.setText(_translate("MainWindow", "Start"))
        self.endlabal.setText(_translate("MainWindow", "End"))
        self.frmc.setText(_translate("MainWindow", "Frame count: ?"))
        self.aply.setText(_translate("MainWindow", "Apply"))
        self.divisorlab.setText(_translate("MainWindow", "Divisor:"))
        self.cmpbtn.setText(_translate("MainWindow", "Compress"))
        self.revbtn.setText(_translate("MainWindow", "Reverse Animation"))
        self.refbtn.setText(_translate("MainWindow", "🔄"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.seqmenu), _translate("MainWindow", "Sequence"))
        self.triangles.setText(_translate("MainWindow", "Faces     :?"))
        self.verts.setText(_translate("MainWindow", "Vertices  :?"))
        self.norms.setText(_translate("MainWindow", "Normals   :?"))
        self.mats.setText(_translate("MainWindow", "Materials :?"))
        self.joints.setText(_translate("MainWindow", "Joints    :?"))
        self.refbtn2.setText(_translate("MainWindow", "🔄"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.exifmenu), _translate("MainWindow", "Statistics"))
        self.sbs.setText(_translate("MainWindow", "Start by selecting a file."))
        self.cslab.setText(_translate("MainWindow", "Custom StudioMdl:"))
        self.stfsel.setText(_translate("MainWindow", "..."))
        self.savebtn.setText(_translate("MainWindow", "Save"))
        self.modlabel.setText(_translate("MainWindow", "Half-Life Mod Dir.:"))
        self.smoddir.setText(_translate("MainWindow", "..."))
        self.shsel.setText(_translate("MainWindow", "..."))
        self.shlab.setText(_translate("MainWindow", "Game Shotrcut:"))
        self.sekmeler.setTabText(self.sekmeler.indexOf(self.cfgmenu), _translate("MainWindow", "Config"))
