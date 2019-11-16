#File: main.py
#Description: Function project, find the volume of various shapes
#Author: Raymond Laughrey
#Email: raymonl4963@student.vvc.edu
#Date of Creation: Mon Sep 30 10:28:10 PDT 2019

import math #I can just call all the functions in here, right? This is for math.pi

def sphere_volume(r):
    sphere_volume = (4 / 3) * math.pi * pow(r,3)
    print("Sphere volume: ",sphere_volume)

def sphere_surface(r):
    sphere_surface = 4 * math.pi * pow(r,2)
    print("Sphere surface area: ",sphere_surface)

def cylinder_volume(r,h):
    cylinder_volume = math.pi * pow(r,2) * h
    print("Cylinder Volume: ",cylinder_volume)

def cylinder_surface(r,h):
    cylinder_surface = 2 * math.pi * r * (r + h) 
    print("Cylinder surface area: ",cylinder_surface)

def cone_volume(r,h):
    cone_volume = math.pi * pow(r,2) * (h/3) 
    print("Cone volume: ",cone_volume)

def cone_surface(r,h):
    cone_surface = math.pi * r * (r + math.sqrt( pow(h,2) + pow(r,2) ))
    print("Cone surface: ",cone_surface)

radius = int(input('Enter radius of sphere to know volume: '))
sphere_volume(radius)

radius = int(input('Enter radius of sphere to know surface area: '))
sphere_surface(radius)

radius = int(input('Enter radius of cylinder to know volume & surface area: '))
height = int(input('Enter height of cylinder to know volume & surface area: '))
cylinder_volume(radius,height)
cylinder_surface(radius,height)

radius = int(input('Enter radius of cone to know volume & surface area: '))
height = int(input('Enter height of cone to know volume & surface area: '))
cone_volume(radius,height)
cone_surface(radius,height)
