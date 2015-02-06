# FIXME: the failing code is complex, I don't know how to fix it -
# AdamW 2009/01
%define Werror_cflags	%nil

%define	fname	tuxmath_w_fonts

# Summary and description stolen from Debian, thanks - AdamW 2009/01

Summary:	Math game for kids with Tux
Name:		tuxmath
Version:	2.0.3
Release:	2
# have to change with each new release as the number after download.php changes :(
Source:		http://alioth.debian.org/frs/download.php/3571/%{fname}-%{version}.tar.gz
URL:		http://alioth.debian.org/frs/?group_id=31080
License:	GPLv3+
Group:		Games/Other
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_Pango-devel
BuildRequires:	SDL_net-devel
BuildRequires:	librsvg-devel
BuildRequires:	pkgconfig(t4k_common)
BuildRequires:	imagemagick

%description 
"Tux, of Math Command" ("TuxMath", for short) is an educational arcade
game starring Tux, the Linux mascot! Based on the classic arcade game
"Missile Command", Tux must defend his cities. In this case, though,
he must do it by solving math problems. 

%prep
%setup -q -n %{fname}-%{version}

# Fix incorrect paths hardcoded into the source (#46417) - AdamW
#sed -i -e 's,/usr/share/fonts/truetype/ttf-.*/,%{_gamesdatadir}/%{name}/fonts/,g' src/loaders.c

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -fr %{buildroot}%{_prefix}/doc

install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=TuxMath
Comment=Math game for kids with Tux
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;KidsGame;Educational;
EOF

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert -scale 16x16 data/images/icons/%{name}.ico %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -scale 32x32 data/images/icons/%{name}.ico %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 48x48 data/images/icons/%{name}.ico %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS doc/changelog doc/README* doc/TODO*
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}admin
%{_gamesbindir}/%{name}server
%{_gamesbindir}/%{name}testclient
%{_gamesbindir}/generate_lesson
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Fri Dec 24 2010 Jani Välimaa <wally@mandriva.org> 1.9.0-1mdv2011.0
+ Revision: 624614
- new version 1.9.0
- fix license
- drop support for old and unsupported mdv releases

* Fri Sep 24 2010 Funda Wang <fwang@mandriva.org> 1.8.0-1mdv2011.0
+ Revision: 580865
- BR rsvg
- BR SDL_net
- new version 1.8.0

* Mon Sep 28 2009 Antoine Ginies <aginies@mandriva.com> 1.7.2-2mdv2010.0
+ Revision: 450503
- bump release

* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 1.7.2-1mdv2010.0
+ Revision: 374066
- Update to new version 1.7.2

* Sat Jan 03 2009 Adam Williamson <awilliamson@mandriva.org> 1.7.0-1mdv2009.1
+ Revision: 323565
- import tuxmath


