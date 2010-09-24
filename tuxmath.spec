# FIXME: the failing code is complex, I don't know how to fix it -
# AdamW 2009/01
%define Werror_cflags	%nil

%define	fname	tuxmath_w_fonts

# Summary and description stolen from Debian, thanks - AdamW 2009/01

Summary:	Math game for kids with Tux
Name:		tuxmath
Version:	1.8.0
Release:	%{mkrel 1}
# have to change with each new release as the number after download.php changes :(
Source0:	http://alioth.debian.org/frs/download.php/2684/%{fname}-%{version}.tar.gz
URL:		http://alioth.debian.org/frs/?group_id=31080
License:	GPLv2+
Group:		Games/Other
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_Pango-devel
BuildRequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
"Tux, of Math Command" ("TuxMath", for short) is an educational arcade
game starring Tux, the Linux mascot! Based on the classic arcade game
"Missile Command", Tux must defend his cities. In this case, though,
he must do it by solving math problems. 

%prep
%setup -q -n %{fname}-%{version}
# Fix incorrect paths hardcoded into the source (#46417) - AdamW
sed -i -e 's,/usr/share/fonts/truetype/ttf-.*/,%{_gamesdatadir}/%{name}/fonts/,g' src/loaders.c

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

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}admin
%{_gamesbindir}/%{name}server
%{_gamesbindir}/%{name}testclient
%{_gamesbindir}/generate_lesson
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

