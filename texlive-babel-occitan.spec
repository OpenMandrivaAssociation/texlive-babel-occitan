Name:		texlive-babel-occitan
Version:	39608
Release:	2
Summary:	Babel support for Occitan
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-occitan
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-occitan.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-occitan.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-occitan.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Occitan language description file with usage instructions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-occitan
%{_texmfdistdir}/tex/generic/babel-occitan
%doc %{_texmfdistdir}/doc/generic/babel-occitan

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
