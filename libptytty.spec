Summary:	OS independent and secure pty/tty and utmp/wtmp/lastlog handling
Name:		libptytty
Version:	2.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://dist.schmorp.de/libptytty/%{name}-%{version}.tar.gz
# Source0-md5:	2a7f3f3c0d3ef71902da745dc7959529
URL:		http://software.schmorp.de/pkg/libptytty.html
BuildRequires:	cmake >= 3.6
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libptytty is an offspring of rxvt-unicode that handles
pty/tty/utmp/wtmp/lastlog handling in mostly OS-independent ways

%package devel
Summary:	Header files for the libptytty library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libptytty library.

%prep
%setup -q

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_libdir}/libptytty.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libptytty.so
%{_includedir}/libptytty.h
%{_pkgconfigdir}/libptytty.pc
%{_mandir}/man3/libptytty.3*
