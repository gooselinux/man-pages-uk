%define date 20071108
Name: man-pages-uk
Version: 0.1
Release: 0.11.%{date}%{?dist}
Summary: Ukrainian man pages from the Linux Documentation Project
License: GFDL
Group: Documentation
URL: http://docs.linux.org.ua/index.php?title=Man:Contents
Source0: http://downloads.sourceforge.net/wiki2man/man-pages-uk-utf8-%{date}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Manual pages from the Linux Documentation Project, translated into
Ukrainian.

%prep
%setup -q -n man-pages-uk-utf8-%{date}

%build
%__make

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_mandir}/uk
%__make INSTALLPATH=%{buildroot}%{_mandir} install 

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING
%lang(uk) %doc CREDITS.UK FAQ.UK NEWS.UK README.UK
%lang(uk) %{_mandir}/uk

%changelog
* Mon Feb 01 2010 Ding-Yi Chen <dchen@redhat.com> - 0.1-0.11.20071108
- Resolves: #560538
  [man-pages-uk] Package wrangler fix

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1-0.10.20071108.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.10.20071108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20071108
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jul 20 2008 Andy Shevchenko <andy@smile.org.ua> 0.1-0.8.20071108
- update URL tag

* Thu Mar 06 2008 Andy Shevchenko <andy@smile.org.ua> 0.1-0.7.20071108
- just fix Source0 URL

* Wed Feb 13 2008 Andy Shevchenko <andy@smile.org.ua> 0.1-0.6.20071108
- update to 20071108 snapshot

* Sun Aug 19 2007 Andy Shevchenko <andy@smile.org.ua> 0.1-0.5.20060830
- fix License tag according to the new guidelines

* Fri Sep 01 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.1-0.4.20060830
- fix tarball name according to mainstream

* Fri Sep 01 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.1-0.3.20060830
- update to 20060830 snapshot

* Wed Jun 07 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.1-0.2.20060328
- change the summary and description according to similar package from FC
- use lang macro for the *.UK files in the doc section
- fix the License tag

* Thu Jun 01 2006 Andy Shevchenko <andriy@asplinux.com.ua> 0.1-0.1.20060328
- renaming based to man-pages-LL
  (http://www.redhat.com/archives/fedora-extras-list/2006-May/msg00927.html)

* Tue Apr 04 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- update to 20060328 snapshot
- change version according to Makefile

* Tue Feb 28 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- change name to original tarball
- update to 20060228 snapshot
- catch version from Makefile

* Fri Feb 24 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- update to last official build
- change url
- use new tarball

* Wed Feb 22 2006 Andy Shevchenko <andriy@asplinux.com.ua>
- fix spec for extras injection

* Tue Oct 25 2005 Andy Shevchenko <andriy@asplinux.ru> 0.2-1
- include all translated pages

* Thu Aug 12 2004 Andy Shevchenko <andriy@asplinux.ru>
- rebuild

* Tue Oct 21 2003 Andy Shevchenko <andriy@asplinux.ru>
- correct URL tag
- update tarball from original site
- fix spec

* Sun May 04 2003 Andy Shevchenko <andriy@asplinux.ru>
- rebuild for ASPLinux

* Mon Sep 30 2002 Michael Shigorin <mike@altlinux.ru> 0.1.1-alt1
- missing apt-cache(8) was added from fixed tarball

* Tue Sep 17 2002 Michael Shigorin <mike@altlinux.ru> 0.1-alt1
- initial release
- manpages from Andriy Dobrovol'skiy <dobr@altlinux.ru>
- based on man-pages-ru-0.7-alt20 spec by Sass <sass@altlinux.ru>
- ENC1<->ENC2 (source was in KOI8-R, uk is in CP1251)
