# Template Dockerfile. Install more dependencies and run more commands as needed

FROM ubuntu:18.04

# Install OS packages
RUN apt-get update --no-install-recommends && apt-get install -y \
  locales \
  python3 \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN python3 -m pip install \
  Pillow \
  pytest \
  # fastapi dependencies
  fastapi[all]
  # project dependencies


# Set the locale (required for click, a dependency of FastAPI, on ubuntu 18)
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8 

# Run the app
WORKDIR /app
CMD uvicorn main:app --host 0.0.0.0 --port 5000