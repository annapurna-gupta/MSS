# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_multiple_flightpath_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultipleViewWidget(object):
    def setupUi(self, MultipleViewWidget):
        MultipleViewWidget.setObjectName("MultipleViewWidget")
        MultipleViewWidget.resize(798, 282)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MultipleViewWidget.sizePolicy().hasHeightForWidth())
        MultipleViewWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MultipleViewWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(MultipleViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ft_color_label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ft_color_label.sizePolicy().hasHeightForWidth())
        self.ft_color_label.setSizePolicy(sizePolicy)
        self.ft_color_label.setObjectName("ft_color_label")
        self.horizontalLayout_3.addWidget(self.ft_color_label)
        self.colorPixmap = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorPixmap.sizePolicy().hasHeightForWidth())
        self.colorPixmap.setSizePolicy(sizePolicy)
        self.colorPixmap.setText("")
        self.colorPixmap.setObjectName("colorPixmap")
        self.horizontalLayout_3.addWidget(self.colorPixmap)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(MultipleViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.cbSlectAll1 = QtWidgets.QCheckBox(self.frame_4)
        self.cbSlectAll1.setGeometry(QtCore.QRect(0, 10, 231, 20))
        self.cbSlectAll1.setObjectName("cbSlectAll1")
        self.cbSlectAll2 = QtWidgets.QCheckBox(self.frame_4)
        self.cbSlectAll2.setGeometry(QtCore.QRect(280, 10, 251, 20))
        self.cbSlectAll2.setObjectName("cbSlectAll2")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.list_flighttrack = QtWidgets.QListWidget(MultipleViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_flighttrack.sizePolicy().hasHeightForWidth())
        self.list_flighttrack.setSizePolicy(sizePolicy)
        self.list_flighttrack.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.list_flighttrack.setObjectName("list_flighttrack")
        self.horizontalLayout_2.addWidget(self.list_flighttrack)
        self.list_operation_track = QtWidgets.QListWidget(MultipleViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.list_operation_track.sizePolicy().hasHeightForWidth())
        self.list_operation_track.setSizePolicy(sizePolicy)
        self.list_operation_track.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.list_operation_track.setObjectName("list_operation_track")
        self.horizontalLayout_2.addWidget(self.list_operation_track)
        self.groupBox = QtWidgets.QGroupBox(MultipleViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 160))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_color = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_color.setGeometry(QtCore.QRect(10, 30, 174, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)
        self.pushButton_color.setObjectName("pushButton_color")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 130, 101, 20))
        self.label.setObjectName("label")
        self.dsbx_linewidth = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.dsbx_linewidth.setGeometry(QtCore.QRect(10, 120, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsbx_linewidth.sizePolicy().hasHeightForWidth())
        self.dsbx_linewidth.setSizePolicy(sizePolicy)
        self.dsbx_linewidth.setAlignment(QtCore.Qt.AlignCenter)
        self.dsbx_linewidth.setObjectName("dsbx_linewidth")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 61, 16))
        self.label_3.setObjectName("label_3")
        self.cbLineStyle = QtWidgets.QComboBox(self.groupBox)
        self.cbLineStyle.setGeometry(QtCore.QRect(10, 90, 101, 22))
        self.cbLineStyle.setObjectName("cbLineStyle")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 81, 20))
        self.label_2.setObjectName("label_2")
        self.hsTransparencyControl = QtWidgets.QSlider(self.groupBox)
        self.hsTransparencyControl.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.hsTransparencyControl.setProperty("value", 20)
        self.hsTransparencyControl.setOrientation(QtCore.Qt.Horizontal)
        self.hsTransparencyControl.setObjectName("hsTransparencyControl")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.labelStatus = QtWidgets.QLabel(MultipleViewWidget)
        self.labelStatus.setObjectName("labelStatus")
        self.verticalLayout_2.addWidget(self.labelStatus)

        self.retranslateUi(MultipleViewWidget)
        QtCore.QMetaObject.connectSlotsByName(MultipleViewWidget)

    def retranslateUi(self, MultipleViewWidget):
        _translate = QtCore.QCoreApplication.translate
        MultipleViewWidget.setWindowTitle(_translate("MultipleViewWidget", "Form"))
        self.ft_color_label.setText(_translate("MultipleViewWidget", "Activated Flighttrack/Operation Vertices Color: "))
        self.cbSlectAll1.setText(_translate("MultipleViewWidget", "Select all list of Open Flighttracks"))
        self.cbSlectAll2.setText(_translate("MultipleViewWidget", "Select all list of MsColab Flighttracks"))
        self.list_flighttrack.setToolTip(_translate("MultipleViewWidget", "List of Open Flighttracks.\n"
"Check box to activate and display track on topview."))
        self.list_operation_track.setToolTip(_translate("MultipleViewWidget", "List of Mscolab Operations.\n"
"Check box to activate and display track on topview."))
        self.groupBox.setTitle(_translate("MultipleViewWidget", "Flight Track style options"))
        self.pushButton_color.setText(_translate("MultipleViewWidget", "Change Color of flight track"))
        self.label.setText(_translate("MultipleViewWidget", "Line thnickness"))
        self.label_3.setText(_translate("MultipleViewWidget", "Line style"))
        self.label_2.setText(_translate("MultipleViewWidget", "Transparency"))
        self.labelStatus.setText(_translate("MultipleViewWidget", "Status: "))