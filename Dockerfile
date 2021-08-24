FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    build-essential \
    python-dev \
    git \
    python3-pip

RUN mkdir -p /usr/spacy

ENV LANG             en_core_web_sm
ENV SPACY_VERSION    3.0.1

RUN pip3 install --upgrade pip setuptools

########################################
# spaCy
########################################
RUN pip3 install spacy==${SPACY_VERSION}
RUN python3 -m spacy download ${LANG}

# Check whether the model was successfully installed
# RUN python3 /usr/spacy/test/load_lang.py
###################

COPY . /usr/spacy/
WORKDIR /usr/spacy

CMD ["python3","app.py"]