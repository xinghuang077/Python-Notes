## !/usr/bin/env python
## -*- coding: utf-8 -*-
## Author: Xing Huang
## Email: xinghuang077@gmail.com
## Date: May 4th, 2022
## Affiliation: University of California, Santa Barbara
## Description:
## This notes is based on: https://stackoverflow.com/questions/63544569/how-do-we-use-python-code-to-convert-a-list-of-integers-in-decimal-format-to-hex
## It is organized to help me convert a list in decimal format to hexadecimal format effectively.

## A decimal list of a sample 
content_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(content_list)

## Method 1. Use for loop to convert the element of the list one by one.
hex_content_list = []
for i in range(0, len(content_list)):
    hex_content_list += [hex(int(content_list[i]))]
print(hex_content_list)

## Method 2. Use the map() function to convert iteratively.
## For map() function, ref here: https://www.geeksforgeeks.org/python-map-function/
# contents = map(int,content_list)
hex_contents =list(map(hex,content_list))
print(hex_contents)

## Method 3.
hex_list = [hex(int(x)) for x in content_list]
print(hex_list)

# new_string=[i.replace("'", "") for i in hex_list ]
# print(new_string)