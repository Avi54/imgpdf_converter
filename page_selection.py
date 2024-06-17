import PyPDF2
import os

def extract_pages(input_pdf_path, output_pdf_path, pages):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Extract the specified pages and add them to the writer object
    for page_num in pages:
        # PyPDF2 uses 0-based indexing for pages
        pdf_writer.add_page(pdf_reader.pages[page_num - 1])
    
    # Write the output PDF
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    
    print(f"Extracted pages {pages} to {output_pdf_path}")

def main():
    # Get the relative paths from the user
    input_pdf_path = input("Enter the relative path to the input PDF file: ")
    output_pdf_path = input("Enter the relative path to the output PDF file: ")

    # Convert the relative paths to absolute paths
    input_pdf_path = os.path.abspath(input_pdf_path)
    output_pdf_path = os.path.abspath(output_pdf_path)
    
    # Get the pages to extract from the user, expecting a comma-separated list of pages
    pages_input = input("Enter the pages to extract (comma-separated, e.g., 1,3,5): ")
    pages = [int(page.strip()) for page in pages_input.split(',')]
    
    extract_pages(input_pdf_path, output_pdf_path, pages)

if __name__ == "__main__":
    main()
