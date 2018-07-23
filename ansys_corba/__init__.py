import sys
import ctypes
import os

# add this directory to the system path
path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, path)

# add shared libaries to the path
libs = ['libomnithread.so.4', 'libomniORB4.so.2',]
for lib in libs:
    libfile = os.path.join(path, lib)
    if os.path.isfile(libfile):
        ctypes.cdll.LoadLibrary(libfile)

from omniORB import CORBA
import AAS_CORBA
