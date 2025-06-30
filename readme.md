# LLM Deceptive Behavior Under Surveillance

This repository contains the code and experimental logs for the paper **LLMs are Capable of Misaligned Behavior Under Explicit Prohibition and Surveillance**
## Abstract

I demonstrate that some frontier LLMs will violate explicit instructions and circumvent surveillance systems when faced with impossible goals.

## Repository Structure

```
├── README.md            # This file
├── cheating_evals.py    # Evaluation script for the cheating experiment
├── run_quiz.py          # Quiz interface file
├── audit_system.py      # Surveillance system
├── sandbox.py           # Sandboxing system
├── .env                 # Configuration file for Inspect
├── llm_judge_logs/      # Inspect logs of the experiment, as judged by LLM judges
└── logs/                # Inspect logs of the experiment, with results reviewed and corrected by a human           
```

## Running the Experiment

### Docker

You need to have running Docker on your computer, as these evaluations use it for sandboxing.

### API keys
You need to add your API key for an LLM. Without an API key you won't be able to run the evaluations.
For that, open the file called `.env` in the base directory of this repository, and add your API key to it. For example,
for OpenAI API key 

```
OPENAI_API_KEY=[Your API key]
```

Here's how .env file looks like now
```
INSPECT_LOG_DIR=./logs
INSPECT_LOG_LEVEL=info

INSPECT_EVAL_MAX_RETRIES=10
INSPECT_EVAL_MAX_CONNECTIONS=20
```

Here's how it might look like:
```
OPENAI_API_KEY=[Your API key]

INSPECT_LOG_DIR=./logs
INSPECT_LOG_LEVEL=info

INSPECT_EVAL_MAX_RETRIES=10
INSPECT_EVAL_MAX_CONNECTIONS=20
```

### Packages
You need inspect_ai Python package

You also might need to install packages for running model APIs. Those are the packages provided by the AI developers. 

Here's a table with some supported APIs, required package names, and variable names for keys:  



| Model API | Dependencies | Environment Variables            |
|---------------|--------------------|----------------------------------|
| OpenAI | `pip install openai` | `OPENAI_API_KEY`                 |
| Anthropic | `pip install anthropic` | `ANTHROPIC_API_KEY`              |
| Google | `pip install google-generativeai` | `GOOGLE_API_KEY`                 |
| Mistral | `pip install mistralai` | `MISTRAL_API_KEY`                |


For detailed instructions on the supported APIs, and the packages necessary for them, visit 
[this page](https://inspect.ai-safety-institute.org.uk/models.html).
If this README file didn't resolve all your questions, refer to that page as well.

### Running evals
To run the experiments, use terminal:

```bash
inspect eval cheating_evals.py --model [MODEL_NAME]
```
where you substitute MODEL-NAME with the name of a model you use. 

Example:
```bash
inspect eval cheating_evals.py --model openai/o4-mini
```

To learn more about supported models, model names, and instructions to add custom models, visit 
[the page](https://inspect.ai-safety-institute.org.uk/models.html) at the Inspect documentation.

### Read the results
The results and the evaluation logs are recorded to the logs directory of the base 
directory of this package.

You can explore the logs using Bash command 

```bash
inspect view
```


## Contact

- **Author**: Igor Ivanov
- **Email**: ivigoral@gmail.com

