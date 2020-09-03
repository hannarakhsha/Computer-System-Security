#!/usr/bin/python
# -*- coding: utf-8 -*-
import gmpy
from Crypto.Util.number import *
import base64
z = open('custom1.enc','r').read().encode('hex')
c = int(z,16)
n= 83107041701747003548951619916073267657052136454079830436578267127977699952641
e = 65537
P1 = 282238357022244718977290902746061069487
P2 = 294456935544012154828625255162223768143
r = (P1-1)*(P2-1)
d = int(gmpy.invert(e, r).digits())
p = pow(c,d,n)
pt = hex(p).strip('0x').strip('L').decode('hex')
print pt

z2 = open('custom2.enc','r').read().encode('hex')
c2 = int(z2,16)
n2= 83107041701747003548951619916073267657052136454079830436578267127977699952641
e2 = 65537
r2 = (P1-1)*(P2-1)
d2 = int(gmpy.invert(e2, r2).digits())
p2 = pow(c2,d2,n2)
pt2 = hex(p2).strip('0x').strip('L').decode('hex')
print pt2

z3 = open('custom3.enc','r').read().encode('hex')
c3 = int(z3,16)
n3= 83107041701747003548951619916073267657052136454079830436578267127977699952641
e3 = 65537
r3 = (P1-1)*(P2-1)
d3 = int(gmpy.invert(e3, r3).digits())
p3 = pow(c3,d3,n3)
pt3 = hex(p3).strip('0x').strip('L').decode('hex')
print pt3

print ('\n' + pt + pt2 + pt3)
