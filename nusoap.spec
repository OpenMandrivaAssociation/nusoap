%define _requires_exceptions pear(f:
%define _provides_exceptions pear(f:

Summary:	NuSOAP - SOAP Toolkit for PHP
Name:		nusoap
Version:	0.7.2
Release:	%mkrel 3
License:	LGPL
Group:		Development/PHP
URL:		http://sourceforge.net/projects/nusoap/
Source0:	http://prdownloads.sourceforge.net/nusoap/nusoap-%{version}.zip
Source1:	http://prdownloads.sourceforge.net/nusoap/nusoap-docs-%{version}.zip
BuildArch:	noarch
Requires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
NuSOAP is a rewrite of SOAPx4, provided by NuSphere and Dietrich Ayala. It is a
set of PHP classes - no PHP extensions required -  that allow developers to
create and consume web services based on SOAP 1.1, WSDL 1.1 and HTTP 1.0/1.1.

%prep

%setup -q -c -n %{name}-%{version} -a1

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

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/nusoap
install -m0644 lib/*.php %{buildroot}%{_datadir}/pear/nusoap/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc lib/changelog docs/* samples
%dir %{_datadir}/pear/nusoap
%{_datadir}/pear/nusoap/*php


