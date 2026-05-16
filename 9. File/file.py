'''python can be used to perform operations on a file.(read and write data)
types of file-
1. Text files : .txt , .docx, .log etc
2. Binary files: .mp4 , .mov , .png ,  .jpeg etc

syntax ->
f = open("file_name","mode")
data = f.read()
f.close()
r - read(default), w - write, x - create a new file and open for it writing, a - open for writing, appending to the 
end of line if it exits, b- binary mode, t- text mode, + -> open a disk file for updating(reading and writing)
data = f.read() reads entire file
data = f.readline() reads one line'''

''' syntax 2 
with open("demo.txt","r") as f:
  data = f.read()
  print(data)'''

'''Deleting a File --->
using os module 
Module is a file written by another programmer that generally has a functions we can use .
import os
os.remove(filename)'''