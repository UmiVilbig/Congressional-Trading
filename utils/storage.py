import os, json, datetime
from pathlib import Path

def write_raw_data(source: str, data, ext="json", meta=None, subdir=None):
    """
    Save raw data with simplified date-based folder structure:
    data/raw/{todaysdate}/{collection_dir}/{filename}.{ext}
    """
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")  # single date dir
    # base dir is data/raw/{todaysdate}/{collection_dir}
    target_dir = Path("data/raw") / today / source
    if subdir:
        target_dir = target_dir / subdir
    target_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
    filename = f"{source}_{timestamp}.{ext}"
    output_path = target_dir / filename

    # Write data
    if ext == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    elif ext in {"txt", "csv"}:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(data)
    else:  # binary (pdf, images, etc.)
        with open(output_path, "wb") as f:
            f.write(data)

    # Write optional metadata sidecar
    if meta:
        meta_path = output_path.with_suffix(output_path.suffix + ".meta.json")
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

    return output_path