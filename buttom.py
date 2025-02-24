from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM


def gen_app_kb(page):
    if page == 1:
        keyboard = [
            [KB(" 𝔸𝕝𝕝 𝔸𝕡𝕡𝕩 𝔸𝕡𝕚 (𝕨𝕖 𝕌𝕣𝕝 𝕠𝕣 𝔸𝕡𝕚) ", callback_data="master")],
            [KB("𝔸𝕝𝕝 ℂ𝕝𝕒𝕤𝕤𝕡𝕝𝕦𝕤 𝔸𝕡𝕜 ", callback_data="cp")],
            [KB("ℂ𝕝𝕒𝕤𝕤ℙ𝕝𝕦𝕤 𝕋𝕠𝕜𝕖𝕟 𝔾𝕖𝕟𝕖𝕣𝕒𝕥𝕠𝕣 ", callback_data="token")],
            [KB(" 𝔼𝕕𝕦𝕜𝕖𝕞𝕪 ", callback_data="edukemy"), KB(" 𝔸𝕡𝕟𝕚 𝕂𝕒𝕜𝕤𝕙𝕒 ", callback_data="kaksha")],
            [KB(" 𝕂𝕙𝕒𝕟 𝔾𝕊 ", callback_data="khan")],
            [KB(" ℕ𝕖𝕠𝕟 ℂ𝕝𝕒𝕤𝕤𝕖𝕤 ", callback_data="neon")],
            [KB(" ℕ𝕚𝕕𝕙𝕚 𝔸𝕔𝕒𝕕𝕖𝕞𝕪 ", callback_data="nidhi"), KB(" 𝕂𝔻 𝕃𝕀𝕍𝔼 ", callback_data="kd")],
            [KB(" ℙ𝕙𝕪𝕤𝕚𝕔𝕤 𝕎𝕒𝕝𝕝𝕒𝕙 ", callback_data="pw")],
            [KB(" 𝕋𝕒𝕣𝕦𝕟 𝔾𝕣𝕠𝕧𝕖𝕣 𝕊𝕚𝕣 ", callback_data="tarun")],
            [KB(" 𝕄𝕪 ℙ𝕒𝕥𝕙𝕤𝕒𝕝𝕒 ", callback_data="path"), KB(" ℂ𝕒𝕣𝕖𝕖𝕣𝕎𝕚𝕝𝕝 ", callback_data="careerwill")],
            [KB(" 𝕄𝕪 ℝ𝕚𝕤𝕚𝕟𝕘 𝕀𝕟𝕕𝕚𝕒 ", callback_data="rising")],
            [KB(" ℕ𝕦𝕣𝕤𝕚𝕟𝕘 ℕ𝕖𝕩𝕥 ", callback_data="nursing")],
            [KB("⏩ Next Page ➡️", callback_data="ext_page_1")]
        ]
    elif page == 2:
        keyboard = [
            [KB("ᎯᏝᏝᎬᏁ ᏁᎬᏯ 𝔙2 ", callback_data="allenv2")],
            [KB(" ᎯᏝᏝᎬᏁ ᎨᏁᏕᎿᎨᎿᏬᎿᎬ", callback_data="allen")],
            [KB(" ᎨᎰᎯᏕ ᎯᏨᎯᎠᎬᎷᎽ ", callback_data="ifas"), KB(" ICS ᏨᎾᎯᏨᎻᎨᏁᎶ", callback_data="ics")],
            [KB(" ᏕᎯᏁᏕᏦᏒᎨᎿᎨ IAS ", callback_data="rising")],
            [KB(" ᏁᏬᏒᏕᎨᏁᎶ ᏁᎬᎲᎿ", callback_data="nursing")],
            [KB(" ᏕᎿᏬᎠᎽ IQ ", callback_data="iq"), KB(" ᏬᎿᏦᎯᏒᏕᎻ ", callback_data="utk")],
            [KB(" ᎰᎾᏒᏬᎷ IAS ", callback_data="forum")],
            [KB(" ᏉᎨᏕᎨᎾᏁ IAS ", callback_data="vision")],
            [KB(" ᎨᏁᏕᎨᎶᎻᎿ IAS ", callback_data="insight"), KB(" ᏉᎯᏠᎨᏒᎯᎷ IAS ", callback_data="vajiram")],
            [KB(" ᏕᏬᏁᎽᎯ IAS ", callback_data="sunya")],
            [KB(" ᏝᎬᏉᎬᏝ UP IAS ", callback_data="level")],
            [KB(" ᏁᎬᎲᎿ IAS ", callback_data="next"), KB("🔧 MadeEasy 🔧", callback_data="madeeasy")],
            [KB(" ᏯᎬᏰᏕᎯᏁᏦᏬᏝ ", callback_data="webs")],
            [KB(" AlᏝ ᏕᏢᎯᎽᎬᎬ ᏯᎬᏰᏕᎨᎿᎬᏕ", callback_data="spayee")],
            [KB(" ᎠᏕᏝ ᏦᏒᎯᏁᎿᎨᏦᎯᏒᎨ", callback_data="dsl")],
            [KB("🔙 Back Page ⬅️", callback_data="ack_page_2"), KB("🏠 Home 🏠", callback_data="home"), KB("➡️ Next Page ➡️", callback_data="ext_page_2")]
        ]
    elif page == 3:
        keyboard = [
            [KB("𝘼𝙥𝙥𝙭 𝘼𝙡𝙡 𝘼𝙥𝙞 ( 𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="appxfree")],
            [KB("𝘼𝙙𝙙𝙖 24/7 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙇𝙤𝙜𝙞𝙣)", callback_data="addafree")],
            [KB("𝘼𝘽𝙃𝙄𝙉𝘼𝙑 𝙈𝘼𝙏𝙃𝙎  (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="abhinavfree")],
            [KB("𝘾𝘿𝙎 𝙅𝙤𝙪𝙧𝙣𝙚𝙮 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙇𝙤𝙜𝙞𝙣) ", callback_data="cdsfree")],
            [KB("𝘾𝙡𝙖𝙨𝙨𝙋𝙡𝙪𝙨 (𝙊𝙧𝙜 𝘾𝙤𝙙𝙚 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="cpfree")],
            [KB("𝘼𝙬𝙖𝙙𝙝 𝙊𝙟𝙝𝙖 𝙎𝙞𝙧 (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="awadhfree")],
            [KB("𝙆𝙝𝙖𝙣 𝙎𝙞𝙧 (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="khanfree")],
            [KB(" 𝙄𝘾𝙎 𝘾𝙤𝙖𝙘𝙝𝙞𝙣𝙜 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙇𝙤𝙜𝙞𝙣) ", callback_data="icsfree")],
            [KB(" 𝙄𝙁𝘼𝙎 𝘼𝙘𝙖𝙙𝙚𝙢𝙮 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙇𝙤𝙜𝙞𝙣) ", callback_data="ifasfree")],
            [KB(" 𝙁𝙤𝙧𝙪𝙢 𝙄𝘼𝙎 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙏𝙤𝙠𝙚𝙣) ", callback_data="forumfree")],
            [KB(" 𝙅𝙍𝙁 𝘼𝙙𝙙𝙖 (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙)", callback_data="jrffree")],
            [KB(" 𝙈𝙮 𝙋𝙖𝙩𝙝𝙨𝙖𝙡𝙖 (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="pathsalafree")],
            [KB(" 𝙋𝙝𝙮𝙨𝙞𝙘𝙨 𝙒𝙖𝙡𝙡𝙖𝙝 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙏𝙤𝙠𝙚𝙣) ", callback_data="pwfree")],
            [KB(" 𝙌𝙪𝙖𝙡𝙞𝙩𝙮 𝙀𝙙𝙪𝙘𝙖𝙩𝙞𝙤𝙣 (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="qualityfree")],
            [KB(" 𝙎𝙩𝙪𝙙𝙮 IQ (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="iqfree")],
            [KB(" 𝙎𝙪𝙣𝙮𝙖 IAS (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="sunyafree")],
            [KB(" 𝙏𝙚𝙨𝙩 𝙋𝙖𝙥𝙚𝙧 (𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="testpaperlivefree")],
            [KB(" 𝙏𝙚𝙨𝙩𝘽𝙤𝙤𝙠 (𝘼𝙣𝙮 𝙍𝙖𝙣𝙙𝙤𝙢 𝙇𝙤𝙜𝙞𝙣) ", callback_data="testbookfree")],
            [KB("  𝙑𝙚𝙧𝙗𝙖𝙡 𝙈𝙖𝙩𝙝𝙨(𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙍𝙚𝙦𝙪𝙞𝙧𝙚𝙙) ", callback_data="verbalfree")],
            [KB("🔙 Back Page ⬅️", callback_data="ack_page_3"), KB("❌ Close ❌", callback_data="close"), KB("🏠 Home 🏠", callback_data="home")]
        ]
    return KM(keyboard)


def home():
    keyboard = [
        [KB("🌟 VIP (Normal App) 🤖", callback_data="page_1"), KB("🚀 PRO (Special App) 🚀", callback_data="page_2")],
        [KB("⚡ Legend (No Login Required) ⚡", callback_data="page_3")],
        [KB("❌ Close ❌", callback_data="close")]
    ]
    return KM(keyboard)