Summary:	Download and assemble multipart binaries from newsgroups
Name:		brag
Version:	1.1.0
Release:	1
License:	GPL
Group:		Applications/News
Group(de):	Applikationen/News
Group(pl):	Aplikacje/News
Source0:	http://brag.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-install.patch
Requires:	tcl >= 8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Brag is command line tool to collect and assemble multipart binary
attachements from newsgroups. Ideal for regular news scanning using
cron. Supported message encodings: uuencode and MIME base64.

%prep
%setup -q
%patch0 -p1

%build

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
