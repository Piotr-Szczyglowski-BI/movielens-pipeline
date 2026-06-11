import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
log = logging.getLogger(__name__)

RAW = Path("data/raw")
BRONZE = Path("data/bronze")
BRONZE.mkdir(exist_ok=True)

def ingest(name: str) -> None:
    "Ingest a raw file and save it to bronze layer"
    src = RAW / f"{name}.csv"
    dst = BRONZE / f"{name}.parquet"
    log.info(f"Ingesting {src} to {dst}")
    df = pd.read_csv(src)
    df.to_parquet(dst,index=False)
    log.info(f"Done - {len(df):,} rows ingested")

if __name__ == "__main__":
    for f in ["movie", "rating", "tag", "link"]:
        ingest(f)
