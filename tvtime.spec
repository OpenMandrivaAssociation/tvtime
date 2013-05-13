%define name    tvtime
%define Name    TVtime
%define version 1.0.2
%define release  17

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
Patch2:		tvtime-1.0.2-fix-str-fmt.patch
#from fedora
Patch3:		tvtime-1.0.2-localedef.patch
Patch4:		tvtime-1.0.2-videoinput.patch
# http://sourceforge.net/tracker/?func=detail&atid=506989&aid=1634306&group_id=64301
Patch5:     tvtime-1.0.2-savematte.patch
Patch6:		tvtime-1.0.2-png15.patch
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  freetype-devel
BuildRequires:  pkgconfig(sdl)
BuildRequires:	pkgconfig(xv)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xxf86vm)
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
%patch0 -p1
%patch1 -p1 -b .v4l
%patch2 -p0 -b .str
%patch3 -p1 -b .locale
%patch4 -p1 -b .videoinput
%patch5 -p1 -b .savematte
%patch6 -p1 -b .png15

%build
%configure2_5x
%make

%install
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
    --add-category="X-MandrivaLinux-CrossDesktop" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

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


%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 1.0.2-13mdv2011.0
+ Revision: 672757
- fix header

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-12mdv2011.0
+ Revision: 608045
- rebuild

* Sun Mar 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-11mdv2010.1
+ Revision: 526282
- apply sf.net patch to save matte setting (fix #58298)

* Wed Feb 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-10mdv2010.1
+ Revision: 503844
- add a patch from linux-uvc project to fix some issue with Philipps webcams (#57557)

* Mon Aug 24 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-9mdv2010.0
+ Revision: 420289
- o add patch from fedora to fix build
  o no need to run autoreconf

* Sat Apr 11 2009 Funda Wang <fwang@mandriva.org> 1.0.2-8mdv2009.1
+ Revision: 366390
- fix str fmt

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-7mdv2009.0
+ Revision: 225892
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-6mdv2008.1
+ Revision: 154063
- add X-MandrivaLinux-CrossDesktop catgeory to xdg menu (fix #36901)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Sep 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-5mdv2008.0
+ Revision: 92927
- fix icon specification in menu

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-4mdv2008.0
+ Revision: 76329
- rebuild for 2008
- don't package copying
- add crossdesktop xdg category so it will show in top level of menus (it's the best tv app for all desktops)
- drop old menu and icons
- add patch1 (fix build by using system v4l / v4l2 headers rather than the obsolete included ones)
- use Fedora license policy

  + Oden Eriksson <oeriksson@mandriva.com>
    - Import tvtime



* Wed Sep 06 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.0.2-3
- add BuildRequires: libxv-devel libxtst-devel libice-devel libsm-devel
                     libxinerama-devel libxxf86vm-devel desktop-file-utils

* Fri Jul 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-2mdv2007.0
- fix compilation
- xdg menu

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdk
- New release 1.0.2

* Thu Sep 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdk
- New release 1.0.1
- drop patch0

* Sat Jul 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.99-2mdk
- Fix Build with gcc4 ( patch from fedora )

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.99-1mdk
- New release 0.99
- spec cleanup

* Tue Nov 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.9.15-1mdk 
- New release 0.9.15
- updated description, additional filters no more useful

* Fri Oct 29 2004 Guillaume Rousse <guillomovitch@mandrakesoft.com> 0.9.14-1mdk
- New release 0.9.14

* Thu Nov 27 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.9.12-2mdk
- buildrequires libSDL-devel

* Tue Nov 25 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.12-1mdk
- new version

* Mon Nov 17 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.11-1mdk
- new version

* Sat Sep 13 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.10-3mdk
- included yet other missing doc files

* Sat Sep 13 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.10-2mdk
- dropped additional icons files, they are already present in tarball

* Sat Sep 13 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.10-1mdk
- 0.9.10
- removed included DScaler libraries
- updated description
- fixed menu entry  
- fixed URL
- fixed doc files
- used original icons
- added freedesktop files

* Fri Sep 05 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.9-1mdk
- 0.9.9

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.9.8.5-2mdk
- rebuild
- change summary macro to avoid possible conflicts if we were to build debug package

* Sat Jun 21 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 0.9.8.5-1mdk
- 0.9.8.5
- icon

* Fri May 09 2003 Laurent Culioli <laurent@pschit.net> 0.9.8.2-1mdk
- initial release
