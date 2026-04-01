# Use bash for all recipes.
set shell := ["bash", "-cu"]

# Show available recipes when running plain `just`.
default:
  @just --list

# Build the MkDocs site into `site/`.
build:
  uv run --no-sync mkdocs build

# Start local docs server with live reload.
serve:
  uv run --no-sync mkdocs serve

# Remove generated build output.
clean:
  rm -rf site
