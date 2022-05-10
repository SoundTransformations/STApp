# Sound Transformations Application

Sound transformations tool for music applications written in python (with a bit of C) plus complementary modules.

How to use
----------

In order to use these tools you have to install python (recommended 3.8.x) and the following modules: ipython, numpy, matplotlib, scipy, and cython. 

In Ubuntu (which we strongly recommend) in order to install all these modules it is as simple as typing in the Terminal:

<code>$ sudo apt-get install python-dev ipython python-numpy python-matplotlib python-scipy cython</code>

In OSX (which we do not support but that should work) you install these modules by typing in the Terminal:

<code>$ pip install ipython numpy matplotlib scipy cython</code>

then, for using the software, after downloading the whole package, you need to compile some C functions. For that you should go to the directory <code>Functions/models/utilFunctions_C</code> and type:</p>

<code>$ python3 compileModule.py build_ext --inplace </code>

The basic sound analysis/synthesis functions, or models, are in the python archive <code>main.py</code>. To execute the application you have to go to the directory where the <code>main.py</code> file is and type: 

<code>$ python3 main.py </code>

Content
-------

All the code is in the <code> Functions </code> directory, with subdirectories for the models, the transformations, and the interfaces.

License
-------
All the software is distributed with the Affero GPL license (http://www.gnu.org/licenses/agpl-3.0.en.html), the lecture slides are distributed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0) license (http://creativecommons.org/licenses/by-nc-sa/4.0/) and the sounds in this repository are released under Creative Commons Attribution 4.0 (CC BY 4.0) license (http://creativecommons.org/licenses/by/4.0/)

