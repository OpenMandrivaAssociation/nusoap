%define __noautoreq 'pear(f:'
%define __noautoprov 'pear(f:'

Summary:	SOAP Toolkit for PHP
Name:		nusoap
Version:	0.9.5
Release:	4
License:	LGPLv2.1+
Group:		Development/PHP
Url:		https://sourceforge.net/projects/nusoap/
Source0:	https://downloads.sourceforge.net/project/nusoap/%{name}/%{version}/%{name}-%{version}.zip
Source1:	https://downloads.sourceforge.net/project/nusoap/%{name}-docs/%{version}/%{name}-docs-%{version}.zip
Requires:	php-pear
BuildArch:	noarch

%description
NuSOAP is a rewrite of SOAPx4, provided by NuSphere and Dietrich Ayala. It is a
set of PHP classes - no PHP extensions required -  that allow developers to
create and consume web services based on SOAP 1.1, WSDL 1.1 and HTTP 1.0/1.1.

%files
%doc lib/changelog docs/* samples
%dir %{_datadir}/pear/nusoap
%{_datadir}/pear/nusoap/*php

#----------------------------------------------------------------------------

%prep
%setup -q -c -a1

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

# strip away annoying ^M
find -type f -print0|xargs -0 file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find -type f -print0|xargs -0 file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

perl -pi -e "s|\(\'\.\.\/lib\/|\(\'%{_datadir}/pear/nusoap/|g" samples/*

mv lib/changelog lib/changelog.old
iconv -f ISO-8859-1 -t UTF-8 lib/changelog.old > lib/changelog

%build

%install
install -d %{buildroot}%{_datadir}/pear/nusoap
install -m0644 lib/*.php %{buildroot}%{_datadir}/pear/nusoap/

