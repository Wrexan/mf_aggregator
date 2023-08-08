# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 701)
        MainWindow.setWindowTitle("MDA")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MDA.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HEAD = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HEAD.sizePolicy().hasHeightForWidth())
        self.HEAD.setSizePolicy(sizePolicy)
        self.HEAD.setMinimumSize(QtCore.QSize(0, 164))
        self.HEAD.setMaximumSize(QtCore.QSize(16777215, 165))
        self.HEAD.setObjectName("HEAD")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.HEAD)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_3 = QtWidgets.QWidget(self.HEAD)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.HEAD_1top = QtWidgets.QFrame(self.widget_3)
        self.HEAD_1top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HEAD_1top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HEAD_1top.setLineWidth(0)
        self.HEAD_1top.setObjectName("HEAD_1top")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.HEAD_1top)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_7 = QtWidgets.QFrame(self.HEAD_1top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.top_menu_frame = QtWidgets.QFrame(self.frame_7)
        self.top_menu_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_menu_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.top_menu_frame.setLineWidth(0)
        self.top_menu_frame.setObjectName("top_menu_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.top_menu_frame)
        self.horizontalLayout_7.setContentsMargins(4, 0, 4, 1)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.help = QtWidgets.QPushButton(self.top_menu_frame)
        self.help.setMinimumSize(QtCore.QSize(100, 28))
        self.help.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.help.setFont(font)
        self.help.setObjectName("help")
        self.horizontalLayout_7.addWidget(self.help)
        self.graph_button = QtWidgets.QPushButton(self.top_menu_frame)
        self.graph_button.setMinimumSize(QtCore.QSize(100, 28))
        self.graph_button.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.graph_button.setFont(font)
        self.graph_button.setObjectName("graph_button")
        self.horizontalLayout_7.addWidget(self.graph_button)
        self.settings_button = QtWidgets.QPushButton(self.top_menu_frame)
        self.settings_button.setMinimumSize(QtCore.QSize(100, 28))
        self.settings_button.setMaximumSize(QtCore.QSize(100, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout_7.addWidget(self.settings_button)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.top_menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_db = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_db.sizePolicy().hasHeightForWidth())
        self.label_db.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_db.setFont(font)
        self.label_db.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_db.setObjectName("label_db")
        self.horizontalLayout_5.addWidget(self.label_db)
        self.widg_web_status = QtWidgets.QWidget(self.widget)
        self.widg_web_status.setObjectName("widg_web_status")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widg_web_status)
        self.verticalLayout_10.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.web_status = QtWidgets.QLabel(self.widg_web_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_status.sizePolicy().hasHeightForWidth())
        self.web_status.setSizePolicy(sizePolicy)
        self.web_status.setMinimumSize(QtCore.QSize(200, 26))
        self.web_status.setMaximumSize(QtCore.QSize(200, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.web_status.setFont(font)
        self.web_status.setFrameShape(QtWidgets.QFrame.Panel)
        self.web_status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.web_status.setAlignment(QtCore.Qt.AlignCenter)
        self.web_status.setObjectName("web_status")
        self.verticalLayout_10.addWidget(self.web_status)
        self.web_progress_bar = QtWidgets.QProgressBar(self.widg_web_status)
        self.web_progress_bar.setMinimumSize(QtCore.QSize(0, 3))
        self.web_progress_bar.setMaximumSize(QtCore.QSize(16777215, 3))
        self.web_progress_bar.setProperty("value", 0)
        self.web_progress_bar.setTextVisible(False)
        self.web_progress_bar.setObjectName("web_progress_bar")
        self.verticalLayout_10.addWidget(self.web_progress_bar)
        self.horizontalLayout_5.addWidget(self.widg_web_status)
        self.bt_upd_web = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_upd_web.sizePolicy().hasHeightForWidth())
        self.bt_upd_web.setSizePolicy(sizePolicy)
        self.bt_upd_web.setMinimumSize(QtCore.QSize(28, 28))
        self.bt_upd_web.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.bt_upd_web.setFont(font)
        self.bt_upd_web.setText("⟳")
        self.bt_upd_web.setFlat(True)
        self.bt_upd_web.setObjectName("bt_upd_web")
        self.horizontalLayout_5.addWidget(self.bt_upd_web)
        self.horizontalLayout_7.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.top_menu_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_price = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_price.sizePolicy().hasHeightForWidth())
        self.label_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_price.setFont(font)
        self.label_price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_price.setObjectName("label_price")
        self.horizontalLayout_11.addWidget(self.label_price)
        self.widg_price_status = QtWidgets.QWidget(self.widget_2)
        self.widg_price_status.setObjectName("widg_price_status")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widg_price_status)
        self.verticalLayout_11.setContentsMargins(0, 3, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.price_status = QtWidgets.QLabel(self.widg_price_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_status.sizePolicy().hasHeightForWidth())
        self.price_status.setSizePolicy(sizePolicy)
        self.price_status.setMinimumSize(QtCore.QSize(200, 26))
        self.price_status.setMaximumSize(QtCore.QSize(200, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.price_status.setFont(font)
        self.price_status.setFrameShape(QtWidgets.QFrame.Panel)
        self.price_status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.price_status.setAlignment(QtCore.Qt.AlignCenter)
        self.price_status.setObjectName("price_status")
        self.verticalLayout_11.addWidget(self.price_status)
        self.price_progress_bar = QtWidgets.QProgressBar(self.widg_price_status)
        self.price_progress_bar.setMinimumSize(QtCore.QSize(0, 3))
        self.price_progress_bar.setMaximumSize(QtCore.QSize(16777215, 3))
        self.price_progress_bar.setProperty("value", 0)
        self.price_progress_bar.setTextVisible(False)
        self.price_progress_bar.setObjectName("price_progress_bar")
        self.verticalLayout_11.addWidget(self.price_progress_bar)
        self.horizontalLayout_11.addWidget(self.widg_price_status)
        self.bt_upd_price = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_upd_price.sizePolicy().hasHeightForWidth())
        self.bt_upd_price.setSizePolicy(sizePolicy)
        self.bt_upd_price.setMinimumSize(QtCore.QSize(28, 28))
        self.bt_upd_price.setMaximumSize(QtCore.QSize(28, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.bt_upd_price.setFont(font)
        self.bt_upd_price.setText("⟳")
        self.bt_upd_price.setFlat(True)
        self.bt_upd_price.setObjectName("bt_upd_price")
        self.horizontalLayout_11.addWidget(self.bt_upd_price)
        self.horizontalLayout_7.addWidget(self.widget_2)
        self.horizontalLayout_10.addWidget(self.top_menu_frame)
        self.verticalLayout_9.addWidget(self.frame_7)
        self.widget_name_descr_price = QtWidgets.QWidget(self.HEAD_1top)
        self.widget_name_descr_price.setObjectName("widget_name_descr_price")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_name_descr_price)
        self.verticalLayout_2.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.widget_name_descr_price)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setLineWidth(0)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lb_username = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_username.sizePolicy().hasHeightForWidth())
        self.lb_username.setSizePolicy(sizePolicy)
        self.lb_username.setMinimumSize(QtCore.QSize(100, 26))
        self.lb_username.setMaximumSize(QtCore.QSize(100, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_username.setFont(font)
        self.lb_username.setText("")
        self.lb_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_username.setObjectName("lb_username")
        self.horizontalLayout_8.addWidget(self.lb_username)
        self.le_cash_name = QtWidgets.QLineEdit(self.frame_10)
        self.le_cash_name.setMinimumSize(QtCore.QSize(0, 26))
        self.le_cash_name.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cash_name.setFont(font)
        self.le_cash_name.setMouseTracking(False)
        self.le_cash_name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.le_cash_name.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.le_cash_name.setAcceptDrops(False)
        self.le_cash_name.setStyleSheet("border: 1px solid rgb(180,180,180);")
        self.le_cash_name.setText("")
        self.le_cash_name.setAlignment(QtCore.Qt.AlignCenter)
        self.le_cash_name.setReadOnly(True)
        self.le_cash_name.setObjectName("le_cash_name")
        self.horizontalLayout_8.addWidget(self.le_cash_name)
        self.le_cash_price = QtWidgets.QLineEdit(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_cash_price.sizePolicy().hasHeightForWidth())
        self.le_cash_price.setSizePolicy(sizePolicy)
        self.le_cash_price.setMinimumSize(QtCore.QSize(100, 26))
        self.le_cash_price.setMaximumSize(QtCore.QSize(100, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cash_price.setFont(font)
        self.le_cash_price.setMouseTracking(False)
        self.le_cash_price.setFocusPolicy(QtCore.Qt.NoFocus)
        self.le_cash_price.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.le_cash_price.setAcceptDrops(False)
        self.le_cash_price.setStyleSheet("border: 1px solid rgb(180,180,180);")
        self.le_cash_price.setText("")
        self.le_cash_price.setAlignment(QtCore.Qt.AlignCenter)
        self.le_cash_price.setReadOnly(True)
        self.le_cash_price.setObjectName("le_cash_price")
        self.horizontalLayout_8.addWidget(self.le_cash_price)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.le_cash_descr = QtWidgets.QLineEdit(self.widget_name_descr_price)
        self.le_cash_descr.setMinimumSize(QtCore.QSize(0, 26))
        self.le_cash_descr.setMaximumSize(QtCore.QSize(16777215, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.le_cash_descr.setFont(font)
        self.le_cash_descr.setMouseTracking(False)
        self.le_cash_descr.setFocusPolicy(QtCore.Qt.NoFocus)
        self.le_cash_descr.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.le_cash_descr.setAcceptDrops(False)
        self.le_cash_descr.setStyleSheet("border: 1px solid rgb(180,180,180);")
        self.le_cash_descr.setText("")
        self.le_cash_descr.setAlignment(QtCore.Qt.AlignCenter)
        self.le_cash_descr.setReadOnly(True)
        self.le_cash_descr.setObjectName("le_cash_descr")
        self.verticalLayout_2.addWidget(self.le_cash_descr)
        self.verticalLayout_9.addWidget(self.widget_name_descr_price)
        self.verticalLayout_3.addWidget(self.HEAD_1top)
        self.HEAD_2middle = QtWidgets.QFrame(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HEAD_2middle.sizePolicy().hasHeightForWidth())
        self.HEAD_2middle.setSizePolicy(sizePolicy)
        self.HEAD_2middle.setMinimumSize(QtCore.QSize(0, 36))
        self.HEAD_2middle.setMaximumSize(QtCore.QSize(16777215, 36))
        self.HEAD_2middle.setBaseSize(QtCore.QSize(0, 36))
        self.HEAD_2middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HEAD_2middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HEAD_2middle.setObjectName("HEAD_2middle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.HEAD_2middle)
        self.horizontalLayout_4.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(287, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.manufacturer_1 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_1.sizePolicy().hasHeightForWidth())
        self.manufacturer_1.setSizePolicy(sizePolicy)
        self.manufacturer_1.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_1.setMaximumSize(QtCore.QSize(120, 30))
        self.manufacturer_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_1.setFlat(True)
        self.manufacturer_1.setObjectName("manufacturer_1")
        self.horizontalLayout_4.addWidget(self.manufacturer_1)
        self.manufacturer_2 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_2.sizePolicy().hasHeightForWidth())
        self.manufacturer_2.setSizePolicy(sizePolicy)
        self.manufacturer_2.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_2.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.manufacturer_2.setFont(font)
        self.manufacturer_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_2.setFlat(True)
        self.manufacturer_2.setObjectName("manufacturer_2")
        self.horizontalLayout_4.addWidget(self.manufacturer_2)
        self.manufacturer_3 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_3.sizePolicy().hasHeightForWidth())
        self.manufacturer_3.setSizePolicy(sizePolicy)
        self.manufacturer_3.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_3.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.manufacturer_3.setFont(font)
        self.manufacturer_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_3.setFlat(True)
        self.manufacturer_3.setObjectName("manufacturer_3")
        self.horizontalLayout_4.addWidget(self.manufacturer_3)
        self.manufacturer_4 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_4.sizePolicy().hasHeightForWidth())
        self.manufacturer_4.setSizePolicy(sizePolicy)
        self.manufacturer_4.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_4.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.manufacturer_4.setFont(font)
        self.manufacturer_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_4.setFlat(True)
        self.manufacturer_4.setObjectName("manufacturer_4")
        self.horizontalLayout_4.addWidget(self.manufacturer_4)
        self.manufacturer_5 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_5.sizePolicy().hasHeightForWidth())
        self.manufacturer_5.setSizePolicy(sizePolicy)
        self.manufacturer_5.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_5.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.manufacturer_5.setFont(font)
        self.manufacturer_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_5.setFlat(True)
        self.manufacturer_5.setObjectName("manufacturer_5")
        self.horizontalLayout_4.addWidget(self.manufacturer_5)
        self.manufacturer_6 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_6.sizePolicy().hasHeightForWidth())
        self.manufacturer_6.setSizePolicy(sizePolicy)
        self.manufacturer_6.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_6.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.manufacturer_6.setFont(font)
        self.manufacturer_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_6.setFlat(True)
        self.manufacturer_6.setObjectName("manufacturer_6")
        self.horizontalLayout_4.addWidget(self.manufacturer_6)
        self.manufacturer_7 = QtWidgets.QPushButton(self.HEAD_2middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manufacturer_7.sizePolicy().hasHeightForWidth())
        self.manufacturer_7.setSizePolicy(sizePolicy)
        self.manufacturer_7.setMinimumSize(QtCore.QSize(120, 30))
        self.manufacturer_7.setMaximumSize(QtCore.QSize(120, 30))
        self.manufacturer_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.manufacturer_7.setFlat(True)
        self.manufacturer_7.setObjectName("manufacturer_7")
        self.horizontalLayout_4.addWidget(self.manufacturer_7)
        spacerItem2 = QtWidgets.QSpacerItem(287, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.HEAD_2middle)
        self.HEAD_3bottom = QtWidgets.QFrame(self.widget_3)
        self.HEAD_3bottom.setFrameShape(QtWidgets.QFrame.Panel)
        self.HEAD_3bottom.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HEAD_3bottom.setObjectName("HEAD_3bottom")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.HEAD_3bottom)
        self.verticalLayout_7.setContentsMargins(9, 2, 9, 2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.HEAD_3bottom)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 32))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame_3.setBaseSize(QtCore.QSize(0, 32))
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chb_show_exact = QtWidgets.QCheckBox(self.frame_4)
        self.chb_show_exact.setEnabled(True)
        self.chb_show_exact.setMaximumSize(QtCore.QSize(120, 16777215))
        self.chb_show_exact.setObjectName("chb_show_exact")
        self.horizontalLayout.addWidget(self.chb_show_exact)
        self.chb_show_date = QtWidgets.QCheckBox(self.frame_4)
        self.chb_show_date.setEnabled(True)
        self.chb_show_date.setMaximumSize(QtCore.QSize(120, 16777215))
        self.chb_show_date.setObjectName("chb_show_date")
        self.horizontalLayout.addWidget(self.chb_show_date)
        self.pb_adv_search = QtWidgets.QPushButton(self.frame_4)
        self.pb_adv_search.setEnabled(True)
        self.pb_adv_search.setMaximumSize(QtCore.QSize(120, 16777215))
        self.pb_adv_search.setAutoDefault(False)
        self.pb_adv_search.setDefault(False)
        self.pb_adv_search.setFlat(False)
        self.pb_adv_search.setObjectName("pb_adv_search")
        self.horizontalLayout.addWidget(self.pb_adv_search)
        self.hboxlayout.addWidget(self.frame_4)
        self.search_widget = QtWidgets.QWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_widget.sizePolicy().hasHeightForWidth())
        self.search_widget.setSizePolicy(sizePolicy)
        self.search_widget.setMinimumSize(QtCore.QSize(80, 30))
        self.search_widget.setMaximumSize(QtCore.QSize(540, 30))
        self.search_widget.setBaseSize(QtCore.QSize(540, 30))
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.search_layout = QtWidgets.QHBoxLayout()
        self.search_layout.setSpacing(0)
        self.search_layout.setObjectName("search_layout")
        self.horizontalLayout_9.addLayout(self.search_layout)
        self.hboxlayout.addWidget(self.search_widget)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(12, 0, 12, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.chb_price_name_only = QtWidgets.QCheckBox(self.frame_5)
        self.chb_price_name_only.setEnabled(True)
        self.chb_price_name_only.setChecked(True)
        self.chb_price_name_only.setObjectName("chb_price_name_only")
        self.horizontalLayout_6.addWidget(self.chb_price_name_only)
        self.chb_search_eng = QtWidgets.QCheckBox(self.frame_5)
        self.chb_search_eng.setEnabled(True)
        self.chb_search_eng.setChecked(True)
        self.chb_search_eng.setObjectName("chb_search_eng")
        self.horizontalLayout_6.addWidget(self.chb_search_eng)
        self.chb_search_narrow = QtWidgets.QCheckBox(self.frame_5)
        self.chb_search_narrow.setChecked(True)
        self.chb_search_narrow.setObjectName("chb_search_narrow")
        self.horizontalLayout_6.addWidget(self.chb_search_narrow)
        self.hboxlayout.addWidget(self.frame_5)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.HEAD_3bottom)
        self.HEAD_3bottom.raise_()
        self.HEAD_2middle.raise_()
        self.HEAD_1top.raise_()
        self.verticalLayout_8.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.HEAD)
        self.BODY = QtWidgets.QWidget(self.centralwidget)
        self.BODY.setObjectName("BODY")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.BODY)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tab_widget = QtWidgets.QTabWidget(self.BODY)
        self.tab_widget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setObjectName("tab_widget")
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_0)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.table_parts = QtWidgets.QTableWidget(self.tab_0)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.table_parts.setFont(font)
        self.table_parts.setFrameShape(QtWidgets.QFrame.Panel)
        self.table_parts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_parts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_parts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_parts.setShowGrid(False)
        self.table_parts.setColumnCount(8)
        self.table_parts.setObjectName("table_parts")
        self.table_parts.setRowCount(0)
        self.table_parts.horizontalHeader().setDefaultSectionSize(4)
        self.table_parts.horizontalHeader().setHighlightSections(False)
        self.table_parts.horizontalHeader().setMinimumSectionSize(4)
        self.table_parts.verticalHeader().setVisible(False)
        self.table_parts.verticalHeader().setDefaultSectionSize(14)
        self.table_parts.verticalHeader().setMinimumSectionSize(14)
        self.verticalLayout_5.addWidget(self.table_parts)
        self.tab_widget.addTab(self.tab_0, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.table_accesory = QtWidgets.QTableWidget(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.table_accesory.setFont(font)
        self.table_accesory.setFrameShape(QtWidgets.QFrame.Panel)
        self.table_accesory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_accesory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_accesory.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_accesory.setShowGrid(False)
        self.table_accesory.setColumnCount(8)
        self.table_accesory.setObjectName("table_accesory")
        self.table_accesory.setRowCount(0)
        self.table_accesory.horizontalHeader().setDefaultSectionSize(4)
        self.table_accesory.horizontalHeader().setHighlightSections(False)
        self.table_accesory.horizontalHeader().setMinimumSectionSize(4)
        self.table_accesory.verticalHeader().setVisible(False)
        self.table_accesory.verticalHeader().setDefaultSectionSize(14)
        self.table_accesory.verticalHeader().setMinimumSectionSize(14)
        self.verticalLayout_6.addWidget(self.table_accesory)
        self.tab_widget.addTab(self.tab_1, "")
        self.horizontalLayout_3.addWidget(self.tab_widget)
        self.price_widget = QtWidgets.QWidget(self.BODY)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.price_widget.sizePolicy().hasHeightForWidth())
        self.price_widget.setSizePolicy(sizePolicy)
        self.price_widget.setObjectName("price_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.price_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.model_widget = QtWidgets.QWidget(self.price_widget)
        self.model_widget.setMinimumSize(QtCore.QSize(0, 20))
        self.model_widget.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.model_widget.setFont(font)
        self.model_widget.setObjectName("model_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.model_widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lay_model_buttons = QtWidgets.QHBoxLayout()
        self.lay_model_buttons.setObjectName("lay_model_buttons")
        self.horizontalLayout_2.addLayout(self.lay_model_buttons)
        self.verticalLayout_4.addWidget(self.model_widget)
        self.table_price = QtWidgets.QTableWidget(self.price_widget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.table_price.setFont(font)
        self.table_price.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_price.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_price.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_price.setShowGrid(False)
        self.table_price.setColumnCount(3)
        self.table_price.setObjectName("table_price")
        self.table_price.setRowCount(0)
        self.table_price.horizontalHeader().setDefaultSectionSize(4)
        self.table_price.horizontalHeader().setHighlightSections(False)
        self.table_price.horizontalHeader().setMinimumSectionSize(4)
        self.table_price.verticalHeader().setVisible(False)
        self.table_price.verticalHeader().setDefaultSectionSize(14)
        self.table_price.verticalHeader().setMinimumSectionSize(14)
        self.verticalLayout_4.addWidget(self.table_price)
        self.horizontalLayout_3.addWidget(self.price_widget)
        self.verticalLayout.addWidget(self.BODY)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.help.setText(_translate("MainWindow", "Помощь"))
        self.graph_button.setText(_translate("MainWindow", "Статистика"))
        self.settings_button.setText(_translate("MainWindow", "Настройки"))
        self.label_db.setText(_translate("MainWindow", "База:"))
        self.label_price.setText(_translate("MainWindow", "Прайс:"))
        self.le_cash_name.setPlaceholderText(_translate("MainWindow", "Даблклік для копіювання"))
        self.chb_show_exact.setText(_translate("MainWindow", "Фильтр модели"))
        self.chb_show_date.setText(_translate("MainWindow", "Показать дату"))
        self.pb_adv_search.setText(_translate("MainWindow", "Расш. поиск"))
        self.chb_price_name_only.setText(_translate("MainWindow", "Модель прайса"))
        self.chb_search_eng.setText(_translate("MainWindow", "Латиница"))
        self.chb_search_narrow.setText(_translate("MainWindow", "Два символа"))
        self.table_parts.setSortingEnabled(True)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_0), _translate("MainWindow", "   ЗАПЧАСТИ   "))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_1), _translate("MainWindow", "  АКСЕССУАРЫ  "))
