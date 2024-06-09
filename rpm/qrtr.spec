Name:       qrtr
Version:    1.0+git21
Release:    0
Summary:    Qualcomm IPC router protocol implementation
License:    BSD-3-Clause
URL:        https://github.com/linux-msm/qrtr
Source0:    %{name}-%{version}.tar.gz
Source1:    qrtr.h

BuildRequires: meson
BuildRequires: systemd-devel

%description
Reference implementation of the QRTR (Qualcomm IPC Router) protocol
used by Qualcomm modems.

%prep
%setup -q -n %{name}-%{version}/qrtr

%build
mkdir -p include/linux
cp %{SOURCE1} include/linux
%meson --wipe
%meson_build

%install
mkdir -p %{buildroot}%{_includedir}/linux
cp %{SOURCE1} %{buildroot}%{_includedir}/linux
%meson_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/qrtr-*
%{_libdir}/libqrtr.so.*
%{_libdir}/systemd/system/*.service

%package kernel-headers
Summary:    Kernel headers for QRTR

%description kernel-headers
Kernel headers required by the QRTR reference implementation that are
not included in the default kernel-headers package.

%files kernel-headers
%defattr(-,root,root,-)
%{_includedir}/linux/qrtr.h

%package devel
Summary:    Development files for QRTR
Requires:   qrtr
Requires:   qrtr-kernel-headers

%description devel
Development files for use with the QRTR reference implementation.

%files devel
%defattr(-,root,root,-)
%{_includedir}/libqrtr.h
%{_libdir}/libqrtr.so
%{_libdir}/pkgconfig/*.pc
