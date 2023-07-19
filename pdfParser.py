from PyPDF2 import PdfReader
import re

# pdfFileName = "./GenCat20232024.pdf" #Insert PDF_Path here (My use: GenCat20232024.pdf")
# reader = PdfReader(pdfFileName)
# number_of_pages = len(reader.pages)

# pdfExtract = open("pdfExtract.txt","w+",encoding="utf-8")

# for i in range(427,number_of_pages,1):
#     page = reader.pages[i]
#     text = page.extract_text()
#     pdfExtract.write(text)
# print("Done Extracting text from pages of pdf")
# pdfExtract.close()

#Opening file just opened
matches = []
filter = open("filtered_PDF_Extract.txt","w+",encoding="utf-8") #Containg course details
with open("pdfExtract.txt","r",encoding="utf-8") as file:
    fileLines = file.read()
    pattern = re.compile("[A-Z]{3} [0-9]{3}[A-Z]* —\xa0.+\)")
    matches = pattern.findall(fileLines)
    print(matches)
    for match in matches:
        filter.write(match+"\n")
        # output.write(match.group(1) + "," + match.group(2) + "," + match.group(3) + ",")
filter.close()

output = open("CoursesOffered.txt","w+",encoding="utf-8") #Containg course details
output.write("SUBJECT,COURSE_NUMBER,NAME,UNIT_COUNT\n")
with open("filtered_PDF_Extract.txt","r",encoding="utf-8") as file:
    fileLines = file.readlines()
    for line in fileLines:
        match = re.match(r"(\b[A-Z]{3}\b) (\b[0-9]{3}[A-Z]*\b) —\xa0(\b.*\b) \((\b.*\b)\)",line)
        if(match != None):
            output.write(match.group(1)+","+match.group(2)+","+match.group(3)+","+match.group(4)+'\n')
output.close()

# with open("courses.txt","w+",encoding="utf-8") as file:
#     for i in matches:
#         file.write(i.group(1) + "," + i.group(2)+"," + i.group(3))
