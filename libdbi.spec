Summary:	Database Independent Abstraction Layer for C
Name:		libdbi
Version:	0.6
Release:	1
License:	LGPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	http://prdownloads.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
URL:		http://libdbi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	libtool
BuildRequires:	postgresql-devel
Requires:	%{name}-dbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of code,
programmers can leverage the power of multiple databases and multiple
simultaneous database connections by using this framework.

%package devel
Summary:	Development files for Database Independent Abstraction Layer for C
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}-%{release}

%description devel
The libdbi-devel package contains the header files and documentation
needed to develop applications with libdbi.

%package static
Summary:	Static Database Independent Abstraction Layer for C libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static Database Independent Abstraction Layer for C libraries.

%package dbd-mysql
Summary:	MySQL plugin for libdbi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-dbd

%description dbd-mysql
This plugin provides connectivity to MySQL database servers through
the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%package dbd-pgsql
Summary:	PostgreSQL plugin for libdbi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-dbd

%description dbd-pgsql
This plugin provides connectivity to PostgreSQL database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%prep
%setup -q

%build
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure \
	--with-mysql \
	--with-pgsql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README* TODO

%clean 
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_libdir}/dbd
%attr(755,root,root) %{_libdir}/libdbi.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/programmers-guide
%{_libdir}/libdbi.a
%attr(755,root,root) %{_libdir}/libdbi.la
%attr(755,root,root) %{_libdir}/libdbi.so
%{_includedir}/dbi

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbi.a
%{_libdir}/dbd/lib*.a

%files dbd-mysql
%defattr(644,root,root,755)
%{_libdir}/dbd/libmysql.so

%files dbd-pgsql
%defattr(644,root,root,755)
%{_libdir}/dbd/libpgsql.so
