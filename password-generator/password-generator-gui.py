#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gui-for-pass_generator.py
#  
#  Copyright 2021  <Itai-Nelken>
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

import random
import tkinter as tk

passlength=''
passcount=''
chars='ABCDEFGHIJKLMNOPQRSTUVWNYZabcdefghijklmnopqrstuvwsyz1234567890!@#$%^&*\(\)_+\[\]\{\}"\'|\\/?.,<>`~'

#def gen_pass():
#    passlength=int(entry.get())
#    passcount=int(entry2.get())
#    for c in range(passcount):
#        password=''
#        for p in range(passlength):
#            password+=random.choice(chars)
#        print(password)
        
def gen_pass():
    passlength=int(entry.get())
    password=''
    for p in range(passlength):
        password+=random.choice(chars)
    #print(password)
    out.delete(0, tk.END)
    out.insert(0, password)

window = tk.Tk()
window.title('Password Generator')
window.minsize(width=263, height=50)

label=tk.Label(text="Password length:")
entry=tk.Entry(bg="white", fg="black", width=27)
#label2=tk.Label(text="how many passwords?")
#entry2=tk.Entry(bg='white', fg='black', width=10)
button=tk.Button(width=15, height=2, bg='green', fg='black', text='Generate!', command=gen_pass)
out=tk.Entry(width=27, bg='#3600FF', fg='#FFCD5A')
out_label=tk.Label(text='Password:')

label.pack()
entry.pack()
#label2.pack()
#entry2.pack()
out_label.pack()
out.pack()
button.pack()

window.mainloop()


