'''pyMKL2
'''

from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Intended Audience :: Science/Research',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python',
'Topic :: Scientific/Engineering',
'Topic :: Scientific/Engineering :: Mathematics',
'Topic :: Scientific/Engineering :: Physics',
'Programming Language :: Python',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
'Operating System :: Microsoft :: Windows',
'Operating System :: POSIX',
'Operating System :: Unix',
'Operating System :: MacOS',
'Natural Language :: English',
]

setup(
    name = 'pyMKL2',
    version = '0.0.4',
    packages = find_packages(),
    install_requires = ['numpy>=1.7',
                        'scipy>=0.13',
                        'future',
                       ],
    author = 'Dave Marchant',
    author_email = 'dwfmarchant@gmail.com',
    description = 'Python wrapper of Intel MKL routines',
    long_description = open('README.rst').read(),
    long_description_content_type='text/x-rst',
    license = 'MIT',
    keywords = 'sparse linear solver mkl pardiso',
    url = 'https://github.com/jvcarli/pyMKL2',
    # TODO: fix download_url
    # download_url = 'https://github.com/dwfmarchant/pyMKL/tarball/0.0.3',
    classifiers = CLASSIFIERS,
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    use_2to3 = False,
)
