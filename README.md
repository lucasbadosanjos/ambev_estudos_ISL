# Project Definition

|Details   							|Answers|
|:--								|:--	|
|**Project Name:**					|Name	|
|**Business area:**					|Area	|
|**Business manager responsible:**	|Name	|
|**Business focal point:**		   	|Name	|
|**Analytics responsible:**  		|Name  	|
|**Manager responsible:**			|Name	|

**1. What is the problem we want to solve?**

	- Answer
    
    
**2. Why do we want to solve this problem?**

	- Answer
    
    
**3. What do we expect of results?**

	- Answer
    
    
**4. What is the expected delivery?**

	- Answer
    
    
**5. What is the success criteria?**

	- Answer



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


Project Methodology (CRISP-DM)
------------

<div display="block" margin-left="auto" margin-right="auto" align="center">
<img src="docs/business_understanding_CRISPDM.PNG" width="60%" alt="Business Understanding from CRISP-DM">
</div>
<br>
<div display="block" margin-left="auto" margin-right="auto" align="center">
<img src="docs/data_understanding_CRISPDM.PNG" width="60%" alt="Data Understanding from CRISP-DM">
</div>
<br>
<div display="block" margin-left="auto" margin-right="auto" align="center">
<img src="docs/data_preparation_CRISPDM.PNG" width="60%" alt="Data Preparation from CRISP-DM">
</div>
<br>
<div display="block" margin-left="auto" margin-right="auto" align="center">
<img src="docs/modeling_CRISPDM.PNG" width="60%" alt="Modeling from CRISP-DM">
</div>
<br>
<div display="block" margin-left="auto" margin-right="auto" align="center">
<img src="docs/evaluation_CRISPDM.PNG" width="60%" alt="Evaluation from CRISP-DM">
</div>
<br>
<div display="block" margin-left="auto" margin-right="auto" align="center">
<img src="docs/deployment_CRISPDM.PNG" width="60%" alt="Deployment from CRISP-DM">
</div>
<br>
<p> <strong>Reference:</strong> The Modeling Agency. CRISP-DM 1.0. 2000. URL: https://www.the-modeling-agency.com/crisp-dm.pdf </p>