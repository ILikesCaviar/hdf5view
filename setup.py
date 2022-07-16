# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from hdf5view import __version__

setup(
    name='hdf5view',
    version=__version__,
    description='HDF5 file viewer',
    long_description='HDF5View is a python based HDF5 file viewer built on PySide2/PyQt5, h5py and pyqtgraph.',
    license='MIT',
    url='https://github.com/marts/hdf5view/',
    author='Martin Swarbrick',
    author_email='martin.swarbrick@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop'
        'Intended Audience :: Science/Research',
        'License :: MIT',
        'Operating System :: POSIX',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering :: Visualization',
    ],

    keywords='',
    packages=find_packages('.'),
    install_requires=[
        'h5py',
        'PyQt6'
    ],
    zip_safe=False,
    include_package_data=True,
    package_data={
        'hdf5view': [
            'resources'
        ]
    },
    entry_points={
        'gui_scripts': [
            'hdf5view=hdf5view.main:main',
        ],
    },
)
