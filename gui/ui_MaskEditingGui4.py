# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaskEditingGui4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MaskEditingGui(object):
    def setupUi(self, MaskEditingGui):
        MaskEditingGui.setObjectName(_fromUtf8("MaskEditingGui"))
        MaskEditingGui.resize(1046, 825)
        self.verticalLayout = QtGui.QVBoxLayout(MaskEditingGui)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gview_submasks = QtGui.QGraphicsView(MaskEditingGui)
        self.gview_submasks.setObjectName(_fromUtf8("gview_submasks"))
        self.gridLayout_2.addWidget(self.gview_submasks, 6, 0, 1, 1)
        self.gview_merged_mask = QtGui.QGraphicsView(MaskEditingGui)
        self.gview_merged_mask.setObjectName(_fromUtf8("gview_merged_mask"))
        self.gridLayout_2.addWidget(self.gview_merged_mask, 6, 2, 1, 1)
        self.gview_final_masks_user = QtGui.QGraphicsView(MaskEditingGui)
        self.gview_final_masks_user.setObjectName(_fromUtf8("gview_final_masks_user"))
        self.gridLayout_2.addWidget(self.gview_final_masks_user, 6, 1, 1, 1)
        self.gview_slic = QtGui.QGraphicsView(MaskEditingGui)
        self.gview_slic.setMaximumSize(QtCore.QSize(500, 500))
        self.gview_slic.setObjectName(_fromUtf8("gview_slic"))
        self.gridLayout_2.addWidget(self.gview_slic, 1, 2, 1, 1)
        self.gview_final_masks_auto = QtGui.QGraphicsView(MaskEditingGui)
        self.gview_final_masks_auto.setMaximumSize(QtCore.QSize(500, 500))
        self.gview_final_masks_auto.setObjectName(_fromUtf8("gview_final_masks_auto"))
        self.gridLayout_2.addWidget(self.gview_final_masks_auto, 1, 0, 1, 1)
        self.gview_thresholded = QtGui.QGraphicsView(MaskEditingGui)
        self.gview_thresholded.setMaximumSize(QtCore.QSize(500, 500))
        self.gview_thresholded.setObjectName(_fromUtf8("gview_thresholded"))
        self.gridLayout_2.addWidget(self.gview_thresholded, 1, 1, 1, 1)
        self.button_slic = QtGui.QPushButton(MaskEditingGui)
        self.button_slic.setObjectName(_fromUtf8("button_slic"))
        self.gridLayout_2.addWidget(self.button_slic, 4, 2, 1, 1)
        self.label_3 = QtGui.QLabel(MaskEditingGui)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(MaskEditingGui)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(MaskEditingGui)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(MaskEditingGui)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.slider_dissimThresh = QtGui.QSlider(MaskEditingGui)
        self.slider_dissimThresh.setOrientation(QtCore.Qt.Horizontal)
        self.slider_dissimThresh.setObjectName(_fromUtf8("slider_dissimThresh"))
        self.horizontalLayout_3.addWidget(self.slider_dissimThresh)
        self.label_dissimThresh = QtGui.QLabel(MaskEditingGui)
        self.label_dissimThresh.setObjectName(_fromUtf8("label_dissimThresh"))
        self.horizontalLayout_3.addWidget(self.label_dissimThresh)
        self.button_submasks = QtGui.QPushButton(MaskEditingGui)
        self.button_submasks.setObjectName(_fromUtf8("button_submasks"))
        self.horizontalLayout_3.addWidget(self.button_submasks)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 8, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.comboBox_channel = QtGui.QComboBox(MaskEditingGui)
        self.comboBox_channel.setObjectName(_fromUtf8("comboBox_channel"))
        self.gridLayout_4.addWidget(self.comboBox_channel, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(MaskEditingGui)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.label_7 = QtGui.QLabel(MaskEditingGui)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_9 = QtGui.QLabel(MaskEditingGui)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 5, 1, 1, 1)
        self.label_6 = QtGui.QLabel(MaskEditingGui)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 5, 2, 1, 1)
        self.button_snake = QtGui.QPushButton(MaskEditingGui)
        self.button_snake.setObjectName(_fromUtf8("button_snake"))
        self.gridLayout_2.addWidget(self.button_snake, 8, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.button_update_merged_mask = QtGui.QPushButton(MaskEditingGui)
        self.button_update_merged_mask.setObjectName(_fromUtf8("button_update_merged_mask"))
        self.horizontalLayout_2.addWidget(self.button_update_merged_mask)
        self.button_toggle_accept_auto = QtGui.QPushButton(MaskEditingGui)
        self.button_toggle_accept_auto.setText(_fromUtf8(""))
        self.button_toggle_accept_auto.setObjectName(_fromUtf8("button_toggle_accept_auto"))
        self.horizontalLayout_2.addWidget(self.button_toggle_accept_auto)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 8, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line = QtGui.QFrame(MaskEditingGui)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_autogenMasks = QtGui.QPushButton(MaskEditingGui)
        self.button_autogenMasks.setObjectName(_fromUtf8("button_autogenMasks"))
        self.horizontalLayout.addWidget(self.button_autogenMasks)
        self.button_saveAll = QtGui.QPushButton(MaskEditingGui)
        self.button_saveAll.setObjectName(_fromUtf8("button_saveAll"))
        self.horizontalLayout.addWidget(self.button_saveAll)
        self.button_uploadMasks = QtGui.QPushButton(MaskEditingGui)
        self.button_uploadMasks.setObjectName(_fromUtf8("button_uploadMasks"))
        self.horizontalLayout.addWidget(self.button_uploadMasks)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MaskEditingGui)
        QtCore.QMetaObject.connectSlotsByName(MaskEditingGui)

    def retranslateUi(self, MaskEditingGui):
        MaskEditingGui.setWindowTitle(_translate("MaskEditingGui", "Review Masks", None))
        self.button_slic.setText(_translate("MaskEditingGui", "Update SLIC", None))
        self.label_3.setText(_translate("MaskEditingGui", "Automatic Masks", None))
        self.label_4.setText(_translate("MaskEditingGui", "Channel", None))
        self.label_5.setText(_translate("MaskEditingGui", "SLIC", None))
        self.label_8.setText(_translate("MaskEditingGui", "Dissim Threshold", None))
        self.label_dissimThresh.setText(_translate("MaskEditingGui", "0.5", None))
        self.button_submasks.setText(_translate("MaskEditingGui", "Update Init Masks", None))
        self.label_2.setText(_translate("MaskEditingGui", "Channel", None))
        self.label_7.setText(_translate("MaskEditingGui", "Initial Masks for Snake", None))
        self.label_9.setText(_translate("MaskEditingGui", "User Masks", None))
        self.label_6.setText(_translate("MaskEditingGui", "Merged Mask", None))
        self.button_snake.setText(_translate("MaskEditingGui", "Update Snake Final Masks", None))
        self.button_update_merged_mask.setText(_translate("MaskEditingGui", "Update Merged Mask", None))
        self.button_autogenMasks.setText(_translate("MaskEditingGui", "Automatically Generate All Masks", None))
        self.button_saveAll.setText(_translate("MaskEditingGui", "Save All Decisions", None))
        self.button_uploadMasks.setText(_translate("MaskEditingGui", "Upload", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MaskEditingGui = QtGui.QDialog()
    ui = Ui_MaskEditingGui()
    ui.setupUi(MaskEditingGui)
    MaskEditingGui.show()
    sys.exit(app.exec_())

