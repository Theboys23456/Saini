import random #NIKHIL SAINI BOTS
import time #NIKHIL SAINI BOTS
import math #NIKHIL SAINI BOTS
import os #NIKHIL SAINI BOTS
from vars import CREDIT #NIKHIL SAINI BOTS
from pyrogram.errors import FloodWait #NIKHIL SAINI BOTS
from datetime import datetime,timedelta #NIKHIL SAINI BOTS

class Timer: #NIKHIL SAINI BOTS
    def __init__(self, time_between=5): #NIKHIL SAINI BOTS
        self.start_time = time.time() #NIKHIL SAINI BOTS
        self.time_between = time_between #NIKHIL SAINI BOTS

    def can_send(self): #NIKHIL SAINI BOTS
        if time.time() > (self.start_time + self.time_between): #NIKHIL SAINI BOTS
            self.start_time = time.time() #NIKHIL SAINI BOTS
            return True #NIKHIL SAINI BOTS
        return False #NIKHIL SAINI BOTS

def hrb(value, digits= 2, delim= "", postfix=""): #NIKHIL SAINI BOTS
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KB", "MB", "GB", "TB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision = 0):
    pieces = []
    value = timedelta(seconds=seconds)
    if value.days:
        pieces.append(f"{value.days}day")
    seconds = value.seconds
    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}hr")
        seconds -= hours * 3600
    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}min")
        seconds -= minutes * 60
    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}sec")
    if not precision:
        return "".join(pieces)
    return "".join(pieces[:precision])

timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            eta = hrt(remaining_bytes / speed, precision=1) if speed > 0 else "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)

            bar_length = 12
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length

            symbol_pairs = [
                ("◾️", "◽️"),
                ("⚫️", "⚪️"),
                ("🔴", "🔵"),
                ("⬛️", "⬜️"),
                ("🟦", "⬜️")
            ]
            completed_symbol, remaining_symbol = random.choice(symbol_pairs)
            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length

            try:
                await reply.edit(
                    f"""<b>🛡️ [𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗨𝗣𝗟𝗢𝗔𝗗 𝗦𝗬𝗦𝗧𝗘𝗠]</b>
<b>⚙️ ENGINE:</b> <code>STRANGER | CyberCore v9.2</code>
<b>👤 THREAD:</b> <code>0x-WLV-DRM-PREM</code>
<b>🧠 HANDLER:</b> <i>Stranger Boy × KRISHNA Matrix</i>

<b>📊 PROGRESS PANEL</b>
{progress_bar}
<b>🔹 Percentage:</b> <code>{perc}</code>
<b>🔹 Speed:</b> <code>{sp}</code>
<b>🔹 Loaded:</b> <code>{cur}</code>
<b>🔹 Total:</b> <code>{tot}</code>
<b>🔹 ETA:</b> <code>{eta}</code>

<code>────────────────────────────</code>
<b>🌌 STATUS:</b> <code>💠 ACTIVE - HACKFLOW MODE 💠</code>
<b>🕘 TIME:</b> <code>{datetime.now().strftime('%H:%M:%S')}</code>
<b>⚡ POWER:</b> <code>PREMIUM CYBERCORE STRATEGY</code>
<code>────────────────────────────</code>
<b>👑 MODE:</b> <code>VIP ELITE HEAVEN DESIGN</code>
<b>🌐 SYSTEM:</b> <code>INFILTRATION ⨉ ILLUSION</code>
<b>🔰 SHIELD:</b> <code>ENCRYPTED 4096-BIT</code>
""")
            except FloodWait as e:
                time.sleep(e.x)
