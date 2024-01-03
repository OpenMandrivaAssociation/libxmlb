%define major 2

Summary:	Library for querying compressed XML metadata
Name:		libxmlb
Version:	0.3.15
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		https://github.com/hughsie/libxmlb
Source0:    https://github.com/hughsie/libxmlb/releases/download/%{version}/libxmlb-%{version}.tar.xz
#Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(uuid)
BuildRequires:	meson
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(libzstd)
# needed for the self tests
BuildRequires:	pkgconfig(shared-mime-info)
Requires:	shared-mime-info

%description
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

This allows an application to mmap the binary XML file, do an XPath query and
return some strings without actually parsing the entire document. This is all
done using (almost) zero allocations and no actual copying of the binary data.

%libpackage xmlb %{major}

%package devel
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{name} = %{EVRD}

%description devel
Files for development with %{name}.

%prep
%autosetup -p1

%build
%meson \
    -Dgtkdoc=true \
    -Dtests=false

%meson_build

%check
%meson_test

%install
%meson_install
rm -rf %{buildroot}%{_datadir}/installed-tests

%files
%doc README.md
%license LICENSE
%{_bindir}/xb-tool
%{_libdir}/girepository-1.0/*.typelib
%doc %{_mandir}/man1/xb-tool.1*

%files devel
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libxmlb
%{_includedir}/libxmlb-%{major}
%{_libdir}/libxmlb.so
%{_libdir}/pkgconfig/xmlb.pc
