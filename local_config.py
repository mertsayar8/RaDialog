
PATH_TO_MIMIC_CXR = "/home/data/DIVA/mimic" #TODO set your own path to MIMIC-CXR-JPG dataset (should point to a folder containing "mimic-cxr-jpg" folder)
PATH_TO_MIMIC_NLE = "<PATH_TO_MIMIC_NLE>" #TODO set your own path to MIMIC-NLE dataset (should point to a folder containing "mimic-nle" folder)
VIS_ROOT = f"{PATH_TO_MIMIC_CXR}/mimic-cxr-jpg/2.0.0"
PATH_TO_PATIENTS = f"{PATH_TO_MIMIC_CXR}/haim/patients"

JAVA_HOME = "<PATH_TO_JAVA>/java/jre1.8.0_361" #TODO set your own path to java home, adapt version if necessary
JAVA_PATH = "PATH_TO_JAVA/java/jre1.8.0_361/bin:"

CHEXBERT_ENV_PATH = '<PATH_TO_ENVS>/miniconda3/envs/chexbert/bin/python' #replace with path to chexbert environment

CHEXBERT_PATH = '<PATH_TO_PROJECT>/RaDialog/chexbert/src' #replace with path to chexbert project in RaDialog folder

WANDB_ENTITY = " " #TODO set your own wandb entity