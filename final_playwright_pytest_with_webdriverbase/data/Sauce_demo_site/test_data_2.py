import json
from pathlib import Path

_DATA_FILE = Path(__file__).with_name("test_data_2.json")

with _DATA_FILE.open("r", encoding="utf-8") as f:
    TEST_DATA_2 = json.load(f)