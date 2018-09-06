Summary:	An implementation of RFC3720 iSCSI
Name:		open-isns
Version:	0.98
Release:	1
License:	GPL
Group:		Networking/Other
Url:		http://www.open-iscsi.org
Source0:	https://github.com/open-iscsi/open-isns/archive/v%{version}.tar.gz
BuildRequires:	glibc-static-devel

%description
Open-iSCSI project is a high-performance, transport independent, multi-platform
implementation of RFC3720 iSCSI. iSCSI is a protocol for distributed disk
access using SCSI commands sent over Internet Protocol networks.

%package	devel
Summary:	devel package for %{name}

%description	devel
Headers for %{name}

%prep
%setup -q
%apply_patches

%build
autoconf
autoheader
%serverbuild
%configure
%make

%install
%makeinstall_std SYSTEMDDIR=%{buildroot}%{_systemunitdir} install_lib install_hdrs

%files
%{_systemunitdir}/isnsd.service
%{_systemunitdir}/isnsd.socket
%{_mandir}/man8/isns*
%{_mandir}/man5/isns*
%{_sysconfdir}/isns/*.conf
%{_sbindir}/isn*

%files devel
%{_includedir}/libisns/*.h
