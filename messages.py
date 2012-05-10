#!/usr/bin/python
################################################
# Message Style to make prints
# C0d3r: Julian Alexander Murillo (Lexinerus)
################################################
import datetime

class Messages():
	_value = ""
	_symbols = (
		"!", "#", "+", "-",
		"=", "*", "_", "?"
	)

	def show_message(self, type_message, message):
		sel_symbol = ""

		try: sel_symbol = self._symbols[type_message]
		except:	pass
		
		message_signature = "(%s)" % sel_symbol			
		show_message = " %s %s" % (message_signature, message)
	
		if type_message == 7:
			show_message += " (S/N): "
			self._value = raw_input(show_message)		
		else:
			print show_message

	def debug_message(self, message):
		date = datetime.datetime.now()
		show_message = "[%s] %s" % (date, message)
		print show_message		

	def help(self):
		index = 0
		for symbol in self._symbols:
			print " [%s] %s" % (index, symbol)
			index += 1
