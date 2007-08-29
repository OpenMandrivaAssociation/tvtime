%define name    tvtime
%define Name    TVtime
%define version 1.0.2
%define release %mkrel 3
%define title       TvTime
%define longtitle   High quality television application

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        High quality television application
Group:          Video
License:        GPL
URL:            http://tvtime.net/
Source0:        http://prdownloads.sourceforge.net/tvtime/%{name}-%{version}.tar.bz2
Patch0:         %{name}-1.0.2.buildfix.patch
BuildRequires:  libx11-devel
BuildRequires:  libxml2-devel
BuildRequires:  libpng-devel
BuildRequires:  freetype2-devel
BuildRequires:  libSDL-devel
BuildRequires:	libxv-devel
BuildRequires:	libxtst-devel
BuildRequires:	libice-devel
BuildRequires:	libsm-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	desktop-file-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Tvtime is a high quality television application for use with video
capture cards.  tvtime processes the input from a capture card and
displays it on a computer monitor or projector.  Unlike other television
applications, tvtime focuses on high visual quality making it ideal for
videophiles.

  tvtime supports:

  o   Deinterlaced output at full interlaced rate of 59.94 frames per
      second for NTSC source, or 50 frames per second for PAL sources.
      This gives smoothness of motion and high visual quality.

  o   Multiple deinterlacing algorithms for finding the optimal mode for
      your video content and available processor speed.

  o   16:9 aspect ratio mode for the highest available resolution when
      processing input from an external DVD player or digital satellite
      receiver.

  o   A super-slick on-screen-display for the complete television
      experience, with a featureful menu system.

  o   2-3 Pulldown detection for optimal quality viewing of film content
      from NTSC sources.

%prep
%setup -q
%patch0 -p 1

%build
%configure
%make

%install
rm -fr %{buildroot}
%makeinstall ROOT=%{buildroot}

# icons
install -D -m 644 docs/%{name}.48x48.png %{buildroot}%{_liconsdir}/%{name}.png 
install -D -m 644 docs/%{name}.32x32.png %{buildroot}%{_iconsdir}/%{name}.png 
install -D -m 644 docs/%{name}.16x16.png %{buildroot}%{_miconsdir}/%{name}.png
# menu entry
install -d -m 755 %{buildroot}%{_menudir}
cat >%{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}):\
    command="%{_bindir}/%{name}"\
    needs="X11"\
    icon="%{name}.png"\
    section="Multimedia/Video"\
    title="%{title}"\
    longtitle="%{longtitle}" \
    xdg="true"
EOF

#xdg
mv %{buildroot}%{_datadir}/applications/net-%{name}.desktop \
%{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="TV" \
    --add-category="X-MandrivaLinux-Multimedia-Video" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -fr %{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc data/COPYING.FreeMonoBold data/COPYING.tvtimeSansBold docs/html
%{_bindir}/*
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/tvtime.xml
%{_datadir}/%{name}
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
# freedesktop stuff
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
