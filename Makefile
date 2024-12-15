#!/bin/bash

test_base_packages:
	@echo "Running test..."
	@echo "Building docker image..."
	docker build --no-cache -t archlinux-packages-test -f ./docker/packages_test.Dockerfile .
	@echo "Running docker container..."
	# docker run --rm -it archlinux-packages-test
	docker run -it archlinux-packages-test
	@echo "Test finished."
