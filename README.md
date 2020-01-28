# tableau-dependency-checks
This is a simple tool developed in order to fetch all used fields from tableau workbooks to help identify dependencies for a specific column across all workbooks

Usage of this tool:

ReadTWBFiles.py -dd "C:\Users\" 

Options:
dd = download directory where you downloaded all twb(tableau workbook) files reside
  
Output:
After looping through all twb xml files, it spits out a csv file called 'all_workbook_fields.csv' in the same download directory as twb files it reads from.
