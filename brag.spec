Summary:	Download and assemble multipart binaries from newsgroups
Name:		brag
Version:	1.1.0
Release:	1
License:	GPL
Group:		Applications/News
Source:		http://brag.sourceforge.net/%{name}-%{version}.tar.gz
Patch:		brag-install.patch
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
%{__make} ROOT="$RPM_BUILD_ROOT" install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/brag.1 CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.gz README.gz
%attr(755,root,root) %{_bindir}/brag
%{_mandir}/man1/brag.1*
