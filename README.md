# (PyQt6 Fork) HDF5View

Simple Qt/Python based viewer for HDF5 files. Currently, it just displays a file tree, data tables and attributes. Everything is loaded dynamically, so hopefully it should be able to handle HDF5 files of any size and structure.

I hope to add pyqtgraph plotting and some image rendering soon.

## Installing

On linux (Ubuntu/Debian) I generally prefer installing the system packages of PyQt5 and/or PySide2 - in that case don't bother with uncommenting stuff in install_requires in setup.py:

```
sudo apt install python3-pyqt5 python3-h5py python3-qtpy
```

To install system wide, download or clone the repo. Uncomment the preferred Qt bindings in setup.py (or install system packages...see below):

```
cd hdf5view
sudo pip3 install .
```

To uninstall:

```
sudo pip3 uninstall hdf5view
```

## Running

```
hdf5view
```

or

```
hdf5view -f <hdf5file>
```

HDF5 files can also be dropped onto the application window once opened.

## Development

To setup a development environment use virtualenv:

```
python3 -m virtualenv -p python3 .
source bin/activate
pip install -e .
```

## Chosing Qt API bindings
(Fork comment)
I didn't bother preserving and of these since this is PyQt6 only

## Building resources

(Fork Comment) This seems to be broken, not supported or very different in PyQt6. No resource building in this version.

## TODO:

* Actually use pyqtgraph to plot some stuff.
* Add an image view
* Add some 3D stuff
* Build a deb package
