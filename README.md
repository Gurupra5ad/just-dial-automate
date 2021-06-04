# just-dial-automate
#### Once the Just-Dial URL is given as input by the user, the python script will scrape 250 people's AD details, phone number, name and address
#### GUI is made with tkinter


pyinstaller -F --onedir --console --icon "C:/Users/gurup/Desktop/just-dial-automate/scrape.ico" --add-data "C:/Users/gurup/Desktop/just-dial-automate/data.csv;." --hidden-import "bs4" "C:/Users/gurup/Desktop/just-dial-automate/just-dial.py"
