Summary:	A missile command clone
Summary(pl):	Klon missile command
Name:		penguin-command
Version:	1.5.0
Release:	1
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.linux-games.com/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Icon:		%{name}.xpm
URL:		http://www.linux-games.com
License:	GPL
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is a clone of the classic "Missile Command" Game, but it has
better graphics and music. You have to defend cities by shooting at
missiles and smartbombs.


%description -l pl
To jest klon klasycznej gry "Missile Command", lecz ma lepsz± grafikê
i muzykê. Musisz obroniæ miasta strzelaj±c pociskami i bombami.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
install data/gfx/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf NEWS README AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
