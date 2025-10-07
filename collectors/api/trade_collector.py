# the point of this collector is to grab the raw pdf from the house.gov
# website and create a local copy for processing later
import io, requests
import pandas as pd

from time import sleep
from urllib.request import urlopen
from config import get_settings
from utils.storage import write_raw_data

class TradeCollector:
  def __init__(self):
    self.settings = get_settings()
  
  def fetch(self, year: int):
    # fetch all the filings for the given year
    url = self.settings['collectors']['trades']['trades_url']
    url = url.format(year=year)
    with urlopen(url) as response:
      data = io.StringIO(response.read().decode())
      df = pd.read_csv(data, sep='\t')
    
    # pull the filings from the given year
    for _, row in df.iterrows():
      sleep(0.1)  # be kind to the server
      doc_id = row["DocID"]
      url = self.settings['collectors']['trades']['filing_url']
      url = url.format(year=year, doc_id=doc_id)
      try:
        resp = requests.get(url, stream=True, timeout=10)
        resp.raise_for_status()

        pdf_bytes = b"".join(chunk for chunk in resp.iter_content(chunk_size=8192))

        meta = {
          "id": doc_id,
          "url": url,
          "year": year,
          "status": resp.status_code,
          "retrieved_at": pd.Timestamp.utcnow().isoformat(),
          "size_bytes": len(pdf_bytes)
        }

        path = write_raw_data(
          source="trades",
          data=pdf_bytes,
          ext="pdf",
          meta=meta,
        )
        print(f"Saved {url} to {path}")
      except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
      except Exception as e:
        print(f"Error processing {url}: {e}")