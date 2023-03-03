#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2022 Cryogenic System <Cryogenic System@CRYOGENICSYSTEM>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#import pyvisa as visa
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtWidgets
import sweep_dialog
import timing_dialog
import sequence_dialog
import graph_dialog
import visalab_ui
import pyqtgraph as pg
import pyvisa
# import numpy as np
from time import localtime, strftime, time

# class TestApp(QtWidgets.QWidget, visalab_dialogs.sweep_Ui_Form):
	# def __init__(self):
		# super().__init__()
		# self.setupUi(self)
class visaLabApp(QtWidgets.QMainWindow, visalab_ui.Ui_visaLab):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		self.run_timer = QtCore.QTimer()
		
		self.rm = pyvisa.ResourceManager()
		
		self.td = timing_dialog.timingDialog()
		self.swdialog = sweep_dialog.sweepDialog(self.rm)
		self.seq_dialog = sequence_dialog.seqDialog(self.rm)
		self.gdialog = graph_dialog.graphDialog()
		self.first_flag = True
		self.settingsList.setReadOnly(True)
		self.swdialog.tumbler.setCheckState(False)
						
		self.state = {}
		self.data =[]
		self.color_index = 0
		self.initSettings()
		self.t_start = time()
		self.p1 = pg.mkPen('#8BFD07', width=1.2)
		self.p2 = pg.mkPen('#FC75F6', width=1.2)
		self.p3 = pg.mkPen('#F69F88', width=1.2)
		#F69F88
		self.initGraphs()
		self.attempts = 0
		
		self.actionTiming.triggered.connect(self.configTiming)
		self.actionExit.triggered.connect(self.okToContinue)
		self.actionSequence.triggered.connect(self.configSequence)
		self.actionAbout.triggered.connect(self.about)
		self.actionSweep_settings.triggered.connect(self.configSweep)
		self.actionChange_File.triggered.connect(self.changeFile)
		self.actionGraph_settings.triggered.connect(self.graphSettings)
		self.swdialog.tumbler.stateChanged.connect(self.onSwTumbler)
		self.run_timer.timeout.connect(self.getData)
		
		self.gdialog.g1xcombo.currentTextChanged.connect(self.confGraphsAxes)
		self.gdialog.g1ycombo.currentTextChanged.connect(self.confGraphsAxes)
		self.gdialog.g2xcombo.currentTextChanged.connect(self.confGraphsAxes)
		self.gdialog.g2ycombo.currentTextChanged.connect(self.confGraphsAxes)
		self.gdialog.g3xcombo.currentTextChanged.connect(self.confGraphsAxes)
		self.gdialog.g3ycombo.currentTextChanged.connect(self.confGraphsAxes)
		self.gdialog.g1xscale.textChanged.connect(self.confGraphsAxes)
		self.gdialog.g1yscale.textChanged.connect(self.confGraphsAxes)
		self.gdialog.g2xscale.textChanged.connect(self.confGraphsAxes)
		self.gdialog.g2yscale.textChanged.connect(self.confGraphsAxes)
		self.gdialog.g3xscale.textChanged.connect(self.confGraphsAxes)
		self.gdialog.g3yscale.textChanged.connect(self.confGraphsAxes)
		
		self.masterButton.clicked.connect(self.onStart)
		
		
	def configTiming(self):
		if self.td.exec():
			self.state['delay1'] = self.td.delay1.cleanText()
			self.state['delay2'] = self.td.delay2.cleanText()
			self.state['nloops'] = self.td.nloops.cleanText()
			self.updateSettings()
		
	def updateSettings(self):
		self.settingsList.clear()
		if self.state['currentFile'] == "No file":
			self.settingsList.append("No file is selected!")
		else:
			self.settingsList.append("Current file name:")
			self.settingsList.append(self.state['currentFile']+"")
		if self.state['isRunning']:
			self.settingsList.append("Time loop is running")
		else:
			self.settingsList.append("Time loop is stopped")
		if self.state['sequenceisEmpty']:
			self.settingsList.append("Sequence is empty")
		else:
			self.settingsList.append("Sequence:")
			s = self.seq_dialog.printSequence()
			for l in s:
				self.settingsList.append(l)
		self.settingsList.append("Primary loop delay"
                                     " is " + self.state['delay1'] + " ms")
		if self.state['sweepstate']:
			self.settingsList.append("Secondary loop delay"
                                     " is " + self.state['delay2'] + " ms")
			self.settingsList.append("Number of secondary loops"
                                     " is " + self.state['nloops'])
			self.settingsList.append("Sweep is enabled")
			self.settingsList.append("Sweep: start value "
                                     "is " + self.state['sweepStart'])
			self.settingsList.append("Sweep: stop value "
                                     "is " + self.state['sweepStop'])
			self.settingsList.append("Sweep: current value "
                                     "is " + self.state['sweepCurrent'])
			self.settingsList.append("Sweep: increment is "
                                     +self.state['sweepIncrement'])
		else:
			self.settingsList.append("Sweep is disabled")
		
		if self.state['testMode']:
			self.settingsList.append("Program is working in test mode!")

	def initSettings(self):
		self.state['delay1'] = self.td.delay1.cleanText()
		self.state['delay2'] = self.td.delay2.cleanText()
		# self.state['currentFile'] = 'No file!'
		self.state['currentFile'] = strftime('data%d-%m-%y_%H-%M-%S.txt',
		localtime())
		self.state['isRunning'] = False
		self.state['sequenceisEmpty'] = True
		self.state['sweepstate'] = False
		self.state['sweepStart'] = self.swdialog.vStart.cleanText()
		self.state['sweepStop'] = self.swdialog.vStop.cleanText()
		self.state['sweepCurrent'] = self.swdialog.vCurrent.displayText()
		self.state['sweepIncrement'] = self.swdialog.increment.cleanText()
		self.state['testMode'] = True
		self.state['nloops'] = self.td.nloops.cleanText()
		self.updateSettings()
		
	def changeFile(self):
		#print('Change file')
		t = strftime('data%d-%m-%y_%H-%M-%S.txt',
		localtime())
		self.t_start = time()
		self.first_flag = True
		save_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Set/Change data file', 
		t, filter = 'Text files (*.txt, *.dat)')
		if save_path[0]:
			self.state['currentFile'] = save_path[0]
			self.updateSettings()
		
	def okToContinue(self):
		#print('okToContinue')
		r = QtWidgets.QMessageBox.warning(self, "visaLab",
                               "Are you sure want to close application?",
                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		if r == QtWidgets.QMessageBox.Yes:
			return self.close()
		else: 
			return False
	
	def configSequence(self):
		if self.seq_dialog.exec():
			print('Sequence changed!')
			self.first_flag = True
			self.state['currentFile'] = strftime('data%d-%m-%y_%H-%M-%S.txt',
				localtime())
			if self.seq_dialog.seqTable.rowCount():
				self.state['sequenceisEmpty'] = False
				self.data = []
				self.data = self.seq_dialog.makeDataStruct()
				self.data.append({'instr':'System',
				'var': 'Time', 'command': 'time', 'data': []})
				self.gdialog.g1xcombo.clear()
				self.gdialog.g1ycombo.clear()
				self.gdialog.g2xcombo.clear()
				self.gdialog.g2ycombo.clear()
				self.gdialog.g3xcombo.clear()
				self.gdialog.g3ycombo.clear()
				
				for i in range(len(self.data)):
					self.gdialog.g1xcombo.addItem('[{0}] {1}'.format(
					i+1, self.data[i]['var']))
					self.gdialog.g1ycombo.addItem('[{0}] {1}'.format(
					i+1, self.data[i]['var']))
					self.gdialog.g2xcombo.addItem('[{0}] {1}'.format(
					i+1, self.data[i]['var']))
					self.gdialog.g2ycombo.addItem('[{0}] {1}'.format(
					i+1, self.data[i]['var']))
					self.gdialog.g3xcombo.addItem('[{0}] {1}'.format(
					i+1, self.data[i]['var']))
					self.gdialog.g3ycombo.addItem('[{0}] {1}'.format(
					i+1, self.data[i]['var']))
			self.updateSettings()
			self.initGraphs()
			self.confGraphsAxes()
		else:
			print('Sequence left unchanged!')
		
	def graphSettings(self):
		if self.gdialog.exec():
			print('Graph settings changed!')
		else:
			print('Graph settings closed!')
	
	def about(self):
		_translate = QtCore.QCoreApplication.translate
		QtWidgets.QMessageBox.about(self, "About visaLab",
                       "<h2> viasLab v0.1 </h2>"
                          "<p>This is simple application for "
                          "measurement automation. It relies "
                          "upon NI-VISA software for communication "
                          "with instruments and upon Qt libraries "
                          "for GUI implementation."
                          "<p>Created by Valera Prudkoglyad in 2022"
                          "<p>The program is provided AS IS with NO WARRANTY "
                          "OF ANY KIND, INCLUDING THE WARRANTY OF DESIGN, "
                          "MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.")
		
	def configSweep(self):
		if self.swdialog.exec():
			self.state['sweepstate']=self.swdialog.tumbler.isChecked()
        
		if self.state['sweepstate']:
			self.state['sweepStart']=self.swdialog.vStart.cleanText()
			self.state['sweepStop']=self.swdialog.vStop.cleanText()
			self.state['sweepCurrent']=self.swdialog.vCurrent.displayText()
			self.state['sweepIncrement']=self.swdialog.increment.cleanText()
		
		self.updateSettings()
	
	def onStart(self):
		if not self.state['isRunning']:
			self.masterButton.setText("Stop")
			self.state['isRunning'] = True
			self.attempts = 0
			self.updateSettings()
        #Here we disable configuration actions as we
        #do not want user to change timing and sequence settings
        #on the fly
			self.actionChange_File.setEnabled(False)
			self.actionSequence.setEnabled(False)
			self.actionSweep_settings.setEnabled(False)
			self.actionTiming.setEnabled(False)
			self.run_timer.setInterval(self.td.delay1.value())
			self.run_timer.start()
		else:
			self.run_timer.stop()
			self.masterButton.setText("Start")
			self.state['isRunning'] = False
			self.updateSettings()
        #As data acquisition stops,
        #we bring back configuration possibilities
			self.actionChange_File.setEnabled(True)
			self.actionSequence.setEnabled(True)
			self.actionSweep_settings.setEnabled(True)
			self.actionTiming.setEnabled(True)
			
			
	def getData(self):
		l = ''
		if self.first_flag and not self.state['sequenceisEmpty']:
			l = 'Time\t'
			for i in range(len(self.data)-1):
				l = l + self.data[i]['var']+'\t'
			
			with open(self.state['currentFile'], 'a') as f:
				f.write(l[:-1]+'\n')
			self.first_flag = False
		elif not self.state['sequenceisEmpty']:				
			try:
				for i in range(len(self.data)):
					if not self.data[i]['command'].find('2s_') == -1:
						inst = self.rm.open_resource(self.data[i]['instr'])
						v = inst.query(self.data[i]['command'][3:]).strip('\n\r').split(',')
						# print(v)
						self.data[i]['data'].append(float(v[0]))
						self.data[i+1]['data'].append(float(v[1]))
						l = l+v[0]+'\t'+ v[1]+'\t'
						
					elif not self.data[i]['command'].find('2e_') == -1:
						pass
					elif not self.data[i]['var'] == 'Time':
						# print('Reading \"{0}\" from \"{1}\"'.format(d['var'],
						# d['instr']))
						inst = self.rm.open_resource(self.data[i]['instr'])
						# print(d['command'])
						v = inst.query(self.data[i]['command'])
						self.data[i]['data'].append(float(v))
						l = l+v.strip('\n\r')+'\t'
						# print('OK')
						
					else:
						elapsed = time() - self.t_start
						l = str(elapsed) + '\t' + l + '\n'
						self.data[i]['data'].append(float(elapsed))
						# print('Time elapsed: {0}'.format(elapsed))
				with open(self.state['currentFile'], 'a') as f:
					f.write(l)
				self.updateGraphs()
			except Exception:
				if self.attempts<2:
					print('Instrument communication failed!')
					self.attempts += 1
				else:
					self.onStart()
		
	def confGraphsAxes(self):
		if not self.gdialog.g1xcombo.count() == 0:
			# setting axis labels
			label = '{0}, scale: {1}'.format
			self.plot1.setLabel('left', label(self.gdialog.g1ycombo.currentText(),
			self.gdialog.g1yscale.value()))
			self.plot1.setLabel('bottom', label(self.gdialog.g1xcombo.currentText(),
			self.gdialog.g1xscale.value()))
			
			self.plot2.setLabel('left', label(self.gdialog.g2ycombo.currentText(),
			self.gdialog.g2yscale.value()))
			self.plot2.setLabel('bottom', label(self.gdialog.g2xcombo.currentText(),
			self.gdialog.g2xscale.value()))
			
			self.plot3.setLabel('left', label(self.gdialog.g3ycombo.currentText(),
			self.gdialog.g3yscale.value()))
			self.plot3.setLabel('bottom', label(self.gdialog.g3xcombo.currentText(),
			self.gdialog.g3xscale.value()))
			
			# setting axis scales
			self.plot1.getAxis('bottom').setScale(self.gdialog.g1xscale.value())
			self.plot1.getAxis('left').setScale(self.gdialog.g1yscale.value())
			self.plot2.getAxis('bottom').setScale(self.gdialog.g2xscale.value())
			self.plot2.getAxis('left').setScale(self.gdialog.g2yscale.value())
			self.plot3.getAxis('bottom').setScale(self.gdialog.g3xscale.value())
			self.plot3.getAxis('left').setScale(self.gdialog.g3yscale.value())
			
			
			
			
	
	def initGraphs(self):
		
		self.plot1.clear()
		self.plot2.clear()
		self.plot3.clear()
		
		self.curve1 = self.plot1.plot(pen=self.p1, 
				symbolBrush=(241,239,26), symbolPen='w', symbol='o', 
				symbolSize=4)
		self.curve2 = self.plot2.plot(pen=self.p2, 
				symbolBrush=(241,239,26), symbolPen='w', symbol='o', 
				symbolSize=4)
		self.curve3 = self.plot3.plot(pen=self.p3, 
				symbolBrush=(241,239,26), symbolPen='w', symbol='o', 
				symbolSize=4)
		
			
		
	def updateGraphs(self):
		# try:
			# print(len(self.data[self.gdialog.g1xcombo.currentIndex()]['data']))
			# print(len(self.data[self.gdialog.g1ycombo.currentIndex()]['data']))
		self.curve1.setData(self.data[self.gdialog.g1xcombo.currentIndex()]['data'],
		self.data[self.gdialog.g1ycombo.currentIndex()]['data'])
		self.curve2.setData(self.data[self.gdialog.g2xcombo.currentIndex()]['data'],
		self.data[self.gdialog.g2ycombo.currentIndex()]['data'])
		self.curve3.setData(self.data[self.gdialog.g3xcombo.currentIndex()]['data'],
		self.data[self.gdialog.g3ycombo.currentIndex()]['data'])
		# except Exception:
			# print('Wrong data!')
		
		
	def onSwTumbler(self, st: bool):
		self.td.delay2.setEnabled(st)
		self.td.nloops.setEnabled(st)
				
def main(args):
	app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
	window = visaLabApp()  # Создаём объект класса visaLabApp
	window.show()  # Показываем окно
	app.exec_()  # и запускаем приложение

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
