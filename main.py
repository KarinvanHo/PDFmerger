import PyPDF2

#TODO 1: get arguments from terminal
#TODO 2: merge all PDFs



#practice with reading and writing PDFs
# with open('dummy.pdf', 'rb') as file:
# 	reader = PyPDF2.PdfFileReader(file)
# 	page = reader.getPage(0)
# 	page.rotateClockwise(180)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilt.pdf', 'wb') as new_file:
# 		writer.write(new_file)