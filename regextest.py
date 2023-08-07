import re
import sys

#sm = "update swearing 0.4"

#print(re.search("^update swearing",sm).start())
#print("AAAA".lower())
print(sys.argv[0])
print(re.search('^.*\/(?=[a-zA-Z]*\.py)',sys.argv[0]).group())