from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb. ...`🙏")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb. ...`🙏")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam wr. wb.`☺️")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumussalam wr. wb.`☺️")


CMD_HELP.update({
    "𝗦𝗔𝗟𝗔𝗠":
    "⚡**CMD**⚡: `.P`\
\n↳ : __Untuk Memberi salam.__\
\n\n⚡**CMD**⚡: `.L`\
\n↳ : __Untuk Menjawab Salam.__"
})
