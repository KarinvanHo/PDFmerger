import PyPDF2
import sys

#TODO 1: get all arguments from terminal
inputs = sys.argv[1:]


#TODO 2: merge PDFs
def pdf_merger(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('merged.pdf')

pdf_merger(inputs)
