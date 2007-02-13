#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Database Independent Abstraction Layer for C
Summary(pl.UTF-8):	Warstwa DBI dla C
Name:		libdbi
Version:	0.8.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
# Source0-md5:	72a3d26b410ffb428b7a02d6224075c1
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

%description -l pl.UTF-8
libdbi jest implementacją w C warstwy abstrakcyjnej niezależnej od
bazy danych, podobnej do warstwy DBI/DBD w Perlu. Używając tego
środowiska programista może za pomocą jednego, wspólnego kodu
odwoływać się do wielu różnych baz danych, także jednocześnie.

%package devel
Summary:	Development files for Database Independent Abstraction Layer for C
Summary(pl.UTF-8):	Pliki dla programistów używających warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libdbi-devel package contains the header files and documentation
needed to develop applications with libdbi.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i dokumentację do tworzenia
aplikacji z użyciem libdbi.

%package static
Summary:	Static Database Independent Abstraction Layer for C libraries
Summary(pl.UTF-8):	Statyczne biblioteki warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Database Independent Abstraction Layer for C libraries.

%description static -l pl.UTF-8
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
