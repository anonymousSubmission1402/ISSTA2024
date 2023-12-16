# Turbulence Execution Instructions

To execute the benchmark, please ensure that your operating system is either Linux or macOS and the version of Python installed is at least 3.10. Follow the steps below in the specified order:

## Step 1: Install Required Libraries

Open the terminal and use the `cd` command to move into the Turbulence folder. Use the following command to install all required packages of Python:

`pip install -r requirements.txt`

## Step 2: Set API Keys as Environmental Variables

Configure the OpenAI and Cohere API keys as environmental variables on your operating system. Name the variable for the OpenAI API key as "OPENAI_KEY" and the variable for the Cohere API key as "COHERE_KEY". If you are running a local LLM, then there is no need to configure any key.

## Step 3: Define Prerequisite Settings in `config.json`

In the `config.json` file, define the prerequisite settings as outlined below:

- Set the "task" to "call_llm" for sending questions to the Large Language Model (LLM) and retrieving generated responses. To test the generated responses, set the "task" to "test".
   
- Specify the model under evaluation and its parameters in the "model_specifications" section.

- Determine the seed value for result replication. The experiments described in the paper utilized a seed value of 1.

- Indicate the range of questions to send to the LLM and test the corresponding responses. For instance, "1-60" covers questions from 1 to 60 (inclusive). Each question is accompanied by the number of instances. Specify whether the list of generated parameter values should be shuffled using the 'shuffle' attribute. Additionally, determine if fuzzy testing should be done and if yes then specify the number of random inputs for the randomized test phase. Some LLM-generated code may have very lengthy runtime or substantial memory usage. Select the maximum allowable runtime in seconds and specify how much memory should be available.

- Set the "number_of_rounds" to specify the number of experiments. For example, using "1-5" will evaluate the results of all five experiments.

- Provide the absolute path of the Turbulence folder as the value for the "path" attribute.

## Step 4: Execution
Make sure you are in the Turbulence folder. Next, enter the command `python3 main.py` and press the enter key to execute it.

