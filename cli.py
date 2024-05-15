import cmd, shlex, os
from backend_server import FTPServer

class FTPClientCLI(cmd.Cmd):
    prompt = 'FTP Client > '

    def __init__(self, server):
        super().__init__()
        self.server = server

    def do_login(self, args):
        try:
            host, port, username, password = args.split()
            port = int(port)
            self.server.login(host, port, username, password)
        except ValueError:
            print("Usage: login <host> <port> <username> <password>")
        except Exception as e:
            print(f"Error during login: {e}")

    def do_cd(self, args):
        try:
            parsed_args = shlex.split(args)
            if len(parsed_args) != 1:
                raise ValueError()
            remote_path = parsed_args[0]
            self.server.navigate(remote_path)
        except ValueError:
            print("Usage: cd <remote_directory>")

    def do_ls(self, args):
        self.server.list_directory()

    def do_get(self, args):
        try:
            parsed_args = shlex.split(args)
            if len(parsed_args) != 2:
                raise ValueError()
            remote_path = parsed_args[0]
            local_path = parsed_args[1]
            self.server.download(remote_path, local_path)
        except ValueError:
            print("Usage: get <remote_file_path> <local_file_path>")

    def do_put(self, args):
        try:
            parsed_args = shlex.split(args)
            if len(parsed_args) != 2:
                raise ValueError()
            local_path = parsed_args[0]
            remote_path = parsed_args[1]
            local_path = os.path.abspath(local_path)
            self.server.upload(local_path, remote_path)
        except ValueError:
            print("Usage: put <local_file_path> <remote_file_path>")

    def do_rename(self, args):
        try:
            parsed_args = shlex.split(args)
            if len(parsed_args) != 2:
                raise ValueError()
            old_name = parsed_args[0]
            new_name = parsed_args[1]
            self.server.rename(old_name, new_name)
        except ValueError:
            print("Usage: rename <old_file_name> <new_file_name>")

    def do_delete(self, filename):
        try:
            self.server.delete(filename)
        except ValueError:
            print("Usage: delete <file_name>")

    def do_exit(self, args):
        self.server.close()
        return True

    def help_login(self):
        print("Usage: login <host> <port> <username> <password>")
        print("Log in to the FTP server.")

    def help_cd(self):
        print("Usage: cd <remote_directory> | cd \"<remote_directory containing whitespaces>\"")
        print("Change directory on the FTP server.")

    def help_ls(self):
        print("Usage: ls")
        print("List files and directories in the current remote directory.")

    def help_get(self):
        print("Usage: get <remote_file_path> <local_file_path> | get <remote_file_path> \"<local_file_path containing whitespaces>\"")
        print("Download a file from the FTP server to the local machine.")

    def help_put(self):
        print("Usage: put <local_file_path> <remote_file_path> | put \"<local_file_path containing whitespaces>\" <remote_file_path>")
        print("Upload a file from the local machine to the FTP server.")

    def help_rename(self):
        print("Usage: rename <old_file_name> <new_file_name> | rename \"<old_file_name containing whitespaces>\" \"<new_file_name containing whitespaces>\"")
        print("Rename a file on the FTP server.")

    def help_delete(self):
        print("Usage: delete <file_name> | delete \"<file_name containing whitespaces>\"")
        print("Delete a file from the FTP server.")

    def help_exit(self):
        print("Usage: exit")
        print("Exit the FTP client.")


print("Remember to use \"help\" command to get information about built-in commands.")
ftp_server = FTPServer()
cli = FTPClientCLI(ftp_server)
cli.cmdloop()
