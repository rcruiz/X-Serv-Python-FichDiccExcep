#!/usr/bin/python
# -*- coding: utf-8 -*-

usuarios = {}
fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
for linea in lineas:
    usuario = linea.split(":")[0]
    usuarios[usuario] = linea.split(":")[-1][:-1]
fd.close()

try:
    print usuarios['root']
    print usuarios['imaginario']
except KeyError:
    print "Usuario no encontrado"

