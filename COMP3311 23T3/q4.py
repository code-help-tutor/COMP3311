WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/python3
# COMP3311 22T3 Ass2 ... print a transcript for a given student

import sys
import psycopg2
import re
from helpers import getStudent

# define any local helper functions here

### set up some globals

usage = f"Usage: {sys.argv[0]} zID"
db = None

### process command-line args

argc = len(sys.argv)
if argc < 2:
  print(usage)
  exit(1)
zid = sys.argv[1]
if zid[0] == 'z':
  zid = zid[1:8]
digits = re.compile("^\d{7}$")
if not digits.match(zid):
  print(f"Invalid student ID {zid}")
  exit(1)

# manipulate database

try:
  db = psycopg2.connect("dbname=ass2")
  stuInfo = getStudent(db,zid)
  if not stuInfo:
    print(f"Invalid student ID {zid}")
    exit()

  #print(stuInfo) # debug
  # Print transcript for Student
  # ... add your code here ...

except Exception as err:
  print("DB error: ", err)
finally:
  if db:
    db.close()

