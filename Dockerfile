FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
python3 \
python3\
git\
curl\
&& rm -rf /var/lib/apt/lists/*


WORKDIR /workspace


CMD ["/bin/bash"]