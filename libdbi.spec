Summary:	Database Independent Abstraction Layer for C
Summary(pl):	Warstwa DBI dla C
Name:		libdbi
Version:	0.6.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/libdbi/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
URL:		http://libdbi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
Requires:	%{name}-dbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of code,
programmers can leverage the power of multiple databases and multiple
simultaneous database connections by using this framework.

%description -l pl
libdbi jest implementacj± w C warstwy abstrakcyjnej niezale¿nej od
bazy danych, podobnej do warstwy DBI/DBD w Perlu. U¿ywaj±c tego
¶rodowiska programista mo¿e za pomoc± jednego, wspólnego kodu
odwo³ywaæ siê do wielu ró¿nych baz danych, tak¿e jednocze¶nie.

%package devel
Summary:	Development files for Database Independent Abstraction Layer for C
Summary(pl):	Pliki dla programistów u¿ywaj±cych warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libdbi-devel package contains the header files and documentation
needed to develop applications with libdbi.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i dokumentacjê do tworzenia
aplikacji z u¿yciem libdbi.

%package static
Summary:	Static Database Independent Abstraction Layer for C libraries
Summary(pl):	Statyczne biblioteki warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Database Independent Abstraction Layer for C libraries.

%description static -l pl
Statyczne biblioteki warstwy DBI w C.

%package dbd-mysql
Summary:	MySQL plugin for libdbi
Summary(pl):	Wtyczka MySQL dla libdbi
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-dbd

%description dbd-mysql
This plugin provides connectivity to MySQL database servers through
the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description dbd-mysql -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z serwerami MySQL poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%package dbd-pgsql
Summary:	PostgreSQL plugin for libdbi
Summary(pl):	Wtyczka PostgreSQL dla libdbi
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-dbd

%description dbd-pgsql
This plugin provides connectivity to PostgreSQL database servers
through the libdbi database independent abstraction layer. Switching a
program's plugin does not require recompilation or rewriting source
code.

%description dbd-pgsql -l pl
Ta wtyczka daje mo¿liwo¶æ ³±czenia siê z serwerami PostgreSQL poprzez
bibliotekê libdbi. Zmiana u¿ywanej wtyczki nie wymaga rekompilacji ani
zmiany ¼róde³ programu.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-mysql \
	--with-pgsql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README* TODO
%dir %{_libdir}/dbd
%attr(755,root,root) %{_libdir}/libdbi.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/programmers-guide
%{_libdir}/libdbi.la
%attr(755,root,root) %{_libdir}/libdbi.so
%{_includedir}/dbi

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbi.a
%{_libdir}/dbd/lib*.a

%files dbd-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dbd/libmysql.so
%{_libdir}/dbd/libmysql.la

%files dbd-pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dbd/libpgsql.so
%{_libdir}/dbd/libpgsql.la
