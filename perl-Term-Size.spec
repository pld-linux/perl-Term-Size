#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Term
%define		pnam	Size
Summary:	Term::Size - Perl extension for retrieving terminal size
Summary(pl.UTF-8):	Term::Size - rozszerzenie Perla do odczytu rozmiaru terminala
Name:		perl-Term-Size
Version:	0.211
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	150b398d5be255883e59e12414c4a0cd
URL:		https://metacpan.org/release/Term-Size
BuildRequires:	perl-ExtUtils-MakeMaker
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%doc Changes README
%{perl_vendorarch}/Term/Size.pm
%dir %{perl_vendorarch}/auto/Term/Size
%attr(755,root,root) %{perl_vendorarch}/auto/Term/Size/Size.so
%{_mandir}/man3/Term::Size.3pm*
