#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	Size
Summary:	Term::Size - Perl extension for retrieving terminal size
Summary(pl):	Term::Size - rozszerzenie Perla do odczytu rozmiaru terminala
Name:		perl-Term-Size
Version:	0.2
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	982b5df8351e7654a42b7bffc0bf1d57
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::Size is a Perl module which provides a straightforward way to
retrieve the terminal size.

%description -l pl
Term::Size to modu³ Perla dostarczaj±cy bezpo¶redni sposób na odczyt
rozmiaru terminala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes Copyright README
%{perl_vendorarch}/Term/Size.pm
%dir %{perl_vendorarch}/auto/Term/Size
%{perl_vendorarch}/auto/Term/Size/autosplit.ix
%{perl_vendorarch}/auto/Term/Size/Size.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Term/Size/Size.so
%{_mandir}/man3/*
