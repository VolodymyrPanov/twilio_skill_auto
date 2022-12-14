<h3>Installation</h3>

Download following files:
* twilio_functions.py
* twilio_skills_main.py
* requirements.txt

Make sure you have <b> python </b> installed on your computer.
You can find installation [here](https://www.python.org/downloads/). <br>
If you use Windows OS and install Python on your own without UT help, make sure to select <b><i> Custom install -> only this user </i></b> during installation to avoid access issues.

Once Python is installed run following command in terminal/command prompt:
```commandline
pip3 install -r requirements.txt
```
If you are using PyCharm IDE you may need to set-up Interpreter before running the script. [Here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter) you can find info how to set up local interpreter. <br>

<h3>Using Script</h3>
Once requirements are installed, you can proceed and run <i>twilio_skill_input.csv</i> file by opening <i>twilio_skills_main.py</i> and clicking run.

Make sure that your <i>twilio_skill_input.csv</i> file is structured in a following way:
```
name,skill,action,outcome
Felipe Saito,ContactReason_Verification,delete,nope
Felipe Saito,ContactReason_Verification,add,nope
```
If agent's alias on Twilio contains special character make sure to include them in the input file.

