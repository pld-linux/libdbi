Summary:	Database Independent Abstraction Layer for C
Name:		libdbi
Version:	0.5
Release:	1
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
License:	LGPL
URL:		http://libdbi.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
BuildRequires: postgresl-devel
BuildRequires: mysql-devel
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

%package dbd-mysql
Summary:	MySQL plugin for libdbi
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}-%{release}, mysqlclient9 >= 3.23.22

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
Requires:	%{name} = %{version}-%{release}, postgresql >= 7.0.3

%description dbd-pgsql
This plugin provides connectivity to PostgreSQL database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%prep
%setup -q

%build
aclocal
automake -a -c
autoconf
%configure --with-mysql --with-pgsql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README PLUGINS TODO

%clean 
rm -rf $RPM_BUILD_ROOT

%post /sbin/ldconfig

%postun /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/libdbi.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/programmers-guide
%{_includedir}/dbi/dbi.h
%{_includedir}/dbi/dbi-dev.h
%{_includedir}/dbi/dbd.h
%{_libdir}/libdbi.a
%{_libdir}/libdbi.la
%{_libdir}/libdbi.so

%files dbd-mysql
%defattr(644,root,root,755)
%{_libdir}/dbd/libmysql.so
%{_libdir}/dbd/libmysql.la

%files dbd-pgsql
%defattr(644,root,root,755)
%{_libdir}/dbd/libpgsql.so
%{_libdir}/dbd/libpgsql.la
