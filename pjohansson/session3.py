import os

class CourseRepo(object):
    """A class for the structure of the course repository."""

    def __init__(self, surname):
        self.surname = surname

    @property
    def required(self):
        """Required files in repository directory structure."""

        return ['.git', 'setup.py',
                'scripts/getting_data.py', 'scripts/check_repo.py',
                self.surname + '/__init__.py', self.surname + '/session3.py'
                ]

    def check(self):
        """Control if all required files present in repository."""

        for file in self.required:
            if not os.path.exists(file):
                return False

        return True

class RepositoryDirectory(object):
    """Switches to a repository directory."""

    def __init__(self, path):
        self.current = os.getcwd()
        self.path = path

    def __enter__(self):
        os.chdir(self.path)

    def __exit__(self, type, value, traceback):
        os.chdir(self.current)
