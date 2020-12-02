class RealFileSystem:

    def __init__(self, context):
        self.context = context

    def get_files(self, path: str):
        pass  # use requests library to get the actual list of files for a path

    def get_directories(self, path: str):
        pass  # use requests library to get the actual list of directories for a path

    def pwd(self):
        pass  # use requests library to get the current working directory for the real file system

    def clear_the_test_bucket(self):
        pass  # use requests library to clear the file system / recreate the bucket
