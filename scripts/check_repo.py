"""Script that checks if a repository has the required files."""

from pjohansson.session3 import CourseRepo, RepositoryDirectory
import sys

full_path = sys.argv[1]

(repository, surname) = full_path.rstrip('/').rsplit('/', 1)

with RepositoryDirectory(repository):
    repo = CourseRepo(surname)
    if repo.check():
        print "TRUE"
    else:
        print "FALSE"
