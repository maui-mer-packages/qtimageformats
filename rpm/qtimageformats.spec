Name:       qt5-qtimageformats
Summary:    Qt Imageformats
Version:    5.0.2
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  libmng-devel
Buildrequires:  libtiff-devel  

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the Qt Image Formats plugin

%package plugin-mng
Summary:    Qt Imageformats - MNG plugin
Group:      Qt/Qt

%description plugin-mng
This package provides the MNG imageformat plugin


%package plugin-tga
Summary:    Qt Imageformats - TGA plugin
Group:      Qt/Qt

%description plugin-tga
This package provides the TGA imageformat plugin


%package plugin-tiff
Summary:    Qt Imageformats - TIFF plugin
Group:      Qt/Qt

%description plugin-tiff
This package provides the TIFF imageformat plugin


%package plugin-wbmp
Summary:    Qt Imageformats - WBMP plugin
Group:      Qt/Qt

%description plugin-wbmp
This package provides the WBMP imageformat plugin


%package plugin-dds
Summary:    Qt Imageformats - DDS plugin
Group:      Qt/Qt

%description plugin-dds
This package provides the DDS imageformat plugin


%package plugin-icns
Summary:    Qt Imageformats - ICNS plugin
Group:      Qt/Qt

%description plugin-icns
This package provides the ICNS imageformat plugin


%package plugin-jp2
Summary:    Qt Imageformats - JP2 plugin
Group:      Qt/Qt

%description plugin-jp2
This package provides the JP2 imageformat plugin


%package plugin-webp
Summary:    Qt Imageformats - WEBP plugin
Group:      Qt/Qt

%description plugin-webp
This package provides the WEBP imageformat plugin

%prep
%setup -q -n %{name}-%{version}/upstream

%build
export QTDIR=/usr/share/qt5
touch .git # Make sure syncqt is run

%qmake5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files plugin-mng
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqmng.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QMngPlugin.cmake

%files plugin-tga
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqtga.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake

%files plugin-tiff
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqtiff.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake

%files plugin-wbmp
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqwbmp.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake

%files plugin-dds
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqdds.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QDDSPlugin.cmake

%files plugin-icns
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqicns.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake

%files plugin-jp2
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqjp2.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake

%files plugin-webp
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/imageformats/libqwebp.so
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake