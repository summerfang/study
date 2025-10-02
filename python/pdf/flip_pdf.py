import pypdf
import os
import sys

def flip_pdf(input_path, output_path=None):
    """
    Flip all pages of a PDF by 180 degrees.
    
    Args:
        input_path: Path to the input PDF file
        output_path: Path to the output PDF file (optional, defaults to input_flipped.pdf)
    """
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return False
    
    # Set default output path if not provided
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}_flipped.pdf"
    
    try:
        # Open the input PDF file
        with open(input_path, 'rb') as pdf_file:
            # Create a PDF reader object
            pdf_reader = pypdf.PdfReader(pdf_file)
            
            # Create a PDF writer object
            pdf_writer = pypdf.PdfWriter()
            
            # Iterate through all pages
            for page_num in range(len(pdf_reader.pages)):
                # Get the page
                page = pdf_reader.pages[page_num]
                
                # Rotate the page by 180 degrees
                page.rotate(180)
                
                # Add the rotated page to the writer
                pdf_writer.add_page(page)
            
            # Write to output file
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
        
        print(f"Successfully flipped PDF: {output_path}")
        print(f"Total pages processed: {len(pdf_reader.pages)}")
        return True
        
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return False


if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python flip_pdf.py <input_pdf> [output_pdf]")
        print("Example: python flip_pdf.py document.pdf")
        print("Example: python flip_pdf.py document.pdf flipped_document.pdf")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    flip_pdf(input_file, output_file)
