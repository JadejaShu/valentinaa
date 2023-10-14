# .
# Please Don't remove credit.
# 
#Share Us R_MvzZ 
# 🥰  Thank you for giving me r  🥰
# for any error please contact me -> Telegram:- @R_MvzZ Join:- @REQUEST_MOvizZ 
# rip paid developers 🤣 - >> No need to Join telegram:- @R_MvzZ 😍😍
def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'
