#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%if "%{pld_release}" == "ti"
%bcond_with	doc		# build documentation
%else
%bcond_with	doc		# build documentation
%endif

%define		subver	20100921
%define		rel		1
Summary:	Database Independent Abstraction Layer for C
Summary(pl.UTF-8):	Warstwa abstrakcji baz danych dla C
Name:		libdbi
Version:	0.9.0
Release:	0.%{subver}.%{rel}
License:	LGPL v2+
Group:		Libraries
#Source0:	http://dl.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
Source0:	%{name}-%{subver}.tar.gz
# Source0-md5:	451346912fdd1c8f66c5942d7f9a99b3
URL:		http://libdbi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
%if %{with doc}
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	jadetex
BuildRequires:	openjade
%if "%{pld_release}" == "ti"
BuildRequires:	tetex-fonts-ams
BuildRequires:	tetex-fonts-stmaryrd
BuildRequires:	tetex-fonts-type1-urw
%else
BuildRequires:	texlive-fonts-ams
BuildRequires:	texlive-fonts-marvosym
BuildRequires:	texlive-fonts-stmaryrd
BuildRequires:	texlive-fonts-type1-urw
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-latex-extend
BuildRequires:	texlive-latex-wasysym
BuildRequires:	texlive-xetex
BuildRequires:	texlive-xmltex
%endif
%endif
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
The libdbi-devel package contains the header files needed to develop
applications with libdbi.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji z użyciem
libdbi.

%package static
Summary:	Static Database Independent Abstraction Layer for C libraries
Summary(pl.UTF-8):	Statyczne biblioteki warstwy DBI w C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Database Independent Abstraction Layer for C libraries.

%description static -l pl.UTF-8
Statyczne biblioteki warstwy DBI w C.

%package doc
Summary:	Documentation for Database Independent Abstraction Layer for C
Summary(pl.UTF-8):	Dokumentacja dla programistów używających warstwy DBI w C
Group:		Documentation

%description doc
Documentation for Database Independent Abstraction Layer for C.

%description devel -l pl.UTF-8
Dokumentacja dla programistów używających warstwy DBI w C.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static} \
	%{!?with_doc:--disable-docs}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/dbd,%{_pkgconfigdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_pkgconfigdir}/dbi.pc <<'EOF'
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/dbi

Name: libdbi
Description: database-independent abstraction layer in C
Version: %{version}
Libs: -L${libdir} -ldbi
Cflags: -I${includedir} -I${includedir}/dbi
EOF

%if %{with doc}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libdbi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbi.so.1
%dir %{_libdir}/dbd

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbi.so
%{_libdir}/libdbi.la
%{_includedir}/dbi
%{_pkgconfigdir}/dbi.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdbi.a
%endif

%if %{with doc}
%files doc
%doc doc/driver-guide doc/driver-guide.pdf doc/programmers-guide doc/programmers-guide.pdf
%endif
