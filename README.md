# shape-classifier-pytorch

## We must tell them to have the required pythoin version installed on their system
See python_version = "3.12" in the Pipfile and automatically use Python 3.12 if it's available on their system.

## We will recomment to use pipenv for smooth installs, or use their prefered virt env manager with the required python version and the requirements.txt file.
Exactly. The README.md will have a section like "Alternative Setup (using venv or conda)" which will instruct them to first create their virtual environment ensuring it uses Python 3.12, and then run pip install -r requirements.txt. This covers all bases.

## Running the Download Script
You are 100% right. The download_artifacts.py script will import the huggingface-hub library. That library will only be available inside our activated virtual environment. Therefore, the instruction must be to run it from the activated environment. This avoids any potential ModuleNotFoundError.

### How a New User Will Use This

This is the beautiful part. Here are the instructions you would put in your `README.md` for a new user:

**1. Prerequisites:**
   You must have `git` and `git-lfs` installed. To install Git LFS:
   ```bash
   # Install on Debian/Ubuntu
   # sudo apt-get install git-lfs

   # Install on macOS with Homebrew
   # brew install git-lfs
   
   # **On Windows:** The Git for Windows installer typically includes an option to install Git LFS. You can also download it directly from [https://git-lfs.github.com/](https://git-lfs.github.com/) and run the installer.
   
   # After installing, you must run this command ONCE per machine:
   git lfs install
   ```

**2. Clone the Project:**
   ```bash
   git clone https://github.com/[Your-GitHub-Username]/shape-classifier-pytorch.git
   cd shape-classifier-pytorch
   ```

**3. Download the Dataset and Models:**
   Run the download script from the project's root directory.
   ```bash
   ./download_artifacts.sh
   ```

That's it! The user runs one command, and the script handles the rest, ensuring the `../shape-classifier-artifacts` directory is created and populated correctly.

### Final Step: Version Control Your New Script

Don't forget to add this new downloader script to your GitHub repository.

1.  From your Git Bash terminal (in `shape-classifier-pytorch/`), run:
    ```bash
    git add download_artifacts.sh
    git commit -m "Add script to download/update HF artifacts for new users"
    git push
    ```

You now have a complete, professional workflow: one script for you (the maintainer) to **push** changes, and another script for your users to easily **pull** them. This is a fantastic setup.

