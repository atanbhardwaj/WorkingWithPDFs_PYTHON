import PyPDF2

# To get the number of pages in the pdf 

with open("Business.pdf","rb") as file1:
    reader1 = PyPDF2.PdfFileReader(file1)
    print("Number of pages in Business pdf are: {}".format(reader1.getNumPages()))

with open("Cognos.pdf","rb") as file2:
    reader2 = PyPDF2.PdfFileReader(file2)
    print("Number of pages in Cognos pdf are: {}".format(reader2.getNumPages()))


#Rotating The PDF 
# with open("Business.pdf","rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("Rotated.pdf","wb") as outputfile:
#         writer.write(outputfile)

#To merge multiple PDFs

merger = PyPDF2.PdfFileMerger()
file_names = ["Business.pdf", "Cognos.pdf"]

for file_name in file_names:
    merger.append(file_name)
merger.write("Combined_Business_Cognos.pdf")
