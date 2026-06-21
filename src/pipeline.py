from prefect import flow, task
import subprocess
from pathlib import Path
import logging
from ingest import run_all

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
log = logging.getLogger(__name__)

# -- TASKS -------------------

@task(name="Bronze Ingestion", retries=2)
def run_ingestion():
    "Read raw CSV files and save as parquet to bronze layer"


    log.info("Starting bronze ingestion...")
    run_all()
    log.info("Bronze ingestion completed")


@task(name="Silver - dbt staging", retries=1)
def run_dbt_staging():
    "Run dbt staging models to build silver layer"
    log.info(f"Starting silver layer staging...")
    result = subprocess.run(
        ["dbt", "run", "--select", "staging.*"],
        cwd = "movielens",
        capture_output=True,
        text = True
    )
    log.info(result.stdout)
    if result.returncode != 0:
        raise Exception(f"dbt staging failed:\n{result.stderr}")
    
@task(name="Gold - dbt gold models", retries = 1)
def run_dbt_gold():
    "Run dbt gold models to build analytical layer"
    log.info("Starting Gold layer data processing")
    result = subprocess.run(
        ["dbt", "run", "--select", "gold.*"],
        cwd = "movielens",
        capture_output = True,
        text = True
    )
    log.info(result.stdout)
    if result.returncode != 0:
        raise Exception(f"dbt staging failed:\n{result.stderr}")
    
@task(name="Data Quality Checks", retries=1)
def run_dbt_tests():
    """Run dbt tests to validate data quality"""
    log.info("Running dbt tests...")
    result = subprocess.run(
        ["dbt", "test", "--select", "staging.*"],
        cwd="movielens",
        capture_output=True,
        text=True
    )
    log.info(result.stdout)
    if result.returncode != 0:
        raise Exception(f"dbt tests failed:\n{result.stderr}")
    
@flow(name="Movielens - Pipeline")
def movielens_pipeline(skip_ingestion: bool = False):
    """
    End-to-End pipelne: Bronze -> Silver -> Gold -> Tests

    Args: 

    Skip Ingestion: set True to skip Bronze ingestion (data already downloaded)
    """
    if not skip_ingestion:
        run_ingestion()
    
    run_dbt_staging()
    run_dbt_gold()
    run_dbt_tests()

    log.info("Pipeline executed successfuly")
    

if __name__ == "__main__":
    movielens_pipeline(skip_ingestion=True)
