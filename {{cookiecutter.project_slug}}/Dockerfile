FROM ubuntu:18.04

#install dependencies.
RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip \
  pkg-config \
  git-core \
  wget \
  && python3 -m pip install pip==19.0.3 \
  && pip3 install numpy \
  Pillow \
  flask \
  flask_restplus


WORKDIR /api/
CMD ["python3", "api.py"]
