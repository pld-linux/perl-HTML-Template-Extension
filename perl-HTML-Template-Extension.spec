#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Template-Extension
Summary:	HTML::Template::Extension - Module support extension for HTML::Template
Summary(pl.UTF-8):   HTML::Template::Extension - rozszerzenie obsługujące moduły dla HTML::Template
Name:		perl-HTML-Template-Extension
Version:	0.24
Release:	1
License:	GPL v2+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25fd982e7aa1efb7acc3362f69b1a60e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-Template >= 2.1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module extends HTML::Template to easily support methods and tags
not implemented in parent module. Piece of code needed to add new tags
syntax and new functionality are called plugins. All plugins can be
dynamically loaded for supporting needed syntax and functionality.

%description -l pl.UTF-8
Ten moduł rozszerza klasę HTML::Template tak, aby mogła łatwo
obsługiwać metody i znaczniki nie zaimplementowane w macierzystym
module. Kawałki kodu potrzebne do dodania składni nowych znaczników i
nowej funkcjonalności są nazywane wtyczkami. Wszystkie wtyczki mogą
być dynamicznie wczytywane w celu obsługi wymaganej składni i
funkcjonalności.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO DISCLAIMER
%{perl_vendorlib}/HTML/Template/*.pm
%dir %{perl_vendorlib}/HTML/Template/Extension
%{perl_vendorlib}/HTML/Template/Extension/*.pm
%{_mandir}/man3/*
