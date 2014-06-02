'''Wrapper for tox.h

Generated with:
./ctypesgen.py -ltoxcore /usr/local/include/tox/tox.h

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes
import os
import sys
from ctypes import *

if sys.version_info[0] == 3:
    def cmp(a, b):
        return (a > b) - (a < b)
    sys.maxint = sys.maxsize
    unicode = str
    str = bytes

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del _int_types


class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]


def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x

        p.from_param = classmethod(from_param)

    return p


class UserString:
    def __init__(self, seq):
        if isinstance(1, (str, bytes)):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0);
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(1, (str, bytes)):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))

    def __radd__(self, other):
        if isinstance(1, (str, bytes)):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1:]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index + 1:]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(1, (str, bytes)):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub) + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(1, (str, bytes)):
            self.data += other
        else:
            self.data += str(other)
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):
    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, bytes, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError as e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # FIXME / TODO return '.' and os.path.dirname(__file__)
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")
        dirs.append(os.path.dirname(__file__))

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")
        directories.append(os.path.dirname(__file__))

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        unix_lib_dirs_list = ['/lib', '/usr/lib', '/usr/lib32', '/lib64', '/usr/lib64', '/usr/local/lib',
                              '/usr/local/lib32', '/usr/local/lib64']
        if sys.platform.startswith('linux'):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            bitage = platform.architecture()[0]
            if bitage.startswith('32'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/i386-linux-gnu', '/usr/lib/i386-linux-gnu']
            elif bitage.startswith('64'):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ['/lib/x86_64-linux-gnu', '/usr/lib/x86_64-linux-gnu']
            else:
                # guess...
                unix_lib_dirs_list += glob.glob('/lib/*linux-gnu')
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["toxcore"] = load_library("toxcore")

# 1 libraries
# End libraries

# No modules

enum_anon_20 = c_int # /usr/local/include/tox/tox.h: 78

TOX_FAERR_TOOLONG = (-1) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_NOMESSAGE = (-2) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_OWNKEY = (-3) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_ALREADYSENT = (-4) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_UNKNOWN = (-5) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_BADCHECKSUM = (-6) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_SETNEWNOSPAM = (-7) # /usr/local/include/tox/tox.h: 78

TOX_FAERR_NOMEM = (-8) # /usr/local/include/tox/tox.h: 78

enum_anon_21 = c_int # /usr/local/include/tox/tox.h: 98

TOX_USERSTATUS_NONE = 0 # /usr/local/include/tox/tox.h: 98

TOX_USERSTATUS_AWAY = (TOX_USERSTATUS_NONE + 1) # /usr/local/include/tox/tox.h: 98

TOX_USERSTATUS_BUSY = (TOX_USERSTATUS_AWAY + 1) # /usr/local/include/tox/tox.h: 98

TOX_USERSTATUS_INVALID = (TOX_USERSTATUS_BUSY + 1) # /usr/local/include/tox/tox.h: 98

TOX_USERSTATUS = enum_anon_21 # /usr/local/include/tox/tox.h: 98

# /usr/local/include/tox/tox.h: 102
class struct_Tox(Structure):
    pass

Tox = struct_Tox # /usr/local/include/tox/tox.h: 102

# /usr/local/include/tox/tox.h: 115
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_address'):
        continue
    tox_get_address = _lib.tox_get_address
    tox_get_address.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_get_address.restype = None
    break

# /usr/local/include/tox/tox.h: 133
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_add_friend'):
        continue
    tox_add_friend = _lib.tox_add_friend
    tox_add_friend.argtypes = [POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_uint16]
    tox_add_friend.restype = c_int32
    break

# /usr/local/include/tox/tox.h: 140
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_add_friend_norequest'):
        continue
    tox_add_friend_norequest = _lib.tox_add_friend_norequest
    tox_add_friend_norequest.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_add_friend_norequest.restype = c_int32
    break

# /usr/local/include/tox/tox.h: 144
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_friend_number'):
        continue
    tox_get_friend_number = _lib.tox_get_friend_number
    tox_get_friend_number.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_get_friend_number.restype = c_int32
    break

# /usr/local/include/tox/tox.h: 151
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_client_id'):
        continue
    tox_get_client_id = _lib.tox_get_client_id
    tox_get_client_id.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8)]
    tox_get_client_id.restype = c_int
    break

# /usr/local/include/tox/tox.h: 158
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_del_friend'):
        continue
    tox_del_friend = _lib.tox_del_friend
    tox_del_friend.argtypes = [POINTER(Tox), c_int32]
    tox_del_friend.restype = c_int
    break

# /usr/local/include/tox/tox.h: 166
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_friend_connection_status'):
        continue
    tox_get_friend_connection_status = _lib.tox_get_friend_connection_status
    tox_get_friend_connection_status.argtypes = [POINTER(Tox), c_int32]
    tox_get_friend_connection_status.restype = c_int
    break

# /usr/local/include/tox/tox.h: 173
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_friend_exists'):
        continue
    tox_friend_exists = _lib.tox_friend_exists
    tox_friend_exists.argtypes = [POINTER(Tox), c_int32]
    tox_friend_exists.restype = c_int
    break

# /usr/local/include/tox/tox.h: 185
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_send_message'):
        continue
    tox_send_message = _lib.tox_send_message
    tox_send_message.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8), c_uint32]
    tox_send_message.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 186
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_send_message_withid'):
        continue
    tox_send_message_withid = _lib.tox_send_message_withid
    tox_send_message_withid.argtypes = [POINTER(Tox), c_int32, c_uint32, POINTER(c_uint8), c_uint32]
    tox_send_message_withid.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 198
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_send_action'):
        continue
    tox_send_action = _lib.tox_send_action
    tox_send_action.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8), c_uint32]
    tox_send_action.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 199
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_send_action_withid'):
        continue
    tox_send_action_withid = _lib.tox_send_action_withid
    tox_send_action_withid.argtypes = [POINTER(Tox), c_int32, c_uint32, POINTER(c_uint8), c_uint32]
    tox_send_action_withid.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 209
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_set_name'):
        continue
    tox_set_name = _lib.tox_set_name
    tox_set_name.argtypes = [POINTER(Tox), POINTER(c_uint8), c_uint16]
    tox_set_name.restype = c_int
    break

# /usr/local/include/tox/tox.h: 219
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_self_name'):
        continue
    tox_get_self_name = _lib.tox_get_self_name
    tox_get_self_name.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_get_self_name.restype = c_uint16
    break

# /usr/local/include/tox/tox.h: 227
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_name'):
        continue
    tox_get_name = _lib.tox_get_name
    tox_get_name.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8)]
    tox_get_name.restype = c_int
    break

# /usr/local/include/tox/tox.h: 232
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_name_size'):
        continue
    tox_get_name_size = _lib.tox_get_name_size
    tox_get_name_size.argtypes = [POINTER(Tox), c_int32]
    tox_get_name_size.restype = c_int
    break

# /usr/local/include/tox/tox.h: 233
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_self_name_size'):
        continue
    tox_get_self_name_size = _lib.tox_get_self_name_size
    tox_get_self_name_size.argtypes = [POINTER(Tox)]
    tox_get_self_name_size.restype = c_int
    break

# /usr/local/include/tox/tox.h: 242
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_set_status_message'):
        continue
    tox_set_status_message = _lib.tox_set_status_message
    tox_set_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8), c_uint16]
    tox_set_status_message.restype = c_int
    break

# /usr/local/include/tox/tox.h: 243
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_set_user_status'):
        continue
    tox_set_user_status = _lib.tox_set_user_status
    tox_set_user_status.argtypes = [POINTER(Tox), c_uint8]
    tox_set_user_status.restype = c_int
    break

# /usr/local/include/tox/tox.h: 248
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_status_message_size'):
        continue
    tox_get_status_message_size = _lib.tox_get_status_message_size
    tox_get_status_message_size.argtypes = [POINTER(Tox), c_int32]
    tox_get_status_message_size.restype = c_int
    break

# /usr/local/include/tox/tox.h: 249
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_self_status_message_size'):
        continue
    tox_get_self_status_message_size = _lib.tox_get_self_status_message_size
    tox_get_self_status_message_size.argtypes = [POINTER(Tox)]
    tox_get_self_status_message_size.restype = c_int
    break

# /usr/local/include/tox/tox.h: 258
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_status_message'):
        continue
    tox_get_status_message = _lib.tox_get_status_message
    tox_get_status_message.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8), c_uint32]
    tox_get_status_message.restype = c_int
    break

# /usr/local/include/tox/tox.h: 259
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_self_status_message'):
        continue
    tox_get_self_status_message = _lib.tox_get_self_status_message
    tox_get_self_status_message.argtypes = [POINTER(Tox), POINTER(c_uint8), c_uint32]
    tox_get_self_status_message.restype = c_int
    break

# /usr/local/include/tox/tox.h: 266
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_user_status'):
        continue
    tox_get_user_status = _lib.tox_get_user_status
    tox_get_user_status.argtypes = [POINTER(Tox), c_int32]
    tox_get_user_status.restype = c_uint8
    break

# /usr/local/include/tox/tox.h: 267
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_self_user_status'):
        continue
    tox_get_self_user_status = _lib.tox_get_self_user_status
    tox_get_self_user_status.argtypes = [POINTER(Tox)]
    tox_get_self_user_status.restype = c_uint8
    break

# /usr/local/include/tox/tox.h: 273
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_last_online'):
        continue
    tox_get_last_online = _lib.tox_get_last_online
    tox_get_last_online.argtypes = [POINTER(Tox), c_int32]
    tox_get_last_online.restype = c_uint64
    break

# /usr/local/include/tox/tox.h: 281
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_set_user_is_typing'):
        continue
    tox_set_user_is_typing = _lib.tox_set_user_is_typing
    tox_set_user_is_typing.argtypes = [POINTER(Tox), c_int32, c_uint8]
    tox_set_user_is_typing.restype = c_int
    break

# /usr/local/include/tox/tox.h: 288
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_is_typing'):
        continue
    tox_get_is_typing = _lib.tox_get_is_typing
    tox_get_is_typing.argtypes = [POINTER(Tox), c_int32]
    tox_get_is_typing.restype = c_uint8
    break

# /usr/local/include/tox/tox.h: 293
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_set_sends_receipts'):
        continue
    tox_set_sends_receipts = _lib.tox_set_sends_receipts
    tox_set_sends_receipts.argtypes = [POINTER(Tox), c_int32, c_int]
    tox_set_sends_receipts.restype = None
    break

# /usr/local/include/tox/tox.h: 298
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_count_friendlist'):
        continue
    tox_count_friendlist = _lib.tox_count_friendlist
    tox_count_friendlist.argtypes = [POINTER(Tox)]
    tox_count_friendlist.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 301
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_num_online_friends'):
        continue
    tox_get_num_online_friends = _lib.tox_get_num_online_friends
    tox_get_num_online_friends.argtypes = [POINTER(Tox)]
    tox_get_num_online_friends.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 308
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_friendlist'):
        continue
    tox_get_friendlist = _lib.tox_get_friendlist
    tox_get_friendlist.argtypes = [POINTER(Tox), POINTER(c_int32), c_uint32]
    tox_get_friendlist.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 313
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_friend_request'):
        continue
    tox_callback_friend_request = _lib.tox_callback_friend_request
    tox_callback_friend_request.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), POINTER(c_uint8), POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_friend_request.restype = None
    break

# /usr/local/include/tox/tox.h: 319
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_friend_message'):
        continue
    tox_callback_friend_message = _lib.tox_callback_friend_message
    tox_callback_friend_message.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_friend_message.restype = None
    break

# /usr/local/include/tox/tox.h: 325
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_friend_action'):
        continue
    tox_callback_friend_action = _lib.tox_callback_friend_action
    tox_callback_friend_action.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_friend_action.restype = None
    break

# /usr/local/include/tox/tox.h: 332
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_name_change'):
        continue
    tox_callback_name_change = _lib.tox_callback_name_change
    tox_callback_name_change.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_name_change.restype = None
    break

# /usr/local/include/tox/tox.h: 339
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_status_message'):
        continue
    tox_callback_status_message = _lib.tox_callback_status_message
    tox_callback_status_message.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_status_message.restype = None
    break

# /usr/local/include/tox/tox.h: 345
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_user_status'):
        continue
    tox_callback_user_status = _lib.tox_callback_user_status
    tox_callback_user_status.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint8, POINTER(None)), POINTER(None)]
    tox_callback_user_status.restype = None
    break

# /usr/local/include/tox/tox.h: 350
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_typing_change'):
        continue
    tox_callback_typing_change = _lib.tox_callback_typing_change
    tox_callback_typing_change.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint8, POINTER(None)), POINTER(None)]
    tox_callback_typing_change.restype = None
    break

# /usr/local/include/tox/tox.h: 361
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_read_receipt'):
        continue
    tox_callback_read_receipt = _lib.tox_callback_read_receipt
    tox_callback_read_receipt.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint32, POINTER(None)), POINTER(None)]
    tox_callback_read_receipt.restype = None
    break

# /usr/local/include/tox/tox.h: 374
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_connection_status'):
        continue
    tox_callback_connection_status = _lib.tox_callback_connection_status
    tox_callback_connection_status.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint8, POINTER(None)), POINTER(None)]
    tox_callback_connection_status.restype = None
    break

# /usr/local/include/tox/tox.h: 381
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_nospam'):
        continue
    tox_get_nospam = _lib.tox_get_nospam
    tox_get_nospam.argtypes = [POINTER(Tox)]
    tox_get_nospam.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 382
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_set_nospam'):
        continue
    tox_set_nospam = _lib.tox_set_nospam
    tox_set_nospam.argtypes = [POINTER(Tox), c_uint32]
    tox_set_nospam.restype = None
    break

# /usr/local/include/tox/tox.h: 391
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_group_invite'):
        continue
    tox_callback_group_invite = _lib.tox_callback_group_invite
    tox_callback_group_invite.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, POINTER(c_uint8), POINTER(None)), POINTER(None)]
    tox_callback_group_invite.restype = None
    break

# /usr/local/include/tox/tox.h: 397
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_group_message'):
        continue
    tox_callback_group_message = _lib.tox_callback_group_message
    tox_callback_group_message.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int, c_int, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_group_message.restype = None
    break

# /usr/local/include/tox/tox.h: 404
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_group_action'):
        continue
    tox_callback_group_action = _lib.tox_callback_group_action
    tox_callback_group_action.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int, c_int, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_group_action.restype = None
    break

enum_anon_22 = c_int # /usr/local/include/tox/tox.h: 416

TOX_CHAT_CHANGE_PEER_ADD = 0 # /usr/local/include/tox/tox.h: 416

TOX_CHAT_CHANGE_PEER_DEL = (TOX_CHAT_CHANGE_PEER_ADD + 1) # /usr/local/include/tox/tox.h: 416

TOX_CHAT_CHANGE_PEER_NAME = (TOX_CHAT_CHANGE_PEER_DEL + 1) # /usr/local/include/tox/tox.h: 416

TOX_CHAT_CHANGE = enum_anon_22 # /usr/local/include/tox/tox.h: 416

# /usr/local/include/tox/tox.h: 418
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_group_namelist_change'):
        continue
    tox_callback_group_namelist_change = _lib.tox_callback_group_namelist_change
    tox_callback_group_namelist_change.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int, c_int, c_uint8, POINTER(None)), POINTER(None)]
    tox_callback_group_namelist_change.restype = None
    break

# /usr/local/include/tox/tox.h: 426
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_add_groupchat'):
        continue
    tox_add_groupchat = _lib.tox_add_groupchat
    tox_add_groupchat.argtypes = [POINTER(Tox)]
    tox_add_groupchat.restype = c_int
    break

# /usr/local/include/tox/tox.h: 433
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_del_groupchat'):
        continue
    tox_del_groupchat = _lib.tox_del_groupchat
    tox_del_groupchat.argtypes = [POINTER(Tox), c_int]
    tox_del_groupchat.restype = c_int
    break

# /usr/local/include/tox/tox.h: 441
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_group_peername'):
        continue
    tox_group_peername = _lib.tox_group_peername
    tox_group_peername.argtypes = [POINTER(Tox), c_int, c_int, POINTER(c_uint8)]
    tox_group_peername.restype = c_int
    break

# /usr/local/include/tox/tox.h: 447
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_invite_friend'):
        continue
    tox_invite_friend = _lib.tox_invite_friend
    tox_invite_friend.argtypes = [POINTER(Tox), c_int32, c_int]
    tox_invite_friend.restype = c_int
    break

# /usr/local/include/tox/tox.h: 454
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_join_groupchat'):
        continue
    tox_join_groupchat = _lib.tox_join_groupchat
    tox_join_groupchat.argtypes = [POINTER(Tox), c_int32, POINTER(c_uint8)]
    tox_join_groupchat.restype = c_int
    break

# /usr/local/include/tox/tox.h: 460
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_group_message_send'):
        continue
    tox_group_message_send = _lib.tox_group_message_send
    tox_group_message_send.argtypes = [POINTER(Tox), c_int, POINTER(c_uint8), c_uint32]
    tox_group_message_send.restype = c_int
    break

# /usr/local/include/tox/tox.h: 466
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_group_action_send'):
        continue
    tox_group_action_send = _lib.tox_group_action_send
    tox_group_action_send.argtypes = [POINTER(Tox), c_int, POINTER(c_uint8), c_uint32]
    tox_group_action_send.restype = c_int
    break

# /usr/local/include/tox/tox.h: 471
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_group_number_peers'):
        continue
    tox_group_number_peers = _lib.tox_group_number_peers
    tox_group_number_peers.argtypes = [POINTER(Tox), c_int]
    tox_group_number_peers.restype = c_int
    break

# /usr/local/include/tox/tox.h: 483
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_group_get_names'):
        continue
    tox_group_get_names = _lib.tox_group_get_names
    tox_group_get_names.argtypes = [POINTER(Tox), c_int, POINTER(c_uint8 * 128), POINTER(c_uint16), c_uint16]
    tox_group_get_names.restype = c_int
    break

# /usr/local/include/tox/tox.h: 489
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_count_chatlist'):
        continue
    tox_count_chatlist = _lib.tox_count_chatlist
    tox_count_chatlist.argtypes = [POINTER(Tox)]
    tox_count_chatlist.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 496
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_get_chatlist'):
        continue
    tox_get_chatlist = _lib.tox_get_chatlist
    tox_get_chatlist.argtypes = [POINTER(Tox), POINTER(c_int), c_uint32]
    tox_get_chatlist.restype = c_uint32
    break

enum_anon_23 = c_int # /usr/local/include/tox/tox.h: 527

TOX_FILECONTROL_ACCEPT = 0 # /usr/local/include/tox/tox.h: 527

TOX_FILECONTROL_PAUSE = (TOX_FILECONTROL_ACCEPT + 1) # /usr/local/include/tox/tox.h: 527

TOX_FILECONTROL_KILL = (TOX_FILECONTROL_PAUSE + 1) # /usr/local/include/tox/tox.h: 527

TOX_FILECONTROL_FINISHED = (TOX_FILECONTROL_KILL + 1) # /usr/local/include/tox/tox.h: 527

TOX_FILECONTROL_RESUME_BROKEN = (TOX_FILECONTROL_FINISHED + 1) # /usr/local/include/tox/tox.h: 527

# /usr/local/include/tox/tox.h: 538
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_file_send_request'):
        continue
    tox_callback_file_send_request = _lib.tox_callback_file_send_request
    tox_callback_file_send_request.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint8, c_uint64, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_file_send_request.restype = None
    break

# /usr/local/include/tox/tox.h: 549
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_file_control'):
        continue
    tox_callback_file_control = _lib.tox_callback_file_control
    tox_callback_file_control.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint8, c_uint8, c_uint8, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_file_control.restype = None
    break

# /usr/local/include/tox/tox.h: 557
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_callback_file_data'):
        continue
    tox_callback_file_data = _lib.tox_callback_file_data
    tox_callback_file_data.argtypes = [POINTER(Tox), CFUNCTYPE(UNCHECKED(None), POINTER(Tox), c_int32, c_uint8, POINTER(c_uint8), c_uint16, POINTER(None)), POINTER(None)]
    tox_callback_file_data.restype = None
    break

# /usr/local/include/tox/tox.h: 566
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_new_file_sender'):
        continue
    tox_new_file_sender = _lib.tox_new_file_sender
    tox_new_file_sender.argtypes = [POINTER(Tox), c_int32, c_uint64, POINTER(c_uint8), c_uint16]
    tox_new_file_sender.restype = c_int
    break

# /usr/local/include/tox/tox.h: 576
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_file_send_control'):
        continue
    tox_file_send_control = _lib.tox_file_send_control
    tox_file_send_control.argtypes = [POINTER(Tox), c_int32, c_uint8, c_uint8, c_uint8, POINTER(c_uint8), c_uint16]
    tox_file_send_control.restype = c_int
    break

# /usr/local/include/tox/tox.h: 584
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_file_send_data'):
        continue
    tox_file_send_data = _lib.tox_file_send_data
    tox_file_send_data.argtypes = [POINTER(Tox), c_int32, c_uint8, POINTER(c_uint8), c_uint16]
    tox_file_send_data.restype = c_int
    break

# /usr/local/include/tox/tox.h: 591
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_file_data_size'):
        continue
    tox_file_data_size = _lib.tox_file_data_size
    tox_file_data_size.argtypes = [POINTER(Tox), c_int32]
    tox_file_data_size.restype = c_int
    break

# /usr/local/include/tox/tox.h: 600
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_file_data_remaining'):
        continue
    tox_file_data_remaining = _lib.tox_file_data_remaining
    tox_file_data_remaining.argtypes = [POINTER(Tox), c_int32, c_uint8, c_uint8]
    tox_file_data_remaining.restype = c_uint64
    break

# /usr/local/include/tox/tox.h: 620
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_bootstrap_from_address'):
        continue
    tox_bootstrap_from_address = _lib.tox_bootstrap_from_address
    tox_bootstrap_from_address.argtypes = [POINTER(Tox), String, c_uint8, c_uint16, POINTER(c_uint8)]
    tox_bootstrap_from_address.restype = c_int
    break

# /usr/local/include/tox/tox.h: 626
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_isconnected'):
        continue
    tox_isconnected = _lib.tox_isconnected
    tox_isconnected.argtypes = [POINTER(Tox)]
    tox_isconnected.restype = c_int
    break

# /usr/local/include/tox/tox.h: 641
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_new'):
        continue
    tox_new = _lib.tox_new
    tox_new.argtypes = [c_uint8]
    tox_new.restype = POINTER(Tox)
    break

# /usr/local/include/tox/tox.h: 645
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_kill'):
        continue
    tox_kill = _lib.tox_kill
    tox_kill.argtypes = [POINTER(Tox)]
    tox_kill.restype = None
    break

# /usr/local/include/tox/tox.h: 648
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_do'):
        continue
    tox_do = _lib.tox_do
    tox_do.argtypes = [POINTER(Tox)]
    tox_do.restype = None
    break

# /usr/local/include/tox/tox.h: 684
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_wait_data_size'):
        continue
    tox_wait_data_size = _lib.tox_wait_data_size
    tox_wait_data_size.argtypes = []
    tox_wait_data_size.restype = c_size_t
    break

# /usr/local/include/tox/tox.h: 685
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_wait_prepare'):
        continue
    tox_wait_prepare = _lib.tox_wait_prepare
    tox_wait_prepare.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_wait_prepare.restype = c_int
    break

# /usr/local/include/tox/tox.h: 686
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_wait_execute'):
        continue
    tox_wait_execute = _lib.tox_wait_execute
    tox_wait_execute.argtypes = [POINTER(c_uint8), c_long, c_long]
    tox_wait_execute.restype = c_int
    break

# /usr/local/include/tox/tox.h: 687
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_wait_cleanup'):
        continue
    tox_wait_cleanup = _lib.tox_wait_cleanup
    tox_wait_cleanup.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_wait_cleanup.restype = c_int
    break

# /usr/local/include/tox/tox.h: 693
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_size'):
        continue
    tox_size = _lib.tox_size
    tox_size.argtypes = [POINTER(Tox)]
    tox_size.restype = c_uint32
    break

# /usr/local/include/tox/tox.h: 696
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_save'):
        continue
    tox_save = _lib.tox_save
    tox_save.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    tox_save.restype = None
    break

# /usr/local/include/tox/tox.h: 703
for _lib in _libs.values():
    if not hasattr(_lib, 'tox_load'):
        continue
    tox_load = _lib.tox_load
    tox_load.argtypes = [POINTER(Tox), POINTER(c_uint8), c_uint32]
    tox_load.restype = c_int
    break

# /usr/local/include/tox/tox.h: 61
TOX_MAX_NAME_LENGTH = 128

# /usr/local/include/tox/tox.h: 63
TOX_MAX_MESSAGE_LENGTH = 1003

# /usr/local/include/tox/tox.h: 64
TOX_MAX_STATUSMESSAGE_LENGTH = 1007

# /usr/local/include/tox/tox.h: 65
TOX_CLIENT_ID_SIZE = 32

# /usr/local/include/tox/tox.h: 67
TOX_FRIEND_ADDRESS_SIZE = ((TOX_CLIENT_ID_SIZE + sizeof(c_uint32)) + sizeof(c_uint16))

# /usr/local/include/tox/tox.h: 69
TOX_PORTRANGE_FROM = 33445

# /usr/local/include/tox/tox.h: 70
TOX_PORTRANGE_TO = 33545

# /usr/local/include/tox/tox.h: 71
TOX_PORT_DEFAULT = TOX_PORTRANGE_FROM

# /usr/local/include/tox/tox.h: 73
TOX_ENABLE_IPV6_DEFAULT = 1

Tox = struct_Tox # /usr/local/include/tox/tox.h: 102

# No inserted files

