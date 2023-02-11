# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_window(object):
    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(597, 565)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings_window.sizePolicy().hasHeightForWidth())
        settings_window.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        settings_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("start_test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settings_window.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings_window)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.frame = QtWidgets.QFrame(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.web_login = QtWidgets.QLineEdit(self.frame)
        self.web_login.setObjectName("web_login")
        self.verticalLayout_6.addWidget(self.web_login)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.web_password = QtWidgets.QLineEdit(self.frame)
        self.web_password.setObjectName("web_password")
        self.verticalLayout_5.addWidget(self.web_password)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addWidget(self.frame)
        self.label_14 = QtWidgets.QLabel(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.frame_7 = QtWidgets.QFrame(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.cb_branch = QtWidgets.QComboBox(self.frame_7)
        self.cb_branch.setObjectName("cb_branch")
        self.verticalLayout_11.addWidget(self.cb_branch)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout.addWidget(self.frame_7)
        self.label_7 = QtWidgets.QLabel(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.frame_4 = QtWidgets.QFrame(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lb_language = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_language.sizePolicy().hasHeightForWidth())
        self.lb_language.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_language.setFont(font)
        self.lb_language.setObjectName("lb_language")
        self.horizontalLayout_11.addWidget(self.lb_language)
        self.cb_language = QtWidgets.QComboBox(self.frame_6)
        self.cb_language.setObjectName("cb_language")
        self.horizontalLayout_11.addWidget(self.cb_language)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.chk_fullscreen = QtWidgets.QCheckBox(self.frame_6)
        self.chk_fullscreen.setObjectName("chk_fullscreen")
        self.horizontalLayout_6.addWidget(self.chk_fullscreen)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_13.addWidget(self.frame_6)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setBaseSize(QtCore.QSize(0, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_13.addWidget(self.label_11)
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chb_show_exact = QtWidgets.QCheckBox(self.frame_2)
        self.chb_show_exact.setEnabled(False)
        self.chb_show_exact.setMinimumSize(QtCore.QSize(130, 0))
        self.chb_show_exact.setMaximumSize(QtCore.QSize(160, 16777215))
        self.chb_show_exact.setObjectName("chb_show_exact")
        self.horizontalLayout.addWidget(self.chb_show_exact)
        self.chb_price_name_only = QtWidgets.QCheckBox(self.frame_2)
        self.chb_price_name_only.setEnabled(True)
        self.chb_price_name_only.setMinimumSize(QtCore.QSize(130, 0))
        self.chb_price_name_only.setMaximumSize(QtCore.QSize(160, 16777215))
        self.chb_price_name_only.setChecked(True)
        self.chb_price_name_only.setObjectName("chb_price_name_only")
        self.horizontalLayout.addWidget(self.chb_price_name_only)
        self.chb_search_eng = QtWidgets.QCheckBox(self.frame_2)
        self.chb_search_eng.setEnabled(True)
        self.chb_search_eng.setMinimumSize(QtCore.QSize(130, 0))
        self.chb_search_eng.setMaximumSize(QtCore.QSize(160, 16777215))
        self.chb_search_eng.setChecked(True)
        self.chb_search_eng.setObjectName("chb_search_eng")
        self.horizontalLayout.addWidget(self.chb_search_eng)
        self.chb_search_narrow = QtWidgets.QCheckBox(self.frame_2)
        self.chb_search_narrow.setMinimumSize(QtCore.QSize(130, 0))
        self.chb_search_narrow.setMaximumSize(QtCore.QSize(160, 16777215))
        self.chb_search_narrow.setChecked(True)
        self.chb_search_narrow.setObjectName("chb_search_narrow")
        self.horizontalLayout.addWidget(self.chb_search_narrow)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_13.addWidget(self.frame_2)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setBaseSize(QtCore.QSize(0, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_13.addWidget(self.label_10)
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zebra_contrast = QtWidgets.QSpinBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zebra_contrast.sizePolicy().hasHeightForWidth())
        self.zebra_contrast.setSizePolicy(sizePolicy)
        self.zebra_contrast.setMaximum(30)
        self.zebra_contrast.setObjectName("zebra_contrast")
        self.horizontalLayout_3.addWidget(self.zebra_contrast)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.colored_price_table = QtWidgets.QCheckBox(self.frame_3)
        self.colored_price_table.setObjectName("colored_price_table")
        self.verticalLayout_2.addWidget(self.colored_price_table)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.word_wrap_web_table = QtWidgets.QCheckBox(self.frame_3)
        self.word_wrap_web_table.setObjectName("word_wrap_web_table")
        self.verticalLayout_9.addWidget(self.word_wrap_web_table)
        self.gridLayout.addLayout(self.verticalLayout_9, 4, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.word_wrap_price_table = QtWidgets.QCheckBox(self.frame_3)
        self.word_wrap_price_table.setObjectName("word_wrap_price_table")
        self.verticalLayout_10.addWidget(self.word_wrap_price_table)
        self.gridLayout.addLayout(self.verticalLayout_10, 4, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.colored_web_table = QtWidgets.QCheckBox(self.frame_3)
        self.colored_web_table.setObjectName("colored_web_table")
        self.verticalLayout_8.addWidget(self.colored_web_table)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tables_font_size = QtWidgets.QSpinBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tables_font_size.sizePolicy().hasHeightForWidth())
        self.tables_font_size.setSizePolicy(sizePolicy)
        self.tables_font_size.setMinimum(8)
        self.tables_font_size.setMaximum(26)
        self.tables_font_size.setProperty("value", 14)
        self.tables_font_size.setObjectName("tables_font_size")
        self.horizontalLayout_2.addWidget(self.tables_font_size)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_13.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.label_8 = QtWidgets.QLabel(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.frame_5 = QtWidgets.QFrame(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.income_overprice_perc = QtWidgets.QSpinBox(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.income_overprice_perc.sizePolicy().hasHeightForWidth())
        self.income_overprice_perc.setSizePolicy(sizePolicy)
        self.income_overprice_perc.setMinimum(0)
        self.income_overprice_perc.setMaximum(200)
        self.income_overprice_perc.setProperty("value", 4)
        self.income_overprice_perc.setObjectName("income_overprice_perc")
        self.horizontalLayout_7.addWidget(self.income_overprice_perc)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(settings_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settings_window)
        self.buttonBox.accepted.connect(settings_window.accept) # type: ignore
        self.buttonBox.rejected.connect(settings_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(settings_window)

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "Настройки"))
        self.label_6.setText(_translate("settings_window", "Доступ"))
        self.frame.setToolTip(_translate("settings_window", "Данные для входа в \"димку\""))
        self.label_2.setText(_translate("settings_window", "DK Логин:"))
        self.label_3.setText(_translate("settings_window", "DK Пароль:"))
        self.label_14.setText(_translate("settings_window", "Сбор статистики"))
        self.frame_7.setToolTip(_translate("settings_window", "Влияет только на сбор статистики"))
        self.label_9.setText(_translate("settings_window", "Ваше отделение (прочерк для отключения):"))
        self.label_7.setText(_translate("settings_window", "Интерфейс"))
        self.lb_language.setText(_translate("settings_window", "Язык интерфейса:"))
        self.chk_fullscreen.setText(_translate("settings_window", "Запуск во весь экран"))
        self.label_11.setText(_translate("settings_window", "Настройки поиска при запуске"))
        self.chb_show_exact.setText(_translate("settings_window", "Искомая модель"))
        self.chb_price_name_only.setText(_translate("settings_window", "Модель прайса"))
        self.chb_search_eng.setText(_translate("settings_window", "Латиница"))
        self.chb_search_narrow.setText(_translate("settings_window", "Минимум 2"))
        self.label_10.setText(_translate("settings_window", "Таблицы"))
        self.label_4.setText(_translate("settings_window", "Контраст зебры"))
        self.colored_price_table.setText(_translate("settings_window", "Цвета прайса"))
        self.word_wrap_web_table.setText(_translate("settings_window", "Перенос строк интернет базы"))
        self.word_wrap_price_table.setText(_translate("settings_window", "Перенос строк прайса"))
        self.colored_web_table.setText(_translate("settings_window", "Цвета интернет базы"))
        self.label_5.setText(_translate("settings_window", "Размер шрифта таблиц"))
        self.label_8.setText(_translate("settings_window", "Калькуляция"))
        self.label_12.setText(_translate("settings_window", "Наценка при поступлени на склад (доп. % к ценам веб базы):"))
