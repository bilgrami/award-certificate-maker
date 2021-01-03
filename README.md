# award-certificate-maker

## About
This python repo created award certificates for students as JPEG image. 

## What we need
- A background image 
- a list of students (name, cert date) in Csv format

---
## How to run
Visit the folowing repl

https://repl.it/@bilgrami/award-certificate-maker#README.md

**Steps**

1) Add a base image under images folder
2) add names in the data/names.csv
3) review config.json file
4) click on run button. Note that existing JPG images inside output folder will be deleted.
5) Review Output image files

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

You can tweak the x,y position inside main.py

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
