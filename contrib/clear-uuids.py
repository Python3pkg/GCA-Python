#!/usr/bin/env python


import argparse
import codecs
import json
import sys


def clean_uuids(d):
    if not isinstance(d, dict):
        return None
    if 'uuid' in d:
        del d['uuid']
    for k, v in d.items():
        if isinstance(d[k], dict):
            clean_uuids(d[k])
        elif isinstance(d[k], list):
            [clean_uuids(x) for x in d[k]]
    return d


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='uuid cleaner tool')
    parser.add_argument('file', type=str, default='-')
    args = parser.parse_args()
    fd = codecs.open(args.file, 'r', encoding='utf-8') if args.file != '-' else sys.stdin
    data = json.load(fd)
    [clean_uuids(d) for d in data]
    js = json.dumps(data, sort_keys=True, indent=4,
                    separators=(',', ': '), ensure_ascii=False)
    sys.stdout.write(js.encode('utf-8'))