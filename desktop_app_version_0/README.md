The program is run by downloading or copying this particular directory and sending it as the working one.

Then dependencies has to be installed by running:

```
pip install -r requirements.txt
```

After installing the requirements, navigate to the folder with the full project, setting it as a working directory:

```
cd your\path\to\interior_design
```


After that, 'main.py' can be executed:

```
python main.py
```

It is supposed, that during the first input, a user will enter a type of room he/she wants to generate (bedroom, living room, dining room, kitchen or bathroom). 
The second input is a prompt written freely as for how user wants the room to be decorated. 


Filenames outputed could be found in labelled_data folder on the main github page of the project.

**Another option is to start a local server with the app (preferred option):**

Dependencies has to be installed by running:

```
pip install -r requirements.txt
```

After installing the requirements, navigate to the folder with the full project, setting it as a working directory:

```
cd your\path\to\interior_design
```

Then run a local server:

```
uvicorn app:app --reload
```

After some time for resource intialization, the app would be avaliable at:

http://127.0.0.1:8000
