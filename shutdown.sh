#!/bin/bash
# Re-direct to remote environment.
export DOCKER_HOST="ssh://park"

# Run your docker-compose commands.
docker-compose down -v

# All docker-compose commands here will be run on remote-host.

# Switch back to your local environment.
unset DOCKER_HOST