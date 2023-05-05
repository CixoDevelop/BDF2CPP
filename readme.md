# BDF to CSV and CSV to C Array

This is converters from bdf to csv, and from csv to C array. You can use it 
to generate C arrays of fonts, to use in Your embedded projects!

## How to make C array from BDF file
```
pip install bdflib
python bdf2csv.py font.bdf > font.csv
python csv2cpp.py font.csv > font.c
```
