generate:
	DOCKER_BUILDKIT=1 docker build . --target=final --output .