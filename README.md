This repository contains a project for training different AI models to detect possible attacks on a system, using system calls.

<hr>

<h1>Setting up</h1>
<ol>
    <li>Download the ADFA-LD dataset from <a target="_blank">https://research.unsw.edu.au/projects/adfa-ids-datasets</a></li>
    <li>Extract the 'ADFA-LD' folder onto the 'Pre-Processamento/Inputs', creating it, if necessary.</li>
    <li>Due to a bug with the dataset, go into 'Validation_Data_Master' and delete the file '.DS_Store'</li>
</ol>

<h2>Dependencies</h2>
This project requires a few 'pip' dependencies. To install them, run the following commands.
<ul>
    <li>pip install pandas</li>
    <li>pip install scikit-learn</li>
    <li>pip install scikit-learn</li>
    <li>pip install scikit-learn</li>
    <li>pip install scikit-learn</li>
</ul>

<h1>Running Pre-Processing phase</h1>
To run the pre-processing scripts, go into the folder 'Pre-Processamento' and run the following command 'python3 Pipeline.p -w [WINDOW_SIZE] -p'.
This will create all the files needed for the models to use. <br>
Example: 'python3 Pipeline.p -w 10 -p' (Runs the pre-processing script with a WINDOW_SIZE of 10)

<h1>Running the Models</h1>
All supported models are stored in the 'Pre-Processamento/Models' folder. To run them, go into the main repository's folder and run the following command: 'python3 Pre-Processamento/Models/[MODEL_SCRIPT]'.<br>
Example: 'python3 Pre-Processamento/Models/KNN.py' (Runs the KNN model)