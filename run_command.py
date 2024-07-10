import os
import shutil
import signal
import sys


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
                    os.chdir(str(" ".join(args)))
                except FileNotFoundError:
                    print("No such file or directory: " + ' '.join(args))
        case "exit":
            sys.exit(0)
        case "echo":  # cant be bothered to remove quotation marks from argument
            print(' '.join(flags+args))
        case "help" | "man":
            print("All shell builtins:")
            print("cd: change directory to specified directory")
            print("exit: exit the shell")
            print("echo: print text to screen")
            print("help: display this help message")
            print("pwd: print the current working directory")
            print("exec: replace shell with specified executable")
            print("type: display type of command")
        case "pwd":
            print(os.getcwd())
        case "exec":
            if len(args) > 0:
                try:
                    os.execvp(f"{args[0]}", (args))
                except FileNotFoundError:
                    print("No such file or directory: " + " ".join(args))
            print("No arguments supplied")
        case "type":
            if len(args) == 1:
                if (args[0]) in ["cd", "echo", "help", "pwd", "exit", "exec", "type"]:
                    print("builtin")
                elif shutil.which(args[0]):  # if None, will fail
                    print("executable file")
                else:
                    print("unknown type")
        case _:
            process = os.fork()
            signal.signal(signal.SIGINT, signal.default_int_handler)
            if process > 0:
                os.waitpid(0, 0)
            else:
                try:
                    try:
                        os.execvp(f"{cmd}", ([f"{cmd}"] + flags + args))
                    except FileNotFoundError:
                        print("No such file or directory: " + cmd)
                except KeyboardInterrupt:
                    return
