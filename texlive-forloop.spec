Name:		texlive-forloop
Version:	15878
Release:	2
Summary:	Iteration in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/forloop
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forloop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forloop.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forloop.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a command \forloop for doing iteration in
LaTeX macro programming.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/forloop/forloop.sty
%doc %{_texmfdistdir}/doc/latex/forloop/README
%doc %{_texmfdistdir}/doc/latex/forloop/forloop.pdf
#- source
%doc %{_texmfdistdir}/source/latex/forloop/forloop.dtx
%doc %{_texmfdistdir}/source/latex/forloop/forloop.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
