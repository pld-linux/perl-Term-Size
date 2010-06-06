#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Term
%define		pnam	Size
Summary:	Term::Size - Perl extension for retrieving terminal size
Summary(pl.UTF-8):	Term::Size - rozszerzenie Perla do odczytu rozmiaru terminala
Name:		perl-Term-Size
Version:	0.207
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	474438fff3f12fca88a23388cc5a7571
URL:		http://search.cpan.org/dist/Term-Size/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::Size is a Perl module which provides a straightforward way to
retrieve the terminal size.

%description -l pl.UTF-8
Term::Size to moduł Perla dostarczający bezpośredni sposób na odczyt
rozmiaru terminala.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
