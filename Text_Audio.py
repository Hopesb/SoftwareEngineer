import os
import docx2txt2
import pyttsx3


def convert(filepath):
    """
    This helps to convert the file to text format.

    ---------
    Parameter: 
        file path

    --------
    Return:
        Saved mp3 file.
    """
    # Checking the file is either docx or txt file extension
    file = os.path.splitext(filepath)
    # Getting the file extension
    extension = file[-1]
    # Initialize the pytts3x libray.
    engine = pyttsx3.init()
    if extension == ".docx":
        # Create a variable txt for the converted file.
        txt = docx2txt2.extract_text(filepath)
        # To read out loud the text in the file.
        engine.say(txt)
        # show that the file is saving.
        print(f"{filepath} is converting to mp3 format")
        # Saving the file
        engine.save_to_file(txt, f"{file[0]}.mp3")
        # End the engine.
        engine.runAndWait()
        return f"File Saved."

    elif extension == ".txt":
        # opening the filepath and reading it.
        txt = open(filepath, "r").read()
        # To read out loud the text in the file.
        engine.say(txt)
        # show that the file is saving.
        print(f"{filepath} is converting to mp3 format")
        # Saving the file.
        engine.save_to_file(txt, f"{file[0]}.mp3")
        # End the engine.
        engine.runAndWait()
        return f"File Saved"

    else:
        print("File extension not supported.")
        print("Check the file extension again. The only format accepted are .docx and .txt")

con = convert("doc.txt")
print(con)