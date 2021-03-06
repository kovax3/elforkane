# norootforbuild
BuildRequires: qt-devel

#%if 0%{?centos_version}<=5
#define qmake /usr/bin/qmake-qt4
#BuildRequires: qt4-phonon-devel 
#Requires:qt47-sqlite,libphonon
#%endif

%if 0%{?centos_version}>=6 
%define qmake /usr/bin/qmake-qt4
   %define qmake /usr/bin/qmake-qt4
   
BuildRequires:	qt-devel
BuildRequires:  phonon-devel
Requires: qt4-sqlite
%endif

%if 0%{?suse_version}
     %define qmake /usr/bin/qmake
BuildRequires:	libqt4-devel
BuildRequires:  phonon-devel
Requires: libqt4-x11 >= 4.6.2
Requires: libqt4-sql-sqlite
%endif

%if 0%{?fedora_version} || 0%{?rhel_version}
   %define qmake /usr/bin/qmake-qt4   
BuildRequires:	qt-devel
BuildRequires:  phonon-devel
Requires: qt4-sqlite
%endif


%if 0%{?mandriva_version}  || 0%{?mdkversion}
      %define qmake /usr/lib/qt4/bin/qmake
BuildRequires: phonon-devel
Requires: qt4-database-plugin-sqlite
%endif


Name:	%{name}
Version:	1.1
Release:	75.1
License:	GPL3
Group:	libriry/office
Summary:	%{name} the Holy Quran
URL:	http://elkirtasse.22web.net/

Source0:	%{name}_%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-build

BuildRequires:	gcc-c++





%description
 المصحف الالكتروني الفرقان.
 يتيح لك هذا البرنامج مطالعة و سماع القرءان الكريم.
 مع مجموعة من التفاسير والتراجم لمعاني القرءان بعدة لغات.
 يمكنك تحميل الاصوات من هذا الموقع http://quran.ksu.edu.sa/ayat/?l=en.

%prep
%setup -q -n %{name}-%{version}

%build
%{qmake}

make

%install
# binary
%{makeinstall} INSTALL_ROOT=%{buildroot}
%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}
%{_bindir}/%{name}
%{_datadir}
%{_datadir}/applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/%{name}/ajzaa.xml
%{_datadir}/%{name}/audhubillah.mp3
%{_datadir}/%{name}/bismillah.mp3
%{_datadir}/%{name}/curan.xml
%{_datadir}/%{name}/fullscreen
%{_datadir}/%{name}/fullscreen/bgrFull.png
%{_datadir}/%{name}/images
%{_datadir}/%{name}/images/datarc
%{_datadir}/%{name}/images/default
%{_datadir}/%{name}/images/default/06.png
%{_datadir}/%{name}/images/default/1.png
%{_datadir}/%{name}/images/default/10.png
%{_datadir}/%{name}/images/default/100.png
%{_datadir}/%{name}/images/default/101.png
%{_datadir}/%{name}/images/default/102.png
%{_datadir}/%{name}/images/default/103.png
%{_datadir}/%{name}/images/default/104.png
%{_datadir}/%{name}/images/default/105.png
%{_datadir}/%{name}/images/default/106.png
%{_datadir}/%{name}/images/default/107.png
%{_datadir}/%{name}/images/default/108.png
%{_datadir}/%{name}/images/default/109.png
%{_datadir}/%{name}/images/default/11.png
%{_datadir}/%{name}/images/default/110.png
%{_datadir}/%{name}/images/default/111.png
%{_datadir}/%{name}/images/default/112.png
%{_datadir}/%{name}/images/default/113.png
%{_datadir}/%{name}/images/default/114.png
%{_datadir}/%{name}/images/default/115.png
%{_datadir}/%{name}/images/default/116.png
%{_datadir}/%{name}/images/default/117.png
%{_datadir}/%{name}/images/default/118.png
%{_datadir}/%{name}/images/default/119.png
%{_datadir}/%{name}/images/default/12.png
%{_datadir}/%{name}/images/default/120.png
%{_datadir}/%{name}/images/default/121.png
%{_datadir}/%{name}/images/default/122.png
%{_datadir}/%{name}/images/default/123.png
%{_datadir}/%{name}/images/default/124.png
%{_datadir}/%{name}/images/default/125.png
%{_datadir}/%{name}/images/default/126.png
%{_datadir}/%{name}/images/default/127.png
%{_datadir}/%{name}/images/default/128.png
%{_datadir}/%{name}/images/default/129.png
%{_datadir}/%{name}/images/default/13.png
%{_datadir}/%{name}/images/default/130.png
%{_datadir}/%{name}/images/default/131.png
%{_datadir}/%{name}/images/default/132.png
%{_datadir}/%{name}/images/default/133.png
%{_datadir}/%{name}/images/default/134.png
%{_datadir}/%{name}/images/default/135.png
%{_datadir}/%{name}/images/default/136.png
%{_datadir}/%{name}/images/default/137.png
%{_datadir}/%{name}/images/default/138.png
%{_datadir}/%{name}/images/default/139.png
%{_datadir}/%{name}/images/default/14.png
%{_datadir}/%{name}/images/default/140.png
%{_datadir}/%{name}/images/default/141.png
%{_datadir}/%{name}/images/default/142.png
%{_datadir}/%{name}/images/default/143.png
%{_datadir}/%{name}/images/default/144.png
%{_datadir}/%{name}/images/default/145.png
%{_datadir}/%{name}/images/default/146.png
%{_datadir}/%{name}/images/default/147.png
%{_datadir}/%{name}/images/default/148.png
%{_datadir}/%{name}/images/default/149.png
%{_datadir}/%{name}/images/default/15.png
%{_datadir}/%{name}/images/default/150.png
%{_datadir}/%{name}/images/default/151.png
%{_datadir}/%{name}/images/default/152.png
%{_datadir}/%{name}/images/default/153.png
%{_datadir}/%{name}/images/default/154.png
%{_datadir}/%{name}/images/default/155.png
%{_datadir}/%{name}/images/default/156.png
%{_datadir}/%{name}/images/default/157.png
%{_datadir}/%{name}/images/default/158.png
%{_datadir}/%{name}/images/default/159.png
%{_datadir}/%{name}/images/default/16.png
%{_datadir}/%{name}/images/default/160.png
%{_datadir}/%{name}/images/default/161.png
%{_datadir}/%{name}/images/default/162.png
%{_datadir}/%{name}/images/default/163.png
%{_datadir}/%{name}/images/default/164.png
%{_datadir}/%{name}/images/default/165.png
%{_datadir}/%{name}/images/default/166.png
%{_datadir}/%{name}/images/default/167.png
%{_datadir}/%{name}/images/default/168.png
%{_datadir}/%{name}/images/default/169.png
%{_datadir}/%{name}/images/default/17.png
%{_datadir}/%{name}/images/default/170.png
%{_datadir}/%{name}/images/default/171.png
%{_datadir}/%{name}/images/default/172.png
%{_datadir}/%{name}/images/default/173.png
%{_datadir}/%{name}/images/default/174.png
%{_datadir}/%{name}/images/default/175.png
%{_datadir}/%{name}/images/default/176.png
%{_datadir}/%{name}/images/default/177.png
%{_datadir}/%{name}/images/default/178.png
%{_datadir}/%{name}/images/default/179.png
%{_datadir}/%{name}/images/default/18.png
%{_datadir}/%{name}/images/default/180.png
%{_datadir}/%{name}/images/default/181.png
%{_datadir}/%{name}/images/default/182.png
%{_datadir}/%{name}/images/default/183.png
%{_datadir}/%{name}/images/default/184.png
%{_datadir}/%{name}/images/default/185.png
%{_datadir}/%{name}/images/default/186.png
%{_datadir}/%{name}/images/default/187.png
%{_datadir}/%{name}/images/default/188.png
%{_datadir}/%{name}/images/default/189.png
%{_datadir}/%{name}/images/default/19.png
%{_datadir}/%{name}/images/default/190.png
%{_datadir}/%{name}/images/default/191.png
%{_datadir}/%{name}/images/default/192.png
%{_datadir}/%{name}/images/default/193.png
%{_datadir}/%{name}/images/default/194.png
%{_datadir}/%{name}/images/default/195.png
%{_datadir}/%{name}/images/default/196.png
%{_datadir}/%{name}/images/default/197.png
%{_datadir}/%{name}/images/default/198.png
%{_datadir}/%{name}/images/default/199.png
%{_datadir}/%{name}/images/default/2.png
%{_datadir}/%{name}/images/default/20.png
%{_datadir}/%{name}/images/default/200.png
%{_datadir}/%{name}/images/default/201.png
%{_datadir}/%{name}/images/default/202.png
%{_datadir}/%{name}/images/default/203.png
%{_datadir}/%{name}/images/default/204.png
%{_datadir}/%{name}/images/default/205.png
%{_datadir}/%{name}/images/default/206.png
%{_datadir}/%{name}/images/default/207.png
%{_datadir}/%{name}/images/default/208.png
%{_datadir}/%{name}/images/default/209.png
%{_datadir}/%{name}/images/default/21.png
%{_datadir}/%{name}/images/default/210.png
%{_datadir}/%{name}/images/default/211.png
%{_datadir}/%{name}/images/default/212.png
%{_datadir}/%{name}/images/default/213.png
%{_datadir}/%{name}/images/default/214.png
%{_datadir}/%{name}/images/default/215.png
%{_datadir}/%{name}/images/default/216.png
%{_datadir}/%{name}/images/default/217.png
%{_datadir}/%{name}/images/default/218.png
%{_datadir}/%{name}/images/default/219.png
%{_datadir}/%{name}/images/default/22.png
%{_datadir}/%{name}/images/default/220.png
%{_datadir}/%{name}/images/default/221.png
%{_datadir}/%{name}/images/default/222.png
%{_datadir}/%{name}/images/default/223.png
%{_datadir}/%{name}/images/default/224.png
%{_datadir}/%{name}/images/default/225.png
%{_datadir}/%{name}/images/default/226.png
%{_datadir}/%{name}/images/default/227.png
%{_datadir}/%{name}/images/default/228.png
%{_datadir}/%{name}/images/default/229.png
%{_datadir}/%{name}/images/default/23.png
%{_datadir}/%{name}/images/default/230.png
%{_datadir}/%{name}/images/default/231.png
%{_datadir}/%{name}/images/default/232.png
%{_datadir}/%{name}/images/default/233.png
%{_datadir}/%{name}/images/default/234.png
%{_datadir}/%{name}/images/default/235.png
%{_datadir}/%{name}/images/default/236.png
%{_datadir}/%{name}/images/default/237.png
%{_datadir}/%{name}/images/default/238.png
%{_datadir}/%{name}/images/default/239.png
%{_datadir}/%{name}/images/default/24.png
%{_datadir}/%{name}/images/default/240.png
%{_datadir}/%{name}/images/default/241.png
%{_datadir}/%{name}/images/default/242.png
%{_datadir}/%{name}/images/default/243.png
%{_datadir}/%{name}/images/default/244.png
%{_datadir}/%{name}/images/default/245.png
%{_datadir}/%{name}/images/default/246.png
%{_datadir}/%{name}/images/default/247.png
%{_datadir}/%{name}/images/default/248.png
%{_datadir}/%{name}/images/default/249.png
%{_datadir}/%{name}/images/default/25.png
%{_datadir}/%{name}/images/default/250.png
%{_datadir}/%{name}/images/default/251.png
%{_datadir}/%{name}/images/default/252.png
%{_datadir}/%{name}/images/default/253.png
%{_datadir}/%{name}/images/default/254.png
%{_datadir}/%{name}/images/default/255.png
%{_datadir}/%{name}/images/default/256.png
%{_datadir}/%{name}/images/default/257.png
%{_datadir}/%{name}/images/default/258.png
%{_datadir}/%{name}/images/default/259.png
%{_datadir}/%{name}/images/default/26.png
%{_datadir}/%{name}/images/default/260.png
%{_datadir}/%{name}/images/default/261.png
%{_datadir}/%{name}/images/default/262.png
%{_datadir}/%{name}/images/default/263.png
%{_datadir}/%{name}/images/default/264.png
%{_datadir}/%{name}/images/default/265.png
%{_datadir}/%{name}/images/default/266.png
%{_datadir}/%{name}/images/default/267.png
%{_datadir}/%{name}/images/default/268.png
%{_datadir}/%{name}/images/default/269.png
%{_datadir}/%{name}/images/default/27.png
%{_datadir}/%{name}/images/default/270.png
%{_datadir}/%{name}/images/default/271.png
%{_datadir}/%{name}/images/default/272.png
%{_datadir}/%{name}/images/default/273.png
%{_datadir}/%{name}/images/default/274.png
%{_datadir}/%{name}/images/default/275.png
%{_datadir}/%{name}/images/default/276.png
%{_datadir}/%{name}/images/default/277.png
%{_datadir}/%{name}/images/default/278.png
%{_datadir}/%{name}/images/default/279.png
%{_datadir}/%{name}/images/default/28.png
%{_datadir}/%{name}/images/default/280.png
%{_datadir}/%{name}/images/default/281.png
%{_datadir}/%{name}/images/default/282.png
%{_datadir}/%{name}/images/default/283.png
%{_datadir}/%{name}/images/default/284.png
%{_datadir}/%{name}/images/default/285.png
%{_datadir}/%{name}/images/default/286.png
%{_datadir}/%{name}/images/default/287.png
%{_datadir}/%{name}/images/default/288.png
%{_datadir}/%{name}/images/default/289.png
%{_datadir}/%{name}/images/default/29.png
%{_datadir}/%{name}/images/default/290.png
%{_datadir}/%{name}/images/default/291.png
%{_datadir}/%{name}/images/default/292.png
%{_datadir}/%{name}/images/default/293.png
%{_datadir}/%{name}/images/default/294.png
%{_datadir}/%{name}/images/default/295.png
%{_datadir}/%{name}/images/default/296.png
%{_datadir}/%{name}/images/default/297.png
%{_datadir}/%{name}/images/default/298.png
%{_datadir}/%{name}/images/default/299.png
%{_datadir}/%{name}/images/default/3.png
%{_datadir}/%{name}/images/default/30.png
%{_datadir}/%{name}/images/default/300.png
%{_datadir}/%{name}/images/default/301.png
%{_datadir}/%{name}/images/default/302.png
%{_datadir}/%{name}/images/default/303.png
%{_datadir}/%{name}/images/default/304.png
%{_datadir}/%{name}/images/default/305.png
%{_datadir}/%{name}/images/default/306.png
%{_datadir}/%{name}/images/default/307.png
%{_datadir}/%{name}/images/default/308.png
%{_datadir}/%{name}/images/default/309.png
%{_datadir}/%{name}/images/default/31.png
%{_datadir}/%{name}/images/default/310.png
%{_datadir}/%{name}/images/default/311.png
%{_datadir}/%{name}/images/default/312.png
%{_datadir}/%{name}/images/default/313.png
%{_datadir}/%{name}/images/default/314.png
%{_datadir}/%{name}/images/default/315.png
%{_datadir}/%{name}/images/default/316.png
%{_datadir}/%{name}/images/default/317.png
%{_datadir}/%{name}/images/default/318.png
%{_datadir}/%{name}/images/default/319.png
%{_datadir}/%{name}/images/default/32.png
%{_datadir}/%{name}/images/default/320.png
%{_datadir}/%{name}/images/default/321.png
%{_datadir}/%{name}/images/default/322.png
%{_datadir}/%{name}/images/default/323.png
%{_datadir}/%{name}/images/default/324.png
%{_datadir}/%{name}/images/default/325.png
%{_datadir}/%{name}/images/default/326.png
%{_datadir}/%{name}/images/default/327.png
%{_datadir}/%{name}/images/default/328.png
%{_datadir}/%{name}/images/default/329.png
%{_datadir}/%{name}/images/default/33.png
%{_datadir}/%{name}/images/default/330.png
%{_datadir}/%{name}/images/default/331.png
%{_datadir}/%{name}/images/default/332.png
%{_datadir}/%{name}/images/default/333.png
%{_datadir}/%{name}/images/default/334.png
%{_datadir}/%{name}/images/default/335.png
%{_datadir}/%{name}/images/default/336.png
%{_datadir}/%{name}/images/default/337.png
%{_datadir}/%{name}/images/default/338.png
%{_datadir}/%{name}/images/default/339.png
%{_datadir}/%{name}/images/default/34.png
%{_datadir}/%{name}/images/default/340.png
%{_datadir}/%{name}/images/default/341.png
%{_datadir}/%{name}/images/default/342.png
%{_datadir}/%{name}/images/default/343.png
%{_datadir}/%{name}/images/default/344.png
%{_datadir}/%{name}/images/default/345.png
%{_datadir}/%{name}/images/default/346.png
%{_datadir}/%{name}/images/default/347.png
%{_datadir}/%{name}/images/default/348.png
%{_datadir}/%{name}/images/default/349.png
%{_datadir}/%{name}/images/default/35.png
%{_datadir}/%{name}/images/default/350.png
%{_datadir}/%{name}/images/default/351.png
%{_datadir}/%{name}/images/default/352.png
%{_datadir}/%{name}/images/default/353.png
%{_datadir}/%{name}/images/default/354.png
%{_datadir}/%{name}/images/default/355.png
%{_datadir}/%{name}/images/default/356.png
%{_datadir}/%{name}/images/default/357.png
%{_datadir}/%{name}/images/default/358.png
%{_datadir}/%{name}/images/default/359.png
%{_datadir}/%{name}/images/default/36.png
%{_datadir}/%{name}/images/default/360.png
%{_datadir}/%{name}/images/default/361.png
%{_datadir}/%{name}/images/default/362.png
%{_datadir}/%{name}/images/default/363.png
%{_datadir}/%{name}/images/default/364.png
%{_datadir}/%{name}/images/default/365.png
%{_datadir}/%{name}/images/default/366.png
%{_datadir}/%{name}/images/default/367.png
%{_datadir}/%{name}/images/default/368.png
%{_datadir}/%{name}/images/default/369.png
%{_datadir}/%{name}/images/default/37.png
%{_datadir}/%{name}/images/default/370.png
%{_datadir}/%{name}/images/default/371.png
%{_datadir}/%{name}/images/default/372.png
%{_datadir}/%{name}/images/default/373.png
%{_datadir}/%{name}/images/default/374.png
%{_datadir}/%{name}/images/default/375.png
%{_datadir}/%{name}/images/default/376.png
%{_datadir}/%{name}/images/default/377.png
%{_datadir}/%{name}/images/default/378.png
%{_datadir}/%{name}/images/default/379.png
%{_datadir}/%{name}/images/default/38.png
%{_datadir}/%{name}/images/default/380.png
%{_datadir}/%{name}/images/default/381.png
%{_datadir}/%{name}/images/default/382.png
%{_datadir}/%{name}/images/default/383.png
%{_datadir}/%{name}/images/default/384.png
%{_datadir}/%{name}/images/default/385.png
%{_datadir}/%{name}/images/default/386.png
%{_datadir}/%{name}/images/default/387.png
%{_datadir}/%{name}/images/default/388.png
%{_datadir}/%{name}/images/default/389.png
%{_datadir}/%{name}/images/default/39.png
%{_datadir}/%{name}/images/default/390.png
%{_datadir}/%{name}/images/default/391.png
%{_datadir}/%{name}/images/default/392.png
%{_datadir}/%{name}/images/default/393.png
%{_datadir}/%{name}/images/default/394.png
%{_datadir}/%{name}/images/default/395.png
%{_datadir}/%{name}/images/default/396.png
%{_datadir}/%{name}/images/default/397.png
%{_datadir}/%{name}/images/default/398.png
%{_datadir}/%{name}/images/default/399.png
%{_datadir}/%{name}/images/default/4.png
%{_datadir}/%{name}/images/default/40.png
%{_datadir}/%{name}/images/default/400.png
%{_datadir}/%{name}/images/default/401.png
%{_datadir}/%{name}/images/default/402.png
%{_datadir}/%{name}/images/default/403.png
%{_datadir}/%{name}/images/default/404.png
%{_datadir}/%{name}/images/default/405.png
%{_datadir}/%{name}/images/default/406.png
%{_datadir}/%{name}/images/default/407.png
%{_datadir}/%{name}/images/default/408.png
%{_datadir}/%{name}/images/default/409.png
%{_datadir}/%{name}/images/default/41.png
%{_datadir}/%{name}/images/default/410.png
%{_datadir}/%{name}/images/default/411.png
%{_datadir}/%{name}/images/default/412.png
%{_datadir}/%{name}/images/default/413.png
%{_datadir}/%{name}/images/default/414.png
%{_datadir}/%{name}/images/default/415.png
%{_datadir}/%{name}/images/default/416.png
%{_datadir}/%{name}/images/default/417.png
%{_datadir}/%{name}/images/default/418.png
%{_datadir}/%{name}/images/default/419.png
%{_datadir}/%{name}/images/default/42.png
%{_datadir}/%{name}/images/default/420.png
%{_datadir}/%{name}/images/default/421.png
%{_datadir}/%{name}/images/default/422.png
%{_datadir}/%{name}/images/default/423.png
%{_datadir}/%{name}/images/default/424.png
%{_datadir}/%{name}/images/default/425.png
%{_datadir}/%{name}/images/default/426.png
%{_datadir}/%{name}/images/default/427.png
%{_datadir}/%{name}/images/default/428.png
%{_datadir}/%{name}/images/default/429.png
%{_datadir}/%{name}/images/default/43.png
%{_datadir}/%{name}/images/default/430.png
%{_datadir}/%{name}/images/default/431.png
%{_datadir}/%{name}/images/default/432.png
%{_datadir}/%{name}/images/default/433.png
%{_datadir}/%{name}/images/default/434.png
%{_datadir}/%{name}/images/default/435.png
%{_datadir}/%{name}/images/default/436.png
%{_datadir}/%{name}/images/default/437.png
%{_datadir}/%{name}/images/default/438.png
%{_datadir}/%{name}/images/default/439.png
%{_datadir}/%{name}/images/default/44.png
%{_datadir}/%{name}/images/default/440.png
%{_datadir}/%{name}/images/default/441.png
%{_datadir}/%{name}/images/default/442.png
%{_datadir}/%{name}/images/default/443.png
%{_datadir}/%{name}/images/default/444.png
%{_datadir}/%{name}/images/default/445.png
%{_datadir}/%{name}/images/default/446.png
%{_datadir}/%{name}/images/default/447.png
%{_datadir}/%{name}/images/default/448.png
%{_datadir}/%{name}/images/default/449.png
%{_datadir}/%{name}/images/default/45.png
%{_datadir}/%{name}/images/default/450.png
%{_datadir}/%{name}/images/default/451.png
%{_datadir}/%{name}/images/default/452.png
%{_datadir}/%{name}/images/default/453.png
%{_datadir}/%{name}/images/default/454.png
%{_datadir}/%{name}/images/default/455.png
%{_datadir}/%{name}/images/default/456.png
%{_datadir}/%{name}/images/default/457.png
%{_datadir}/%{name}/images/default/458.png
%{_datadir}/%{name}/images/default/459.png
%{_datadir}/%{name}/images/default/46.png
%{_datadir}/%{name}/images/default/460.png
%{_datadir}/%{name}/images/default/461.png
%{_datadir}/%{name}/images/default/462.png
%{_datadir}/%{name}/images/default/463.png
%{_datadir}/%{name}/images/default/464.png
%{_datadir}/%{name}/images/default/465.png
%{_datadir}/%{name}/images/default/466.png
%{_datadir}/%{name}/images/default/467.png
%{_datadir}/%{name}/images/default/468.png
%{_datadir}/%{name}/images/default/469.png
%{_datadir}/%{name}/images/default/47.png
%{_datadir}/%{name}/images/default/470.png
%{_datadir}/%{name}/images/default/471.png
%{_datadir}/%{name}/images/default/472.png
%{_datadir}/%{name}/images/default/473.png
%{_datadir}/%{name}/images/default/474.png
%{_datadir}/%{name}/images/default/475.png
%{_datadir}/%{name}/images/default/476.png
%{_datadir}/%{name}/images/default/477.png
%{_datadir}/%{name}/images/default/478.png
%{_datadir}/%{name}/images/default/479.png
%{_datadir}/%{name}/images/default/48.png
%{_datadir}/%{name}/images/default/480.png
%{_datadir}/%{name}/images/default/481.png
%{_datadir}/%{name}/images/default/482.png
%{_datadir}/%{name}/images/default/483.png
%{_datadir}/%{name}/images/default/484.png
%{_datadir}/%{name}/images/default/485.png
%{_datadir}/%{name}/images/default/486.png
%{_datadir}/%{name}/images/default/487.png
%{_datadir}/%{name}/images/default/488.png
%{_datadir}/%{name}/images/default/489.png
%{_datadir}/%{name}/images/default/49.png
%{_datadir}/%{name}/images/default/490.png
%{_datadir}/%{name}/images/default/491.png
%{_datadir}/%{name}/images/default/492.png
%{_datadir}/%{name}/images/default/493.png
%{_datadir}/%{name}/images/default/494.png
%{_datadir}/%{name}/images/default/495.png
%{_datadir}/%{name}/images/default/496.png
%{_datadir}/%{name}/images/default/497.png
%{_datadir}/%{name}/images/default/498.png
%{_datadir}/%{name}/images/default/499.png
%{_datadir}/%{name}/images/default/5.png
%{_datadir}/%{name}/images/default/50.png
%{_datadir}/%{name}/images/default/500.png
%{_datadir}/%{name}/images/default/501.png
%{_datadir}/%{name}/images/default/502.png
%{_datadir}/%{name}/images/default/503.png
%{_datadir}/%{name}/images/default/504.png
%{_datadir}/%{name}/images/default/505.png
%{_datadir}/%{name}/images/default/506.png
%{_datadir}/%{name}/images/default/507.png
%{_datadir}/%{name}/images/default/508.png
%{_datadir}/%{name}/images/default/509.png
%{_datadir}/%{name}/images/default/51.png
%{_datadir}/%{name}/images/default/510.png
%{_datadir}/%{name}/images/default/511.png
%{_datadir}/%{name}/images/default/512.png
%{_datadir}/%{name}/images/default/513.png
%{_datadir}/%{name}/images/default/514.png
%{_datadir}/%{name}/images/default/515.png
%{_datadir}/%{name}/images/default/516.png
%{_datadir}/%{name}/images/default/517.png
%{_datadir}/%{name}/images/default/518.png
%{_datadir}/%{name}/images/default/519.png
%{_datadir}/%{name}/images/default/52.png
%{_datadir}/%{name}/images/default/520.png
%{_datadir}/%{name}/images/default/521.png
%{_datadir}/%{name}/images/default/522.png
%{_datadir}/%{name}/images/default/523.png
%{_datadir}/%{name}/images/default/524.png
%{_datadir}/%{name}/images/default/525.png
%{_datadir}/%{name}/images/default/526.png
%{_datadir}/%{name}/images/default/527.png
%{_datadir}/%{name}/images/default/528.png
%{_datadir}/%{name}/images/default/529.png
%{_datadir}/%{name}/images/default/53.png
%{_datadir}/%{name}/images/default/530.png
%{_datadir}/%{name}/images/default/531.png
%{_datadir}/%{name}/images/default/532.png
%{_datadir}/%{name}/images/default/533.png
%{_datadir}/%{name}/images/default/534.png
%{_datadir}/%{name}/images/default/535.png
%{_datadir}/%{name}/images/default/536.png
%{_datadir}/%{name}/images/default/537.png
%{_datadir}/%{name}/images/default/538.png
%{_datadir}/%{name}/images/default/539.png
%{_datadir}/%{name}/images/default/54.png
%{_datadir}/%{name}/images/default/540.png
%{_datadir}/%{name}/images/default/541.png
%{_datadir}/%{name}/images/default/542.png
%{_datadir}/%{name}/images/default/543.png
%{_datadir}/%{name}/images/default/544.png
%{_datadir}/%{name}/images/default/545.png
%{_datadir}/%{name}/images/default/546.png
%{_datadir}/%{name}/images/default/547.png
%{_datadir}/%{name}/images/default/548.png
%{_datadir}/%{name}/images/default/549.png
%{_datadir}/%{name}/images/default/55.png
%{_datadir}/%{name}/images/default/550.png
%{_datadir}/%{name}/images/default/551.png
%{_datadir}/%{name}/images/default/552.png
%{_datadir}/%{name}/images/default/553.png
%{_datadir}/%{name}/images/default/554.png
%{_datadir}/%{name}/images/default/555.png
%{_datadir}/%{name}/images/default/556.png
%{_datadir}/%{name}/images/default/557.png
%{_datadir}/%{name}/images/default/558.png
%{_datadir}/%{name}/images/default/559.png
%{_datadir}/%{name}/images/default/56.png
%{_datadir}/%{name}/images/default/560.png
%{_datadir}/%{name}/images/default/561.png
%{_datadir}/%{name}/images/default/562.png
%{_datadir}/%{name}/images/default/563.png
%{_datadir}/%{name}/images/default/564.png
%{_datadir}/%{name}/images/default/565.png
%{_datadir}/%{name}/images/default/566.png
%{_datadir}/%{name}/images/default/567.png
%{_datadir}/%{name}/images/default/568.png
%{_datadir}/%{name}/images/default/569.png
%{_datadir}/%{name}/images/default/57.png
%{_datadir}/%{name}/images/default/570.png
%{_datadir}/%{name}/images/default/571.png
%{_datadir}/%{name}/images/default/572.png
%{_datadir}/%{name}/images/default/573.png
%{_datadir}/%{name}/images/default/574.png
%{_datadir}/%{name}/images/default/575.png
%{_datadir}/%{name}/images/default/576.png
%{_datadir}/%{name}/images/default/577.png
%{_datadir}/%{name}/images/default/578.png
%{_datadir}/%{name}/images/default/579.png
%{_datadir}/%{name}/images/default/58.png
%{_datadir}/%{name}/images/default/580.png
%{_datadir}/%{name}/images/default/581.png
%{_datadir}/%{name}/images/default/582.png
%{_datadir}/%{name}/images/default/583.png
%{_datadir}/%{name}/images/default/584.png
%{_datadir}/%{name}/images/default/585.png
%{_datadir}/%{name}/images/default/586.png
%{_datadir}/%{name}/images/default/587.png
%{_datadir}/%{name}/images/default/588.png
%{_datadir}/%{name}/images/default/589.png
%{_datadir}/%{name}/images/default/59.png
%{_datadir}/%{name}/images/default/590.png
%{_datadir}/%{name}/images/default/591.png
%{_datadir}/%{name}/images/default/592.png
%{_datadir}/%{name}/images/default/593.png
%{_datadir}/%{name}/images/default/594.png
%{_datadir}/%{name}/images/default/595.png
%{_datadir}/%{name}/images/default/596.png
%{_datadir}/%{name}/images/default/597.png
%{_datadir}/%{name}/images/default/598.png
%{_datadir}/%{name}/images/default/599.png
%{_datadir}/%{name}/images/default/6.png
%{_datadir}/%{name}/images/default/60.png
%{_datadir}/%{name}/images/default/600.png
%{_datadir}/%{name}/images/default/601.png
%{_datadir}/%{name}/images/default/602.png
%{_datadir}/%{name}/images/default/603.png
%{_datadir}/%{name}/images/default/604.png
%{_datadir}/%{name}/images/default/61.png
%{_datadir}/%{name}/images/default/62.png
%{_datadir}/%{name}/images/default/63.png
%{_datadir}/%{name}/images/default/64.png
%{_datadir}/%{name}/images/default/65.png
%{_datadir}/%{name}/images/default/66.png
%{_datadir}/%{name}/images/default/67.png
%{_datadir}/%{name}/images/default/68.png
%{_datadir}/%{name}/images/default/69.png
%{_datadir}/%{name}/images/default/7.png
%{_datadir}/%{name}/images/default/70.png
%{_datadir}/%{name}/images/default/71.png
%{_datadir}/%{name}/images/default/72.png
%{_datadir}/%{name}/images/default/73.png
%{_datadir}/%{name}/images/default/74.png
%{_datadir}/%{name}/images/default/75.png
%{_datadir}/%{name}/images/default/76.png
%{_datadir}/%{name}/images/default/77.png
%{_datadir}/%{name}/images/default/78.png
%{_datadir}/%{name}/images/default/79.png
%{_datadir}/%{name}/images/default/8.png
%{_datadir}/%{name}/images/default/80.png
%{_datadir}/%{name}/images/default/81.png
%{_datadir}/%{name}/images/default/82.png
%{_datadir}/%{name}/images/default/83.png
%{_datadir}/%{name}/images/default/84.png
%{_datadir}/%{name}/images/default/85.png
%{_datadir}/%{name}/images/default/86.png
%{_datadir}/%{name}/images/default/87.png
%{_datadir}/%{name}/images/default/88.png
%{_datadir}/%{name}/images/default/89.png
%{_datadir}/%{name}/images/default/9.png
%{_datadir}/%{name}/images/default/90.png
%{_datadir}/%{name}/images/default/91.png
%{_datadir}/%{name}/images/default/92.png
%{_datadir}/%{name}/images/default/93.png
%{_datadir}/%{name}/images/default/94.png
%{_datadir}/%{name}/images/default/95.png
%{_datadir}/%{name}/images/default/96.png
%{_datadir}/%{name}/images/default/97.png
%{_datadir}/%{name}/images/default/98.png
%{_datadir}/%{name}/images/default/99.png
%{_datadir}/%{name}/language
%{_datadir}/%{name}/language/%{name}_ar.qm
%{_datadir}/%{name}/language/%{name}_ar.ts
%{_datadir}/%{name}/language/%{name}_en.qm
%{_datadir}/%{name}/language/%{name}_en.ts
%{_datadir}/%{name}/language/%{name}_fr.qm
%{_datadir}/%{name}/language/%{name}_fr.ts
%{_datadir}/%{name}/language/launguagerc
%{_datadir}/%{name}/quran.db
%{_datadir}/%{name}/reciterInfo
%{_datadir}/%{name}/tafasir
%{_datadir}/%{name}/tafasir/sa3dy.db
%{_datadir}/%{name}/tafasir/tafasirInfo
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/themes/arabesque
%{_datadir}/%{name}/themes/arabesque/bot.png
%{_datadir}/%{name}/themes/arabesque/bot_left.png
%{_datadir}/%{name}/themes/arabesque/bot_right.png
%{_datadir}/%{name}/themes/arabesque/left.png
%{_datadir}/%{name}/themes/arabesque/right.png
%{_datadir}/%{name}/themes/arabesque/top.png
%{_datadir}/%{name}/themes/arabesque/top_left.png
%{_datadir}/%{name}/themes/arabesque/top_right.png
%{_datadir}/%{name}/themes/arabesque2
%{_datadir}/%{name}/themes/arabesque2/bot.png
%{_datadir}/%{name}/themes/arabesque2/bot_left.png
%{_datadir}/%{name}/themes/arabesque2/bot_right.png
%{_datadir}/%{name}/themes/arabesque2/left.png
%{_datadir}/%{name}/themes/arabesque2/right.png
%{_datadir}/%{name}/themes/arabesque2/top.png
%{_datadir}/%{name}/themes/arabesque2/top_left.png
%{_datadir}/%{name}/themes/arabesque2/top_right.png
%{_datadir}/%{name}/themes/mashaf
%{_datadir}/%{name}/themes/mashaf/bot.png
%{_datadir}/%{name}/themes/mashaf/bot_left.png
%{_datadir}/%{name}/themes/mashaf/bot_right.png
%{_datadir}/%{name}/themes/mashaf/left.png
%{_datadir}/%{name}/themes/mashaf/preview.png
%{_datadir}/%{name}/themes/mashaf/right.png
%{_datadir}/%{name}/themes/mashaf/top.png
%{_datadir}/%{name}/themes/mashaf/top_left.png
%{_datadir}/%{name}/themes/mashaf/top_right.png
%{_datadir}/%{name}/themes/mashaf2
%{_datadir}/%{name}/themes/mashaf2/bot.png
%{_datadir}/%{name}/themes/mashaf2/bot_left.png
%{_datadir}/%{name}/themes/mashaf2/bot_right.png
%{_datadir}/%{name}/themes/mashaf2/left.png
%{_datadir}/%{name}/themes/mashaf2/preview.png
%{_datadir}/%{name}/themes/mashaf2/right.png
%{_datadir}/%{name}/themes/mashaf2/top.png
%{_datadir}/%{name}/themes/mashaf2/top_left.png
%{_datadir}/%{name}/themes/mashaf2/top_right.png
%{_datadir}/%{name}/themes/mashaf3
%{_datadir}/%{name}/themes/mashaf3/bot.png
%{_datadir}/%{name}/themes/mashaf3/bot_left.png
%{_datadir}/%{name}/themes/mashaf3/bot_right.png
%{_datadir}/%{name}/themes/mashaf3/left.png
%{_datadir}/%{name}/themes/mashaf3/right.png
%{_datadir}/%{name}/themes/mashaf3/top.png
%{_datadir}/%{name}/themes/mashaf3/top_left.png
%{_datadir}/%{name}/themes/mashaf3/top_right.png
%{_datadir}/%{name}/themes/zakhrafa
%{_datadir}/%{name}/themes/zakhrafa/bot.png
%{_datadir}/%{name}/themes/zakhrafa/bot_left.png
%{_datadir}/%{name}/themes/zakhrafa/bot_right.png
%{_datadir}/%{name}/themes/zakhrafa/left.png
%{_datadir}/%{name}/themes/zakhrafa/right.png
%{_datadir}/%{name}/themes/zakhrafa/top.png
%{_datadir}/%{name}/themes/zakhrafa/top_left.png
%{_datadir}/%{name}/themes/zakhrafa/top_right.png
%{_datadir}/%{name}/themes/zakhrafa2
%{_datadir}/%{name}/themes/zakhrafa2/bot.png
%{_datadir}/%{name}/themes/zakhrafa2/bot_left.png
%{_datadir}/%{name}/themes/zakhrafa2/bot_right.png
%{_datadir}/%{name}/themes/zakhrafa2/left.png
%{_datadir}/%{name}/themes/zakhrafa2/right.png
%{_datadir}/%{name}/themes/zakhrafa2/top.png
%{_datadir}/%{name}/themes/zakhrafa2/top_left.png
%{_datadir}/%{name}/themes/zakhrafa2/top_right.png
%{_datadir}/%{name}/translat
%{_datadir}/%{name}/translat/ar_muyassar.db
%{_datadir}/%{name}/translat/en_sahih.db
%{_datadir}/%{name}/translat/fr_hamidullah.db
%{_datadir}/%{name}/translat/translatInfo
%{_datadir}/icons
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/22x22
%{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24
%{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48
%{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64
%{_datadir}/icons/hicolor/64x64/apps
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png

%changelog


