''' 
10.a
 Write a python program to combine pages from many PDFs
 '''

from PyPDF2 import PdfFileMerger

#Create and instance of PdfFileMerger() class
merger = PdfFileMerger()

#Create a list with file names
pdf_files = ['pdf_files/sample_page1.pdf', 'pdf_files/sample_page2.pdf']

#Iterate over the list of file names
for pdf_file in pdf_files:
    #Append PDF files
    merger.append(pdf_file)

#Write out the merged PDF
merger.write("merged_2_pages.pdf")
merger.close()