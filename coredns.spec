Name:       coredns
Version:    1
Release:    1
Summary:    CoreDNS is a DNS server that chains plugins 
License:    ASL 2.0
Source0:    coredns
Source1:    coredns.service
Source2:    coredns.default
Source3:    Corefile

%description
CoreDNS is a DNS server/forwarder, written in Go, that chains plugins. Each plugin performs a (DNS) function.

CoreDNS is a Cloud Native Computing Foundation graduated project.

%prep
%setup -c
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
%build

%install
rm -rf %{buildroot}
install -D -m 755 coredns %{buildroot}%{_bindir}/coredns
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/coredns/Corefile

install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/coredns.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/coredns

%clean
rm -rf %{buildroot}

%pre
getent group coredns >/dev/null || groupadd -r coredns
getent passwd coredns >/dev/null || \
  useradd -r -g coredns -s /sbin/nologin \
          -c "CoreDNS services" coredns
exit 0

%post
%systemd_post coredns.service

%preun
%systemd_preun coredns.service

%postun
%systemd_postun coredns.service

%files

%defattr(-,root,root,-)
%{_unitdir}/coredns.service
%{_bindir}/coredns
%config(noreplace) %{_sysconfdir}/coredns/Corefile
%config(noreplace) %{_sysconfdir}/sysconfig/coredns

%changelog
# let's skip this for now
