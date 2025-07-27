#!/bin/bash

# --- Configuration ---
# Define the local directories for your repositories using relative paths
# from this script's location (shape-classifier-pytorch/).
ARTIFACTS_BASE_DIR="../shape-classifier-artifacts"
DATASET_DIR="$ARTIFACTS_BASE_DIR/shape-classifier-datasets"
MODEL_DIR="$ARTIFACTS_BASE_DIR/shape-classifier-models"
COMMIT_MSG="Synchronize local changes with Hugging Face Hub"

# --- Main Logic ---

# Function to synchronize a single repository
# It takes one argument: the directory name of the repo
sync_repo() {
  REPO_PATH=$1
  echo "" # Add a blank line for readability
  echo "--- Syncing repository: $REPO_PATH ---"

  # Check if the directory exists
  if [ ! -d "$REPO_PATH" ]; then
    echo "Error: Directory '$REPO_PATH' not found. Skipping."
    return
  fi

  # Change into the repository directory
  cd "$REPO_PATH" || return

  # Pull the latest changes from the remote repository
  echo "1. Pulling latest changes..."
  git pull

  # Add all changes (new, modified, and DELETED files) to the staging area
  echo "2. Staging all local changes (adds, mods, deletes)..."
  git add -A

  # Check if there are any changes to commit
  if ! git diff-index --quiet HEAD --; then
    echo "3. Changes detected. Committing and pushing..."
    git commit -m "$COMMIT_MSG"
    git push
    echo "Push complete for $REPO_PATH."
  else
    echo "3. No new changes detected. Nothing to commit or push."
  fi

  # Go back to the original script directory
  cd - >/dev/null # 'cd -' goes back to the previous directory. '>/dev/null' silences its output.
}

echo "--- Starting Hugging Face Synchronization ---"

# Call the function for each of your repositories
sync_repo "$DATASET_DIR"
sync_repo "$MODEL_DIR"

echo ""
echo "--- Synchronization Finished ---"
