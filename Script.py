#Modified By ScroogeX
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """𝙷𝙴𝙻𝙻𝙾 {} 𝙱𝚁𝙾😉,
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿. 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚉... 😍"""
    HELP_TXT = """𝙷𝙾𝚆 𝙰𝚁𝙴 𝚈𝙾𝚄 {} 𝙱𝚁𝙾😜
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂. 𝙱𝚄𝚃 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙽𝙾𝚃 𝚄𝚂𝙴 𝙰𝙳𝙼𝙸𝙽 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂\n\n𝙼𝚈 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙸𝚂 <a href=https://t.me/scrooge010>ScroogeX</a> """
    ABOUT_TXT = """ 🤡 𝙸 𝚊𝚖 <a href=https://t.me/adgautofilter1_bot>ADG Auto Filter</a>
🏅 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/scrooge010>ScroogeX</a>
🥇 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
🥈 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
🥉 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
🎖️ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: HEROKU
🛠 ️𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0 [ 𝙱𝙴𝚃𝙰 ]
👨‍💻 𝙼𝚈 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙸𝚂 <a href=https://t.me/scrooge010>SCROOGEX</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a privat edition. 
- Source - locked🔐

<b>👨‍💻DEVELOPERS👩‍💻:</b>
- <a href=https://t.me/scrooge010>ScroogeX</a>"""
    MANUELFILTER_TXT = """𝙷𝙴𝙻𝙿: <b>𝙵𝙸𝙻𝚃𝙴𝚁𝚂</b>

- Filter is the feature were users can set automated replies for a particular keyword and ADG auto filter will respond whenever a keyword is found the message

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🖥️ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂 𝚂𝙰𝚅𝙴𝙳: <code>{}</code>
🕵️ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
📋 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⚖️ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
🧮 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """𝗡𝗘𝗪 𝗚𝗥𝗢𝗨𝗣
⚔️𝙶𝚁𝙾𝚄𝙿 = {}(<code>{}</code>)
🎰𝚃𝙾𝚃𝙰𝙻 𝙼𝙴𝙼𝙱𝙴𝚁𝚂= <code>{}</code>
👽𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 - {}
©️ADG MOVIES
"""
    LOG_TEXT_P = """𝗡𝗘𝗪 𝗠𝗘𝗠𝗕𝗘𝗥
🆔𝙸𝙳 - <code>{}</code>
💡𝙽𝙰𝙼𝙴 - {}
©️ADG MOVIES
"""
