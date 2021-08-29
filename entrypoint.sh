#!/usr/bin/env bash

git clone https://github.com/coredns/coredns.git
pushd coredns
git checkout $VERSION

echo "unbound:github.com/coredns/unbound"     >> plugin.cfg
echo "mdns:github.com/openshift/coredns-mdns" >> plugin.cfg

go get github.com/coredns/unbound
go get github.com/openshift/coredns-mdns

go generate
go build
cp coredns /el8/SOURCES

popd
pushd el8

rpmbuild --undefine=_disable_source_fetch -ba \
	--verbose /el8/SPECS/coredns.spec \
	--define "_topdir /el8" --define "dist $(redhat-packages-dist)"

popd
