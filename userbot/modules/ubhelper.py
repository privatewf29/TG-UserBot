""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai  {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` "
        


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/W29F/TG-UserBot/TG-UserBot/varshelper.txt)")


CMD_HELP.update({
    "ubhelper":
    "`.ubhelp`\
\nPenjelasan: Bantuan Untuk TG-UserBot.\
\n`.lordvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
