# ADVANCED PYTHON CODE READER
This project was created with the aim of providing code and instructions useful for configuring the 'Visual Studio Code' editor for those who are visually impaired and wish to program in Python. The goal is to make code development more accessible to their needs. The code sources that will be mentioned in some steps are available in the 'files' folder.

What is presented is the result of the curricular internship of the student Mattia Donà (Degree in
Computer Science, University of Verona) with the supervision of prof. David Quaglia
(Departments of Computer Science, University of Verona), Manuela Boschiero (Department of
Foreign Languages and Literatures, University of Verona) and Marco Rospocher (Department of
Foreign Languages and Literatures, University of Verona).

# STEP 1: INSTALL A SCREEN READER

To start you need a screen-reader that reads the contents of the pages displayed on the screen through a synthesized voice. There are several depending on the operating system you have, here are some main examples:

   - MAC-OS -> VOICE-OVER : already present in apple devices, does not require download and installation, can be activated via Siri or command bar
                            (COMMAND+SPACE). Documentation link: https://support.apple.com/it-it/guide/voiceover/voic010/mac
                           
   - Windows -> NVDA: To download and install, download link: https://www.nvaccess.org/download/ , documentation link: https://www.nvda.it
  
   - Linux -> ORCA: already present in Linux operating systems, link to documentation: https://help.gnome.org/users/orca/stable/index.html.en

# STEP 2: INSTALL VISUAL STUDIO CODE

If you don't already have the 'Visual Studio Code' editor, you can download it in this step using the following link: https://code.visualstudio.com/download. Once downloaded, you will need to install and open it to continue.
It is highly recommended to use the editor mentioned above as the next steps will refer to it.

# STEP 3: INSTALL PYTHON IN VISUAL STUDIO CODE

Python is the language with which it will be possible to develop code in a more accessible way through this guide.

Here is an installation guide using the 'Visual Studio Code' editor.

   - Open Visual studio Code
   - On the left shoulder of the editor select the 'extensions' section
   - In the search field that appears type 'python'

  <img width="550" alt="Schermata 2023-03-09 alle 10 57 42" src="https://user-images.githubusercontent.com/63148243/223986978-ac0da31f-b163-403a-a2d6-0473c554d9f4.png">
  
   - If you have not yet installed it, the 'install' button will be visible, you will have to click on it
     it to start the installation
   - Wait for the installation, then close and reopen the editor
 
Then you will have to download and install the Python language interpreter, depending on your operating system you can find the most suitable version using the following link: https://www.python.org/downloads/

# STEP 4: ACTIVATE THE 'SCREEN READER OPTIMIZED' OPTION IN VISUAL STUDIO CODE

Once the screen reader is activated and 'Visual Studio Code' is opened, the next step will be to achieve a better interaction with the editor thanks to the activation of the 'screen reader optimized' mode.
  
   - Open the editor, on the left shoulder select the bottom section 'settings'
     ('manage')
   - From the drop-down menu items select 'settings'
   - In the search bar that will appear type 'screen reader'
   - An 'Editor: Accessibility Support' entry will appear
   - Set to 'on' if you want the editor to always be optimized for screen readers, or
     to 'auto' if you want it to be optimized only when it detects an active one.
    
<img width="550" alt="Schermata 2023-03-09 alle 11 11 01" src="https://user-images.githubusercontent.com/63148243/223990138-b505b015-d21c-46cd-80ad-0e1b6ea0d59a.png">

This option will allow easier movement within the editor and between the various sections, and will also add properties such as reading lines of code in full unlike normal screen readers, which tend to read text word by word .

# STEP 5: SAVE THE 'parser.py' FILE IN THE WORK DIRECTORY

Now on the editor workspace, create a new python file, copy the contents of the [parser.py](./files/parser.py) file.
This code developed by me allows you to have an advanced parsing of python code, so that the user can better understand how the code he wrote works, being able to listen to a more detailed reading of the construct he wants to know more about to the reading of the code as it is written proposed by its screen reader.
The way it works, without going into details, is that of having built 'triggers' which are activated every time it detects a main construct of the Python language (cycles, conditions, variables,...) and, for each of them, performs a certain planned action.
Basically all the triggers have the programmed action of inserting a sentence like "I read the variable 'a'" in a global string, or "I just read a for loop", so that this long string can then be read using a device such as a screen reader or speech synthesizer.

NOTES: The following libraries will be needed for parser.py to work:
   - 'ast': pre-installed from python 2.5 version -> parsing tree creation
   - 'pyttsx3': "pip install pyttsx3" -> speech synthesizer
   - 'tokenize': pre-installed from python version 2.2 -> being able to parse also
      comments within the code
   - 'io','os','sys' -> pre-installed python libraries
   - 
# STEP 6: CREATE A TASK IN VISUAL STUDIO CODE BY MODIFYING THE 'task.json' FILE

We create a 'Task', i.e. a series of events that are collected in a single action that we can invoke whenever we want. To do this, you need to follow the following steps on 'Visual Studio Code'.

  - On the screen where the file written in Python is displayed, type: CTRL+SHIFT+P (on MAC-OS: COMMAND+SHIFT+P)
  - The 'command bar' will open
  - Type in the bar 'Configure Tasks'
  - Select 'Tasks: Configure Tasks'
  - Click 'Create task.json file from template'

<img width="813" alt="Schermata 2023-03-13 alle 09 33 42" src="https://user-images.githubusercontent.com/63148243/224648133-274d5cd9-a4e0-4781-a252-3467b22e6dfe.png">

The 'task.json' file will open. If desired, the content present in the file can be eliminated, it will not be useful for the end of the project. Copy the code from the file in [task.json](./files/task.json) into 'task.json'.

Now a Task has been created in the editor that executes 'parser.py' and takes as argument the name of the file we want to perform an advanced parsing of a given line of code.

# STEP 7: CREATE A SHORTCUT TO RUN THE ADVANCED PARSER

Let's create a combination of hotkeys that will invoke the Task created in the previous step.
Still within 'Visual Studio Code' we must proceed as follows:
  - On the screen where the file written in python is present, type CTRL+SHIFT+P (on MAC-OS: COMMAND+SHIFT+P)
  - The 'command bar' will open
  - Type in the 'Open Keyboard Shortcuts' bar
  - Select the item: 'Preferences: Open Keyboard ShortCuts(JSON)'

<img width="624" alt="Schermata 2023-03-09 alle 11 58 46" src="https://user-images.githubusercontent.com/63148243/224004192-7853a33c-abf1-43e6-9680-61947f7b5d2f.png">


The 'keybindings.json' file will open which allows you to associate an event with a series of keys, copy the contents of the file inside [keybindings.json](./files/keybindings.json)

It is possible to set different key combinations, the only suggestion is not to set key combinations corresponding to other keyboard-shortcuts.

# CONCLUSIONS

Now you can create python code, highlight a portion of the code with the cursor, click the key combination CTRL+SHIFT+X to listen to an advanced reading of the piece of python code.

Program Limits:

  - Currently the program is not able to parse all python constructs, but it is possible to implement them in the code once you understand the logic of its operation. Therefore, the main constructs used in programming Python code are present.
   
  - It is necessary to highlight a construct with the cursor in its entirety for advanced parsing to be performed successfully, otherwise the parser will respond with a generic error.

 - To see which constructs the code currently covers see the file [implementations.md](./implementations.md)
