# 50
Youtube Auto Comments Using Localhost ports using selenium with python

go to chrome and right click and go to in properties copy the start in line full and enter cmd and enter cd and paste the code and hit enter button in my case 
my chrome properties start in line 

C:\Users\Hp\AppData\Local\Google\Chrome\Application

after added cd and pasted again

cd C:\Users\Hp\AppData\Local\Google\Chrome\Application

create a new folder in desktop and go to your chrome setting and you will find about version and see the version then download the same chromedriver and unzip that chromedriver and paste to the folder then in that folder only

create new folder named as localhost then double click on localhost and copy the path and paste in below code where in last dir after where double inverted comma started 


chrome.exe --remote-debugging-port=9222 --user-data-dir=""(in "enter your localhost path") 

in my case

chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\Hp\Desktop\Bots\Chromedriver\Localhost"   #after copy these and paste in command prompt and hit enter button then it goes to new localhost chrome and its stores all data to you created localhost
then login with your un authenticated google acc with password then 

copy my h.py code and create a new text file in that folder an paste my code and save as your 1.py then in cmd enter 1.py or double click on 1.py python file...
when opening 1.py you must open the localhost chrome where you created....

in 12 line in code change if you needed other comments inside ...

in 20th line change with your required movie url...

thats all done the url will open in that opened localhost chrome and automatically do the comments....

in cmd enter

pip install Random 

and hit enter button

👉Note:-

👉if your selenium version is in latest version then the code never run

👉open cmd and enter pip uninstall selenium

And enter

pip install selenium==4.2.0

and hit enter

and

python -c "import selenium; print(selenium.version)"

𝙏𝙝𝙞𝙨 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙞𝙨 𝙤𝙣𝙡𝙮 𝙛𝙤𝙧 𝙚𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣al 𝙥𝙪𝙧𝙥𝙤𝙨𝙚 𝙖𝙣𝙙 𝙬𝙚 𝙖𝙧𝙚 𝙣𝙤𝙩 𝙧𝙚𝙨𝙥𝙤𝙣𝙨𝙞𝙗𝙡𝙚 𝙛𝙤𝙧 𝙖𝙣𝙮 𝙠𝙞𝙣𝙙 𝙤𝙛 𝙞𝙡𝙡𝙚𝙜𝙖𝙡 𝙖𝙘𝙩𝙞𝙫𝙞𝙩𝙮 𝙙𝙤𝙣𝙚 𝙗𝙮 𝙩𝙝𝙞𝙨 𝙩𝙤𝙤𝙡.
