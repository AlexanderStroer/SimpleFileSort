import os

path = r"C:\Users\Legend\Downloads"
downloads = os.scandir(path)


with (downloads) as file:
    for f in file:
        if f.name.endswith(".pdf"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\PDFs\\" + f.name)
        elif f.name.endswith(".mp4"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\Videos\\" + f.name)
        elif f.name.endswith(".docx") or f.name.endswith(".txt"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\Word-Text Docs\\" + f.name)
        elif f.name.endswith(".pptx"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\PowerPoints\\" + f.name)
        elif f.name.endswith(".xlsx"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\Excel Docs\\" + f.name)
        elif f.name.endswith(".png") or f.name.endswith(".jpeg") or f.name.endswith(".jpg"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\Images\\" + f.name)
        elif f.name.endswith(".apkg"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\Anki\\" + f.name)
        elif f.name.endswith(".pkt") or f.name.endswith(".pkz") or f.name.endswith(".pka"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\CiscoPacketTracer\\" + f.name)
        elif f.name.endswith(".exe") or f.name.endswith(".gz") or f.name.endswith(".tar") or f.name.endswith(".zip"):
            os.rename("C:\\Users\\Legend\\Downloads\\" + f.name, "C:\\Users\\Legend\\Downloads\\Junk\\" + f.name)




