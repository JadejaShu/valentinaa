class script(object):
    START_TXT = """Hello {},
Myself <a href=https://telegram.me/{}>{}</a>,\n\nTrust me ! I can't even imagine how super-fast i can drive your Database channel \n\nAre you ready for Long Drive Baby...🤪"""
    LZTHMB_TEXT = """Hello {},
Glad to see you here. LOVE FROM  <a href=https://telegram.me/R_MvzZ >R_MvzZ</a> work.\n\n<b>Thumbnail extracting</b> feature will be available soon, please join <a href=https://telegram.me/R_MvzZ>Dev Channel</a> and stay tuned for next <a href=https://telegram.me/R_MvzZ>update</a>.\n\n  🐞 REPORT A BUG: <a href=http://telegram.me/Off_topic_discussion>R_MvzZ Support</a>
    """
    LZLINK_TEXT = """Hey {},
Glad to see you here. LOVE FROM  <a href=https://telegram.me/R_MvzZ >R_MvzZ</a> .\n\n<b>File to LiNK converting</b> feature will be available soon, please join <a href=https://telegram.me/R_MvzZ>Dev Channel</a> and stay tuned for next <a href=https://telegram.me/R_MvzZ>update</a>.\n\n  🐞 REPORT A BUG: <a href=http://telegram.me/Off_topic_discussion>R_MvzZ Support</a>
    """
    DNT_TEXT = """Hey Sirji / Madamji {},
Thanks for thinking about us.\nLOVE FROM  <a href=https://telegram.me/R_MvzZ >R_MvzZ</a> work.\n\n<b>For your kind information, we do not ask or force anyone for any kind of payment</b>. But if you really want to donate us then you can send money to us from below links...\n\n💵 Reach Donation Page : <a href=http://telegram.me/R_MvzZ>Click here...</a>\n\nT❤️ hank you so much..
    """
    REQ_AUTH_TEXT = """Hello {},
\nSorry Sirji / Madamji.. You must have to be the Authentic User to complete this operation...\n\n👮‍♀ REPORT ISSUE AT: <a href=https://telegram.me/R_MvzZ>R_MvzZ Support</a>\n\n
    """
    ALRDY_UPLDD_TEXT = """✅ Content is already uploaded.\n\nName:{}\nPlease make sure about your spelling before submitting request..."""
    HELP_TXT = """𝙷𝙴𝚈 {}
Here is the help for my COMMANDS."""
    ABOUT_TXT = """✯ MY NAME: {}
✯ CREATOR: <a href=https://telegram.me/harshsoni_008> HARSH </a>
✯ LIBRARY: PYROGRAM
✯ Programmed In:- PYTHON
✯ DATABASE: Mongo-DB
✯ MY SERVER: HEROKU <i>(Basic)</i>"""
    SOURCE_TXT = """<b>NOTE:</b>
- We do not sell or help to make this type of bot
- We will think about source very soon  

<b>DEVS:</b>
- <a href=https://telegram.me/R_MvzZ>R_MvzZ </a>"""
    MANUELFILTER_TXT = """
    Help: <b>Filters</b>

    - Filter is the feature were users can set automated replies for
    a particular keyword and this bot will respond whenever that 
    keyword hits the message

    <b>NOTE:</b>
    1. BOT should have admin privilege.
    2. Only admins can add filters in a chat.
    3. Alert buttons have a limit of 64 characters.

    <b>Commands and Usage:</b>
    • /filter - <code>add a filter in chat</code>
    • /filters - <code>list all the filters of a chat</code>
    • /del - <code>delete a specific filter in chat</code>
    • /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    
    BUTTON_TXT = """
    Help for: <b>Button module</b>

    - Supports both url and alert inline buttons.

    <b>NOTE:</b>
    1. Telegram will not allows you to send buttons without any content,
    so content is mandatory.
    2. BOT supports buttons with any telegram media type.
    3. Buttons should be properly parsed as markdown format

    <b>URL buttons:</b>
    <code>[Button Text](buttonurl:https://telegram.me/R_MvzZ)</code>

    <b>Alert buttons:</b>
    <code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """
    Help for: <b>Auto Filter</b>

    <b>NOTE:</b>
    1. Make me the admin of your channel if it's private.
    2. Make sure that your channel does not contains CAM-Rips, 
    p*rn/nude or fake files.
    3. Forward the last message to me with quotes.
    I'll add all the files in that channel to my db."""
 
    CONNECTION_TXT = """
    Help for: <b>Connections</b>

    - Used to connect bot to PM for managing 
    filters & helps to avoid spamming in groups.

    <b>NOTE:</b>
    1. Only group admins can add a connection.
    2. Send <code>/connect</code> for connecting me to ur PM

    <b>Commands and Usage:</b>
    • /connect  - <code>connect a particular chat to your PM</code>
    • /disconnect  - <code>disconnect from a chat</code>
    • /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """
    Help for: <b>Extra Modules
    
    NOTE:- these are the extra features of This bot
    Commands and Usage:</b>
    • /id - <code>get id of a specified user.</code>
    • /info  - <code>get information about a user.</code>
    • /imdb  - <code>get the film information from IMDb source.</code>
    • /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """
    Help for: <b>Admin mods
    NOTE:- This module only works for my admins

    Commands and Usage:</b>
    • /logs - <code>to get the recent errors</code>
    • /stats - <code>to get status of files in db.</code>
    • /delete - <code>to delete a specific file from db.</code>
    • /users - <code>to get list of my users and ids.</code>
    • /chats - <code>to get list of the my chats and ids </code>
    • /leave  - <code>to leave from a chat.</code>
    • /disable  -  <code>do disable a chat.</code>
    • /ban  - <code>to ban a user.</code>
    • /unban  - <code>to un-ban a user.</code>
    • /channel - <code>to get list of total connected channels</code>
    • /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """
    ★TOTAL FILES: <code>{}</code>
    ★TOTAL USERS: <code>{}</code>
    ★TOTAL CHATS: <code>{}</code>
    ★USED STORAGE: <code>{}</code> 
    ★FREE STORAGE: <code>{}</code>"""

    LOG_TEXT_G = """
    #New_valentine_Group
    Group = {}(<code>{}</code>)
    Total Members = <code>{}</code>
    Added By - {}"""

    LOG_TEXT_P = """
    #New_valentine_User
    ID - <code>{}</code>
    Name - {}"""
    
    PROGRESS_BAR = """\n
╭━━━━❰ PROGRESS BAR ❱━➣
┣⪼ 🗂️: {1} | {2}
┣⪼ ⏳️: {0}%
┣⪼ 🚀: {3}/s
┣⪼ ⏱️: {4}
╰━━━━━━━━━━━━━━━➣ """
