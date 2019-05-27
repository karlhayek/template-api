# Template Dockerfile. Install more dependencies and run more commands as needed

FROM ubuntu:19.04

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


# Copy the app code into the image
ADD ./app $HOME/app

# Run the app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]