# Base image
FROM python:3.8.10

# Updating repository sources

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y \
        gcc \
        build-essential \
        zlib1g-dev \
        wget \
        unzip \
        cmake \
        python3-dev \
        gfortran \
        libblas-dev \
        liblapack-dev \
        libatlas-base-dev \
        pkg-config \
        libhdf5-dev \
	&& apt-get install ffmpeg libsm6 libxext6  -y \
    && apt-get clean

RUN pip install --upgrade pip
RUN pip install jupyter
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --find-links https://download.pytorch.org/whl/cu113/torch_stable.html
RUN git clone https://github.com/eleldar/Translator.git -b master


CMD jupyter notebook --no-browser --port=2527 --ip=0.0.0.0 --allow-root --NotebookApp.token='1'
