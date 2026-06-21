import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
log = logging.getLogger(__name__)

RAW = Path("data/raw")
BRONZE = Path("data/bronze")

def ingest(name: str) -> None:
    """Read CSV from Raw layer and save to Bronze as Parquet"""
    BRONZE.mkdir(exist_ok=True)
    src = RAW / f"{name}.csv"
    dst = BRONZE / f"{name}.parquet"
    log.info(f"Ingesting {src} → {dst}")
    df = pd.read_csv(src)
    df.to_parquet(dst, index=False)
    log.info(f"Done - {len(df):,} rows")

def run_all() -> None:
    """Ingest all MovieLens source files"""
    for name in ["movie", "rating", "tag", "link"]:
        ingest(name)

if __name__ == "__main__":
    run_all()