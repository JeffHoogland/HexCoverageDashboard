#!/bin/bash
rm -f ui_*.py
rm -f ui_*.pyc
pyside-uic MainWindow.ui > ui_MainWindow.py
