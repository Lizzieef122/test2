# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:12:41 2018

@author: ef122
"""
import matplotlib.pyplot as plt
import scipy.io as sio
filename = 'E:/NAPH02_distraction'
a = sio.loadmat(filename, squeeze_me=True, struct_as_record=False)
b = a['output']
data = b.blue
plt.plot(data)
data2 = b.uv
 
plt.plot(data2)
plt.xlabel('time in s')
plt.ylabel('signal magnitude')
distractiondata =plt.show()
#plotting actual data stream (of lick-rate?) compared to control/baseline


plt.ylim(400,580)
plt.xlim(0,300000)
plt.plot(data2)
plt.savefig('distraction_data_plots.png')

import xlwt 

x=1
y=2
z=3

list1= b.tick

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")

blue_data = b.blue
uv_data = b.uv
sheet1.write(0, 0, "blue_data")
sheet1.write(1, 0, "uv_data")
sheet1.write(2, 0, (uv_data - blue_data))

sheet1.write(0, 1, x)
sheet1.write(1, 1, y)
sheet1.write(2, 1, z)

sheet1.write(4, 0, "Corrected time(s)")
sheet1.write(4, 1, "Magnitude of Signal different")

i=4

for n in list1:
    i = i+1
    sheet1.write(i, 0, n)



book.save("distractiontask.xls"








#file = open(“distractiondata.txt”,”w”) 
# blue_data = b.blue
#uv_data = b.uv
#time_correction = b.tick
#file.write(“blue_data”) 
#file.write(“uv_data”) 
#file.write(“time_correction”) 
#file.close()                         
