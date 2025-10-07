# this file was vibe coded
import os
import yaml
from pathlib import Path
from functools import lru_cache

def _expand_env_vars(value: str) -> str:
    """Recursively expand ${VAR} environment variables in strings."""
    if isinstance(value, str):
        return os.path.expandvars(value)
    elif isinstance(value, dict):
        return {k: _expand_env_vars(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [_expand_env_vars(v) for v in value]
    return value

def _deep_merge(base: dict, overrides: dict) -> dict:
    """Recursively merge two dicts."""
    for k, v in overrides.items():
        if isinstance(v, dict) and k in base and isinstance(base[k], dict):
            base[k] = _deep_merge(base[k], v)
        else:
            base[k] = v
    return base

@lru_cache(maxsize=1)
def get_settings(env: str = None) -> dict:
  """Load settings.yml from the config folder and merge with environment overrides."""
  # Point to config/settings.yml
  settings_path = Path(__file__).parent.parent / "config" / "settings.yml"
  
  if not settings_path.exists():
      raise FileNotFoundError(f"Settings file not found: {settings_path}")
  
  with open(settings_path, "r") as f:
      cfg = yaml.safe_load(f)

  env = env or os.getenv("PIPELINE_ENV", "default")
  merged = cfg.get("default", {}).copy()

  if env in cfg:
      merged = _deep_merge(merged, cfg[env])

  return _expand_env_vars(merged)