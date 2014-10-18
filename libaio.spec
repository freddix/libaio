Summary:	Linux-native asynchronous I/O facility (aio) library
Name:		libaio
Version:	0.3.110
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.de.debian.org/debian/pool/main/liba/libaio/%{name}_%{version}.orig.tar.gz
# Source0-md5:	2a35602e43778383e2f4907a4ca39ab8
URL:		http://lse.sourceforge.net/io/aio.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AIO enables even a single application thread to overlap I/O operations
with other processing, by providing an interface for submitting one or
more I/O requests in one system call (io_submit()) without waiting for
completion, and a separate interface (io_getevents()) to reap
completed I/O operations associated with a given completion group.

%package devel
Summary:	Development files for AIO library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header and support files necessary to compile applications using AIO.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	prefix=$RPM_BUILD_ROOT%{_prefix}    \
	libdir=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %ghost %{_libdir}/libaio.so.1
%attr(755,root,root) %{_libdir}/libaio.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/libaio.h

