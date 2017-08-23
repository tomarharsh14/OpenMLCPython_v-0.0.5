CONFIG +=  compile_examples qpa largefile precompile_header use_gold_linker enable_new_dtags sse2 sse3 ssse3 sse4_1 sse4_2 avx avx2 avx512f avx512er avx512cd avx512pf pcre
QT_BUILD_PARTS += libs tools
QT_NO_DEFINES =  ALSA CUPS EGL EGLFS EGL_X11 GLIB IMAGEFORMAT_JPEG LIBPROXY OPENVG PULSEAUDIO TSLIB ZLIB
QT_QCONFIG_PATH = 
host_build {
    QT_CPU_FEATURES.x86_64 =  mmx sse sse2
} else {
    QT_CPU_FEATURES.x86_64 =  mmx sse sse2
}
QT_COORD_TYPE = double
QT_LFLAGS_ODBC   = -lodbc
styles += mac fusion windows
DEFINES += QT_NO_MTDEV
QMAKE_INCDIR_OPENGL =  "/usr/include/libdrm"
QMAKE_LIBDIR_OPENGL = 
QMAKE_LIBS_OPENGL =  "-lGL"
QMAKE_CFLAGS_OPENGL = 
QMAKE_CFLAGS_FONTCONFIG = -I/usr/include/freetype2 
QMAKE_LIBS_FONTCONFIG = -lfontconfig -lfreetype 
DEFINES += QT_NO_LIBUDEV
DEFINES += QT_NO_TSLIB
QMAKE_INCDIR_XKBCOMMON_EVDEV = 
QMAKE_LIBS_XKBCOMMON_EVDEV = -lxkbcommon 
DEFINES += QT_NO_LIBINPUT
QMAKE_LIBXI_VERSION_MAJOR = 1
QMAKE_LIBXI_VERSION_MINOR = 7
QMAKE_LIBXI_VERSION_PATCH = 4
QMAKE_X11_PREFIX = /usr
QMAKE_XKB_CONFIG_ROOT = /usr/share/X11/xkb
QMAKE_CFLAGS_XCB = 
QMAKE_LIBS_XCB = -lxcb 
sql-drivers = 
sql-plugins =  sqlite
