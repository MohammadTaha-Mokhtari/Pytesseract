import cv2 as cv
import pytesseract
import pyperclip

# Set path to tesseract if needed (uncomment and set the correct path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
languages = {
    1: ("English", "eng"),
    2: ("French", "fra"),
    3: ("German", "deu"),
    4: ("Spanish", "spa"),
    5: ("Italian", "ita"),
    6: ("Chinese", "chi_sim"),
    7: ("Japanese", "jpn"),
    8: ("Arabic", "ara"),
    9: ("Persian", "fas")
}
print("select a language:")
for key, value in languages.items():
    print(f"{key}. {value[0]}")
while True:
    try:
        lang_choice = int(input("enter the number of your language choice: "))
        if lang_choice in languages:
            lang_code = languages[lang_choice][1]
            break
        else:
            print("please enter a valid number.")
    except ValueError:
        print("invalid input. please enter a number.")
print("\nchoose input method:")
print("1. webcam (Live)")
print("2. load from image file")
while True:
    try:
        input_choice = int(input("enter your choice (1 or 2): "))
        if input_choice in [1, 2]:
            break
        else:
            print("only 1 or 2 are valid choices.")
    except ValueError:
        print("please enter a number.")
if input_choice == 1:
    cap = cv.VideoCapture(0)
    print("press 's' to capture an image from webcam.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("could not access webcam.")
            break
        cv.imshow("live feed", frame)
        if cv.waitKey(1) & 0xFF == ord('s'):
            image = frame
            break
    cap.release()
    cv.destroyAllWindows()
else:
    image_path = input("enter the path to the image file: ")
    image = cv.imread(image_path)
    if image is None:
        print("image could not be loaded.")
        exit()
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray, lang=lang_code)
print("\n✅ detected Text:\n")
print(text.strip())
pyperclip.copy(text.strip())
print("\n📋 text copied to clipboard.")
