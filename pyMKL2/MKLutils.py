from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from ctypes import Structure, POINTER, c_int, c_char_p
from . import MKLlib

class pyMKL2Version(Structure):
    _fields_ = [('MajorVersion',c_int),
                ('MinorVersion',c_int),
                ('UpdateVersion',c_int),
                ('ProductStatus',c_char_p),
                ('Build',c_char_p),
                ('Processor',c_char_p),
                ('Platform',c_char_p)]
_mkl_get_version = MKLlib.mkl_get_version
_mkl_get_version.argtypes = [POINTER(pyMKL2Version)]
_mkl_get_version.restype = None

def mkl_get_version():
    MKLVersion = pyMKL2Version()
    _mkl_get_version(MKLVersion)
    version = {'MajorVersion':MKLVersion.MajorVersion,
               'MinorVersion':MKLVersion.MinorVersion,
               'UpdateVersion':MKLVersion.UpdateVersion,
               'ProductStatus':MKLVersion.ProductStatus,
               'Build':MKLVersion.Build,
               'Platform':MKLVersion.Platform}

    versionString = 'Intel(R) Math Kernel Library Version {MajorVersion}.{MinorVersion}.{UpdateVersion} {ProductStatus} Build {Build} for {Platform} applications'.format(**version)

    return versionString


_mkl_get_max_threads = MKLlib.mkl_get_max_threads
_mkl_get_max_threads.argtypes = None
_mkl_get_max_threads.restype = c_int

def mkl_get_max_threads():
    max_threads = _mkl_get_max_threads()
    return max_threads


_mkl_set_num_threads = MKLlib.mkl_set_num_threads
_mkl_set_num_threads.argtypes = [POINTER(c_int)]
_mkl_set_num_threads.restype = None

def mkl_set_num_threads(num_threads):
    _mkl_set_num_threads(c_int(num_threads))
