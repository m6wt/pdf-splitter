import fitz
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def rotate_pdf(input_pdf, output_pdf, rotation_angle):
    """Rotates all pages in a PDF file by a given angle and saves a new PDF."""
    doc = fitz.open(input_pdf)
    
    for page in doc:
        page.set_rotation(rotation_angle)  # Rotate by the specified angle (90, 180, 270)
    
    doc.save(output_pdf)
    doc.close()
    print(f"Rotated PDF saved as {output_pdf}")

def split_and_rotate_pdf_by_pairs(input_pdf, output_folder, rotation_angle):
    """Splits a PDF into separate files, each containing two consecutive pages, and rotates them."""
    doc = fitz.open(input_pdf)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    num_pages = len(doc)
    for i in range(0, num_pages, 2):  # Step by 2 to get pairs
        new_doc = fitz.open()
        start_page = i
        end_page = min(i + 1, num_pages - 1)  # Ensure we don't go out of range

        # Extract and rotate each page
        for page_num in range(start_page, end_page + 1):
            page = doc[page_num]
            page.set_rotation(rotation_angle)  # Rotate the page

            # Create a new temporary PDF with rotated page
            temp_doc = fitz.open()
            temp_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
            new_doc.insert_pdf(temp_doc)
            temp_doc.close()
        
        output_path = os.path.join(output_folder, f"pages_{start_page+1}-{end_page+1}.pdf")
        new_doc.save(output_path)
        new_doc.close()
        print(f"Saved rotated {output_path}")

    doc.close()
    print(f"PDF split and rotated into {num_pages // 2} separate files in {output_folder}")

def select_pdf_file():
    """Opens a file dialog for the user to select a PDF file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
    return file_path

if __name__ == "__main__":
    input_pdf = select_pdf_file()  # Ask user to select a PDF file

    if not input_pdf:
        print("No file selected. Exiting program.")
    else:
        output_split_folder = "split_pairs"

        # Ask the user for a rotation angle
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        rotation_angle = simpledialog.askinteger("Rotation", "Enter rotation angle (0, 90, 180, 270):", minvalue=0, maxvalue=270)

        if rotation_angle is None:
            print("No rotation angle entered. Exiting program.")
        else:
            # Split PDF into pairs of pages and rotate them
            split_and_rotate_pdf_by_pairs(input_pdf, output_split_folder, rotation_angle)



