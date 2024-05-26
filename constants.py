import os

BASE_PATH = os.path.dirname(__file__)
PATHS = {
    "DATASET": os.path.join(BASE_PATH, "dataset", "dataset.csv"),
    "METADATA_INDICATORS": os.path.join(
        BASE_PATH, "dataset", "Indicators.csv"
    ),
    "METADATA_COUNTRIES": os.path.join(
        BASE_PATH, "dataset", "Countries.csv"
    ),
    "METADATA_MAPPINGS": os.path.join(
        BASE_PATH, "dataset", "Mapping.csv"
    ),
}
