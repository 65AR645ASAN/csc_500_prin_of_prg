import os
import subprocess


def check_anaconda():
    try:
        # Check if conda is in the PATH
        subprocess.run(["conda", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Anaconda is installed.")
    except FileNotFoundError:
        print("Anaconda is not installed or not in the PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

    # Check if Anaconda environment variables are set
    anaconda_env_var = os.getenv('CONDA_PREFIX')
    if anaconda_env_var:
        print(f"Anaconda environment detected: {anaconda_env_var}")
    else:
        print("Anaconda environment variables are not set.")


if __name__ == "__main__":
    check_anaconda()
