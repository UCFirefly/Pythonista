# coding: utf-8
import ui
import clipboard
#from console import hud_alert

def addbutton_tapped(sender):
	input = sender.superview['inputbox'].text
	table = sender.superview['table'].data_source.items
	if '' in table:
		table.remove('')
	if not input in table:
	  table.append(input)
	sender.superview['inputbox'].text = ''

def subbutton_tapped(sender):
	input = sender.superview['inputbox'].text
	table = sender.superview['table'].data_source.items
	if input in table:
	  table.remove(input)
	  sender.superview['table'].data_source.items = table
	sender.superview['inputbox'].text = ''
	  
def inputbutton_tapped(sender):
  text = clipboard.get()
  sender.superview['inputbox'].text = text
	  
def cell_tapped(self): 
  #hud_alert(sender.items[self.selected_row])
  #hud_alert(v['inputbox'].text)
  textbox = v['inputbox']
  textbox.text = self.items[self.selected_row]
  clipboard.set(self.items[self.selected_row])
	  
	  
v = ui.load_view('Clipboard_Manager')
v.present('sheet')