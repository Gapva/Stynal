![stynalSplashBevel](https://github.com/Gapva/Stynal/assets/90116898/71cb1e33-c1a1-42de-872e-a3fe44874cb4)
*[Signal](https://signal.org/), but ✨ stylish ✨*

# Overview
https://github.com/Gapva/Stynal/assets/90116898/0d632eba-426d-4225-b477-f072c9f074fa

# Installation
Prerequisites
- The latest [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- - This is optional if you want to [download the repository yourself](https://github.com/Gapva/Stynal/releases/latest/Stynal.zip) and extract it

Clone the repository
> (Optional if you downloaded the repository yourself and extracted it)
```console
git clone Gapva/Stynal
```

Navigate to wherever you cloned Stynal, then to the `cli` subfolder
> (Alternatively, you can navigate to the extracted directory in a file manager)
```console
cd Stynal
cd cli
```

Install the required dependencies using PIP (pre-packaged with Python)
> (If you do not have a terminal interface open yet, you will need to open one to complete this step)
```console
pip install -r requirements.txt
```

Run Stynal
```console
python stynal.py --help
```

At this point, you are finished with the required setup.  
For something more convenient, you should add the Stynal directory to your `PATH` environment variable.  
If done correctly, you should be able to just run `stynal.py --help` (or any other Stynal command) from anywhere on your system.  
I will not be providing extensive documentation on how to do this, but you can find out how from these resources:
- [Windows](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho)
- [Linux](https://phoenixnap.com/kb/linux-add-to-path)
- [Mac](https://stackoverflow.com/questions/22465332/setting-path-environment-variable-in-osx-permanently)

Alternatively, you can edit your Powershell `$PROFILE`. [Install Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.4) on any OS if you haven't already.  
To do so, check that it exists. It probably doesn't, but try opening it in `notepad` (or whatever text editor you prefer) to be safe, as shown below.
```console
notepad $PROFILE
```
If it fails, you can create your `$PROFILE` by running the below command.
```console
New-Item -ItemType File -Path $PROFILE -Force
```
Now that it is created, repeat the previous step to open it in your preferred text editor.

Paste the following information into the file, and make necessary changes:
```ps1
function stynal {
  $stynalPath = "A:\path\to\Stynal\cli\stynal.py" # EDIT THIS TO REFLECT THE ACTUAL STYNAL PATH
  & python $stynalPath @args
}
```

Save the script and restart Powershell to apply changes. 🎉

# Finding Themes
You can find (and contribute to) a list of themes [here](https://github.com/Gapva/stynal-themes).

# Updating
You can update Stynal by navigating to wherever you have its master branch installed, and pulling changes.
```console
cd path\to\Stynal
git pull
```
