import sys, os, subprocess, re, shlex

VALID_DIRNAME = r"^[A-Za-z0-9 ._-]+"
OPTIONAL_SUBDIRECTORY = r"(?:/.*)?"
PLAIN_DIRNAME_FIRST_PATTERN = rf"^{VALID_DIRNAME}{OPTIONAL_SUBDIRECTORY}$"

bulitin_commands = ["echo", "exit", "type", "pwd", "cd"]
current_directory = os.getcwd()


def get_absolute_path(path: str):
    absolute_path = None

    # Expand leading '~' or '~user' to the user's home directory path from the HOME environment variable
    path = os.path.expanduser(path)

    if path.startswith("/") and os.path.isdir(path):
        absolute_path = path

    elif re.match(PLAIN_DIRNAME_FIRST_PATTERN, path) or path.startswith(("../", "./")):
        full_abs_path = os.path.abspath(os.path.join(current_directory, path))

        if os.path.isdir(full_abs_path):
            absolute_path = full_abs_path

    return absolute_path


def get_executable_path(command):
    env_path = os.environ.get("PATH")
    paths = env_path.split(os.pathsep)
    path_to_executable = None

    for path in paths:
        full_path = os.path.join(path, command)

        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            path_to_executable = full_path
            break

    return path_to_executable


def main():
    global current_directory
    global bulitin_commands

    while True:

        sys.stdout.write("$ ")
        user_input = input()

        if not user_input:
            continue

        command_name, *command_args = shlex.split(user_input)

        if ">" in user_input or "1>" in user_input:
            os.system(user_input)
            continue

        if command_name == "exit":
            break

        if command_name == "echo":
            print(*command_args)

        elif command_name == "type":
            subcommand_name = command_args[0]

            if subcommand_name in bulitin_commands:
                print(f"{subcommand_name} is a shell builtin")

            else:
                executable_path = get_executable_path(subcommand_name)

                if executable_path:
                    print(f"{subcommand_name} is {executable_path}")
                else:
                    print(f"{subcommand_name}: not found")

        elif command_name == "pwd":
            print(current_directory)

        elif command_name == "cd":
            path_arg = command_args[0]
            absolute_path = get_absolute_path(path_arg)

            if absolute_path:
                current_directory = absolute_path
            else:
                print(f"cd: {path_arg}: No such file or directory")

        elif command_name:
            executable_path = get_executable_path(command_name)

            if executable_path:
                subprocess.run([command_name, *command_args])
            else:
                print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()