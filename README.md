#Disclaimer

This project involves writing bypasses for Windows Defender. All actions performed within this code are intended for learning and experimentation purposes only.

Any use of the main script or any other code within this repository should be exclusively for learning purposes. The author is not responsible for any misuse of the project.
#General Info

This repository currently contains the main.py code.

The Python script will:

    Install the GitPython library using pip.
    Add GitPython to the environment variables.
    Create a folder with the project name, date, and a unique name.
    Attempt to pull Mimikatz and execute it.
    If successful, a message will indicate that the file was successfully used.

Additionally, the script will dump all folder and file names into a text file for enumeration outside of the current machine.
#Future Actions

The code will be organized into the following folders:

    main: General build, Python downloader, and a command-based script.
    actions: Files that can activate multiple actions, either by calling them using a command or directly from main.
    pulls: Files to be pulled using GitPython to continue the actions performed by the main script.
