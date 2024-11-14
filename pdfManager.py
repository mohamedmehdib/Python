import PyPDF2
import os


while True:
    choice = int(input("Please choise ( 1 for merge and 2 for demerger ) : "))
    if choice in [1,2]:
        break

if choice==1:
    print("ATTENTION : Please put the merger files in one folder !")
    name = input("Please choice the name of the merger file : ")
    merger = PyPDF2.PdfMerger()

    all_files = os.listdir(os.curdir)
    pdf_files = [file for file in all_files if file.endswith(".pdf")]
    
    for file in pdf_files:
        if file.endswith(".pdf"):
            merger.append(file)
    merger.write(f"{name}.pdf")

    print("The files was merged !")


else:
    name = input("Please input the name of the demerged file : ")
    try:
        with open(f'{name}.pdf', 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(reader.pages)):
                writer = PyPDF2.PdfWriter()
                page = reader.pages[page_num]
                writer.add_page(page)
                
                with open(f'page_{page_num + 1}.pdf', 'wb') as output_file:
                    writer.write(output_file)
    except:
        print("Please verify the file name")

    print("Done !")