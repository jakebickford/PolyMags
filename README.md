# PolyMags

This project aimed to unlock new ways of accessing a digitised collection of historic magazines held by the University of Westminster Archive. 

The Polytechnic Magazine was the in-house magazine of the [Regent Street Polytechnic](https://westminster-atom.arkivum.net/index.php/rsp), one of the predecessor institutions of the [University of Westminster](https://www.westminster.ac.uk/). Since 2011, a digitised run of more than 1700 issues of the magazine covering the years 1879 to 1960 has been made available by the [University Archive](http://recordsandarchives.westminster.ac.uk/). This has proved an invaluable resource for academic researchers, family historians and university staff. You can search and read the digitised magazines themselves via the University Archive's [Polymags site](https://polymags.westminster.ac.uk/).

This project aims to complement the existing resource by opening up computational methods of access to the collection.

## Project outputs

### Public notebooks
These are designed to be accessible to all users, and to serve as an introduction to the corpus and the sort of techniques that could be used with it. 
The notebooks are available to run live, in Google collab. Note that to run the code you need to be signed in with a Google account.
* [Frequency Analysis and Named Entity Recognition](https://colab.research.google.com/drive/1Wa44qr8xMK2kd-eIk-M0_-IqW41D2nB3?usp=sharing)
* [Topic modelling](https://colab.research.google.com/drive/1HAS-Xo3EH_O93Lp_nTV4pZT3eV8F5bBX?usp=sharing) 

### The corpus 
If you are more experienced with computational analysis of text, you might prefer to download the corpus itself. This is available to download from Google drive as either:
* A pickled [Pandas DataFrame](https://drive.google.com/file/d/1uvog_cKlc3fFbVdkmUgoYtRzB9Dv8GEj/view?usp=sharing)
  The DataFrame contains a row for each issue of the magazine, with columns containing the text, metadata such as the date of the issue, and with different instances of text processing such as tokenisation, and lemmatisation.
* A zipped [set of the OCR'd text files](https://drive.google.com/file/d/17NlNzqnHHE8be3YR1cz7dC8xFG9kTgTH/view?usp=sharing). When I began the project, I re-OCR'd the existing scanned documents with Tesseract v5 and did some basic correction with regular expressions. This is the result. There is one .txt file for each of the 1725 issues I chose to look at. 
