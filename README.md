# Edit-PDF-file-with-Python

# Project Goal
Automate adding names to certification. 

# Project Breakdown 
Automatically edit PDF files using Python.

# Approach 
1. Create a new pdf file using Reportlab and write the names on the position you want 
2. Overlay the newly created file on top of your template file 

# Template PDF file 
![Screen Shot 2021-06-14 at 21 16 56](https://user-images.githubusercontent.com/64785877/121907022-dc7c9b00-cd55-11eb-967b-d7779bfeb3cd.jpg)

# Result 
![Screen Shot 2021-06-14 at 21 18 03](https://user-images.githubusercontent.com/64785877/121907170-0209a480-cd56-11eb-9c19-e684bbbc598f.jpg)

You can use this as a guide to edit your own pdf using Python :D


# File Structure 
### [create_new_pdf.py](https://github.com/AiNguyen237/Edit-PDF-file-with-Python/blob/main/create_new_pdf.py)
This file is responsible for create a new pdf file with customized text.

### [merge_two_pdf.py](https://github.com/AiNguyen237/Edit-PDF-file-with-Python/blob/main/merge_two_pdf.py)
This file is responsible for overlaying the two pdf files.

### [position.py](https://github.com/AiNguyen237/Edit-PDF-file-with-Python/blob/main/position.py)
This file is responsible for getting your text position inside the pdf. 
