import PyPDF2

num = int(input("How many PDF files to merge? "))

pdfiles = []
for i in range(num):
    name = input(f"Enter file {i+1} name: ")
    pdfiles.append(name)

merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    with open(filename, 'rb') as pdfFile:
        merger.append(pdfFile)

output_name = input("Enter output file name: ")
merger.write(output_name)
merger.close()

print("PDFs merged successfully!")