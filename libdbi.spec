Summary:	Database Independent Abstraction Layer for C
Summary(pl):	Warstwa DBI dla C
Name:		libdbi
Version:	0.7.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
# Source0-md5:	d16eff24c26be4ff917d32d4ddb30da9
Patch0:		%{name}-opt.patch
URL:		http://libdbi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-dbd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdbi implements a database-independent abstraction layer in C,
similar to the DBI/DBD layer in Perl. Writing one generic set of code,
programmers can leverage the power of multiple databases and multiple
simultaneous database connections by using this framework.

%description -l pl
libdbi jest implementacj� w C warstwy abstrakcyjnej niezale�nej od
bazy danych, podobnej do warstwy DBI/DBD w Perlu. U�ywaj�c tego
�rodowiska programista mo�e za pomoc� jednego, wsp�lnego kodu
odwo�ywa� si� do wielu r�nych baz danych, tak�e jednocze�nie.

%package devel
Summary:	Development files for Database Independent Abstraction Layer for C
Summary(pl):	Pliki dla programist�w u�ywaj�cych warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libdbi-devel package contains the header files and documentation
needed to develop applications with libdbi.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe i dokumentacj� do tworzenia
aplikacji z u�yciem libdbi.

%package static
Summary:	Static Database Independent Abstraction Layer for C libraries
Summary(pl):	Statyczne biblioteki warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Database Independent Abstraction Layer for C libraries.

%description static -l pl
Statyczne biblioteki warstwy DBI w C.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dbd

%{__make} DESTDIR=$RPM_BUILD_ROOT install

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
%{_libdir}/libdbi.la
%attr(755,root,root) %{_libdir}/libdbi.so
%{_includedir}/dbi

%files static
%defattr(644,root,root,755)
%{_libdir}/libdbi.a
