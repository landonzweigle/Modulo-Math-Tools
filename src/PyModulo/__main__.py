#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyModulo.__init__ import *


import PySimpleGUI as sg

eqDefault="%i ≡ %i (Mod %i)"
eqValues=[1,2,3]

if __name__ == "__main__":

	sg.theme('Topanga')   # Add a touch of color
	# All the stuff inside your window.
	layout = [  [sg.Text('Some text on Row 1'), sg.In(key="test0"), sg.Button("Button 1")],
				[sg.Text('Some text on Row 2'), sg.In(), sg.Button("Button 2")],
				[sg.Text("HI?"), sg.In(eqDefault%(eqValues[0], eqValues[1], eqValues[2]), key="test2", enable_events=True), sg.FolderBrowse(key="test",enable_events=True)],
				[sg.Text('Enter something on Row 2'), sg.InputText()],
				[sg.Button('Ok'), sg.Button('Cancel')] ]

	# Create the Window
	window = sg.Window('WEE WOO', layout, margins=(0,0))
	# Event Loop to process "events" and get the "values" of the inputs
	while True:
		event, values = window.read()
		print(event,values,sep='\n')
		if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
			break
		print('You entered ', values[0])

	window.close()


	print(find_inverse(3,10))
	print(flipped_congruence(-5, 32), flipped_congruence(flipped_congruence(-5, 32), 32))
	print(shanks_algorithm(156, 116, 593))
	print(get_gcd_fast(423,191))

