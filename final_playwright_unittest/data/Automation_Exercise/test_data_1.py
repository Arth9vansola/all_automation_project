import json
from pathlib import Path

_DATA_FILE = Path(__file__).with_name("test_data_1.json")

with _DATA_FILE.open("r", encoding="utf-8") as f:
    TEST_DATA_1 = json.load(f)