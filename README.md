![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=❣️Welcome+To+🕵️ADG+AUTOFILTER+BOT!;Created+by+🔥SCROOGE+X🔥;A+simple+auto+film+filter+Bot!;Do+Not+Deploy+This+Repository!;This+Is+Privat+Edition!!)
</p>
<h1 align="center">
  <b>ADG AUTO FILTER</b>
</h1>

<a href="https://t.me/adgmovies">
  <img src="https://img.shields.io/badge/Join-blue?logo=telegram" width="70">

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this 
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
* `SUPPORT_CHAT` : @TeamDarkDevil
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
* `FILE_CHANNEL` : File redirect to channel
* `DELETE_CHANNELS` : you can delete multiple files by forwarding those files into a private channel. Firstly make a private channel, add your bot as admin, add that channel's ID as a variable named DELETE_CHANNELS and forward the files to that private channel and the bot will delete those files from its database. You can check logs to confirm whether the file is deleted from the bot's database or not.
### Optional Variables

</details>

## Deploy
You can deploy this bot anywhere.


<details><summary>Deploy To Heroku</summary>
<br>
<p>
<a href="https://heroku.com/deploy?template=https://github.com/DARK-DEVIL-BOTZ/Film-Detective">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p></details>

<details><summary>Deploy To Koyeb</summary>
<br>
<p>
<a href="https://app.koyeb.com/deploy?type=git&repository=github.com/DARK-DEVIL-BOTZ/Film-Detective&env[BOT_TOKEN]&env[API_ID]&env[API_HASH]&env[CHANNELS]&env[ADMINS]&env[PICS]&env[LOG_CHANNEL]&env[AUTH_CHANNEL]&env[CUSTOM_FILE_CAPTION]&env[DATABASE_URI]&env[DATABASE_NAME]&env[COLLECTION_NAME]=Telegram_files&env[FILE_CHANNEL]=-1001832732995&env[SUPPORT_CHAT]&env[IMDB]=False&env[IMDB_TEMPLATE]&env[SINGLE_BUTTON]=True&env[AUTH_GROUPS]&env[P_TTI_SHOW_OFF]=True&branch=main&name=doctor-strainge">
 <img src="https://www.koyeb.com/static/images/deploy/button.svg">
</p>
</details>
<details><summary> Deploy To Okteto </summary>
<br>
<p>
<a href="https://cloud.okteto.com/deploy?repository=https://github.com/DARK-DEVIL-BOTZ/Film-Detective&branch=main">
  <img src="https://okteto.com/develop-okteto.svg" alt="Develop on Okteto">
</a>
</p>
</details>
<details><summary>Deploy To VPS</summary>
<p>
<pre>
git clone https://github.com/DARK-DEVIL-BOTZ/Film-Detective
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 Film-Detective.py
</pre>
</p>
</details>

## Commands

```
* /logs - to get the rescent errors
* /stats - to get status of files in db.
* /filter - add manual filters
* /filters - view filters
* /connect - connect to PM.
* /disconnect - disconnect from PM
* /del - delete a filter
* /delall - delete all filters
* /deleteall - delete all index(autofilter)
* /delete - delete a specific file from index.
* /info - get user info
* /id - get tg ids.* /imdb - fetch info from imdb.
* /users - to get list of my users and ids.
* /chats - to get list of the my chats and ids* /broadcast - to broadcast a message to all Elsa users
* /gfilter - group filter
* /grp_broadcast - broadcast to all group
* /song - get song
* /video - get video
* /setskip - used in index where indexing a specific number
* /font - fonts for your text
```