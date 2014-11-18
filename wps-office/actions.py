#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde4

#WorkDir = "./"
pisitools.

def install():
    pisitools.insinto("/usr/share/kingsoft", 
    pisitools.get.workDIR()+"/wps-office_9.1.0.4909~a16p1_x86/",    
    #!üstteki yol düzenlenmeli. Arşiv ismi yazılmalı
    "wps-office")
    
#     pisitools.remove(pisitools.get.installDIR()+"/usr/share/kingsoft/wps-office/et")
#     pisitools.remove(pisitools.get.installDIR()+"/usr/share/kingsoft/wps-office/wpp")
#     pisitools.remove(pisitools.get.installDIR()+"/usr/share/kingsoft/wps-office/wps")

# By PiSiDo 2.0.0
