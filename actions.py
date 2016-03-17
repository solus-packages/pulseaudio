#!/usr/bin/python


from pisi.actionsapi import get, autotools, pisitools, shelltools


def setup():
    shelltools.system("./bootstrap.sh")
    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib \
                         --enable-alsa \
                         --disable-bluez4 \
                         --enable-bluez5 \
                         --enable-bluez5-native-headset \
                         --enable-orc \
                         --with-udev-rules-dir=/usr/lib/udev/rules.d \
                         --enable-dbus")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/etc/bash_completion.d")

    pisitools.dodoc("LICENSE")
