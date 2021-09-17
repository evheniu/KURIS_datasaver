import fnmatch
import os.path
import re
from datetime import datetime
import shutil

includes = ['*.txt'] # for files only
excludes = ["C:\\Zat3\\BDE"] # for dirs and files
to_dir = "K:\\Cutting\\Cutter\\CUTTER DEPARTMENT REPORTS\\ZVIT-C-Zat3-BDE\\REPORT\\Kuris_(9)"


# transform glob patterns to regular expressions
includes = r'|'.join([fnmatch.translate(x) for x in includes])
excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

for root, dirs, files in os.walk("C:\\Zat3\\BDE"):

       # exclude dirs
       dirs[:] = [os.path.join(root, d) for d in dirs]
       dirs[:] = [d for d in dirs if not re.match(excludes, d)]

       # exclude/include files
       files = [os.path.join(root, f) for f in files]
       files = [f for f in files if not re.match(excludes, f)]
       files = [f for f in files if re.match(includes, f)]

       for fname in files:
          path = os.path.join(root, fname)
          mtime = os.path.getmtime(path)
          date = datetime.fromtimestamp(mtime)
          date = date.strftime("%Y-%m-%d")
          date_folder = os.path.join(to_dir, date)
          if not os.path.exists(date_folder):
              os.mkdir(date_folder)
          des = fname.split("\\")
          shutil.copyfile(path, os.path.join(date_folder, des[-1]))
