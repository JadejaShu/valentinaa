# .
# Please Don't remove credit.
# 
#Share Us R_MvzZ 
# 🥰  Thank you for giving me r  🥰
# for any error please contact me -> Telegram:- @R_MvzZ Join:- @REQUEST_MOvizZ 
# rip paid developers 🤣 - >> No need to Join telegram:- @R_MvzZ 😍😍 
from os import environ
from typing import Dict, Optional


class TokenParser:
    def __init__(self, config_file: Optional[str] = None):
        self.tokens = {}
        self.config_file = config_file

    def parse_from_env(self) -> Dict[int, str]:
        self.tokens = dict(
            (c + 1, t)
            for c, (_, t) in enumerate(
                filter(
                    lambda n: n[0].startswith("MULTI_TOKEN"), sorted(environ.items())
                )
            )
        )
        return self.tokens
