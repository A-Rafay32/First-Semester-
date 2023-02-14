import os
import subprocess
src = input("location of source: ")
des = input("location of destination: " )
ext = input("extension: ")
bat = open( "cp.bat" , 'w' ) #open in write mode
                            #file object is created

bat.write("@echo off\ncopy  ")
bat.write(src)
bat.write("*.")
bat.write(ext)
bat.write("  ")
bat.write(des)
bat.write("\npause")
bat.close() 

subprocess.call([r'C:\Users\DELL\Documents\copy program\cp.bat'])

 
