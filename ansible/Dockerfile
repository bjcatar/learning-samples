FROM ubuntu

RUN apt update -y && apt install -y --no-install-recommends \
    acl \
    apache2 \
    asciidoc \
    bzip2 \
    cdbs \
    curl \
    debhelper \
    debianutils \
    devscripts \
    docbook-xml \
    dpkg-dev \
    fakeroot \
    gawk \
    gcc \
    git \
    libffi-dev \
    libssl-dev \
    libxml2-utils \
    locales \
    make \
    mercurial \
    mysql-server \
    openssh-client \
    openssh-server \
    python-dev \
    pass \
    python-httplib2 \
    python-jinja2 \
    python-keyczar \
    python-lxml \
    python-mock \
    python-mysqldb \
    python-nose \
    python-paramiko \
    python-passlib \
    python-pip \
    python-setuptools \
    python-virtualenv \
    python-yaml \
    reprepro \
    rsync \
    ruby \
    sshpass \
    subversion \
    sudo \
    unzip \
    xsltproc \
    zip \
    vim

RUN pip install pip --upgrade
RUN pip install --upgrade pycrypto cryptography

RUN pip install ansible

RUN adduser --gecos "" --disabled-password ubuntu
RUN usermod -aG sudo ubuntu
RUN echo "ubuntu ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu
RUN chmod 0440 /etc/sudoers.d/ubuntu

WORKDIR /home/ubuntu

RUN mkdir /home/ubuntu/.ssh
COPY ./gh_dev_ohio.pem /home/ubuntu/.ssh/
RUN chown -R ubuntu:ubuntu /home/ubuntu

USER ubuntu
RUN mkdir ansible
