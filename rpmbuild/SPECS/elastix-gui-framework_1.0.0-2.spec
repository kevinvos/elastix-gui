Summary: Elastix GUI is ElastixMT framework based and any other modules. The idea is to have a basic panel for using it in various projects.
Name: elastix-gui-framework
Vendor: iPERFEX
Version: 1.0.0
Release: 2
License: GPL
Group: Applications/System
#Source compression example: tar -czvf elastix-gui-framework_1.0.0-1.tgz elastix-gui-framework/
Source: elastix-gui-framework_%{version}-%{release}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
#Prereq: /sbin/chkconfig, /etc/sudoers, sudo
Requires: php, php-gd, php-pear, php-xml, php-mysql, php-pdo, php-imap, php-soap, php-process
Requires: httpd, mysql-server, ntp, nmap, mod_ssl
Requires: perl

%description
Elastix GUI is ElastixMT framework based and any other modules. The idea is to have a basic panel for using it in various projects.

%prep
%setup -n elastix-gui-framework

%install
## ** Step 1: Creation path for the installation ** ##
rm -rf   $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

# ** /var path ** #
mkdir -p $RPM_BUILD_ROOT/var/www/db
mkdir -p $RPM_BUILD_ROOT/var/www/html
mkdir -p $RPM_BUILD_ROOT/var/www/backup
mkdir -p $RPM_BUILD_ROOT/var/www/elastixdir/uploadAttachs
mkdir -p $RPM_BUILD_ROOT/var/www/elastixdir/asteriskconf
mkdir -p $RPM_BUILD_ROOT/var/lib/php/session-asterisk

# ** /usr path ** #
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/elastix
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/elastix
mkdir -p $RPM_BUILD_ROOT/usr/share/pear/DB
mkdir -p $RPM_BUILD_ROOT/usr/share/elastix/privileged
mkdir -p $RPM_BUILD_ROOT/usr/share/elastix/module_installer/%{name}-%{version}-%{release}/

# ** /etc path ** #
mkdir -p $RPM_BUILD_ROOT/etc/cron.d
mkdir -p $RPM_BUILD_ROOT/etc/cron.hourly
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d
mkdir -p $RPM_BUILD_ROOT/etc/php.d
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
mkdir -p $RPM_BUILD_ROOT/etc/init.d


## ** Step 2: Installation of files and folders ** ##
# ** Installating framework elastix webinterface ** #
rm -rf $RPM_BUILD_DIR/elastix-gui-framework/framework/html/modules/userlist/  # Este modulo no es el modificado para soporte de correo, eso se encuentra en modules-core

mv $RPM_BUILD_DIR/elastix-gui-framework/framework/html/*                              $RPM_BUILD_ROOT/var/www/html/
if [ -d $RPM_BUILD_ROOT/var/www/html/admin/web/themes/giox ]; then
	rm -rf $RPM_BUILD_ROOT/var/www/html/admin/web/themes/giox
fi

if [ -d $RPM_BUILD_ROOT/var/www/html/admin/web/themes/blackmin ]; then
	rm -rf $RPM_BUILD_ROOT/var/www/html/admin/web/themes/blackmin
fi

mkdir -p $RPM_BUILD_ROOT/usr/share/elastix/apps/
bdir=%{_builddir}/%{name}/framework/system
for FOLDER0 in $(ls -A $bdir/)
do
		if [ "$FOLDER0" == "apps" ]; then
			for FOLDER1 in $(ls -A $bdir/$FOLDER0/)
			do
				for FOLDER2 in $(ls -A $bdir/$FOLDER0/$FOLDER1/)
				do
				for FOLDER3 in $(ls -A $bdir/$FOLDER0/$FOLDER1/$FOLDER2/)
				do
				for FOLFI in $(ls -A $bdir/$FOLDER0/$FOLDER1/$FOLDER2/$FOLDER3/)
				do
					case "$FOLDER3" in
						frontend)
							if [ -d $bdir/$FOLDER0/$FOLDER1/$FOLDER2/$FOLDER3/$FOLFI/web/ ]; then
								mkdir -p $RPM_BUILD_ROOT/var/www/html/web/$FOLDER0/$FOLFI/
							mv $bdir/$FOLDER0/$FOLDER1/$FOLDER2/$FOLDER3/$FOLFI/web/* $RPM_BUILD_ROOT/var/www/html/web/$FOLDER0/$FOLFI/
							fi
						;;
						backend)
							if [ -d $bdir/$FOLDER0/$FOLDER1/$FOLDER2/$FOLDER3/$FOLFI/web/ ]; then
								mkdir -p $RPM_BUILD_ROOT/var/www/html/admin/web/$FOLDER0/$FOLFI/
						mv $bdir/$FOLDER0/$FOLDER1/$FOLDER2/$FOLDER3/$FOLFI/web/* $RPM_BUILD_ROOT/var/www/html/admin/web/$FOLDER0/$FOLFI/
							fi
						;;
					esac
					mkdir -p $RPM_BUILD_ROOT/usr/share/elastix/$FOLDER0/$FOLFI
					mv $bdir/$FOLDER0/$FOLDER1/$FOLDER2/$FOLDER3/$FOLFI/* $RPM_BUILD_ROOT/usr/share/elastix/$FOLDER0/$FOLFI/
				done
				done
				done
			done
		else
			mkdir -p $RPM_BUILD_ROOT/usr/share/elastix/$FOLDER0
			mv $bdir/$FOLDER0/* $RPM_BUILD_ROOT/usr/share/elastix/$FOLDER0/
		fi
done

chmod 777 $RPM_BUILD_ROOT/var/www/db/
chmod 755 $RPM_BUILD_ROOT/usr/share/elastix/privileged

# ** Httpd and Php config ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/httpd/conf.d/elastix.conf        $RPM_BUILD_ROOT/etc/httpd/conf.d/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/httpd/conf.d/elastix-htaccess.conf  $RPM_BUILD_ROOT/etc/httpd/conf.d/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/php.d/elastix.ini                $RPM_BUILD_ROOT/etc/php.d/

# ** crons config ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/framework/setup/etc/cron.hourly/elastix_emailattach_cleanup	$RPM_BUILD_ROOT/etc/cron.hourly/

# ** /var/www/elastixdir/asteriskconf/elastix_pbx.conf ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/framework/setup/var/www/elastixdir/asteriskconf/elastix_pbx.conf  $RPM_BUILD_ROOT/var/www/elastixdir/asteriskconf/

# ** Repos config ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/yum.repos.d/CentOS-Base.repo     $RPM_BUILD_ROOT/usr/share/elastix/

# ** sudoers config ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/sudoers                          $RPM_BUILD_ROOT/usr/share/elastix/

# ** /usr/local/ files ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/local/elastix/sampler.php        $RPM_BUILD_ROOT/usr/local/elastix/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/local/sbin/motd.sh               $RPM_BUILD_ROOT/usr/local/sbin/
chmod 755 $RPM_BUILD_ROOT/usr/local/sbin/motd.sh

# ** /usr/share/ files ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/share/elastix/menusAdminElx                  $RPM_BUILD_ROOT/usr/share/elastix/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/share/pear/DB/sqlite3.php                    $RPM_BUILD_ROOT/usr/share/pear/DB/

# ** setup ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/framework/setup/usr/share/elastix/privileged/*   $RPM_BUILD_ROOT/usr/share/elastix/privileged/
rmdir framework/setup/usr/share/elastix/privileged/ framework/setup/usr/share/elastix framework/setup/usr/share framework/setup/usr
mv $RPM_BUILD_DIR/elastix-gui-framework/framework/setup/ 	                             $RPM_BUILD_ROOT/usr/share/elastix/module_installer/%{name}-%{version}-%{release}/

# ** elastix-* file ** #
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/bin/elastix-menumerge            $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/bin/elastix-menuremove           $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/bin/elastix-dbprocess            $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/bin/compareVersion		   $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/bin/search_ami_admin_pwd             $RPM_BUILD_ROOT/usr/bin/
chmod 755 $RPM_BUILD_ROOT/usr/bin/compareVersion
chmod 755 $RPM_BUILD_ROOT/usr/bin/search_ami_admin_pwd

# ** Moving elastix_helper
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/bin/elastix-helper               $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/sbin/elastix-helper              $RPM_BUILD_ROOT/usr/sbin/

chmod 755 $RPM_BUILD_ROOT/usr/sbin/elastix-helper
chmod 755 $RPM_BUILD_ROOT/usr/bin/elastix-helper


# Archivos generic-cloexec y close-on-exec.pl
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/usr/sbin/close-on-exec.pl            $RPM_BUILD_ROOT/usr/sbin/
mv $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/init.d/generic-cloexec           $RPM_BUILD_ROOT/etc/init.d/

#Logrotate
mkdir -p    $RPM_BUILD_ROOT/etc/logrotate.d/
mv          $RPM_BUILD_DIR/elastix-gui-framework/additionals/etc/logrotate.d/*           $RPM_BUILD_ROOT/etc/logrotate.d/

# File Elastix Access Audit log
mkdir -p    $RPM_BUILD_ROOT/var/log/elastix
touch       $RPM_BUILD_ROOT/var/log/elastix/audit.log
touch	    $RPM_BUILD_ROOT/var/log/elastix/postfix_stats.log

%pre
###Automatizando instalacion.

#creacion /etc/elastix.conf
cat > /etc/elastix.conf <<ENDLINE
amiadminpwd=PASSWORD
mysqlrootpwd=eLaStIx.2o16
cyrususerpwd=eLaStIx.2o16
ENDLINE


#creando archivo configuracion del panel.
source /etc/elastix.conf

#creacion de usuario mysql asteriskuser
echo "CREATE DATABASE IF NOT EXISTS elxpbx;" | mysql -u root -p${mysqlrootpwd}
echo "GRANT ALL PRIVILEGES ON elxpbx.* TO 'asteriskuser'@'localhost' IDENTIFIED BY '${amiadminpwd}' WITH GRANT OPTION;" | mysql -u root -p${mysqlrootpwd}

#Para conocer la version de elastix antes de actualizar o instalar
mkdir -p /usr/share/elastix/module_installer/%{name}-%{version}-%{release}/
touch /usr/share/elastix/module_installer/%{name}-%{version}-%{release}/preversion_elastix-gui-framework.info
if [ $1 -eq 2 ]; then
    rpm -q --queryformat='%{VERSION}-%{RELEASE}' %{name} > /usr/share/elastix/module_installer/%{name}-%{version}-%{release}/preversion_elastix-gui-framework.info
fi

# if not exist add the asterisk group
grep -c "^asterisk:" %{_sysconfdir}/group &> /dev/null
if [ $? = 1 ]; then
    echo "   0:adding group asterisk..."
    /usr/sbin/groupadd -r -f asterisk
else
    echo "   0:group asterisk already present"
fi

# Modifico usuario asterisk para que tenga "/bin/bash" como shell
/usr/sbin/usermod -c "Asterisk VoIP PBX" -g asterisk -s /bin/bash -d /var/lib/asterisk asterisk

# TODO: TAREA DE POST-INSTALACIÓN
#useradd -d /var/ftp -M -s /sbin/nologin ftpuser
#(echo asterisk2007; sleep 2; echo asterisk2007) | passwd ftpuser

%post
######### Administration Menus and permission ###############
#. /usr/share/elastix/menusAdminElx `cat /usr/share/elastix/pre_elastix_version.info`
################## End Administration Menus and permission ##########################



# TODO: tarea de post-instalación.
# Habilito inicio automático de servicios necesarios
chkconfig --level 345 ntpd on
chkconfig --level 345 mysqld on
chkconfig --level 345 httpd on
chkconfig --del cups  &> /dev/null
chkconfig --del gpm   &> /dev/null


# ** Change content of sudoers ** #
cat   /usr/share/elastix/sudoers > /etc/sudoers
rm -f /usr/share/elastix/sudoers

# ** Change content of CentOS-Base.repo ** #
if [ -e /etc/yum.repos.d/CentOS-Base.repo ] ; then
    cat   /usr/share/elastix/CentOS-Base.repo > /etc/yum.repos.d/CentOS-Base.repo
    rm -f /usr/share/elastix/CentOS-Base.repo
fi

# Patch httpd.conf so that User and Group directives in elastix.conf take effect
sed --in-place "s,User\sapache,#User apache,g" /etc/httpd/conf/httpd.conf
sed --in-place "s,Group\sapache,#Group apache,g" /etc/httpd/conf/httpd.conf

# ** Uso de elastix-dbprocess ** #
pathModule="/usr/share/elastix/module_installer/%{name}-%{version}-%{release}"
preversion=`cat $pathModule/preversion_elastix-framework.info`
rm -f $pathModule/preversion_elastix-framework.info
#elastix-menumerge $pathModule/setup/infomodules
service mysqld status &>/dev/null
res=$?
if [ $res -eq 0 ]; then
	#service is up
	elastix-menumerge $pathModule/setup/infomodules	
else
	#copio el contenido de infomodules a una carpeta para su posterior ejecucion		
	if [ "$(ls -A $pathModule/setup/infomodules)" != "" ]; then
		mkdir -p /var/spool/elastix-infomodulesxml/%{name}-%{version}-%{release}/infomodules		
		mv $pathModule/setup/infomodules/* /var/spool/elastix-infomodulesxml/%{name}-%{version}-%{release}/infomodules
	fi
fi

if [ $1 -eq 1 ]; then #install
    # The installer database
    elastixversion=`rpm -q --queryformat='%{VERSION}-%{RELEASE}' elastix`
    verifyVersion=`echo $elastixversion | grep -oE "^[0-9]+(\.[0-9]+){1,2}-[0-9]+$"`
    if [ "$verifyVersion" == "" ]; then
	elastix-dbprocess "install" "$pathModule/setup/db"
    else
	elastix-dbprocess "update"  "$pathModule/setup/db" "$verifyVersion"
    fi
    /sbin/service httpd status > /dev/null 2>&1
    if [ "$?" == "0" ]; then
    	echo "Restarting apache..."
    	/sbin/service httpd restart > /dev/null 2>&1
    fi
elif [ $1 -eq 2 ]; then #update
    elastix-dbprocess "update"  "$pathModule/setup/db" "$preversion"
    /sbin/service httpd status > /dev/null 2>&1
    if [ "$?" == "0" ]; then
    	# Para versiones menores a 2.2.0-15 se debe reiniciar el apache debido a cambios en elastix.conf
    	compareVersion "$preversion" "2.2.0-15"
    	if [ "$?" == "9" ]; then
        	echo "Restarting apache..."
        	/sbin/service httpd restart > /dev/null 2>&1
    	fi
    fi
fi



#cambiando credenciales elastix_pbx.conf
source /etc/elastix.conf
sed -i "s/\(DBPASSWORD *= *\)\(.*\)/\1${amiadminpwd}/" /var/www/elastixdir/asteriskconf/elastix_pbx.conf
sed -i "s/\(MGPASSWORD *= *\)\(.*\)/\1${amiadminpwd}/" /var/www/elastixdir/asteriskconf/elastix_pbx.conf


# Para que agrege el contenido de /etc/motd
/bin/grep -r '/usr/local/sbin/motd.sh > /etc/motd' /etc/rc.local
if [ "$?" == "1" ]; then
  echo "/usr/local/sbin/motd.sh > /etc/motd" >> /etc/rc.local
fi

# Para q se actualice smarty (tpl updates)
rm -rf /var/www/html/var/templates_c/*

# Patch elastix.ini to work around %config(noreplace) in previous versions
sed --in-place "s,/tmp,/var/lib/php/session-asterisk,g" /etc/php.d/elastix.ini
umask 007 /var/lib/php/session-asterisk
if [ $1 -eq 1 ]; then #install
    /sbin/service httpd status > /dev/null 2>&1
    if [ "$?" == "0" ]; then
        echo "Restarting apache..."
        /sbin/service httpd restart > /dev/null 2>&1
    fi
elif [ $1 -eq 2 ]; then #update
    /sbin/service httpd status > /dev/null 2>&1
    if [ "$?" == "0" ]; then
        # Para versiones menores a 2.4.0-11 se debe reiniciar el apache debido a cambios en elastix.ini
        compareVersion "$preversion" "2.4.0-11"
        if [ "$?" == "9" ]; then
            echo "Restarting apache..."
            /sbin/service httpd restart > /dev/null 2>&1
        fi
    fi
fi

# Para cambiar la clave automaticamente segun el archivo /etc/elastix.conf
source /etc/elastix.conf
echo "UPDATE elxpbx.acl_user SET md5_password = MD5('${amiadminpwd}') WHERE id=1;" | mysql -u root -p${mysqlrootpwd}

elastix-menumerge /usr/share/elastix/module_installer/elastix-gui-framework-%{version}-%{release}/setup/infomodules/

%preun
# Reverse the patching of httpd.conf
sed --in-place "s,#User\sapache,User apache,g" /etc/httpd/conf/httpd.conf
sed --in-place "s,#Group\sapache,Group apache,g" /etc/httpd/conf/httpd.conf
pathModule="/usr/share/elastix/module_installer/%{name}-%{version}-%{release}"
if [ $1 -eq 0 ] ; then # Validation for desinstall this rpm
  echo "Dump and delete %{name} databases"
  elastix-dbprocess "delete" "$pathModule/setup/db"
  elastix-menuremove $pathModule/setup/infomodules
fi

%clean
rm -rf $RPM_BUILD_ROOT

# basic contains some reasonable sane basic tiles
%files
%defattr(-, asterisk, asterisk)
#/var/www/html/
/var/www/db
/var/www/backup
/var/log/elastix
/var/log/elastix/*
/var/www/html/favicon.ico
/var/www/html/admin
/var/www/html/tmp
/var/www/html/web
/var/www/html/*.php
/var/www/html/robots.txt
/usr/share/elastix/apps/*
/var/www/elastixdir/uploadAttachs
/var/www/elastixdir/asteriskconf
/var/www/elastixdir/asteriskconf/elastix_pbx.conf
%defattr(644, asterisk, asterisk)
/usr/share/elastix/libs/*
# %config(noreplace) /var/www/db/
%defattr(-, root, root)
/usr/share/elastix/*
/usr/share/pear/DB/sqlite3.php
/usr/local/elastix/sampler.php
/usr/local/sbin/motd.sh
/usr/sbin/close-on-exec.pl
/usr/bin/elastix-menumerge
/usr/bin/elastix-menuremove
/usr/bin/elastix-dbprocess
/usr/bin/elastix-helper
/usr/bin/compareVersion
/usr/bin/search_ami_admin_pwd
/usr/sbin/elastix-helper
%config(noreplace) /etc/httpd/conf.d/elastix.conf
%config(noreplace) /etc/php.d/elastix.ini
#%config(noreplace) /etc/logrotate.d/elastixAccess.logrotate
%config(noreplace) /etc/logrotate.d/elastixAudit.logrotate
%config /etc/httpd/conf.d/elastix-htaccess.conf
/etc/init.d/generic-cloexec
%defattr(755, root, root)
/usr/share/elastix/privileged/*
/etc/cron.hourly/elastix_emailattach_cleanup
%defattr(770, root, asterisk, 770)
/var/lib/php/session-asterisk

%changelog
* Wed Feb 03 2016 Federico Pereira <fpereira@iperfex.com> 1.0.0-2
- CHANGED: module organization.
- CHANGED: Code cleanup.

* Fri Jan 29 2016 Federico Pereira <fpereira@iperfex.com> 1.0.0-1
- CHANGED: Framework - elastix-gui-framework.spec: Update specfile with latest
- CHANGED: modules basic.

