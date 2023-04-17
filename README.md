This script can run by itself however I set it up so that an executable was generated after running specific terminal commands. 

pyinstaller --onefile --windowed --icon=icon.icns --add-data "/Library/Frameworks/Python.framework/Versions/3.10/lib/tcl8.6:tcl8.6" --add-data "/Library/Frameworks/Python.framework/Versions/3.10/lib/tk8.6:tk8.6" BMRegex.py

To use the above command, you have to install pyinstaller via terminal. 

pip install -U pyinstaller or pip3 install -U pyinstaller

Since Tkinter isn't a natively supported package on end users' computers, it's important to include it within the pyinstaller command. You can find needed frameworks by the error the application will throw. From there, you can navigate to the pathname "/Library/Frameworks/Python.framework/Versions/3.10/lib" (this will differ per computer/version) and locate the folders that you need to include in the --add-data command option. 