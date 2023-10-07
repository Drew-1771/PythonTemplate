# PythonTemplate
This repository contains scripts to manage python environments.

## make_env.bat
This script generates a **basic** python virtual environment inside the current folder. Once a virtual environment is created, it cannot be easily moved, so it is intended you move this script to the desired folder where you want your environment to reside.

## activate.bat
This script is a 1 click activation of the above environment. Should reside next to the env folder.

## conda_create.bat
This script generates a **conda** virtual environment inside the current folder. Once a virtual environment is created, it cannot be easily moved, so it is intended you move this script to the desired folder where you want your environment to reside.

## conda_activate.bat
This script is a template for 1 click activation of a conda virtual environment. The format is below:

**start "Anaconda Prompt" cmd /k "\<anaconda_install_dir\>\Scripts\activate.bat" \<env_dir>**

_Replace the \<anaconda_install_dir\> with where you installed anaconda_

_Replace the \<env_dir> with the desired environment directory you want to activate_

## conda_activate example
I have installed miniconda3 to **C:\Users\Rupert\miniconda3**. I found this information by using the command "conda info" in cmd prompt and looked at the **base environment** variable. I use the command "conda env list" in cmd prompt and see the environment I want to activate is located at **E:\Stuff\MoreStuff\env**. I would then change my conda_activate.bat to the following:

**start "Anaconda Prompt" cmd /k ""C:\Users\Rupert\miniconda3\Scripts\activate.bat" E:\Stuff\MoreStuff\env**"
