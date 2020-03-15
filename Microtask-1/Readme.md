!! Intentionally uploaded venv folder to show succesful installation of perceval !!
# Microtask-1
Set up Perceval to be executed from PyCharm.

## Procedure
There are two ways:

### For end users
1. Create a virtual environment. Not necessary but recommended. PyCharm automatically creates one. `Pycharm -> New Project`.
2. `pip3 install perceval` Use pip if you don't have pip3.
3. You can now import perceval and its backends now.

### For Developers
1. Create a virtual environment. Not necessary but recommended. PyCharm automatically creates one. `Pycharm -> New Project`.
2. Fork https://github.com/chaoss/grimoirelab-perceval. Clone your fork in your loacal machine.
3. Add upstream to original repo. `git remote add upstream https://github.com/chaoss/grimoirelab-perceval.git`.
4. Add the directory to your project. `File -> Settings -> Project -> Project Structure -> Add content root`, select the directory in this menu which contains the clone of your fork of perceval. Then confirm the addition
3. You can now import perceval and its backends now.

## Result
perceval setted up!!

## Attachments
![Image-perceval-user](/Microtask-1/Microtasks1.png)
![Image-perceval-dev](/Microtask-1/perceval-dev.png)
