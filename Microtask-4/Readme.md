# Microtask-4
Set up a dev environment to work on GrimoireLab. Have a look to https://github.com/chaoss/grimoirelab-sirmordred#setting-up-a-pycharm-dev-environment.

# Procedure
* Fork all the given repos.
* For every repo forked (say fork_repo)
  * ```git clone https://github.com/abhiandthetruth/fork_repo.git```
  * ```cd fork_repo```
  * ```git remote add upstream https://github.com/{org}/fork_repo.git```
  where the ```org``` refers to the owner of forked repo, it is either ```chaoss``` or ```bitergia```.
* Now open a new pycharm project in the ```grimoirelab-sirmordred``` folder. If asked whether to use existing resources, decline it. A virtual environment should be created.
* Open the integrated terminal. Go to each ```repo/requirements.txt```, where ```repo``` is a place holder for the forked repo's name and comment out or delete the grimoirelab components requirement, all are prefixed with the editable mode option ```-e```. You can install each component later by going into the respective folder and running ```python3 setup.py install```.
* Install from each ```requirements.txt``` by running ```pip3 install -r requirements.txt``` in the respective folders.
* You can add the grimoire components via File -> Settings -> Project -> Project Structure. Click the ```+``` and select the corresponding folder. Do this for all folders. 

# Result

* Set up Finished. You can now run micro-mordred or p2o whatever you want.

# Attachments
  
