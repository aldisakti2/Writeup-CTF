#!/usr/bin/env python3
import blacklist  # you don't get to see this :p

print("Pybidden: python with forbidden function(s)")
while True:
    try:
        command = input(">>> ")
        if any([x in command for x in blacklist.BLACKLIST]):
            raise Exception("not allowed!!")

        final_cmd = """d651a39ca = getattr(__import__('base64'), 'b64decode')\n""" + command
        
        exec(final_cmd)

    except (KeyboardInterrupt, EOFError):
        break
    except Exception as e:
        print(f"Exception: {e}")
