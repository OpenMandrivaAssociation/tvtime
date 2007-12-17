%define name    tvtime
%define Name    TVtime
%define version 1.0.2
%define release %mkrel 5

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        High quality television application
Group:          Video
License:        GPLv2+ and LGPLv2+
URL:            http://tvtime.net/
Source0:        http://prdownloads.sourceforge.net/tvtime/%{name}-%{version}.tar.bz2
Patch0:         tvtime-1.0.2.buildfix.patch
# Build against system v4l / v4l2 headers rather than the obsolete
# ones included, which cause the build to fail - AdamW 2007/08
Patch1:		tvtime-1.0.2-v4lheaders.patch
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
%patch1 -p1 -b .v4l

%build
%configure
%make

%install
rm -fr %{buildroot}
%makeinstall ROOT=%{buildroot}

#xdg
mv %{buildroot}%{_datadir}/applications/net-%{name}.desktop \
%{buildroot}%{_datadir}/applications/%{name}.desktop

perl -pi -e 's/tvtime.png/tvtime/' \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
    --remove-category="Application" \
    --add-category="TV" \
    --add-category="Video" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%clean
rm -fr %{buildroot}

%post
%{update_menus}
%{update_icon_cache hicolor}

%postun
%{clean_menus}
%{clean_icon_cache hicolor}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%doc data/COPYING.FreeMonoBold data/COPYING.tvtimeSansBold docs/html
%{_bindir}/*
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/tvtime.xml
%{_datadir}/%{name}
# freedesktop stuff
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
