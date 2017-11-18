# coding: utf-8
import ui
import clipboard
from random import random
from console import hud_alert
import pprint
import hashlib
import base64
import getpass

p = getpass.getpass()
chpw = list(map(chr,list(range(32,127))))
chpwlist = chpw + chpw + chpw
  
def byte2char(byte):
  char = chpwlist[byte]
  return char

def hashmatic(password,site,user,salt):
  #please design your own function here
  pass

def addbutton_tapped(sender):
	input = sender.superview['inputbox'].text
	table = sender.superview['table'].data_source.items
	if '' in table:
		table.remove('')
	if not input in table:
	  table.append(input)
	sender.superview['inputbox'].text = ''

def subbutton_tapped(sender):
	v['inputbox'].text = ''
	clipboard.set('')
	  
def inputbutton_tapped(sender):
  text = clipboard.get()
  sender.superview['inputbox'].text = text
	  
def cell_tapped(self):
  #self.items[self.selected_row]
  v['sites'].selected_rows=[self.selected_row]
  v['users'].selected_rows=[self.selected_row]
  v['salts'].selected_rows=[self.selected_row]
  
  sites = v['sites'].data_source
  users = v['users'].data_source
  salts = v['salts'].data_source
  
  site = sites.items[self.selected_row]
  user = users.items[self.selected_row]
  salt = salts.items[self.selected_row]
  
  textbox = hashmatic(p,site,user,salt)
  
  lengths = v['lengths'].segments
  length_index = v['lengths'].selected_index
  length = int(lengths[length_index])
  
  #hud_alert(textbox)
  v['inputbox'].text = textbox[:length]
  clipboard.set(textbox[:length])
	  
	  
v = ui.load_view('phelp')
v.present('sheet')






