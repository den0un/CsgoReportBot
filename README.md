# CSGO ReportBot
<p>This is a csgo/steam report bot coded using python, to get it working you need to install some pakages:</p>
<p>-pip install bs4</p>
<p>-pip install requests</p>
<p>-pip install pycryptodome</p>

# What you need
<p>First of all you need Steam Accounts that have steam guard disabled (this code can not work with Steam Guard). Then you get the accounts and put them to the usernames/passwords txt file.</p>

Note: make sure that every username is at the same line as the password on the txt files !!<br>

this code works fine on windows, but if you want it to work on linux you need to change os.system('cls') to os.system('clear')<br>

-its better to put the steam accounts into a mysql database to make it easy to manage.<br>

-if there is any mistakes or potential upgrades to the code please contact me.</p>

# How to use it

<p>-git clone https://github.com/den0un/CsgoReportBot.git</p>

<p>-python3 main.py</p>

# How it works

<p> basically the script logins to steam and make the report operation all of that using requests library.</p>

### -1 Login to steam

the steam login process consists of 2 urls<br>
1- https://steamcommunity.com/login/getrsakey/ to get the RSA Key for password encryption.<br>
2- https://steamcommunity.com/login/dologin/ its for loging in, it needs a username and an encrypted password and some other form data.<br>


### -2 The Report Process

to start reporting we need the Victim's ID, so we get it from his profile using beautifulsoup library.<br>
the report process consists of 3 urls, those url's are the steps of reporting from the main profile page, which are:<br>
1- Clicking On Report Player https://steamcommunity.com/actions/ReportProfile/<br>
2- Choosing They are cheating in a game https://steamcommunity.com/actions/AjaxGetReportProfileStep/<br>
3- Submiting the report https://steamcommunity.com/actions/ReportAbuse/ with a discription and a game to choose (AppID).





