import os 
from pathlib import Path

name = "src"

lst_files = [
    f"{name}/__init__.py",
    f"{name}/components/__init__.py",
    f"{name}/components/data_ingestion.py",
    f"{name}/components/data_transformation.py",
    f"{name}/components/model_trainer.py",
    f"{name}/components/model_evaluation.py",
    f"{name}/components/model_pusher.py",
    f"{name}/configuration/__init__.py",
    f"{name}/configuratoin/mongo_db_connection.py",
    f"{name}/configuration/aws_connection.py",
    f"{name}/cloud_storage/__init__.py",
    f"{name}/cloud_storage/aws_storage.py",
    f"{name}/data_access/__init__.py",
    f"{name}/data_access/project_data.py",
    f"{name}/constants/__init__.py",
    f"{name}/entity/__init__.py",
    f"{name}/entity/config_entity.py",
    f"{name}/entity/artifact_entity.py",
    f"{name}/entity/estimator.py",
    f"{name}/entity/s3_estimator.py",
    f"{name}/exception/__init__.py",
    f"{name}/logger/__init__.py",
    f"{name}/pipeline/__init__.py",
    f"{name}/pipeline/training_pipeline.py",
    f"{name}/pipeline/prediction_pipeline.py",
    f"{name}/utils/__init__.py",
    f"{name}/utils/main_utils.py"
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in lst_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
        with open(filepath, "w") as f:
            pass
    else:
        print("File already exists at: {filepath}")        

