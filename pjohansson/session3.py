import os

class CourseRepo(object):
    """A class for the structure of the course repository."""

    def __init__(self, surname):
        self.surname = surname

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, new_surname):
        """Set surname and update .required list."""
        self._surname = new_surname
        self.required = [
                '.git', 'setup.py', 'README.md',
                'scripts/getting_data.py', 'scripts/check_repo.py',
                self._surname + '/__init__.py', self._surname + '/session3.py'
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
