Summary:	Download and assemble multipart binaries from newsgroups
Summary(pl.UTF-8):	Ściąganie i łączenie wieloczęściowych binariów z grup dyskusyjnych
Name:		brag
Version:	1.4.3
Release:	2
License:	GPL
Group:		Applications/News
Source0:	http://dl.sourceforge.net/brag/%{name}-%{version}.tar.gz
# Source0-md5:	8d9317bb5a8e239e9593d5811c541dfa
Patch0:		%{name}-install.patch
URL:		http://brag.sourceforge.net/
Requires:	sharutils
Requires:	tcl >= 8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brag is command line tool to collect and assemble multipart binary
attachments from newsgroups. Ideal for regular news scanning using
cron. Supported message encodings: uuencode and MIME base64.

%description -l pl.UTF-8
Brag jest narzędziem uruchamianym z linii komend służącym do ściągania
i łączenia wieloczęściowych załączników binarnych z grup dyskusyjnych.
Jest idealny do regularnego skanowania grup przy wykorzystaniu crona.
Obsługuje następujące kodowania wiadomości: uuencode oraz MIME base64.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	ROOT="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/brag
%{_mandir}/man1/brag.1*
