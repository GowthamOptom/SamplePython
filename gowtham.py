import docx2txt
import re

my_txt = docx2txt.process("C:/Users/91875/Downloads/resume.docx")

years = re.compile(r'[\.1|2\.][0-9\.]{3}')
matches = years.finditer(my_txt)

for x in matches:
    print(x.group())


email = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z\.]*[\.a-zA-Z]')
matches = email.finditer(my_txt)

for y in matches:
    print(y.group(0))