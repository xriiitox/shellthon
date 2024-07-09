import os
import signal


def run_cmd(command):
    command = command.split()
    cmd = ""
    flags = []
    args = []
    for i in range(0, len(command)):
        if i == 0:
            cmd = command[i]
        elif command[i][0] == '-':
            flags.append(command[i])
        else:
            args.append(command[i])

    """
    this match statement checks for shell builtins and if it is not a shell builtin, forks and runs the exe with execv
    if it exists in /usr/bin
    """
    match cmd:
        case "cd":
            if not args:
                os.chdir(f'/home/{os.getlogin()}')
            else:
                try:
                    os.chdir(str(args[0]))
                except FileNotFoundError:
                    print("No such file or directory: " + args[0])
        case _:
            processid = os.fork()
            signal.signal(signal.SIGINT, signal.default_int_handler)
            if processid > 0:
                os.waitpid(0, 0)
            else:
                try:
                    try:
                        os.execv(f"/usr/bin/{cmd}", ([f"/usr/bin/{cmd}"] + flags + args))
                    except FileNotFoundError:
                        print("No such file or directory: " + cmd)
                except KeyboardInterrupt:
                    return
