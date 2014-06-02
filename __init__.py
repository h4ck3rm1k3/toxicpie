# this file is part of toxicpie - a ctypes python wrapper for Project Tox
# Copyright (C) 2014  tox.im project
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .tox import Tox, ToxError
from .tox import \
    TOX_FAERR_TOOLONG, \
    TOX_FAERR_NOMESSAGE, \
    TOX_FAERR_OWNKEY, \
    TOX_FAERR_ALREADYSENT, \
    TOX_FAERR_UNKNOWN, \
    TOX_FAERR_BADCHECKSUM, \
    TOX_FAERR_SETNEWNOSPAM, \
    TOX_FAERR_NOMEM, \
    TOX_USERSTATUS_NONE, \
    TOX_USERSTATUS_AWAY, \
    TOX_USERSTATUS_BUSY, \
    TOX_USERSTATUS_INVALID, \
    TOX_CHAT_CHANGE_PEER_ADD, \
    TOX_CHAT_CHANGE_PEER_DEL, \
    TOX_CHAT_CHANGE_PEER_NAME, \
    TOX_FILECONTROL_ACCEPT, \
    TOX_FILECONTROL_PAUSE, \
    TOX_FILECONTROL_KILL, \
    TOX_FILECONTROL_FINISHED, \
    TOX_FILECONTROL_RESUME_BROKEN, \
    TOX_MAX_NAME_LENGTH, \
    TOX_MAX_MESSAGE_LENGTH, \
    TOX_MAX_STATUSMESSAGE_LENGTH, \
    TOX_CLIENT_ID_SIZE, \
    TOX_FRIEND_ADDRESS_SIZE, \
    TOX_PORTRANGE_FROM, \
    TOX_PORTRANGE_TO, \
    TOX_PORT_DEFAULT, \
    TOX_ENABLE_IPV6_DEFAULT
