import pypdf
import os
dir_path = os.path.dirname(os.path.abspath(__file__))
pdf_path = f'{dir_path}{os.sep}f8938.pdf'

# Open the PDF file
pdf_file = open(pdf_path, 'rb')

# Create a PDF reader object
pdf_reader = pypdf.PdfReader(pdf_file)

# Get the last page of the PDF file
last_page = pdf_reader.pages[len(pdf_reader.pages) - 1]

# Create a PDF writer object
pdf_writer = pypdf.PdfWriter()
first_page = pdf_reader.pages[0]
pdf_writer.add_page(first_page)

# Add the last page to the PDF writer object 5 times
for i in range(5):
    pdf_writer.add_page(last_page)

# Save the output PDF file
new_file = f'{dir_path}{os.sep}5.pdf'
output_file = open(new_file, 'wb')
pdf_writer.write(output_file)

# Close the files
pdf_file.close()
output_file.close()
