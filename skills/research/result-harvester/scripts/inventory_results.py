#!/usr/bin/env python3
"""Conservatively inventory experiment artifacts without inventing schema.

The script scans one or more experiment roots and emits JSONL records for
candidate configs, metrics/results, logs, and checkpoints. It intentionally
indexes files rather than interpreting arbitrary project-specific metrics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable

CONFIG_NAMES = ("config", "cfg", "params", "hparams", "args")
METRIC_NAMES = ("metric", "metrics", "result", "results", "score", "scores", "eval")
LOG_SUFFIXES = {".log", ".out", ".err"}
CHECKPOINT_SUFFIXES = {".pt", ".pth", ".ckpt", ".safetensors", ".onnx"}
TEXT_STRUCTURED_SUFFIXES = {".json", ".jsonl", ".csv", ".yaml", ".yml", ".toml"}

def sha256_prefix(path: Path, max_bytes: int = 8 * 1024 * 1024) -> str | None:
    try:
        if path.stat().st_size > max_bytes:
            return None
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None

def classify(path: Path) -> str | None:
    name = path.name.lower(); stem = path.stem.lower(); suffix = path.suffix.lower()
    if suffix in CHECKPOINT_SUFFIXES: return "checkpoint"
    if suffix in LOG_SUFFIXES: return "log"
    if suffix in TEXT_STRUCTURED_SUFFIXES:
        if any(token in stem for token in CONFIG_NAMES): return "config"
        if any(token in stem for token in METRIC_NAMES): return "metrics_or_results"
        if name in {"summary.json", "summary.csv", "history.json", "history.csv"}: return "metrics_or_results"
    return None

def iter_records(root: Path) -> Iterable[dict]:
    root = root.resolve()
    if not root.exists():
        yield {"type": "error", "root": str(root), "error": "root_not_found"}; return
    for path in sorted(root.rglob("*")):
        if not path.is_file(): continue
        category = classify(path)
        if category is None: continue
        try:
            stat = path.stat(); rel = path.relative_to(root)
            yield {"type":"artifact","category":category,"root":str(root),"relative_path":str(rel),"absolute_path":str(path),"size_bytes":stat.st_size,"mtime_ns":stat.st_mtime_ns,"sha256":sha256_prefix(path)}
        except OSError as exc:
            yield {"type":"error","root":str(root),"absolute_path":str(path),"error":f"stat_failed:{exc}"}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); args.output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with args.output.open("w", encoding="utf-8") as f:
        for root in args.roots:
            for record in iter_records(root):
                f.write(json.dumps(record, ensure_ascii=False) + "\n"); count += 1
    print(f"Wrote {count} inventory records to {args.output}")
    print("No project-specific metric interpretation was performed.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
