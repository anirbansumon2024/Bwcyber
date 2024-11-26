import subprocess
import sys
import time

# List of packages you want to install
packages = ["pyfiglet", "colorama", "termcolor","rich","tqdm","progressbar2"]

# Run pip install for each package
subprocess.check_call([sys.executable, "-m", "pip", "install"] + packages)


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')

# Simulate progress
total = 100
for i in range(total + 1):
    time.sleep(0.05)
    print_progress_bar(i, total, prefix='Proccesing', suffix='Complete', length=50)

