import os
import urllib.request
import zipfile
from src.datascience.entity.config_entity import DataValidationConfig
from src.datascience import logger
import pandas as pd


class DataValidation:
    def __init__(self,config = DataValidationConfig) -> None:
        self.config = config

    def validate_columns(self):
        

        try:

            schema = list(self.config.all_schema.keys())
            data = pd.read_csv(self.config.unzip_data_dir)

            columns = list(data.columns)


            for col in columns:
                if col not in schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            

        except Exception as e:
            raise e
    
    def validate_datatype(self):
        try:
            expected_schema = self.config.all_schema  # This is already a dict
            data = pd.read_csv(self.config.unzip_data_dir)

            row_dtypes = data.dtypes  # actual column data types
            mismatches = []

            # Check each column's dtype against expected
            for col, expected_type in expected_schema.items():
                if col in data.columns:
                    actual_dtype = row_dtypes[col]
                    # Pandas uses float64, int64 etc., so we normalize both to string
                    if expected_type == "float" and not pd.api.types.is_float_dtype(actual_dtype):
                        mismatches.append((col, "Expected float"))
                    elif expected_type == "int" and not pd.api.types.is_integer_dtype(actual_dtype):
                        mismatches.append((col, "Expected int"))
                    elif expected_type == "object" and not pd.api.types.is_object_dtype(actual_dtype):
                        mismatches.append((col, "Expected object (string)"))
                else:
                    mismatches.append((col, "Column missing"))

            validation_status = len(mismatches) == 0

            # Write status to file
            with open(self.config.STATUS_FILE, 'a') as f:  # 'a' so it doesn’t overwrite column check
                if validation_status:
                    f.write("\nData type validation: PASS")
                else:
                    f.write("\nData type validation: FAIL")
                    for col, reason in mismatches:
                        f.write(f"\n - {col}: {reason}")

            logger.info("Data type validation completed.")

        except Exception as e:
            logger.error(f"Error in data type validation: {e}")
            raise


    def run_validation(self):
        self.validate_columns()
        self.validate_datatype()
