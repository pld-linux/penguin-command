Summary:	A missile command clone
Summary(pl):	Klon missile command
Name:		penguin-command
Version:	1.6.10
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/penguin-command/%{name}-%{version}.tar.gz
# Source0-md5:	84ac5c85ea7d832b94e2ac1d5b363a43
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.linux-games.com/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
