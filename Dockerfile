FROM registry.access.redhat.com/ubi8/ubi:8.4

RUN dnf install -y unbound-devel golang git rpm-build

VOLUME /out

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN mkdir /el8 /el8/SPECS /el8/SOURCES

COPY coredns.default /el8/SOURCES
COPY coredns.service /el8/SOURCES
COPY coredns.spec /el8/SPECS

ENV CGO_ENABLED=1
ENV VERSION=v1.8.4

ENTRYPOINT ["/entrypoint.sh"]
