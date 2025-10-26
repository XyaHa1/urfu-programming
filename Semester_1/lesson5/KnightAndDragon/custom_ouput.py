import time


def custom_output(msg):
    for ch in msg:
        print(ch, end="", flush=True)
        time.sleep(0.05)
    print(flush=True)
