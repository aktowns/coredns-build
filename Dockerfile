FROM registry.access.redhat.com/ubi8/ubi:8.4

RUN dnf install -y unbound-devel golang git

ENV CGO_ENABLED=1

ENTRYPOINT ["bash"]
