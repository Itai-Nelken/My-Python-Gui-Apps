#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  password-generator.py
#  
#  Copyright 12.04.2021 <Itai-Nelken>
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

chars='ABCDEFGHIJKLMNOPQRSTUVWNYZabcdefghijklmnopqrstuvwsyz1234567890!@#$%^&*\(\)_+\[\]\{\}"\'|\\/?.,<>`~'

passlength=input('Enter the lentgh of the password to generate: ')
passlength=int(passlength)
passcount=input('How much passwords do you want to generate? ')
passcount=int(passcount)

for c in range(passcount):
    password=''
    for p in range(passlength):
        password+=random.choice(chars)
    print(password)
