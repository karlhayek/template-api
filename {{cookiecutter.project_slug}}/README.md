# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}.

## Build the Docker image

To build the docker image:

```sh
$ docker build -t <tag_name> .
```
The Dockerfile installs the project's dependencies.

## Run the Docker container

To run the built image in a container, mounting the local `app/` directory to the container in `/app/`:

```sh
$ docker run -p <port_of_your_choice>:5000 -v $(pwd)/app:/app <tag_name>
```

The API file will be run automatically, and the service will listen to HTTP requests to the chosen port.

## OpenAPI

To view the service's possible routes and their documentation using the OpenAPI standard, open `<host_ip>:<port_of_your_choice>/docs` after running the docker image.

## Testing

Unit tests can be written in `src/test_api.py` and ran using `$ pytest src/`.


## Directory Structure

```
├── Dockerfile          -- Dockerfile for building a Docker image where API is run
├── Dockerfile_TF_GPU   -- Dockerfile for building an image that uses Tensorflow and runs it on GPU
├── README.md           -- Existential crisis
|
└── app/                -- Directory that contains the API code
    ├── main.py             -- API code for the server to listen to requests and execute commands 
    ├── model_utils.py      -- Classes and functions that deal with machine learning
    ├── utils.py            -- Functions that perform miscellaneous tasks (IO, etc.)
    ├── test_api.py         -- Unit tests for the API 
    └── models/             -- Directory for storing models. The project boilerplate contains a sample model config for the simple example API
```