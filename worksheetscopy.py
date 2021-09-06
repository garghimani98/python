import threading
from time import sleep
import xlrd
import xlsxwriter

wb = xlrd.open_workbook(r'C:\\Users\\Users\\Documents\\File_name_with_extension')
wb1 = xlsxwriter.Workbook(r'C:\\Users\\Users\\Documents\\File_name_with_extension')
def thread_1():
    print('Starting thread 1')
    s1=wb.sheet_by_index(0)
    sh1=wb1.add_worksheet('Base')
    for i in range(17815):
        sh1.write(i,0,s1.cell(i,0).value)
    for i in range(80):
        sh1.write(0,i,s1.cell(0,i).value)
    print('Ending thread 1')
t1=threading.Thread(name='t1',target=thread_1)
t1.start()
def thread_2():
    print('Starting thread 2')
    s2=wb.sheet_by_index(1)
    sh2=wb1.add_worksheet('Her2')
    for i in range(17815):
        sh2.write(i,0,s2.cell(i,0).value)
    for i in range(57):
        sh2.write(0,i,s2.cell(0,i).value)
    print('Ending thread 2')
t2=threading.Thread(name='t2',target=thread_2)
t2.start()
#similarly for rest of the sheets
t1.join()
t2.join()
wb1.close()
print("Done")
