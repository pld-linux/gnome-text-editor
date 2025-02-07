# TODO: use gtk4-update-icon-cache
Summary:	GNOME Text Editor
Summary(pl.UTF-8):	Edytor tekstowy dla GNOME
Name:		gnome-text-editor
Version:	47.3
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-text-editor/47/%{name}-%{version}.tar.xz
# Source0-md5:	b5456e3751a24396e4d712001bb59c90
Patch0:		%{name}-no-update.patch
URL:		https://gitlab.gnome.org/GNOME/gnome-text-editor
BuildRequires:	cairo-devel
BuildRequires:	editorconfig-devel
BuildRequires:	glib2-devel >= 1:2.80
BuildRequires:	gtk4-devel >= 4.15
BuildRequires:	gtksourceview5-devel >= 5.10.0
BuildRequires:	libadwaita-devel >= 1.6
BuildRequires:	libicu-devel
BuildRequires:	libspelling-devel >= 0.3.0
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.80
Requires:	gtk4 >= 4.15
Requires:	gtksourceview5 >= 5.10.0
Requires:	libadwaita >= 1.6
Requires:	libspelling >= 0.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Text Editor is a simple text editor that focus on session
management. It works hard to keep track of changes and state even if
you quit the application. You can come back to your work even if
you've never saved it to a file.

%description -l pl.UTF-8
GNOME Text Editor to prosty edytor tekstowy, skupiający się na
zarządzaniu sesją. Usilnie stara się śledzić zmiany i stan, nawet
przy zamknięciu aplikacji. Można wrócić do pracy nawet, jeśli nigdy
nie została zapisana do pliku.

%prep
%setup -q
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-text-editor
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_datadir}/gnome-text-editor
%{_datadir}/metainfo/org.gnome.TextEditor.appdata.xml
%{_desktopdir}/org.gnome.TextEditor.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.TextEditor.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.TextEditor-symbolic.svg
