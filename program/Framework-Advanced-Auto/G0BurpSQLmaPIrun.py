#!/usr/bin/python
import os
import time

os.system("go run G0BurpSQLmaPI.go")
time.sleep(5)
os.system("executor.go")
	
