%define _requires_exceptions pear(f:
%define _provides_exceptions pear(f:

Summary:	SOAP Toolkit for PHP
Name:		nusoap
Version:	0.9.5
Release:	%mkrel 1
License:	LGPLv2.1+
Group:		Development/PHP
URL:		http://sourceforge.net/projects/nusoap/
Source0:	https://downloads.sourceforge.net/project/nusoap/%{name}/%{version}/%{name}-%{version}.zip
Source1:	https://downloads.sourceforge.net/project/nusoap/%{name}-docs/%{version}/%{name}-docs-%{version}.zip
BuildArch:	noarch
Requires:	php-pear

%description
NuSOAP is a rewrite of SOAPx4, provided by NuSphere and Dietrich Ayala. It is a
set of PHP classes - no PHP extensions required -  that allow developers to
create and consume web services based on SOAP 1.1, WSDL 1.1 and HTTP 1.0/1.1.

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

%files
%defattr(-,root,root)
%doc lib/changelog docs/* samples
%dir %{_datadir}/pear/nusoap
%{_datadir}/pear/nusoap/*php


%changelog
* Tue Feb 07 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.5-1mdv2012.0
+ Revision: 771620
- new version 0.9.5

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2010.0
+ Revision: 430190
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-1mdv2009.0
+ Revision: 239097
- 0.7.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.2-4mdv2008.0
+ Revision: 90012
- rebuild


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-3mdv2007.0
+ Revision: 113862
- Import nusoap

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-3mdv2007.1
- use the mkrel macro

* Fri Dec 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdk
- re-added into contrib (where did it go?)
- move it to /usr/share/pear/nusoap to make it easier

* Thu Oct 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-1mdk
- initial Mandriva package

