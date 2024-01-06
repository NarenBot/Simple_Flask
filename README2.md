## Project Folder Structure:

```bash
Credit-Card-Default-Prediction/

├── .gitignore
├── LICENSE
├── .ebextensions/
│   └── python.config
├── config/
│   ├── config.yaml
│   ├── model.yaml
│   └── schema.yaml
├── notebook/
│   └── ... (Jupyter notebooks)
├── saved_models/
│   └── ... (saved models)
├── templates/
│   └── ... (HTML templates for the web app)
├── Documents/
│   ├── High Level Design.pdf
│   ├── Low Level Design.pdf
│   └── Wireframe.pdf
└── src/
    ├── components/
    │   ├── __init__.py
    │   ├── data_ingestion.py
    │   ├── data_validation.py
    │   ├── data_transformation.py
    │   ├── model_trainer.py
    │   ├── model_evaluation.py
    │   └── model_pusher.py
    ├── config/
    │   ├── __init__.py
    │   └── configuration.py
    ├── constant/
    │   ├── __init__.py
    ├── entity/
    │   ├── __init__.py
    │   ├── artifact_entity.py
    │   ├── config_entity.py
    │   ├── model_factory.py
    │   └── predictor.py
    ├── pipeline/
    │   ├── __init__.py
    │   └── pipeline.py
    ├── __init__.py
    ├── exception.py
    ├── logger.py
├── setup.py
├── README.md
├── application.py
├── pipeline.py
├── requirements.txt

```