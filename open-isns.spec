%define major	0
%define libname	%mklibname open-isns %{major}
%define devname	%mklibname -d open-isns

Summary:	An implementation of RFC4171 iSNS
Name:		open-isns
Version:	0.99
Release:	1
License:	GPL
Group:		Networking/Other
Url:		http://www.open-iscsi.org
Source0:	https://github.com/open-iscsi/open-isns/archive/v%{version}.tar.gz
BuildRequires:	glibc-static-devel
BuildRequires:	openssl-devel

%description
This is a partial implementation of iSNS, according to RFC4171.
The implementation is still somewhat incomplete, but I'm releasing
it for your reading pleasure.

%package -n	%{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n	%{libname}
This is a partial implementation of iSNS, according to RFC4171.
The implementation is still somewhat incomplete, but I'm releasing
it for your reading pleasure.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
autoconf
autoheader
%serverbuild
%configure --enable-shared
%make

%install
%makeinstall_std SYSTEMDDIR=%{buildroot}%{_unitdir} install_lib install_hdrs

%files
%{_unitdir}/isnsd.service
%{_unitdir}/isnsd.socket
%{_mandir}/man8/isns*
%{_mandir}/man5/isns*
%{_sysconfdir}/isns/*.conf
%{_sbindir}/isn*

%files -n %{libname}
%{_libdir}/libisns.so.%{major}*

%files -n %{devname}
%{_includedir}/libisns/*.h
%{_libdir}/libisns.so
