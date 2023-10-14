# .
# Please Don't remove credit.
# 
#Share Us R_MvzZ 
# 🥰  Thank you for giving me r  🥰
# for any error please contact me -> Telegram:- @R_MvzZ Join:- @REQUEST_MOvizZ 
# rip paid developers 🤣 - >> No need to Join telegram:- @R_MvzZ 😍😍
def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of bytes """
    return str(bytes) + units[0] if int(bytes) < 1024 else human_size(int(bytes)>>10, units[1:])
