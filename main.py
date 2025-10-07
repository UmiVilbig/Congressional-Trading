# from collectors.api
from storage.local_storage import LocalDataWriter

def run_batch_pipeline():
  writer = LocalDataWriter() # swap to kafka writer in the future if needed
  # data = col

if __name__ == "__main__":
  run_batch_pipeline()