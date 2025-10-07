from collectors.api.trade_collector import TradeCollector
from config import get_settings

if __name__ == "__main__":
  settings = get_settings()

  start_year = settings['collectors']['trades']['start_year']
  end_year = settings['collectors']['trades']['end_year']
  collector = TradeCollector()
  for year in range(start_year, end_year + 1):
    collector.fetch(year)