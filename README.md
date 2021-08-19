Img2Pdf

# PreRequisites

1. Add the directory containing this python file in .profile or bin in wsl
2. Modify the first line of code to point to your python interpreter

# Conditions

1. The jpg files' file name must be in the order to be arranged in pdf 
    
    * eg. 1. jpg must be the first page 
             
          .. 2. jpg will be the second page in the pdf , Similarly the n.pdf will be the nth page of the pdf
2. Subcategories are also allowed 
    
    * eg. a1.jpg ,a2.jpg , b1.jpg,b2.jpg etc.

# Execution 

1. Open wsl 
2. Go to the directory that contains the jpg files 
3. Enter 'the_py_file_name the_name_for_the pdf directory_location'
    
    * eg. In this case img2pdf pdffile123 .  or  img2pdf.py pdffile123 .
4. Or we can execute this in any location by specifying the directory path 
    
    * eg. img2pdf pdffile /mnt/c/files/jpg_directory  where jpg directory contains the jpg files to be converted to pdf

## Thank You
