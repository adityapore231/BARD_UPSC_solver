# Open the file in read mode
from bardapi import Bard
import os
from fpdf import FPDF
from reportlab.pdfgen import canvas

os.environ['_BARD_API_KEY']="XXXXXXXXXXXXX"

def bard(question):
    print("Getting the answer..........")
    answer = Bard().get_answer(question)['content']
    print("Writing........")
    return answer

def make_pdf():
    pdf = FPDF()
    pdf.add_page()
 
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
    f = open("output.txt", "r")
    
# insert the texts in pdf
    for x in f:
        w = pdf.get_string_width(x) + 6
        pdf.cell(w, 10, txt = x, ln = 1, align = 'L')
    # Save the PDF document
    pdf.output("UPSC answer Key.pdf")

def main():

    with open('F:/Data science/Projects/UPSC solver/upsc_question_paper.txt', 'r',encoding='utf-8') as file:
    # Read the contents of the file
        content = file.read()

    # Split the content into individual questions
    questions = content.split('\n\n')
    
    # Iterate through each question
    for question in questions:
        # Check if the line starts with 'Q'
        if question.startswith('Q'):
            try:   
                print(question)
                answer = question + "\n\n"  + "Answer :" + "\n\n"  + bard(question) + "\n\n"
                print(answer)
                with open('output.txt', 'a') as file:
            # Write content to the file
                    file.write(answer)
            except:
                print("Not Answered")
            print("---------------------------------------------------------------------")
    print("Writing to PDF")
    make_pdf()
if __name__ == "__main__":
    main()
