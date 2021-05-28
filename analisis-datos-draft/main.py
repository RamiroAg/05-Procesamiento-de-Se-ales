import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
# for dirname, _, filenames in os.walk('D:\Github\05-Procesamiento-de-Señales'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# prefix_path = "D:/Github/05-Procesamiento-de-Señales/analisis-datos-draft/drug-use-by-age.csv"
# prefix = os.path.abspath(prefix_path)
# print(prefix)

nba = pd.read_csv("D:/Github/05-Procesamiento-de-Señales/analisis-datos-draft/drug-use-by-age.csv")
type(nba)
print(len(nba))
nba.head()


# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))