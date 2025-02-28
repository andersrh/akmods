#!/bin/sh

set -oeux pipefail


cp /tmp/ublue-os-akmods-addons/rpmbuild/SOURCES/negativo17-fedora-multimedia.repo /etc/yum.repos.d/

ARCH="$(rpm -E '%_arch')"
KERNEL="$(rpm -q kernel-cachyos-lts --queryformat '%{VERSION}-%{RELEASE}.%{ARCH}')"
RELEASE="$(rpm -E '%fedora')"


### BUILD evdi (succeed or fail-fast with debug output)
export CFLAGS="-fno-pie -no-pie"
rpm-ostree install \
    akmod-evdi-*.fc${RELEASE}.${ARCH}
akmods --force --kernels "${KERNEL}" --kmod evdi
modinfo /usr/lib/modules/${KERNEL}/extra/evdi/evdi.ko.xz > /dev/null \
|| (find /var/cache/akmods/evdi/ -name \*.log -print -exec cat {} \; && exit 1)

rm -f /etc/yum.repos.d/negativo17-fedora-multimedia.repo
unset CFLAGS
