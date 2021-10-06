Summary:	GNOME Text Editor
Summary(pl.UTF-8):	Edytor tekstowy dla GNOME
Name:		gnome-text-editor
Version:	41.1
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-text-editor/41/%{name}-%{version}.tar.xz
# Source0-md5:	c8aa02bbfc3e94887b7d3d5f3122f042
URL:		https://gitlab.gnome.org/GNOME/gnome-text-editor
BuildRequires:	enchant2-devel >= 2.2.0
BuildRequires:	glib2-devel >= 1:2.69
BuildRequires:	gtk4-devel >= 4.3
BuildRequires:	gtksourceview5-devel >= 5.0
BuildRequires:	libadwaita-devel >= 1.1.0-0.20210927
BuildRequires:	libicu-devel
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	enchant2 >= 2.2.0
Requires:	glib2 >= 1:2.69
Requires:	gtk4 >= 4.3
Requires:	libadwaita >= 1.1.0-0.20210927
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

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%{_datadir}/appdata/org.gnome.TextEditor.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.TextEditor.service
%{_datadir}/glib-2.0/schemas/org.gnome.TextEditor.gschema.xml
%{_desktopdir}/org.gnome.TextEditor.desktop
%{_iconsdir}/hicolor/scalable/actions/document-modified-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.TextEditor.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.TextEditor-symbolic.svg
