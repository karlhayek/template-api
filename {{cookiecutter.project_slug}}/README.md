# {{cookiecutter.project_name}}

This document provides a walkthrough to how to build Docker image containing the API, then run it in a container.

## Build The Docker Image

To build the docker image:

  ```sh
  $ sudo docker build -f Dockerfile -t <tag_name> .
  ```

## Run the Docker container

To run a container:

```sh
$ sudo docker run -p <port_of_your_choice>:5000 -v <path_to_tflite>/api/:/api/ <tag_name>
```
The API file will be run automatically, and the service will listen to http requests to the port you chose. To prevent this, remove "CMD ["python3", "api.py"]" from the Dockerfile.

## OpenAPI

To view the service's possible routes and their documentation, open <host_ip>:<chosen_port>.