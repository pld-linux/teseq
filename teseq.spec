#
# TODO:
# - better place for teseq-post.sed ?
#
Summary:	Tool for analyzing control characters
Summary(pl.UTF-8):	Narzędzie do analizy znaków kontrolnych
Name:		teseq
Version:	1.0.0
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://ftp.gnu.org/gnu/teseq/%{name}-%{version}.tar.bz2
# Source0-md5:	a9d7338d2ac22f2e4b5c44c8f34ffb65
URL:		http://www.gnu.org/software/teseq/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.10.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Teseq is a tool for analyzing files that contain control
characters and terminal control sequences. It is intended to be useful
for diagnosing terminal emulators and programs that make heavy use of
terminal features (such as those based on the Curses library). It is
primarily targeted at individuals who possess a basic understanding of
terminal control sequences, especially CSI sequences. However, by
default Teseq will try to identify and describe the sequences that it
encounters and the behavior they might produce in a terminal.

%description -l pl.UTF-8
GNU Teseq to narzędzie do analizy plików zawierających znaki kontrolne
oraz sekwencje kontrolne terminali. W zamierzeniu ma być to narzędzie
przydatne do diagnozowania emulatorów terminali i programów
korzystających z możliwości terminali (np. tych opartych na bibliotece
curses). Program skierowany jest do osób posiadających podstawową
wiedzę o sekwencjach kontrolnych terminali, w szczególności o
sekwencjach CSI. Domyślnie Teseq spróbuje zidentyfikować i opisać
napotkane sekwencje oraz zachowanie jakie mogą one spowodować w
terminalu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/teseq-post.sed
%{_mandir}/man1/[tr]eseq.1*
%{_infodir}/teseq.info*
