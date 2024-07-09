import os


def run_cmd(command):
    cmd = command.split()[0]
    flags = []
    
    match cmd:
        case "cd":
            os.chdir(cmd[1])
        case _:
            sys.