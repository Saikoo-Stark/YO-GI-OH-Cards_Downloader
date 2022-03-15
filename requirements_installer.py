import os 
requirements = [ "--upgrade pip" , "requests" , "termcolor" , "pyfiglet"]

for req in requirements:
	os.system(f"pip install {req}")