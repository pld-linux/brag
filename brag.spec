Summary:	Download and assemble multipart binaries from newsgroups
Summary(pl):	¦ci±ganie i ³±czenie wieloczê¶ciowych binariów z news-grup
Name:		brag
Version:	1.1.0
Release:	2
License:	GPL
Group:		Applications/News
Source0:	http://prdownloads.sourceforge.net/brag/%{name}-%{version}.tar.gz
Patch0:		%{name}-install.patch
Patch1:		%{name}-tclsh.patch
Requires:	tcl >= 8.0
Requires:	sharutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brag is command line tool to collect and assemble multipart binary
attachements from newsgroups. Ideal for regular news scanning using
cron. Supported message encodings: uuencode and MIME base64.

%description -l pl
Brag jest narzêdziem uruchamianym z linii komend s³u¿±cym do ¶ci±gania
i ³±czenia wieloczê¶ciowych za³±czników binarnych z grup dyskusyjnych.
Jest idealny do regularnego skanowania grup przy wykorzystaniu crona.
Obs³uguje nastêpuj±ce kodowania wiadomo¶ci: uuencode oraz MIME base64.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install ROOT="$RPM_BUILD_ROOT"

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/brag
%{_mandir}/man1/brag.1*
