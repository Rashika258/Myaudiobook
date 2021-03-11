#python text to speech conversion
import pyttsx3
#pdf lib
import PyPDF2
#select your book open in read binary mode
book = open('CN.pdf', 'rb')
#create pdfReader object
pdfReader = PyPDF2.PdfFileReader(book)
#count the total pages
total_pages = pdfReader.numPages
print("Total number of pages " +str(total_pages))
#initialise speaker object
speaker = pyttsx3.init()
# print("Enter your starting page")
# start_page = int(input())
print("Menu\n 1. Play a single page\n 2. Play between start and end points\n 3. Play the entire book ")
print("Enter your choice")
choice = int(input())
if (choice  == 1):
    print("Enter index number")
    page = int(input())
    page = pdfReader.getPage(page)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
elif (choice == 2):
    print("Enter starting page number")
    start_page = int(input())
    print("Enter ending page number")
    end_page = int(input())
    for page in range(start_page+1, end_page):
        page = pdfReader.getPage(start_page+1)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
elif (choice == 3):
    for page in range(total_pages+1):
        page = pdfReader.getPage(page)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
else:
    print("Haha!! Please enter valid choice")




