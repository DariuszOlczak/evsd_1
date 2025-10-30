Just in case, Steps to follow with github repository clonning and virtual environment set up. I checked it on a different PC (Windows OS, Project so far developed in Linux environment) and everything works. At the moment only working in Jupyter notebook where I test functions (queries).
(Linux, Git Bash commands):
-Got to directory where project clone will be created:
git clone https://github.com/DariuszOlczak/evsd_1.git

-After project is cloned, go to project directory and create virtual environment 
python -m venv venv

-Activate this environment (needs to be created once but activated every single time to allow libraries to run)
source venv/bin/activate

-Install required libraries from requirements.txt provided in project files
pip install -r requirements.txt

-to start new branch and commit
git checkout -b feature/your feature
git add.
git commit -m “changes applied”
git push -u origin feature/your feature
login: gitlogin
password: generated token

Might need to update libraries in IDE separately but this one is standard update.
