#!/usr/bin/env python3
import json
import os
import argparse

# ディレクトリ設定
JSON_DIR = os.path.join(os.path.dirname(__file__), '..', 'json')

# 引数処理
parser = argparse.ArgumentParser(description="Merge JSON rule files into one file.")
parser.add_argument('--include-hidden', action='store_true', help='Include rules with visible: false')
args = parser.parse_args()

# meta.json の読み込み
with open(os.path.join(JSON_DIR, 'meta.json'), 'r', encoding='utf-8') as f:
    meta = json.load(f)

# order.json の読み込み（順序と公開情報の定義）
with open(os.path.join(JSON_DIR, 'order.json'), 'r', encoding='utf-8') as f:
    order = json.load(f)

# 指定順序でルールを結合
rules = []
for entry in order:
    if not args.include_hidden and not entry.get("visible", False):
        continue
    rule_path = os.path.join(JSON_DIR, f"{entry['id']}.json")
    with open(rule_path, 'r', encoding='utf-8') as f:
        rule = json.load(f)
        # メタ情報は除外（上位で付加される）
        rule.pop('_license', None)
        rule.pop('author', None)
        rule.pop('affiliation', None)
        rules.append(rule)

# 出力構築
merged = dict(meta)
merged['rules'] = rules

# 出力
print(json.dumps(merged, ensure_ascii=False, indent=2))
