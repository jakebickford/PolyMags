# Computational access to the Polytechnic Magazine (1879 - 1960)

This project aimed to unlock new ways of accessing a digitised collection of historic magazines held by the University of Westminster Archive. It was undertaken as part of my PG Cert. in Applied Data Science at Birkbeck. 

The Polytechnic Magazine was the in-house magazine of the [Regent Street Polytechnic](https://westminster-atom.arkivum.net/index.php/rsp), one of the predecessor institutions of the [University of Westminster](https://www.westminster.ac.uk/). Since 2011, a digitised run of more than 1700 issues of the magazine covering the years 1879 to 1960 has been made available by the [University Archive](http://recordsandarchives.westminster.ac.uk/). This has proved an invaluable resource for academic researchers, family historians and university staff. You can search and read the digitised magazines themselves via the University Archive's [Polymags site](https://polymags.westminster.ac.uk/). This project aimed to complement the existing resource by opening up computational methods of access to the collection.

## Project outputs

### Public notebooks
These are designed to be accessible to all users regardless of their level of experience with digital analysis of texts, and to serve as an introduction to the corpus and the sort of techniques that could be used with it. 
The notebooks are available to run live, in Google Colab. Note that to run the code you need to be signed in with a Google account.
* [Frequency Analysis and Named Entity Recognition](https://colab.research.google.com/drive/1Wa44qr8xMK2kd-eIk-M0_-IqW41D2nB3?usp=sharing)
* [Topic modelling](https://colab.research.google.com/drive/1HAS-Xo3EH_O93Lp_nTV4pZT3eV8F5bBX?usp=sharing) 

The notebooks are designed to run in Google Colab and make use of Colab's forms functionality to manage user input, however if you would like to try running them locally, you can download the back-up copies from the [Public Notebooks](https://github.com/jakebickford/PolyMags/tree/main/PublicNotebooks) folder above.

### The corpus 
If you are more experienced with computational analysis of text, you might prefer to download the corpus itself. This is available to download from Google drive as either:
* A pickled [Pandas DataFrame](https://drive.google.com/file/d/1uvog_cKlc3fFbVdkmUgoYtRzB9Dv8GEj/view?usp=sharing) (774.6MB)
  The DataFrame contains a row for each issue of the magazine, with columns containing the text, metadata such as the date of the issue, and with different instances of text processing such as tokenisation, and lemmatisation.
* A zipped [set of the OCR'd text files](https://drive.google.com/file/d/17NlNzqnHHE8be3YR1cz7dC8xFG9kTgTH/view?usp=sharing) (78MB). When I began the project, I re-OCR'd the existing scanned documents with Tesseract v5 and did some basic correction with regular expressions. This is the result. There is one .txt file for each of the 1725 issues I chose to look at. 

## Secondary material

### Preparatory notebooks
These were used to prepare the corpus and to experiment with natural language processing techniques to use in the public notebooks. If you would like to see how the text was processed to create the corpus DataFrame and the public notebooks, you can download the preparatory notebooks from the [PreparatoryNotebooksFinal](https://github.com/jakebickford/PolyMags/tree/main/PreparatoryNotebooksFinalfolder) above.

### File list
This csv contains the 
