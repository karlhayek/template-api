# Template Dockerfile. Install more dependencies and run more commands as needed

FROM ubuntu:18.04

# Install python dependencies
RUN apt-get update && apt-get install -y \
  locales \
  python3 \
  python3-pip \
  wget \
  pkg-config \
  && python3 -m pip install pip==19.0.3 \
  Pillow \
  pytest \
  # fastapi dependencies
  fastapi[all]
  # project dependencies


# Set the locale (required for uvicorn)
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8 

WORKDIR /"{{cookiecutter.project_slug}}/src"/
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]