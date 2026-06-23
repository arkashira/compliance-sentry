import argparse
import json
from dataclasses import dataclass
from typing import List

@dataclass
class DataRow:
    uuid: str
    data: str

class ConsentStore:
    def __init__(self):
        self.consents = {}

    def add_consent(self, uuid: str):
        self.consents[uuid] = True

    def has_consent(self, uuid: str) -> bool:
        return self.consents.get(uuid, False)

class Middleware:
    def __init__(self, consent_store: ConsentStore):
        self.consent_store = consent_store

    def filter_rows(self, rows: List[DataRow]) -> List[DataRow]:
        filtered_rows = []
        filtered_out_count = 0
        for row in rows:
            if self.consent_store.has_consent(row.uuid):
                filtered_rows.append(row)
            else:
                filtered_out_count += 1
        return filtered_rows, filtered_out_count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--consent-store', type=str, help='Path to consent store file')
    parser.add_argument('--data-file', type=str, help='Path to data file')
    args = parser.parse_args()

    consent_store = ConsentStore()
    with open(args.consent_store, 'r') as f:
        consents = json.load(f)
        for uuid in consents:
            consent_store.add_consent(uuid)

    rows = []
    with open(args.data_file, 'r') as f:
        for line in f:
            uuid, data = line.strip().split(',')
            rows.append(DataRow(uuid, data))

    middleware = Middleware(consent_store)
    filtered_rows, filtered_out_count = middleware.filter_rows(rows)

    print(f'Filtered out {filtered_out_count} rows')
    print(f'Filtered rows: {len(filtered_rows)}')

if __name__ == '__main__':
    main()
