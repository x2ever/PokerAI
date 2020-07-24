"""Test Module with sigle file during developing"""
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def search(test_path):
    """
    Get every python file's path
    """
    temp = list()
    for paths, _, file_names in os.walk(test_path):
        for file_name in file_names:
            ext = os.path.splitext(file_name)[-1]
            if ext == '.py':
                temp.append("%s\\%s" % (paths, file_name))
    return temp


if __name__ == "__main__":
    TEST_PATH = 'gym_poker'
    TEST_FILES = search(TEST_PATH)
    # install development dependency
    print(bcolors.HEADER + "install development dependency" + bcolors.ENDC)
    os.system('%s %s' % (sys.executable, '-m pip install -r requirements.txt'))
    # install module
    print(bcolors.HEADER + "installing gym_poker module" + bcolors.ENDC)
    os.system('%s %s' % (sys.executable, '-m pip install -e .'))
    # lint test
    print(bcolors.HEADER + "Lint test" + bcolors.ENDC)
    os.system('%s %s %s' % (sys.executable, '-m pylint', TEST_PATH))
    # run test
    print(bcolors.HEADER + "Running test" + bcolors.ENDC)
    for test_file in TEST_FILES:
        os.system('%s %s' % (sys.executable, test_file))

    print(bcolors.OKGREEN + "The testing is done. Check the result." + bcolors.ENDC)