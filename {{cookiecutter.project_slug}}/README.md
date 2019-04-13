# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}.

The following provides a walkthrough on how to build a Docker image containing the API, then run it in a container.

## Build The Docker Image

To build the docker image:

```sh
$ docker build -f Dockerfile -t <tag_name> .
```

## Run the Docker container

To run the built image in a container:

```sh
$ docker run -p 1111:5000 --mount src="$(pwd)",target=/{{cookiecutter.project_slug}},type=bind <tag_name>
```

The API file will be run automatically, and the service will listen to http requests on port 1111.

## OpenAPI

To view the service's possible routes and their documentation using the OpenAPI standard, open `localhost:1111/docs` after running the docker image.

## Testing

Unit tests can be written in `src/test_api.py` and ran using `$ pytest src/`