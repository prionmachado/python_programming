import PyPDF2

merger = PyPDF2.PdfMerger() 
pdfiles = ['Projects/1.pdf', 'Projects/2.pdf']

for filename in pdfiles:
    pdfFile = open(filename, 'rb') 
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(filename) 

pdfFile.close()
merger.write('Projects/merged.pdf') 
merger.close() 