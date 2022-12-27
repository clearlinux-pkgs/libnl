#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libnl
Version  : 3.7.0
Release  : 26
URL      : https://github.com/thom311/libnl/archive/libnl3_7_0/libnl-3.7.0.tar.gz
Source0  : https://github.com/thom311/libnl/archive/libnl3_7_0/libnl-3.7.0.tar.gz
Summary  : Netlink Routing Family Library
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.0 LGPL-2.1
Requires: libnl-bin = %{version}-%{release}
Requires: libnl-data = %{version}-%{release}
Requires: libnl-lib = %{version}-%{release}
Requires: libnl-license = %{version}-%{release}
Requires: libnl-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : bison
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : graphviz
BuildRequires : pkg-config
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(check)
BuildRequires : sed

%description
***************************************************************************
NOTE: The python wrapper is experimental and may or may not work.

%package bin
Summary: bin components for the libnl package.
Group: Binaries
Requires: libnl-data = %{version}-%{release}
Requires: libnl-license = %{version}-%{release}

%description bin
bin components for the libnl package.


%package data
Summary: data components for the libnl package.
Group: Data

%description data
data components for the libnl package.


%package dev
Summary: dev components for the libnl package.
Group: Development
Requires: libnl-lib = %{version}-%{release}
Requires: libnl-bin = %{version}-%{release}
Requires: libnl-data = %{version}-%{release}
Provides: libnl-devel = %{version}-%{release}
Requires: libnl = %{version}-%{release}

%description dev
dev components for the libnl package.


%package dev32
Summary: dev32 components for the libnl package.
Group: Default
Requires: libnl-lib32 = %{version}-%{release}
Requires: libnl-bin = %{version}-%{release}
Requires: libnl-data = %{version}-%{release}
Requires: libnl-dev = %{version}-%{release}

%description dev32
dev32 components for the libnl package.


%package lib
Summary: lib components for the libnl package.
Group: Libraries
Requires: libnl-data = %{version}-%{release}
Requires: libnl-license = %{version}-%{release}

%description lib
lib components for the libnl package.


%package lib32
Summary: lib32 components for the libnl package.
Group: Default
Requires: libnl-data = %{version}-%{release}
Requires: libnl-license = %{version}-%{release}

%description lib32
lib32 components for the libnl package.


%package license
Summary: license components for the libnl package.
Group: Default

%description license
license components for the libnl package.


%package man
Summary: man components for the libnl package.
Group: Default

%description man
man components for the libnl package.


%prep
%setup -q -n libnl-libnl3_7_0
cd %{_builddir}/libnl-libnl3_7_0
pushd ..
cp -a libnl-libnl3_7_0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672180360
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%autogen --disable-static --sysconfdir=/usr/share/defaults
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static --sysconfdir=/usr/share/defaults  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1672180360
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnl
cp %{_builddir}/libnl-libnl3_7_0/COPYING %{buildroot}/usr/share/package-licenses/libnl/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/libnl-libnl3_7_0/doc/COPYING %{buildroot}/usr/share/package-licenses/libnl/31a3d460bb3c7d98845187c716a30db81c44b615
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/genl-ctrl-list
/usr/bin/idiag-socket-details
/usr/bin/nf-ct-add
/usr/bin/nf-ct-events
/usr/bin/nf-ct-list
/usr/bin/nf-exp-add
/usr/bin/nf-exp-delete
/usr/bin/nf-exp-list
/usr/bin/nf-log
/usr/bin/nf-monitor
/usr/bin/nf-queue
/usr/bin/nl-addr-add
/usr/bin/nl-addr-delete
/usr/bin/nl-addr-list
/usr/bin/nl-class-add
/usr/bin/nl-class-delete
/usr/bin/nl-class-list
/usr/bin/nl-classid-lookup
/usr/bin/nl-cls-add
/usr/bin/nl-cls-delete
/usr/bin/nl-cls-list
/usr/bin/nl-fib-lookup
/usr/bin/nl-link-enslave
/usr/bin/nl-link-ifindex2name
/usr/bin/nl-link-list
/usr/bin/nl-link-name2ifindex
/usr/bin/nl-link-release
/usr/bin/nl-link-set
/usr/bin/nl-link-stats
/usr/bin/nl-list-caches
/usr/bin/nl-list-sockets
/usr/bin/nl-monitor
/usr/bin/nl-neigh-add
/usr/bin/nl-neigh-delete
/usr/bin/nl-neigh-list
/usr/bin/nl-neightbl-list
/usr/bin/nl-pktloc-lookup
/usr/bin/nl-qdisc-add
/usr/bin/nl-qdisc-delete
/usr/bin/nl-qdisc-list
/usr/bin/nl-route-add
/usr/bin/nl-route-delete
/usr/bin/nl-route-get
/usr/bin/nl-route-list
/usr/bin/nl-rule-list
/usr/bin/nl-tctree-list
/usr/bin/nl-util-addr

%files data
%defattr(-,root,root,-)
/usr/share/defaults/libnl/classid
/usr/share/defaults/libnl/pktloc

%files dev
%defattr(-,root,root,-)
/usr/include/libnl3/netlink/addr.h
/usr/include/libnl3/netlink/attr.h
/usr/include/libnl3/netlink/cache-api.h
/usr/include/libnl3/netlink/cache.h
/usr/include/libnl3/netlink/cli/addr.h
/usr/include/libnl3/netlink/cli/class.h
/usr/include/libnl3/netlink/cli/cls.h
/usr/include/libnl3/netlink/cli/ct.h
/usr/include/libnl3/netlink/cli/exp.h
/usr/include/libnl3/netlink/cli/link.h
/usr/include/libnl3/netlink/cli/mdb.h
/usr/include/libnl3/netlink/cli/neigh.h
/usr/include/libnl3/netlink/cli/qdisc.h
/usr/include/libnl3/netlink/cli/route.h
/usr/include/libnl3/netlink/cli/rule.h
/usr/include/libnl3/netlink/cli/tc.h
/usr/include/libnl3/netlink/cli/utils.h
/usr/include/libnl3/netlink/data.h
/usr/include/libnl3/netlink/errno.h
/usr/include/libnl3/netlink/fib_lookup/lookup.h
/usr/include/libnl3/netlink/fib_lookup/request.h
/usr/include/libnl3/netlink/genl/ctrl.h
/usr/include/libnl3/netlink/genl/family.h
/usr/include/libnl3/netlink/genl/genl.h
/usr/include/libnl3/netlink/genl/mngt.h
/usr/include/libnl3/netlink/handlers.h
/usr/include/libnl3/netlink/hash.h
/usr/include/libnl3/netlink/hashtable.h
/usr/include/libnl3/netlink/idiag/idiagnl.h
/usr/include/libnl3/netlink/idiag/meminfo.h
/usr/include/libnl3/netlink/idiag/msg.h
/usr/include/libnl3/netlink/idiag/req.h
/usr/include/libnl3/netlink/idiag/vegasinfo.h
/usr/include/libnl3/netlink/list.h
/usr/include/libnl3/netlink/msg.h
/usr/include/libnl3/netlink/netfilter/ct.h
/usr/include/libnl3/netlink/netfilter/exp.h
/usr/include/libnl3/netlink/netfilter/log.h
/usr/include/libnl3/netlink/netfilter/log_msg.h
/usr/include/libnl3/netlink/netfilter/netfilter.h
/usr/include/libnl3/netlink/netfilter/nfnl.h
/usr/include/libnl3/netlink/netfilter/queue.h
/usr/include/libnl3/netlink/netfilter/queue_msg.h
/usr/include/libnl3/netlink/netlink-compat.h
/usr/include/libnl3/netlink/netlink-kernel.h
/usr/include/libnl3/netlink/netlink.h
/usr/include/libnl3/netlink/object-api.h
/usr/include/libnl3/netlink/object.h
/usr/include/libnl3/netlink/route/act/gact.h
/usr/include/libnl3/netlink/route/act/mirred.h
/usr/include/libnl3/netlink/route/act/nat.h
/usr/include/libnl3/netlink/route/act/skbedit.h
/usr/include/libnl3/netlink/route/act/vlan.h
/usr/include/libnl3/netlink/route/action.h
/usr/include/libnl3/netlink/route/addr.h
/usr/include/libnl3/netlink/route/class.h
/usr/include/libnl3/netlink/route/classifier.h
/usr/include/libnl3/netlink/route/cls/basic.h
/usr/include/libnl3/netlink/route/cls/cgroup.h
/usr/include/libnl3/netlink/route/cls/ematch.h
/usr/include/libnl3/netlink/route/cls/ematch/cmp.h
/usr/include/libnl3/netlink/route/cls/ematch/meta.h
/usr/include/libnl3/netlink/route/cls/ematch/nbyte.h
/usr/include/libnl3/netlink/route/cls/ematch/text.h
/usr/include/libnl3/netlink/route/cls/flower.h
/usr/include/libnl3/netlink/route/cls/fw.h
/usr/include/libnl3/netlink/route/cls/matchall.h
/usr/include/libnl3/netlink/route/cls/police.h
/usr/include/libnl3/netlink/route/cls/u32.h
/usr/include/libnl3/netlink/route/link.h
/usr/include/libnl3/netlink/route/link/api.h
/usr/include/libnl3/netlink/route/link/bonding.h
/usr/include/libnl3/netlink/route/link/bridge.h
/usr/include/libnl3/netlink/route/link/can.h
/usr/include/libnl3/netlink/route/link/geneve.h
/usr/include/libnl3/netlink/route/link/inet.h
/usr/include/libnl3/netlink/route/link/inet6.h
/usr/include/libnl3/netlink/route/link/info-api.h
/usr/include/libnl3/netlink/route/link/ip6gre.h
/usr/include/libnl3/netlink/route/link/ip6tnl.h
/usr/include/libnl3/netlink/route/link/ip6vti.h
/usr/include/libnl3/netlink/route/link/ipgre.h
/usr/include/libnl3/netlink/route/link/ipip.h
/usr/include/libnl3/netlink/route/link/ipvlan.h
/usr/include/libnl3/netlink/route/link/ipvti.h
/usr/include/libnl3/netlink/route/link/macsec.h
/usr/include/libnl3/netlink/route/link/macvlan.h
/usr/include/libnl3/netlink/route/link/macvtap.h
/usr/include/libnl3/netlink/route/link/ppp.h
/usr/include/libnl3/netlink/route/link/sit.h
/usr/include/libnl3/netlink/route/link/sriov.h
/usr/include/libnl3/netlink/route/link/team.h
/usr/include/libnl3/netlink/route/link/veth.h
/usr/include/libnl3/netlink/route/link/vlan.h
/usr/include/libnl3/netlink/route/link/vrf.h
/usr/include/libnl3/netlink/route/link/vxlan.h
/usr/include/libnl3/netlink/route/link/xfrmi.h
/usr/include/libnl3/netlink/route/mdb.h
/usr/include/libnl3/netlink/route/neighbour.h
/usr/include/libnl3/netlink/route/neightbl.h
/usr/include/libnl3/netlink/route/netconf.h
/usr/include/libnl3/netlink/route/nexthop.h
/usr/include/libnl3/netlink/route/pktloc.h
/usr/include/libnl3/netlink/route/qdisc.h
/usr/include/libnl3/netlink/route/qdisc/cbq.h
/usr/include/libnl3/netlink/route/qdisc/dsmark.h
/usr/include/libnl3/netlink/route/qdisc/fifo.h
/usr/include/libnl3/netlink/route/qdisc/fq_codel.h
/usr/include/libnl3/netlink/route/qdisc/hfsc.h
/usr/include/libnl3/netlink/route/qdisc/htb.h
/usr/include/libnl3/netlink/route/qdisc/mqprio.h
/usr/include/libnl3/netlink/route/qdisc/netem.h
/usr/include/libnl3/netlink/route/qdisc/plug.h
/usr/include/libnl3/netlink/route/qdisc/prio.h
/usr/include/libnl3/netlink/route/qdisc/red.h
/usr/include/libnl3/netlink/route/qdisc/sfq.h
/usr/include/libnl3/netlink/route/qdisc/tbf.h
/usr/include/libnl3/netlink/route/route.h
/usr/include/libnl3/netlink/route/rtnl.h
/usr/include/libnl3/netlink/route/rule.h
/usr/include/libnl3/netlink/route/tc-api.h
/usr/include/libnl3/netlink/route/tc.h
/usr/include/libnl3/netlink/socket.h
/usr/include/libnl3/netlink/types.h
/usr/include/libnl3/netlink/utils.h
/usr/include/libnl3/netlink/version.h
/usr/include/libnl3/netlink/xfrm/ae.h
/usr/include/libnl3/netlink/xfrm/lifetime.h
/usr/include/libnl3/netlink/xfrm/sa.h
/usr/include/libnl3/netlink/xfrm/selector.h
/usr/include/libnl3/netlink/xfrm/sp.h
/usr/include/libnl3/netlink/xfrm/template.h
/usr/lib64/libnl-3.so
/usr/lib64/libnl-cli-3.so
/usr/lib64/libnl-genl-3.so
/usr/lib64/libnl-idiag-3.so
/usr/lib64/libnl-nf-3.so
/usr/lib64/libnl-route-3.so
/usr/lib64/libnl-xfrm-3.so
/usr/lib64/pkgconfig/libnl-3.0.pc
/usr/lib64/pkgconfig/libnl-cli-3.0.pc
/usr/lib64/pkgconfig/libnl-genl-3.0.pc
/usr/lib64/pkgconfig/libnl-idiag-3.0.pc
/usr/lib64/pkgconfig/libnl-nf-3.0.pc
/usr/lib64/pkgconfig/libnl-route-3.0.pc
/usr/lib64/pkgconfig/libnl-xfrm-3.0.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnl-3.so
/usr/lib32/libnl-cli-3.so
/usr/lib32/libnl-genl-3.so
/usr/lib32/libnl-idiag-3.so
/usr/lib32/libnl-nf-3.so
/usr/lib32/libnl-route-3.so
/usr/lib32/libnl-xfrm-3.so
/usr/lib32/pkgconfig/32libnl-3.0.pc
/usr/lib32/pkgconfig/32libnl-cli-3.0.pc
/usr/lib32/pkgconfig/32libnl-genl-3.0.pc
/usr/lib32/pkgconfig/32libnl-idiag-3.0.pc
/usr/lib32/pkgconfig/32libnl-nf-3.0.pc
/usr/lib32/pkgconfig/32libnl-route-3.0.pc
/usr/lib32/pkgconfig/32libnl-xfrm-3.0.pc
/usr/lib32/pkgconfig/libnl-3.0.pc
/usr/lib32/pkgconfig/libnl-cli-3.0.pc
/usr/lib32/pkgconfig/libnl-genl-3.0.pc
/usr/lib32/pkgconfig/libnl-idiag-3.0.pc
/usr/lib32/pkgconfig/libnl-nf-3.0.pc
/usr/lib32/pkgconfig/libnl-route-3.0.pc
/usr/lib32/pkgconfig/libnl-xfrm-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnl-3.so.200
/usr/lib64/libnl-3.so.200.26.0
/usr/lib64/libnl-cli-3.so.200
/usr/lib64/libnl-cli-3.so.200.26.0
/usr/lib64/libnl-genl-3.so.200
/usr/lib64/libnl-genl-3.so.200.26.0
/usr/lib64/libnl-idiag-3.so.200
/usr/lib64/libnl-idiag-3.so.200.26.0
/usr/lib64/libnl-nf-3.so.200
/usr/lib64/libnl-nf-3.so.200.26.0
/usr/lib64/libnl-route-3.so.200
/usr/lib64/libnl-route-3.so.200.26.0
/usr/lib64/libnl-xfrm-3.so.200
/usr/lib64/libnl-xfrm-3.so.200.26.0
/usr/lib64/libnl/cli/cls/basic.so
/usr/lib64/libnl/cli/cls/cgroup.so
/usr/lib64/libnl/cli/qdisc/bfifo.so
/usr/lib64/libnl/cli/qdisc/blackhole.so
/usr/lib64/libnl/cli/qdisc/fq_codel.so
/usr/lib64/libnl/cli/qdisc/hfsc.so
/usr/lib64/libnl/cli/qdisc/htb.so
/usr/lib64/libnl/cli/qdisc/ingress.so
/usr/lib64/libnl/cli/qdisc/pfifo.so
/usr/lib64/libnl/cli/qdisc/plug.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnl-3.so.200
/usr/lib32/libnl-3.so.200.26.0
/usr/lib32/libnl-cli-3.so.200
/usr/lib32/libnl-cli-3.so.200.26.0
/usr/lib32/libnl-genl-3.so.200
/usr/lib32/libnl-genl-3.so.200.26.0
/usr/lib32/libnl-idiag-3.so.200
/usr/lib32/libnl-idiag-3.so.200.26.0
/usr/lib32/libnl-nf-3.so.200
/usr/lib32/libnl-nf-3.so.200.26.0
/usr/lib32/libnl-route-3.so.200
/usr/lib32/libnl-route-3.so.200.26.0
/usr/lib32/libnl-xfrm-3.so.200
/usr/lib32/libnl-xfrm-3.so.200.26.0
/usr/lib32/libnl/cli/cls/basic.so
/usr/lib32/libnl/cli/cls/cgroup.so
/usr/lib32/libnl/cli/qdisc/bfifo.so
/usr/lib32/libnl/cli/qdisc/blackhole.so
/usr/lib32/libnl/cli/qdisc/fq_codel.so
/usr/lib32/libnl/cli/qdisc/hfsc.so
/usr/lib32/libnl/cli/qdisc/htb.so
/usr/lib32/libnl/cli/qdisc/ingress.so
/usr/lib32/libnl/cli/qdisc/pfifo.so
/usr/lib32/libnl/cli/qdisc/plug.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnl/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libnl/31a3d460bb3c7d98845187c716a30db81c44b615

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/genl-ctrl-list.8
/usr/share/man/man8/nl-classid-lookup.8
/usr/share/man/man8/nl-pktloc-lookup.8
/usr/share/man/man8/nl-qdisc-add.8
/usr/share/man/man8/nl-qdisc-delete.8
/usr/share/man/man8/nl-qdisc-list.8
