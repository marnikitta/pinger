host := alpinist
deploy_files := Makefile pinger poetry.lock poetry.toml pyproject.toml

all: 

push:
	rsync --delete --verbose --archive --compress --rsh=ssh $(deploy_files) $(host):~/pinger

.PHONY: all push
