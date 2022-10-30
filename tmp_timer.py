import msvcrt
import time
import sys

class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) # just to yield to other processes/threads
    raise TimeoutExpired

while 1:
    try:
        time_to_decide = 5
        prompt = f'interrupt processing ? ({time_to_decide} sec to answer) \n'
        answer = input_with_timeout(prompt, time_to_decide)
    except TimeoutExpired:
        print(' process, will continue....')
    else:
        if answer == 'y':
            print ('bye.')
            sys.exit(0)