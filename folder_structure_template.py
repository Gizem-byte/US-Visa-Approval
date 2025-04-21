import os
from pathlib import Path

project_name = "us_visa"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

#Loop through the list of files we created up
for filepath in list_of_files:

    #Cross-Platform Path Handling,Automatically uses / or \ correctly on Windows, Linux, or macOS
    #Converts string path to a Path object
    #Takes a string path (e.g., "us_visa/components/data_ingestion.py"),#Returns a Path object for easy manipulation.
    filepath = Path(filepath)

    #Splits filepath into two parts: directory and filename
    #filedir → The directory path (e.g., "us_visa/components")
    #filename → The filename (e.g., "data_ingestion.py")
    #output is tuple ("us_visa/components", "data_ingestion.py")
    filedir, filename = os.path.split(filepath)


    #Check if the directory part of the path is not empty
    #If it's not empty, create the directory using os.makedirs() with exist_ok=True to avoid errors if it already exists.
    #This ensures that the directory structure is created before creating the file.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    #Check if the file already exists and is not empty
    #If it doesn't exist or is empty, create the file using open() in write mode ("w").
    #If it does exist and is not empty, print a message indicating that the file is already present.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")



# #Dict to create the project structure

# project_name = "us_visa"

# project_structure = {
#     project_name: {
#         "__init__.py": "",
#         "components": {
#             "__init__.py": "",
#             "data_ingestion.py": "",
#             "data_validation.py": "",
#             "data_transformation.py": "",
#             "model_trainer.py": "",
#             "model_evaluation.py": "",
#             "model_pusher.py": ""
#         },
#         "configuration": {
#             "__init__.py": ""
#         },
#         "constants": {
#             "__init__.py": ""
#         },
#         "entity": {
#             "__init__.py": "",
#             "config_entity.py": "",
#             "artifact_entity.py": ""
#         },
#         "exception": {
#             "__init__.py": ""
#         },
#         "logger": {
#             "__init__.py": ""
#         },
#         "pipeline": {  
#             "__init__.py": "",
#             "training_pipeline.py": "",
#             "prediction_pipeline.py": ""
#         },
#         "utils": {
#             "__init__.py": "",
#             "main_utils.py": ""
#         }
#     },
#     "config": {
#         "model.yaml": "",
#         "schema.yaml": ""
#     },
#     "root_files": [
#         "app.py",
#         "requirements.txt",
#         "Dockerfile",
#         ".dockerignore",
#         "demo.py",
#         "setup.py"
#     ]
# }




