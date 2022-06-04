# Sound Transformations Application

Project description
----------
The purpose of the project is to build a standalone application software that can be executed to 
make sound transformations with intuitive interfaces. Those interfaces will tend to ensure facility 
for the user to make the sound transformations and modifications without a huge background knowledge 
of sound processing. The transformations that our application will focus on are equalization, pitch 
shifting and time stretching.


How to Install and Run the Project
----------

In order to use these tools you have to install Python 3.8.x (recommended) and the following modules: 
ipython, numpy, matplotlib, scipy, cython and sounddevice.

Regarding the visualization and edition of the code, you might need to install a python integrated 
development environment such as PyCharm Community where you will need to configure the interpreter 
to Python 3.8 and after that you should install all the modules mentioned before. 

In Ubuntu (which we strongly recommend) in order to install all these modules it is as simple as typing
in the Terminal:

<code>$ sudo apt-get install python-dev ipython python-numpy python-matplotlib python-scipy cython</code>

In OSX (which we do not support but that should work) you install these modules by typing in the Terminal:

<code>$ pip install ipython numpy matplotlib scipy cython</code>

then, for using the software, after downloading the whole package, you need to compile some C functions. 
For that you should go to the directory <code>Functions/models/utilFunctions_C</code> and type:</p>

<code>$ python3 compileModule.py build_ext --inplace </code>

The basic sound analysis/synthesis functions, or models, are in the python archive <code>main.py</code>. 
To execute the application you have to go to the directory where the <code>main.py</code> file is and type: 

<code>$ python3 main.py </code>


How to Use the Application
-------
As a user you will enter to the equalizer interface as soon as you execute the application. 
Once you are inside the application, you are able to get around all transformations and switch 
between them by clicking the labeled buttons (left side of the interface). Our software is implemented 
in order to work offline without the need of internet connection. Sounds need to be stored in the 
system/computer before starting the development process, the application is thought to not be in 
real-time.

This app does not require authentication like passwords or usernames.

Code Content
-------

The project is structured in different folders.
On one hand, there is this folder called <code>Functions</code> where it can be found most of the 
coding part with its corresponding subdirectories for the <code>models</code> functions, the 
<code>transformations</code>, and the <code>GUIs</code> with all the interfaces' code. On the other 
hand, there is another folder called <code>sounds</code> in order to have some trial sounds and be 
able to play with the sound transformations. These sounds are split up among two folders: band playing 
and instrument sounds, and human voices audios. Finally, there is the <code>main.py</code> file which 
is the seed from where all interfaces and functions are called.

Authors
-------
Here is the list with all the collaborators:

- Albert Gubau Viñas: https://github.com/AlbertGubau 

- Andrea Sánchez Sarrablo: https://github.com/AndreaSanchezSarrablo
- Marc Rodríguez Jareño: 
- Nil Martí Valverde: https://github.com/U172772-NilMarti
- Paula Catà Coll: https://github.com/paulacata 



License
-------
All the software is distributed with the Affero GPL license (http://www.gnu.org/licenses/agpl-3.0.en.html), 
the lecture slides are distributed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 
(CC BY-NC-SA 4.0) license (http://creativecommons.org/licenses/by-nc-sa/4.0/) and the sounds in this 
repository are released under Creative Commons Attribution 4.0 (CC BY 4.0) license
(http://creativecommons.org/licenses/by/4.0/)

