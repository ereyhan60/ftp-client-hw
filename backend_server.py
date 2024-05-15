from ftplib import FTP

class FTPServer:
    def __init__(self):
        self.ftp = FTP()

    def login(self, hostname, port, username, password):
        try:
            self.ftp.connect(hostname, port)
            self.ftp.login(username, password)
            print("Successfully logged in to FTP server.")
        except Exception as e:
            print(f"Failed to login: {e}")

    def navigate(self, remote_path):
        try:
            self.ftp.cwd(remote_path)
            print(f"Remote directory changed to {remote_path}")
        except Exception as e:
            print(f"Failed to navigate remote directory: {e}")

    def list_directory(self):
        try:
            data = []
            self.ftp.dir(data.append)
            for line in data:
                print(line)
        except Exception as e:
            print(f"Failed to list remote directory: {e}")

    def download(self, remote_path, local_path):
        try:
            with open(local_path, 'wb') as local_file:
                self.ftp.retrbinary('RETR ' + remote_path, local_file.write)
            print(f"Downloaded file {remote_path} to {local_path}")
        except Exception as e:
            print(f"Failed to download file: {e}")

    def upload(self, local_path, remote_path):
        try:
            with open(local_path, 'rb') as local_file:
                self.ftp.storbinary('STOR ' + remote_path, local_file)
            print(f"Uploaded file {local_path} to {remote_path}")
        except Exception as e:
            print(f"Failed to upload file: {e}")

    def rename(self, old_name, new_name):
        try:
            self.ftp.rename(old_name, new_name)
            print(f"Renamed {old_name} to {new_name}")
        except Exception as e:
            print(f"Failed to rename file: {e}")

    def delete(self, filename):
        try:
            self.ftp.delete(filename)
            print(f"Deleted file {filename}")
        except Exception as e:
            print(f"Failed to delete file: {e}")

    def close(self):
        try:
            self.ftp.quit()
            print("Connection to FTP server closed.")
        except Exception as e:
            print(f"Failed to close connection: {e}")
