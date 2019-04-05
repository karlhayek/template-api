# Template Dockerfile. Install more dependencies and run more commands as needed

FROM ubuntu:18.04

# Install python dependencies
RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  wget \
  pkg-config \
  && python3 -m pip install pip==19.0.3 \
  Pillow \
  werkzeug==0.14.1 \
  flask \
  flask_restplus

WORKDIR /"{{cookiecutter.project_slug}}"/
CMD ["python3", "src/api.py"]
