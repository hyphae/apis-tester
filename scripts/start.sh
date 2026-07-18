#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.."

echo "Starting tester..."

exec uv run python startTester.py