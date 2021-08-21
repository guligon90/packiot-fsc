# Auxiliary function, calling the devenv.py script
define devenv
    ./scripts/python/devenv.py $(1)
endef

# Sets DB environment variables
itsetenv:
	./scripts/sh/set-env.sh

# Builds a Docker image
itbuild:
	$(call devenv, build)

# Start a container with logs
itstartwlogs:
	$(call devenv, startwlogs pgsqlserver)

# Stop all containers
itstop:
	$(call devenv, stop)

# Restart all containers
itrestart:
	$(call devenv, restart)

# Show all Docker resources' status
itshowstatus:
	$(call devenv, status)

# Show all Docker resources' status
itclean:
	$(call devenv, clean)

# Kill all Docker resources' status
itkill:
	$(call devenv, kill)

# Creates DB tables
itcreatetables:
	$(call devenv, createtables)

# Drops the current database
itdropdb:
	$(call devenv, dropdb)
