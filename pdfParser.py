from PyPDF2 import PdfReader #turns pdf into string
import re #Used for parsing what we need from pdf
import json #Need for output to enter into database

## Commented out because, I only needed to read from pdf file once.
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
filter = open("filtered_PDF_Extract.txt","w+",encoding="utf-8") #Containing course details
with open("pdfExtract.txt","r",encoding="utf-8") as file:
    fileLines = file.read()
    pattern = re.compile("[A-Z]{3} [0-9]{3}[A-Z]* —\xa0.+\)")
    matches = pattern.findall(fileLines)
    for match in matches:
        filter.write(match+"\n")
filter.close()

array = []
id = 0
with open("filtered_PDF_Extract.txt","r",encoding="utf-8") as file:
    fileLines = file.readlines()
    for line in fileLines:
        match = re.match(r"(\b[A-Z]{3}\b) (\b[0-9]{3}[A-Z]*\b) —\xa0(\b.*\b) \((\b.*\b)\)",line)
        dict2 = {}
        if(match != None):
            fields = dict()
            #output.write(match.group(1)+","+match.group(2)+","+match.group(3)+","+match.group(4)+'\n')
            fields["subject"] = match.group(1)
            fields["subject_code"] = match.group(2)
            fields["name"] = match.group(3)
            fields["units"] = match.group(4)
            array.append(fields)
        id+=1

#Outputs in a array holding objects, used to import into mongoDB
with open("CoursesOffered.json","w+",encoding="utf-8") as output: #Containing course details
    json.dump(array, output, indent = 4, sort_keys = False)