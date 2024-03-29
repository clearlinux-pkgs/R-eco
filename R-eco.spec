#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-eco
Version  : 4.0.1
Release  : 32
URL      : https://cran.r-project.org/src/contrib/eco_4.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/eco_4.0-1.tar.gz
Summary  : Ecological Inference in 2x2 Tables
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-eco-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-eco package.
Group: Libraries

%description lib
lib components for the R-eco package.


%prep
%setup -q -c -n eco
cd %{_builddir}/eco

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589531201

%install
export SOURCE_DATE_EPOCH=1589531201
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library eco
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library eco
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library eco
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc eco || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/eco/CITATION
/usr/lib64/R/library/eco/DESCRIPTION
/usr/lib64/R/library/eco/INDEX
/usr/lib64/R/library/eco/Meta/Rd.rds
/usr/lib64/R/library/eco/Meta/data.rds
/usr/lib64/R/library/eco/Meta/features.rds
/usr/lib64/R/library/eco/Meta/hsearch.rds
/usr/lib64/R/library/eco/Meta/links.rds
/usr/lib64/R/library/eco/Meta/nsInfo.rds
/usr/lib64/R/library/eco/Meta/package.rds
/usr/lib64/R/library/eco/NAMESPACE
/usr/lib64/R/library/eco/R/eco
/usr/lib64/R/library/eco/R/eco.rdb
/usr/lib64/R/library/eco/R/eco.rdx
/usr/lib64/R/library/eco/data/Rdata.rdb
/usr/lib64/R/library/eco/data/Rdata.rds
/usr/lib64/R/library/eco/data/Rdata.rdx
/usr/lib64/R/library/eco/help/AnIndex
/usr/lib64/R/library/eco/help/aliases.rds
/usr/lib64/R/library/eco/help/eco.rdb
/usr/lib64/R/library/eco/help/eco.rdx
/usr/lib64/R/library/eco/help/paths.rds
/usr/lib64/R/library/eco/html/00Index.html
/usr/lib64/R/library/eco/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/eco/libs/eco.so
/usr/lib64/R/library/eco/libs/eco.so.avx2
/usr/lib64/R/library/eco/libs/eco.so.avx512
