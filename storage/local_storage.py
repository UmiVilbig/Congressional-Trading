import json, os
from .base import DataWriter, DataReader

class LocalDataWriter(DataWriter):
  def write(self, data, destination: str):
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    with open(destination, 'w') as f:
      json.dump(data, f)

class LocalDataReader(DataReader):
  def read(self, source: str):
    with open(source) as f:
      return json.load(f)