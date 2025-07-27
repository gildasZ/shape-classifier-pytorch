#!/bin/bash

# --- Configuration ---
# The Hugging Face user/organization that owns the repositories
HF_USERNAME="CaveMindLabs"

# The base directory where artifacts will be downloaded, relative to this script
ARTIFACTS_BASE_DIR="../shape-classifier-artifacts"

# --- Repository Definitions ---
# Define the dataset repository URL and its local target directory
DATASET_REPO_URL="https://huggingface.co/datasets/${HF_USERNAME}/shape-classifier-datasets"
DATASET_TARGET_DIR="$ARTIFACTS_BASE_DIR/shape-classifier-datasets"

# Define the model repository URL and its local target directory
MODEL_REPO_URL="https://huggingface.co/${HF_USERNAME}/shape-classifier-models"
MODEL_TARGET_DIR="$ARTIFACTS_BASE_DIR/shape-classifier-models"

# --- Main Logic ---

# A function to either clone a new repo or pull updates to an existing one
download_or_update_repo() {
  local REPO_URL=$1
  local TARGET_DIR=$2

  echo ""
  echo "--- Processing repository: $TARGET_DIR ---"

  # Check if the target directory already exists and is a git repository
  if [ -d "$TARGET_DIR/.git" ]; then
    echo "Directory exists. Pulling latest changes..."
    # Change into the directory, pull, and change back
    (cd "$TARGET_DIR" && git pull)
    echo "Pull complete."
  else
    echo "Directory not found. Cloning from $REPO_URL..."
    # Create the parent artifacts directory if it doesn't exist
    mkdir -p "$ARTIFACTS_BASE_DIR"
    # Clone the repository into the specified target directory
    git clone "$REPO_URL" "$TARGET_DIR"
    echo "Clone complete."
  fi
}

echo "--- Starting Artifact Download/Update Process ---"
echo "This requires 'git' and 'git-lfs' to be installed."

download_or_update_repo "$DATASET_REPO_URL" "$DATASET_TARGET_DIR"
download_or_update_repo "$MODEL_REPO_URL" "$MODEL_TARGET_DIR"

echo ""
echo "--- Artifacts are up-to-date in '$ARTIFACTS_BASE_DIR' ---"
