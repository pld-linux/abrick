Summary:	Abandoned Bricks is SDL based tetris clone
Summary(hu.UTF-8):	Egy Tetris-klón
Summary(pl.UTF-8):	Abandoned Bricks to gra typu tetris oparta o SDL
Name:		abrick
Version:	1.12
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/project/abrick/abrick/abrick-1.12/%{name}-%{version}-src.tar.gz
# Source0-md5:	56bdb952e2c247abfccf6e4a5251753c
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-paths.patch
Patch2:		%{name}-usage.patch
URL:		http://abrick.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abandoned Bricks is yet anonther teris clone. It has SDL-based
interface.

For single player game there are three game modes. In Classic mode you
start each level with clean screen. In Challenge mode you start levels
with some garbage at bottom, and you only have two brick types
(shapes) for the level. In Bastet mode you start levels with clean
screen. You always get the worst possible brick for the moment, and
next brick preview is not available. You get 20 points for each brick,
and high bonuses for lines.

In two player games (duel), the goal is to remain the only one still
playing. When you drop more than one line, the other player gets
additional garbage lines at the bottom. For two lines he gets one, for
three he gets two and for four he gets three (in short: what you've
dropped minus one).

%description -l pl.UTF-8
Abandoned Bricks jest kolejnym klonem gry tetris. Interface gry
wykorzystuje bibliotekę SDL.

Dla jednego gracza są dostępne trzy tryby gry: "Klasyczny" w którym
każdy poziom gracz rozpoczyna z czystym ekranem, "Wyzwanie" w którym
każdy poziom na początku jest zaśmiecony pewną ilością klocków, oraz
są dostępne tylko dwa typy klocków oraz "Bastet" w którym gra dobiera
zawsze najgorszy klocek w danej sytuacji.

Dla dwóch graczy celem gry jest przetrwać w grze dłużej niż
przeciwnik. Jeżeli jednemu graczowi uda się usunąć więcej niż jedną
linię, przeciwnik otrzymuje dodatkowe śmieci.

%prep
%setup -q -n %{name}-%{version}-src

# undos sources
%{__sed} -i -e 's,\r$,,' *.cpp *.h

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/var/games/abrick,%{_bindir},%{_datadir}}
install abrick $RPM_BUILD_ROOT%{_bindir}/abrick
touch $RPM_BUILD_ROOT/var/games/abrick/hiscore.dat
cp -a data $RPM_BUILD_ROOT%{_datadir}/abrick

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/abrick
%dir %attr(775,root,games) /var/games/abrick
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/abrick/hiscore.dat
