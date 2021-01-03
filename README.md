# award-certificate-maker

## About
Use this Python repo to create award certificates for students in bulk. 

## What we need
- A background image 
- a list of students (name, cert date) in Csv format

---
## How to run

Visit the folowing repl

https://repl.it/@bilgrami/award-certificate-maker#README.md

**Steps**

1) Upload your award certificate background image to images folder
2) Edit names in the data/names.csv
3) Update and review config.json file
4) Click on run button. CAUTION: All existing JPG images inside output folder will be deleted.
5) Review Output image files for each student. If you think the position is off, you can tweat the x,y position inside main.py

## Config file 

```json
{
    "DataFileLocation": "data/names.csv",
    "BackgroundImageFileLocation": "images/BalighaCertificate.jpg",
    "OutputFolderLocation": "output",
    "OutputFilePrefix": "cert-",
    "FontName": "FreeMono.ttf"
}
```

### Data file 

```csv
name,date
Fancy Fungus,14th February 2020
Underground Labrat,14th February 2020
Carbonated Sugar,14th February 2020
Wood wide web,14th February 2020
```

### Background Image File 

![background image](images/BalighaCertificate.jpg)

### Output
A separate image file is generated for each student
