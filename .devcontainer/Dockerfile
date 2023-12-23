FROM python:3.11.4-slim-bullseye

ENV LANG=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONBUFFERED=1 \
    PYTHONPATH=/workspaces/LangChain_Agents_GitHub

# Set working directory
WORKDIR /opt/app

# Install packages and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    libbz2-dev \
    unzip \
    curl

# Copy files
COPY requirements.in install_dependencies.sh ./

# Install dependencies
RUN bash ./install_dependencies.sh ./requirements.in && \
    rm ./install_dependencies.sh ./requirements.in
