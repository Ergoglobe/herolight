# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 679)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vehicle_year = QComboBox(self.groupBox)
        self.vehicle_year.setObjectName("vehicle_year")

        self.horizontalLayout.addWidget(self.vehicle_year)

        self.vehicle_make = QComboBox(self.groupBox)
        self.vehicle_make.setObjectName("vehicle_make")

        self.horizontalLayout.addWidget(self.vehicle_make)

        self.vehicle_model = QComboBox(self.groupBox)
        self.vehicle_model.setObjectName("vehicle_model")

        self.horizontalLayout.addWidget(self.vehicle_model)

        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.vehicle_vin = QLineEdit(self.groupBox_2)
        self.vehicle_vin.setObjectName("vehicle_vin")

        self.verticalLayout_3.addWidget(self.vehicle_vin)

        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.oil_output_table = QTableWidget(self.frame)
        if self.oil_output_table.columnCount() < 8:
            self.oil_output_table.setColumnCount(8)
        self.oil_output_table.setObjectName("oil_output_table")
        self.oil_output_table.setSortingEnabled(True)
        self.oil_output_table.setColumnCount(8)
        self.oil_output_table.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_5.addWidget(self.oil_output_table)

        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Vehicle", None)
        )
        self.vehicle_year.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Year", None)
        )
        self.vehicle_make.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Make", None)
        )
        self.vehicle_model.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Model", None)
        )
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", "VIN", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Search", None)
        )

    # retranslateUi
