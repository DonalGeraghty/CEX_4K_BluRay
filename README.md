This app using a playwright script to crawl ie.webuy.com and search for any 4k blu rays available online.

It will record them to a csv, and then when it runs the following day it will compare today with yesterday and email the list of any NEW blu rays.

to run install all dependencies

create a .env file in the root and add the following

MY_KEY="xxxx yyyy zzzz oooo"
RECIPIENT="recipient@gmail.com"
SENDER="sender@gmail.com"

generate a pass key for MY_KEY , https://www.google.com/account/about/passkeys/ 
