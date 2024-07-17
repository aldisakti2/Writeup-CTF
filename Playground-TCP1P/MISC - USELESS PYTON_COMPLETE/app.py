#!/bin/python3
import re

BLACKLIST = r" |__|\(|\)|globals|system|import|builtins|sub|eval|exec|compile|locals|vars|open|file|input|subprocess|os|sys|shutil|popen|system|commands|ctypes|f_locals|frame|traceback|dir|getattr|setattr|delattr|code|marshal|base64|pickle|chr|ord|format|replace|re|sre_|search|match|findall|finditer|compile|escape|purge|findall|finditer|sub|subn|split|findall|finditer|purge|template|Scanner|Pattern"

if text := input("input: "):
    if re.search(BLACKLIST, text, re.DOTALL):
        print("Blacklist detected!")
        exit(1)
    exec(text, {"__builtins__": {}})

print("goodbye!")
