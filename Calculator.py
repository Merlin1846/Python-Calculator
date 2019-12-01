#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Calculator.py
#  
#  Copyright 2019 Atticus <atticus@HAL4000>
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


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    
    KeyPress = 0
    
    Num1 = 0
    Operator1 = "+"
    Num2 = 0
    
    print("Hello and welcome to the calculator.\nTo use first type a number then click enter.\nThen type + - * or / in ''.\nThen type the second number and click enter.\n")
    
    num1 = input()
    Operator1 = input()
    num2 = input()
    
    if Operator1 == "+":
		print(num1 + num2)
    if Operator1 == "-":
		print(num1 - num2)
    if Operator1 == "*":
		print(num1 * num2)
    if Operator1 == "/":
		print(num1 / num2)
    
    sys.exit(main(sys.argv))
