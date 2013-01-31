#!/usr/bin/env python
#!/usr/bin/env python
import os
from os import rename, listdir

print os.listdir(".")
for filename in os.listdir("."):
	if filename.startswith("quotation-"):
		print filename
		os.rename(filename, filename[10:])