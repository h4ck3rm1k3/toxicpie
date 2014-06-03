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


import datetime
from .ctox import *
from .util import ToxError
from . import util


class Tox(object):
    instance_map = {}

    @staticmethod
    def friend_request_callback(tox, public_key, data, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_friend_request(util.buffer_to_hex(public_key), util.ptr_to_string(data, length))

    @staticmethod
    def friend_message_callback(tox, friend_id, message, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_friend_message(friend_id, util.ptr_to_string(message, length))

    @staticmethod
    def friend_action_callback(tox, friend_id, action, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_friend_action(friend_id, util.ptr_to_string(action, length))

    @staticmethod
    def name_change_callback(tox, friend_id, new_name, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_name_change(friend_id, util.ptr_to_string(new_name, length))

    @staticmethod
    def status_message_callback(tox, friend_id, new_status, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_status_message(friend_id, util.ptr_to_string(new_status, length))

    @staticmethod
    def user_status_callback(tox, friend_id, user_status, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_user_status(friend_id, user_status)

    @staticmethod
    def typing_change_callback(tox, friend_id, is_typing, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_typing_change(friend_id, is_typing)

    @staticmethod
    def read_receipt_callback(tox, friend_id, message_id, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_read_receipt(friend_id, message_id)

    @staticmethod
    def connection_status_callback(tox, friend_id, status, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_connection_status(friend_id, status)

    @staticmethod
    def group_invite_callback(tox, friend_id, group_pk, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_group_invite(friend_id, group_pk)

    @staticmethod
    def group_message_callback(tox, group_id, peer_id, message, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_group_message(group_id, peer_id, util.ptr_to_string(message, length))

    @staticmethod
    def group_action_callback(tox, group_id, peer_id, action, length, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_group_action(group_id, peer_id, util.ptr_to_string(action, length))

    @staticmethod
    def group_namelist_change_callback(tox, group_id, peer_id, change, userdata):
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_group_namelist_change(group_id, peer_id, change)

    @staticmethod
    def file_send_request_callback(tox, friend_id, file_id, file_size, filename, filename_length, userdata):
        if filename_length == 0:
            return
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_file_send_request(friend_id, file_id, file_size, util.ptr_to_string(filename, filename_length))

    @staticmethod
    def file_control_callback(tox, friend_id, receive_send, file_id, control_type, data, length, userdata):
        if length == 0:
            return
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_file_control(friend_id, receive_send, file_id, control_type, util.ptr_to_buffer(data, length))

    @staticmethod
    def file_data_callback(tox, friend_id, file_id, data, length, userdata):
        if length == 0:
            return
        try:
            self = Tox.instance_map[addressof(tox.contents)]
        except KeyError:
            return
        with self._lock:
            self.on_file_data(friend_id, file_id, util.ptr_to_buffer(data, length))

    def __init__(self, ipv6_enabled=TOX_ENABLE_IPV6_DEFAULT):
        self._p = tox_new(int(ipv6_enabled))
        if self._p == 0:
            raise ToxError('Could not create tox instance')
        self.instance_map[addressof(self._p.contents)] = self
        self._lock = util.ScopedRLock()

        # These are required, otherwise python will destroy function objects due to lost references
        self._ref_tox_friend_request_callback = tox_callback_friend_request.argtypes[1](self.friend_request_callback)
        self._ref_friend_message_callback = tox_callback_friend_message.argtypes[1](self.friend_message_callback)
        self._ref_friend_action_callback = tox_callback_friend_action.argtypes[1](self.friend_action_callback)
        self._ref_name_change_callback = tox_callback_name_change.argtypes[1](self.name_change_callback)
        self._ref_status_message_callback = tox_callback_status_message.argtypes[1](self.status_message_callback)
        self._ref_user_status_callback = tox_callback_user_status.argtypes[1](self.user_status_callback)
        self._ref_typing_change_callback = tox_callback_typing_change.argtypes[1](self.typing_change_callback)
        self._ref_read_receipt_callback = tox_callback_read_receipt.argtypes[1](self.read_receipt_callback)
        self._ref_connection_status_callback = tox_callback_connection_status.argtypes[1](self.connection_status_callback)
        self._ref_group_invite_callback = tox_callback_group_invite.argtypes[1](self.group_invite_callback)
        self._ref_group_message_callback = tox_callback_group_message.argtypes[1](self.group_message_callback)
        self._ref_group_action_callback = tox_callback_group_action.argtypes[1](self.group_action_callback)
        self._ref_group_namelist_change_callback = tox_callback_group_namelist_change.argtypes[1](self.group_namelist_change_callback)
        self._ref_file_send_request_callback = tox_callback_file_send_request.argtypes[1](self.file_send_request_callback)
        self._ref_file_control_callback = tox_callback_file_control.argtypes[1](self.file_control_callback)
        self._ref_file_data_callback = tox_callback_file_data.argtypes[1](self.file_data_callback)

        tox_callback_friend_request(self._p, self._ref_tox_friend_request_callback, 0)
        tox_callback_friend_message(self._p, self._ref_friend_message_callback, 0)
        tox_callback_friend_action(self._p, self._ref_friend_action_callback, 0)
        tox_callback_name_change(self._p, self._ref_name_change_callback, 0)
        tox_callback_status_message(self._p, self._ref_status_message_callback, 0)
        tox_callback_user_status(self._p, self._ref_user_status_callback, 0)
        tox_callback_typing_change(self._p, self._ref_typing_change_callback, 0)
        tox_callback_read_receipt(self._p, self._ref_read_receipt_callback, 0)
        tox_callback_connection_status(self._p, self._ref_connection_status_callback, 0)
        tox_callback_group_invite(self._p, self._ref_group_invite_callback, 0)
        tox_callback_group_message(self._p, self._ref_group_message_callback, 0)
        tox_callback_group_action(self._p, self._ref_group_action_callback, 0)
        tox_callback_group_namelist_change(self._p, self._ref_group_namelist_change_callback, 0)
        tox_callback_file_send_request(self._p, self._ref_file_send_request_callback, 0)
        tox_callback_file_control(self._p, self._ref_file_control_callback, 0)
        tox_callback_file_data(self._p, self._ref_file_data_callback, 0)

    def on_connection_status(self, friend_id, status):
        pass

    def on_file_control(self, friend_id, receive_send, file_id, control_type, data):
        pass

    def on_file_data(self, friend_id, file_id, data):
        pass

    def on_file_send_request(self, friend_id, file_id, file_size, filename):
        pass

    def on_friend_action(self, friend_id, action):
        pass

    def on_friend_message(self, friend_id, message):
        pass

    def on_friend_request(self, address, message):
        pass

    def on_group_action(self, group_id, peer_id, action):
        pass

    def on_group_invite(self, friend_id, group_key):
        pass

    def on_group_message(self, group_id, peer_id, message):
        pass

    def on_group_namelist_change(self, group_id, peer_id, change):
        pass

    def on_name_change(self, friend_id, name):
        pass

    def on_read_receipt(self, friend_id, message_id):
        pass

    def on_status_message(self, friend_id, message):
        pass

    def on_typing_change(self, friend_id, is_typing):
        pass

    def on_user_status(self, friend_id, status):
        pass

    def kill(self):
        with self._lock:
            assert self._p
            del self.instance_map[addressof(self._p.contents)]
            tox_kill(self._p)
            self._p = None

    def save(self, file):
        with self._lock:
            assert self._p
            buffer_size = tox_size(self._p)
            assert buffer_size > 0
            buffer = create_string_buffer(buffer_size)
            tox_save(self._p, buffer)
            with open(file, 'w+b') as fp:
                fp.write(buffer.raw)

    def load(self, file):
        with self._lock:
            assert self._p
            with open(file, 'rb') as fp:
                data = fp.read()
                buffer = create_string_buffer(data, len(data))
                err = tox_load(self._p, buffer, len(buffer))
                if err == -1:
                    raise ToxError('Could not load tox data due to internal error')

    def get_address(self):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(TOX_FRIEND_ADDRESS_SIZE)
            tox_get_address(self._p, buffer)
            return util.buffer_to_hex(buffer)

    def add_friend(self, address, message):
        with self._lock:
            assert self._p
            message = message.encode('utf-8')
            try:
                address = util.hex_to_buffer(address)
            except:
                raise ToxError('Invalid ID format')
            message = create_string_buffer(message, len(message))
            friend_id = err = tox_add_friend(self._p, address, message, len(message))
            if err < 0:
                raise ToxError('Could not add friend', err)
            return friend_id

    def add_friend_norequest(self, address):
        with self._lock:
            assert self._p
            address = util.hex_to_buffer(address)
            assert len(address) == TOX_CLIENT_ID_SIZE
            friend_id = err = tox_add_friend_norequest(self._p, address)
            if err < 0:
                raise ToxError('Could not add friend', err)
            return friend_id

    def get_friend_number(self, address):
        with self._lock:
            assert self._p
            address = util.hex_to_buffer(address)
            assert len(address) == TOX_CLIENT_ID_SIZE
            friend_id = tox_get_friend_number(self._p, address)
            return None if friend_id < 0 else friend_id

    def get_client_id(self, friend_id):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(TOX_CLIENT_ID_SIZE)
            if tox_get_client_id(self._p, friend_id, buffer) == 0:
                return util.buffer_to_hex(buffer)

    def del_friend(self, friend_id):
        with self._lock:
            assert self._p
            return tox_del_friend(self._p, friend_id) == 0

    def get_friend_connection_status(self, friend_id):
        with self._lock:
            assert self._p
            status = tox_get_friend_connection_status(self._p, friend_id)
            if status < 0:
                return None
            return status

    def friend_exists(self, friend_id):
        with self._lock:
            assert self._p
            return tox_friend_exists(self._p, friend_id) != 0

    def send_message(self, friend_id, message):
        with self._lock:
            assert self._p
            message = message.encode('utf-8')
            buffer = create_string_buffer(message, len(message))
            return tox_send_message(self._p, friend_id, buffer, len(buffer))

    def send_message_withid(self, friend_id, message_id, message):
        with self._lock:
            assert self._p
            message = message.encode('utf-8')
            buffer = create_string_buffer(message, len(message))
            message_id = tox_send_message_withid(self._p, friend_id, message_id, buffer, len(buffer))
            if message_id < 0:
                return None
            return message_id

    def send_action(self, friend_id, action):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(action, len(action))
            action_id = tox_send_action(self._p, friend_id, buffer, len(buffer))
            if action_id < 0:
                return None
            return action_id

    def send_action_withid(self, friend_id, action_id, action):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(action, len(action))
            action_id = tox_send_action_withid(self._p, friend_id, action_id, buffer, len(buffer))
            if action_id < 0:
                return None
            return action_id

    def set_name(self, name):
        with self._lock:
            assert self._p
            name = name.encode('utf-8')
            buffer = create_string_buffer(name, len(name))
            return tox_set_name(self._p, buffer, len(buffer)) == 0

    def get_self_name(self):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(self.get_self_name_size())
            if tox_get_self_name(self._p, buffer) < 1:
                return None
            return buffer.value.decode('utf-8')

    def get_name(self, friend_id):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(self.get_name_size(friend_id))
            if tox_get_name(self._p, friend_id, buffer) < 0:
                return None
            return buffer.value.decode('utf-8')

    def get_name_size(self, friend_id):
        with self._lock:
            assert self._p
            return int(tox_get_name_size(self._p, friend_id))

    def get_self_name_size(self):
        with self._lock:
            assert self._p
            return int(tox_get_self_name_size(self._p))

    def set_status_message(self, message):
        with self._lock:
            assert self._p
            message = message.encode('utf-8')
            buffer = create_string_buffer(message, len(message))
            return tox_set_status_message(self._p, buffer, len(buffer)) == 0

    def set_user_status(self, status):
        with self._lock:
            assert self._p
            return tox_set_user_status(self._p, status) == 0

    def get_status_message_size(self, friend_id):
        with self._lock:
            assert self._p
            return int(tox_get_status_message_size(self._p, friend_id))

    def get_self_status_message_size(self):
        with self._lock:
            assert self._p
            return int(tox_get_self_status_message_size(self._p))

    def get_status_message(self, friend_id):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(self.get_status_message_size(friend_id))
            if tox_get_status_message(self._p, friend_id, buffer, len(buffer)) < 0:
                return None
            return buffer.value.decode('utf-8')

    def get_self_status_message(self):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(self.get_self_status_message_size())
            if tox_get_self_status_message(self._p, buffer, len(buffer)) < 0:
                return None
            return buffer.value.decode('utf-8')

    def get_user_status(self, friend_id):
        with self._lock:
            assert self._p
            return int(tox_get_user_status(self._p, friend_id))

    def get_self_user_status(self):
        with self._lock:
            assert self._p
            return int(tox_get_self_user_status(self._p))

    def get_last_online(self, friend_id):
        with self._lock:
            assert self._p
            timestamp = tox_get_last_online(self._p, friend_id)
            if timestamp > 0:
                return datetime.datetime.fromtimestamp(timestamp)
            return None

    def set_user_is_typing(self, friend_id, is_typing):
        with self._lock:
            assert self._p
            return tox_set_user_is_typing(self._p, friend_id, int(is_typing)) == 0

    def get_is_typing(self, friend_id):
        with self._lock:
            assert self._p
            return tox_get_is_typing(self._p, friend_id) > 0

    def set_sends_receipts(self, friend_id, yesno):
        with self._lock:
            assert self._p
            tox_set_sends_receipts(self._p, friend_id, int(yesno))

    def count_friendlist(self):
        with self._lock:
            assert self._p
            return int(tox_count_friendlist(self._p))

    def get_num_online_friends(self):
        with self._lock:
            assert self._p
            return int(tox_get_num_online_friends(self._p))

    def get_friendlist(self):
        with self._lock:
            assert self._p
            friendlist_count = self.count_friendlist()
            friend_id_array = (c_int * friendlist_count)()
            tox_get_friendlist(self._p, friend_id_array, friendlist_count)
            return [int(id) for id in friend_id_array]

    def get_nospam(self):
        with self._lock:
            assert self._p
            return int(tox_get_nospam(self._p))

    def set_nospam(self, nospam):
        with self._lock:
            assert self._p
            tox_set_nospam(self._p, nospam)

    def add_groupchat(self):
        with self._lock:
            assert self._p
            group_id = tox_add_groupchat(self._p)
            if group_id < 0:
                return None
            return group_id

    def del_groupchat(self, group_id):
        with self._lock:
            assert self._p
            return tox_del_groupchat(self._p, group_id) == 0

    def group_peername(self, group_id, peer_id):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(TOX_MAX_NAME_LENGTH)
            if tox_group_peername(self._p, group_id, peer_id, buffer) < 0:
                return None
            return buffer.value.decode('utf-8')

    def invite_friend(self, friend_id, group_id):
        with self._lock:
            assert self._p
            return tox_invite_friend(self._p, friend_id, group_id) == 0

    def join_groupchat(self, friend_id, group_pk):
        with self._lock:
            assert self._p
            buffer = util.hex_to_buffer(group_pk)
            return tox_join_groupchat(self._p, friend_id, buffer) == 0

    def group_message_send(self, group_id, message):
        """
        Returns: 1 on success, 0 on failure
        """
        with self._lock:
            assert self._p
            message = message.encode('utf-8')
            buffer = create_string_buffer(message, len(message))
            # Return value is made compatible with message_send() API.
            # 0 = failure, 1 = simulating valid message id
            return tox_group_message_send(self._p, group_id, buffer, len(buffer)) + 1

    def group_action_send(self, group_id, action):
        with self._lock:
            assert self._p
            buffer = create_string_buffer(action, len(action))
            return tox_group_action_send(self._p, group_id, buffer, len(buffer)) == 0

    def group_number_peers(self, group_id):
        with self._lock:
            assert self._p
            return int(tox_group_number_peers(self._p, group_id))

    def group_get_names(self, group_id):
        with self._lock:
            assert self._p
            peerlist_count = self.group_number_peers(group_id)
            name_len_array = (c_uint16 * peerlist_count)()
            name_array = (c_char * peerlist_count * TOX_MAX_NAME_LENGTH)()
            if tox_group_get_names(self._p, group_id, name_array, name_len_array, peerlist_count) < 0:
                return None
            names = []
            for i in len(peerlist_count):
                length = name_array[i]
                names.append(name_array[i * TOX_MAX_NAME_LENGTH])

    def count_chatlist(self):
        with self._lock:
            assert self._p
            return int(tox_count_chatlist(self._p))

    def get_chatlist(self):
        with self._lock:
            assert self._p
            chatlist_count = self.count_chatlist()
            chat_id_array = (c_int * chatlist_count)()
            tox_get_chatlist(self._p, chat_id_array, chatlist_count)
            return [int(id) for id in chat_id_array]

    def new_file_sender(self, friend_id, file_size, file_name):
        with self._lock:
            assert self._p
            # # /usr/local/include/tox/tox.h: 566
            # for _lib in _libs.values():
            #     if not hasattr(_lib, 'tox_new_file_sender'):
            #         continue
            #     tox_new_file_sender = _lib.tox_new_file_sender
            #     tox_new_file_sender.argtypes = [POINTER(Tox), c_int32, c_uint64, POINTER(c_uint8), c_uint16]
            #     tox_new_file_sender.restype = c_int

    def file_send_control(self, friend_id, send_receive, file_id, message_id, data):
        with self._lock:
            assert self._p
            # # /usr/local/include/tox/tox.h: 576
            # for _lib in _libs.values():
            #     if not hasattr(_lib, 'tox_file_send_control'):
            #         continue
            #     tox_file_send_control = _lib.tox_file_send_control
            #     tox_file_send_control.argtypes = [POINTER(Tox), c_int32, c_uint8, c_uint8, c_uint8, POINTER(c_uint8), c_uint16]
            #     tox_file_send_control.restype = c_int

    def file_send_data(self, friend_id, file_id, data):
        with self._lock:
            assert self._p
            # # /usr/local/include/tox/tox.h: 584
            # for _lib in _libs.values():
            #     if not hasattr(_lib, 'tox_file_send_data'):
            #         continue
            #     tox_file_send_data = _lib.tox_file_send_data
            #     tox_file_send_data.argtypes = [POINTER(Tox), c_int32, c_uint8, POINTER(c_uint8), c_uint16]
            #     tox_file_send_data.restype = c_int

    def file_data_size(self, file_id):
        with self._lock:
            assert self._p
            # # /usr/local/include/tox/tox.h: 591
            # for _lib in _libs.values():
            #     if not hasattr(_lib, 'tox_file_data_size'):
            #         continue
            #     tox_file_data_size = _lib.tox_file_data_size
            #     tox_file_data_size.argtypes = [POINTER(Tox), c_int32]
            #     tox_file_data_size.restype = c_int

    def file_data_remaining(self, friend_id, file_id, send_receive):
        with self._lock:
            assert self._p
            # # /usr/local/include/tox/tox.h: 600
            # for _lib in _libs.values():
            #     if not hasattr(_lib, 'tox_file_data_remaining'):
            #         continue
            #     tox_file_data_remaining = _lib.tox_file_data_remaining
            #     tox_file_data_remaining.argtypes = [POINTER(Tox), c_int32, c_uint8, c_uint8]
            #     tox_file_data_remaining.restype = c_uint64

    def bootstrap_from_address(self, address, ipv6_enabled, port, pk):
        with self._lock:
            assert self._p
            # # /usr/local/include/tox/tox.h: 620
            # for _lib in _libs.values():
            #     if not hasattr(_lib, 'tox_bootstrap_from_address'):
            #         continue
            #     tox_bootstrap_from_address = _lib.tox_bootstrap_from_address
            #     tox_bootstrap_from_address.argtypes = [POINTER(Tox), String, c_uint8, c_uint16, POINTER(c_uint8)]
            #     tox_bootstrap_from_address.restype = c_int

    def isconnected(self):
        with self._lock:
            return self._p and tox_isconnected(self._p) != 0

    def do(self):
        with self._lock:
            assert self._p
            tox_do(self._p)

    # # /usr/local/include/tox/tox.h: 684
    # for _lib in _libs.values():
    #     if not hasattr(_lib, 'tox_wait_data_size'):
    #         continue
    #     tox_wait_data_size = _lib.tox_wait_data_size
    #     tox_wait_data_size.argtypes = []
    #     tox_wait_data_size.restype = c_size_t
    #
    # # /usr/local/include/tox/tox.h: 685
    # for _lib in _libs.values():
    #     if not hasattr(_lib, 'tox_wait_prepare'):
    #         continue
    #     tox_wait_prepare = _lib.tox_wait_prepare
    #     tox_wait_prepare.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    #     tox_wait_prepare.restype = c_int
    #
    # # /usr/local/include/tox/tox.h: 686
    # for _lib in _libs.values():
    #     if not hasattr(_lib, 'tox_wait_execute'):
    #         continue
    #     tox_wait_execute = _lib.tox_wait_execute
    #     tox_wait_execute.argtypes = [POINTER(c_uint8), c_long, c_long]
    #     tox_wait_execute.restype = c_int
    #
    # # /usr/local/include/tox/tox.h: 687
    # for _lib in _libs.values():
    #     if not hasattr(_lib, 'tox_wait_cleanup'):
    #         continue
    #     tox_wait_cleanup = _lib.tox_wait_cleanup
    #     tox_wait_cleanup.argtypes = [POINTER(Tox), POINTER(c_uint8)]
    #     tox_wait_cleanup.restype = c_int

