'''
Script: calculate the GPA and CPA of a HUST student

Instruction:
    Copy 'Bang diem hoc phan' into file all_grades.xlsx before executing this script.

Note:
    This script is dirty, I know. It's just a 10-minutes work, don't be too judgy :)

Author: minhdq99hp@gmail.com
Modified: 23/08/2020 11:47 PM
'''

import xlrd

convert_grade = {
    'F': 0.0,
    'D': 1.0,
    'D+': 1.5,
    'C': 2.0,
    'C+': 2.5,
    'B': 3.0,
    'B+': 3.5,
    'A': 4.0,
    'A+': 4.0
}

wb = xlrd.open_workbook('all_grades.xlsx')

sheet = wb.sheet_by_index(0)

cpa = 0.0
total_credits = 0
term_total_credits = 0
gpa = 0
term = sheet.cell_value(sheet.nrows-1, 0)
for row in range(sheet.nrows-1, -1, -1):
    if sheet.cell_value(row, 3) == 0 or sheet.cell_value(row, 7) == 'R':
        continue
    if sheet.cell_value(row, 0) != term:
        if term_total_credits == 0:
            print(f'GPA {int(term)}: R')
        else:
            print(f'GPA {int(term)}: {round(gpa/term_total_credits, 2)}')
        term_total_credits = 0
        gpa = 0
        term = sheet.cell_value(row, 0)

    term_total_credits += sheet.cell_value(row, 3)
    gpa += sheet.cell_value(row, 3) * convert_grade[sheet.cell_value(row, 7)]
    total_credits += sheet.cell_value(row, 3)
    cpa += sheet.cell_value(row, 3) * convert_grade[sheet.cell_value(row, 7)]

print(f'GPA {int(term)}: {round(gpa/term_total_credits, 2)}')

print(f'CPA: {round(cpa/total_credits, 2)}')
