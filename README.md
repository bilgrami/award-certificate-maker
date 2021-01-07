# award-certificate-maker

## About

Use this program to create award certificates for students in bulk.

All you need is

- A background image
- A list of students (name, cert date) in CSV format
- Run the code

Continue reading the following sections to learn further details about the above steps.

---

## Run the program

You can run the code online by visiting [here](https://repl.it/@bilgrami/award-certificate-maker#README.md).

Alternatively, you can clone this repo and run it locally via the following command.

```base
git clone https://github.com/bilgrami/award-certificate-maker.git
pip3 install -r requirements.txt 
python3 main.py
```

## Quick-Start Instructions

Follow below **Steps**

1) Add/Update student names inside [data/names.csv](data/names.csv)
2) Run the code

---

## Generated Certificate

A separate certificate JPG file gets generated for each student under the output folder.

![background image](public/images/certificate-[march-17th-1969]-[allama-mahboobeh].jpg)

## Detailed Instructions

Follow below **Steps**

1) Upload your award certificate background image to the [images/](images/) folder
2) Add student names inside [data/names.csv](data/names.csv)
3) Review and Update [config.json](config.json) file
4) Run the code

   __CAUTION__: All existing JPG images inside the output folder will be deleted.

5) Review Generated certificate

   Review Output certificate image. You can tweak the x,y positions for the name, date inside the image. Edit [main.py](main.py) and change the following variables

      - NAME_X
      - NAME_Y
      - DATE_X
      - DATE_Y

   and then re-run the code.

---

### Output folder location

Output folder is located at ```./output/{OutputFolderLocation}```, where ```{OutputFolderLocation}``` is the name of folder specified in [config.json](config.json).

### Output filename

Output file is named as  ```{OutputFilePrefix}[{dt}]-[{name}]```, where ```{OutputFilePrefix}``` is the prefix name specified in [config.json](config.json), while ```{name}``` and ```{dt}``` values are specified inside [data/names.csv](data/names.csv).

---

## Background Image

![background image](public/images/BalighaCertificate.jpg)

---

## Student list

![background image](public/images/names.png)

---

## Config file

![background image](public/images/config.png)

---

## Shell-Output

```shell

>>>>> START of Award Certificate Maker <<<<<

Removing JPG files at folder [output/saba/class-of-2021]..done!
Generating certificates ..
        [Fancy Fungus] certificate generated at:  output/saba/class-of-2021/certificate-[14th-january-2020]-[fancy-fungus].jpg
        [Underground Labrat] certificate generated at:  output/saba/class-of-2021/certificate-[feb-2020]-[underground-labrat].jpg
        [Allama Mahboobeh] certificate generated at:  output/saba/class-of-2021/certificate-[march-17th-1969]-[allama-mahboobeh].jpg
        [Wood wide web] certificate generated at:  output/saba/class-of-2021/certificate-[april-2021]-[wood-wide-web].jpg
        [Chew Kok Long] certificate generated at:  output/saba/class-of-2021/certificate-[may-2021]-[chew-kok-long].jpg
        [Sam Sung] certificate generated at:  output/saba/class-of-2021/certificate-[june-2021]-[sam-sung].jpg
        [Saad Butt] certificate generated at:  output/saba/class-of-2021/certificate-[25-july-2022]-[saad-butt].jpg
        [Jed I Knight] certificate generated at:  output/saba/class-of-2021/certificate-[august-1969]-[jed-i-knight].jpg
        [Dr. Joelle Rollo-Koster] certificate generated at:  output/saba/class-of-2021/certificate-[ocotober-2020]-[dr.-joelle-rollo-koster].jpg
        [Dr. Faartz] certificate generated at:  output/saba/class-of-2021/certificate-[november-1999]-[dr.-faartz].jpg
        [Mister Love] certificate generated at:  output/saba/class-of-2021/certificate-[december-2000]-[mister-love].jpg
        [Janice Keihanaikuakahihuliheekahaunaele] certificate generated at:  output/saba/class-of-2021/certificate-[1st-january-1]-[janice-keihanaikuakahihuliheekahaunaele].jpg
done! Generated a total of 12 certificates

>>>>> END of Award Certificate Maker <<<<<

```
