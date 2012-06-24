Summary:	An image viewer and browser for GNOME
Summary(pl):	Przegl�darka obrazk�w dla GNOME
Name:		gnome-photo-printer
Version:	0.6.5
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://www.fogman.de/gpp/gpp-%{version}.tar.gz
# Source0-md5:	9a349f7fc2210dea0663f08d86cc5731
URL:		http://www.fogman.de/gpp/
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	pkgconfig >= 1:0.6.0
BuildRoot:	%{tmpdir}/gpp-%{version}-root-%(id -u -n)

%description
Gnome Photo Printer is intended for printing photos in an easy way.
Just drag your Photos from Nautilus to the Gnome Photo Printer window
and drop it. Make some selections like Photo or Paper size, hit
Preview or Print, and see your pictures printed.

%description -l pl
Gnome Photo Printer to program przeznaczony do �atwego drukowania
zdj��. Wystarczy przeci�gn�� zdj�cia z Nautilusa do okienka Gnome
Photo Printer i upu�ci� je. Po wybraniu paru rzeczy, takich jak
rozmiar zdj�cia lub papieru wystarczy wybra� podgl�d lub wydruk i
ogl�da� wydrukowane zdj�cia.

%prep
%setup -q -n gpp-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
