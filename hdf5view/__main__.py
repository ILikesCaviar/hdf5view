# -*- coding: utf-8 -*-

import os
import sys
import argparse

from hdf5view.utility import resource_path

if not os.environ.get('QT_API'):  # noqa
    os.environ['QT_API'] = 'pyqt5'

if not os.environ.get('PYQTGRAPH_QT_LIB'):  # noqa
    os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt5'

from PyQt6.QtGui import (
    QIcon,
)

from PyQt6.QtWidgets import (
    QApplication,
)

from . import __version__
from .mainwindow import MainWindow


def main():
    """
    Main application entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    parser.add_argument("-f", "--file", type=str, required=False)
    args = parser.parse_args()


    app = QApplication(sys.argv)
    app.setOrganizationName('hdf5view')
    app.setApplicationName('hdf5view')
    app.setWindowIcon(QIcon(resource_path('images/hdf5view.svg')))

    window = MainWindow(app)
    window.show()

    # Open a file if supplied on command line
    if args.file:
        window.open_file(args.file)

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
