# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Database Independent Abstraction Layer for C
Summary(pl):	Warstwa DBI dla C
Name:		libdbi
Version:	0.7.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
# Source0-md5:	308e5746a2d0804be1d638319ad7b9c0
Patch0:		%{name}-opt.patch
URL:		http://libdbi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Database Independent Abstraction Layer for C libraries.

%description static -l pl
Statyczne biblioteki warstwy DBI w C.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dbd

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{_libdir}/dbd
%attr(755,root,root) %{_libdir}/libdbi.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/programmers-guide
%attr(755,root,root) %{_libdir}/libdbi.so
%{_libdir}/libdbi.la
%{_includedir}/dbi

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdbi.a
%endif
