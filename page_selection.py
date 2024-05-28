import PyPDF2

def extract_pages(input_pdf_path, output_pdf_path, pages):
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in pages:
        pdf_writer.add_page(pdf_reader.pages[page_num - 1])
    
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    
    print(f"Extracted pages {pages} to {output_pdf_path}")

def main():
    input_pdf_path = input("Enter the path to the input PDF file: ")
    output_pdf_path = input("Enter the path to the output PDF file: ")
    
    pages_input = input("Enter the pages to extract (comma-separated, e.g., 1,3,5): ")
    pages = [int(page.strip()) for page in pages_input.split(',')]
    
    extract_pages(input_pdf_path, output_pdf_path, pages)

if __name__ == "__main__":
    main()
