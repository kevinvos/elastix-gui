# Elastix GUI

This code is distributed under the GNU LGPL v3.0 license.

iPERFEX (c) 2012-2016
 Federico Pereira <fpereira@iperfex.com>

 Join our Google Group <elastix-gui@googlegroups.com>

## Introduction
Elastix GUI is ElastixMT framework based and any other modules. The idea is to have a basic panel for using it in various projects.

## Modules

| Module  | Description  | Message |
| :------------ |:---------------:| :-----: |
| applet_admin  | module manager dashboard | ok |
| currency      | module to change currency | ok |
| dashboard | module dashboard | ok |
| _elastixutils | - | - |
| grouplist | - | - |
| group_permission | - | - |
| language | module to change language | ok |
| network_parameters | - | - |
| organization | - | - |
| organization_permission | - | - |
| packages | - | - |
| repositories | - | - |
| shutdown | module for shutdown | ok |
| themes_system | - | - |
| time_config | - | - |
| userlist | - | - |


## Installation

[![ScreenShot](https://)](https://www.youtube.com/watch?v=gTYvmzRJEWc)


Install the git package and follow the instructions on a CentOS 6.

[Download ISO 32bit](http://mirrors.dcarsat.com.ar/centos/6.7/isos/i386/CentOS-6.7-i386-netinstall.iso)
or 
[Download ISO 64bit](http://mirrors.dcarsat.com.ar/centos/6.7/isos/x86_64/CentOS-6.7-x86_64-minimal.iso)


```bash

## Disable Selinux
sed -i 's/enforcing/disabled/g' /etc/selinux/config

## Activating the interface eth0
sed -i "s/^\(ONBOOT=\).*$/\1yes/g" /etc/sysconfig/network-scripts/ifcfg-eth0

## disable iptables
service iptables save
service iptables stop
chkconfig iptables off

## Yum Update
yum -y update
yum -y install vim wget

## System packages
yum -y install system-config-date system-config-firewall-base system-config-keyboard system-config-language system-config-network-tui system-config-users
#Packages for this implementation.
yum -y install dialog vim mc screen nmap wget mlocate mailx
#Packages for Development
yum -y groupinstall "Development Tools" 
yum -y install gcc gcc-c++ make openssl openssl-devel newt-devel ncurses-devel autoconf automake libpcap-devel
yum -y install rpm-build redhat-rpm-config rpmdevtools
#Packages for web server.
yum -y groupinstall "Web Server"
yum -y install mod_ssl openssl
#Packages to the database.
yum -y install mysql-server mysql-connector-odbc
#Packages for php
wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm -O /usr/src/epel-release-6-8.noarch.rpm
rpm -ivh /usr/src/epel-release-6-8.noarch.rpm
yum -y install php-mcrypt
yum -y install php php-cli php-common php-devel php-gd php-imap php-mbstring  php-mysql php-pdo php-pear php-pear-DB php-process php-soap php-xml
#Packages for perl
yum -y install perl-Archive-Tar perl-Archive-Zip perl-CGI perl-Convert-BinHex perl-Crypt-OpenSSL-Bignum perl-Crypt-OpenSSL-RSA perl-Date-Manip perl-Digest-HMAC perl-Digest-SHA perl-Encode-Detect perl-HTML-Parser perl-HTML-TokeParser-Simple perl-HTTP-Response-Encoding perl-IO-Multiplex perl-IO-Socket-INET6 perl-IO-Socket-SSL perl-IO-stringy perl-MIME-tools perl-Mail-DKIM perl-Mail-IMAPClient perl-Net-IP perl-Net-Server perl-Net-Telnet perl-NetAddr-IP perl-String-CRC32 perl-URI perl-Unix-Syslog perl-WWW-Mechanize perl-XML-Parser  perl-suidperl

#Git 2.0.4
yum -y remove git
yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
yum -y install  gcc perl-ExtUtils-MakeMaker

## Git 2.0.4
cd /usr/src
wget https://www.kernel.org/pub/software/scm/git/git-2.0.4.tar.gz
tar xzf git-2.0.4.tar.gz
cd git-2.0.4
make prefix=/usr/local/git all
make prefix=/usr/local/git install
echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/bashrc
source /etc/bashrc

# User asterisk 
/usr/sbin/adduser asterisk
/usr/sbin/usermod -c "Asterisk VoIP PBX" -g asterisk -s /bin/bash -d /var/lib/asterisk asterisk

## Start Services
/etc/init.d/htpd start
/etc/init.d/mysqld start
/etc/init.d/httpd start

chkconfig --level 345 ntpd on
chkconfig --level 345 mysqld on
chkconfig --level 345 httpd on


## MySQL Change root Password
echo "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('eLaStIx.2o16');" | mysql -u root
```


## Developer: Create RPM & install

```bash
## Create RPM
## Cloning repository
cd /usr/src
git clone https://github.com/lordbasex/elastix-gui.git
rpmdev-setuptree
rm -fr /root/rpmbuild/
ln -s /usr/src/elastix-gui/rpmbuild /root/
rpmbuild -ba /root/rpmbuild/SPECS/elastix-gui-framework.spec

## INSTALL RPM ##

#Install elastix-gui-framework 
rpm -i /root/rpmbuild/RPMS/noarch/elastix-gui-framework-1.0.0-1.noarch.rpm
```


## Install only rpm
```bash
rpm -i https://github.com/lordbasex/elastix-gui/raw/master/rpmbuild/RPMS/noarch/elastix-gui-framework-1.0.0-1.noarch.rpm
```

## Uninstall
```bash
rpm -e --nodeps elastix-gui-framework
```

## Password
The password is: PASSWORD
