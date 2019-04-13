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
  pytest \
  fastapi[all]

WORKDIR /"{{cookiecutter.project_slug}}/src"/
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]