from PyPDF2 import PdfReader
import re

reader = PdfReader("./GenCat20232024.pdf")
number_of_pages = len(reader.pages)

# pdfExtract = open("pdfExtract.txt","w+",encoding="utf-8")

# for i in range(427,number_of_pages,1):
#     page = reader.pages[i]
#     text = page.extract_text()
#     pdfExtract.write(text)
# print("Done Extracting text from pages of pdf")
# pdfExtract.close()

#Opening file just opened
matches = []
courses = open("courses.txt","w+",encoding="utf-8")
courses.write("SUBJECT,COURSE_NUMBER,NAME")
with open("pdfExtract.txt","r",encoding="utf-8") as file:
    fileLines = file.readlines()
    for line in fileLines:
        match = re.match(r"(\b[A-Z]{3}\b) (\b[0-9]{3}[A-Z]*\b) —\xa0(\b.*\b)",line)
        if(match != None):
            courses.write(match.group(1)+","+match.group(2)+","+match.group(3)+'\n')
courses.close()

# with open("courses.txt","w+",encoding="utf-8") as file:
#     for i in matches:
#         file.write(i.group(1) + "," + i.group(2)+"," + i.group(3))
