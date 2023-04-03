# VanProj

A place to collect all of the code used for various van-related projects. Current projects include:
 - **graph2.py:** Making use of plotly to graph variables such as voltage against time. Reads from .csv files storing the data.


## First steps
### Cloning the repo
To get the repo on to your computer, type the following commands into the directory in which you would like this repo to exist:

```bash
git clone https://github.com/jamesdidathing/vanproj.git
```
### Setting up your environment
Create a virtual environment in which you can develop in:

```bash
pip install virtualenv 
python -m pip virtualenv venv
source venv/bin/activate
``` 
You should now be in your virtual environment (venv). To install the modules that this repo requires:
```bash
pip install -r requirements.txt
``` 

## Using Git

With the repo cloned, and your virtual environemnt made, some basic commands for using Git are:

```
git status                      # Tells you which branch you are on, what files have been modified and what changes are "staged"
git add 'filename'              # Stages the file for commit. Do this when you've made a change you would like to push back to the repo
git commit -m "message here"    # Commits the changes with the message. Message should be what the change has done
git push origin main            # Will push the changes you have committed to the 'main' repo branch
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.