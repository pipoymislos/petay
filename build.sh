#!/usr/bin/env bash
set -e

# Set Cargo home to writable location
export CARGO_HOME=/tmp/cargo
mkdir -p $CARGO_HOME

# Install dependencies
pip install -r requirements.txt
