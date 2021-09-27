# Copyright 2020-present Open Networking Foundation
# Original copyright 2020-present ADTRAN, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
from grpc_robot.grpc_robot import _package_version_get

from voltha_protos import events_pb2
from voltha_protos import tech_profile_pb2
from grpc_robot.tools.protobuf_to_dict import protobuf_to_dict


class VolthaTools(object):
    """
    Tools for the voltha, e.g decoding / conversions.
    """

    try:
        ROBOT_LIBRARY_VERSION = _package_version_get('grpc_robot')
    except NameError:
        ROBOT_LIBRARY_VERSION = 'unknown'

    @staticmethod
    def _convert_string_to_bytes(string):
        """Converts a string to a bytes object."""
        try:
            return bytes.fromhex(string.replace('\\x', ' '))
        except:
            try:
                b = bytearray()
                b.extend(map(ord, string))
                return bytes(b)
            except (TypeError, AttributeError, SystemError):
                return string

    def events_decode_event(self, bytestring, return_enum_integer='false', return_defaults='false', human_readable_timestamps='true'):
        """
        Converts bytes to an Event as defined in _message Event_ from events.proto

        *Parameters*:
        - bytestring: <bytes>; Byte string, e.g. as it comes from Kafka messages.
        - return_enum_integer: <string> or <bool>; Whether or not to return the enum values as integer values rather than their labels. Default: _false_.
        - return_defaults: <string> or <bool>; Whether or not to return the default values. Default: _false_.
        - human_readable_timestamps: <string> or <bool>; Whether or not to convert the timestamps to human-readable format. Default: _true_.

        *Return*: A dictionary with _event_ structure.

        *Example*:
        | Import Library | grpc_robot.VolthaTools | WITH NAME | voltha_tools |
        | ${kafka_records} | kafka.Records Get |
        | FOR | ${kafka_record} | IN | @{kafka_records} |
        |  | ${event} | voltha_tools.Events Decode Event | ${kafka_record}[message] |
        |  | Log | ${event} |
        | END |
        """
        return_enum_integer = str(return_enum_integer).lower() == 'true'
        result = events_pb2.Event.FromString(self._convert_string_to_bytes(bytestring))
        return protobuf_to_dict(result,
                                use_enum_labels=not return_enum_integer,
                                including_default_value_fields=str(return_defaults).lower() == 'true',
                                human_readable_timestamps=str(human_readable_timestamps).lower() == 'true')

    def tech_profile_decode_resource_instance(self, bytestring, return_enum_integer='false', return_defaults='false', human_readable_timestamps='true'):
        """
        Converts bytes to an resource instance as defined in _message ResourceInstance_ from tech_profile.proto

        *Parameters*:
        - bytestring: <bytes>; Byte string, e.g. as it comes from Kafka messages.
        - return_enum_integer: <string> or <bool>; Whether or not to return the enum values as integer values rather than their labels. Default: _false_.
        - return_defaults: <string> or <bool>; Whether or not to return the default values. Default: _false_.
        - human_readable_timestamps: <string> or <bool>; Whether or not to convert the timestamps to human-readable format. Default: _true_.

        *Return*: A dictionary with _event_ structure.

        *Example*:
        | Import Library | grpc_robot.VolthaTools | WITH NAME | voltha_tools |
        | ${kafka_records} | kafka.Records Get |
        | FOR | ${kafka_record} | IN | @{kafka_records} |
        |  | ${event} | voltha_tools. Tech Profile Decode Resource Instance | ${kafka_record}[message] |
        |  | Log | ${event} |
        | END |
        """
        return_enum_integer = str(return_enum_integer).lower() == 'true'
        result = tech_profile_pb2.ResourceInstance.FromString(self._convert_string_to_bytes(bytestring))
        return protobuf_to_dict(result,
                                use_enum_labels=not return_enum_integer,
                                including_default_value_fields=str(return_defaults).lower() == 'true',
                                human_readable_timestamps=str(human_readable_timestamps).lower() == 'true')


if __name__ == '__main__':
    messages = [
        b'\nD\n#Voltha.openolt..1626255789301080436\x10\x02 \x02*\x030.12\x06\x08\xad\xe3\xba\x87\x06:\x0c\x08\xad\xe3\xba\x87\x06\x10\xd9\xc9\xc8\x8f\x01"\xc2\x02\x11\x00\x00@k\xac;\xd8A\x1a\xb6\x02\n\x93\x01\n\x08PONStats\x11\x00\x00@k\xac;\xd8A*$65950aaf-b40f-4697-b5c3-8deb50fedd5d2-\n\x05oltid\x12$65950aaf-b40f-4697-b5c3-8deb50fedd5d2\x15\n\ndevicetype\x12\x07openolt2\x12\n\tportlabel\x12\x05pon-0\x12\x10\n\tTxPackets\x15\x00\x00\x8bC\x12\x15\n\x0eTxMcastPackets\x15\x00\x00\xa6B\x12\x15\n\x0eTxBcastPackets\x15\x00\x00\xa6B\x12\x0e\n\x07RxBytes\x15\x00\x00\x8bF\x12\x10\n\tRxPackets\x15\x00\x00\x8bC\x12\x15\n\x0eRxMcastPackets\x15\x00\x00\xa6B\x12\x15\n\x0eRxBcastPackets\x15\x00\x00\xa6B\x12\x0e\n\x07TxBytes\x15\x00\x00\x8bF',
        b'\nD\n#Voltha.openolt..1613491472935896440\x10\x02 \x02*\x030.12\x06\x08\xad\xe3\xba\x87\x06:\x0c\x08\xad\xe3\xba\x87\x06\x10\xd9\xc9\xc8\x8f\x01"\xc2\x02\x11\x00\x00@k\xac;\xd8A\x1a\xb6\x02\n\x93\x01\n\x08PONStats\x11\x00\x00@k\xac;\xd8A*$65950aaf-b40f-4697-b5c3-8deb50fedd5d2-\n\x05oltid\x12$65950aaf-b40f-4697-b5c3-8deb50fedd5d2\x15\n\ndevicetype\x12\x07openolt2\x12\n\tportlabel\x12\x05pon-0\x12\x10\n\tTxPackets\x15\x00\x00\x8bC\x12\x15\n\x0eTxMcastPackets\x15\x00\x00\xa6B\x12\x15\n\x0eTxBcastPackets\x15\x00\x00\xa6B\x12\x0e\n\x07RxBytes\x15\x00\x00\x8bF\x12\x10\n\tRxPackets\x15\x00\x00\x8bC\x12\x15\n\x0eRxMcastPackets\x15\x00\x00\xa6B\x12\x15\n\x0eRxBcastPackets\x15\x00\x00\xa6B\x12\x0e\n\x07TxBytes\x15\x00\x00\x8bF'
    ]
    for message in messages:
        print(VolthaTools().events_decode_event(message))

    messages = [
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x39\x35\x36\x31\x37\x31\x32\x62\x2d\x35\x33\x32\x33\x2d\x34\x64\x64\x63\x2d\x38\x36\x62\x34\x2d\x64\x35\x31\x62\x62\x34\x61\x65\x30\x37\x33\x39\x7d\x2f\x70\x6f\x6e\x2d\x7b\x31\x7d\x2f\x6f\x6e\x75\x2d\x7b\x32\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x81\x08\x2a\x10\x88\x08\x89\x08\x8a\x08\x8b\x08\x8c\x08\x8d\x08\x8e\x08\x8f\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x35\x66\x35\x39\x61\x32\x32\x63\x2d\x37\x63\x37\x65\x2d\x34\x65\x30\x63\x2d\x39\x38\x30\x65\x2d\x37\x34\x66\x31\x35\x33\x62\x33\x32\x33\x38\x31\x7d\x2f\x70\x6f\x6e\x2d\x7b\x30\x7d\x2f\x6f\x6e\x75\x2d\x7b\x31\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x81\x08\x2a\x10\x88\x08\x89\x08\x8a\x08\x8b\x08\x8c\x08\x8d\x08\x8e\x08\x8f\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x35\x66\x35\x39\x61\x32\x32\x63\x2d\x37\x63\x37\x65\x2d\x34\x65\x30\x63\x2d\x39\x38\x30\x65\x2d\x37\x34\x66\x31\x35\x33\x62\x33\x32\x33\x38\x31\x7d\x2f\x70\x6f\x6e\x2d\x7b\x30\x7d\x2f\x6f\x6e\x75\x2d\x7b\x32\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x80\x08\x2a\x10\x80\x08\x81\x08\x82\x08\x83\x08\x84\x08\x85\x08\x86\x08\x87\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x35\x66\x35\x39\x61\x32\x32\x63\x2d\x37\x63\x37\x65\x2d\x34\x65\x30\x63\x2d\x39\x38\x30\x65\x2d\x37\x34\x66\x31\x35\x33\x62\x33\x32\x33\x38\x31\x7d\x2f\x70\x6f\x6e\x2d\x7b\x31\x7d\x2f\x6f\x6e\x75\x2d\x7b\x31\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x81\x08\x2a\x10\x88\x08\x89\x08\x8a\x08\x8b\x08\x8c\x08\x8d\x08\x8e\x08\x8f\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x35\x66\x35\x39\x61\x32\x32\x63\x2d\x37\x63\x37\x65\x2d\x34\x65\x30\x63\x2d\x39\x38\x30\x65\x2d\x37\x34\x66\x31\x35\x33\x62\x33\x32\x33\x38\x31\x7d\x2f\x70\x6f\x6e\x2d\x7b\x31\x7d\x2f\x6f\x6e\x75\x2d\x7b\x32\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x80\x08\x2a\x10\x80\x08\x81\x08\x82\x08\x83\x08\x84\x08\x85\x08\x86\x08\x87\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x38\x34\x62\x35\x64\x35\x61\x39\x2d\x33\x34\x64\x66\x2d\x34\x61\x33\x37\x2d\x62\x66\x37\x64\x2d\x63\x37\x37\x61\x34\x65\x33\x34\x33\x61\x37\x64\x7d\x2f\x70\x6f\x6e\x2d\x7b\x30\x7d\x2f\x6f\x6e\x75\x2d\x7b\x31\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x81\x08\x2a\x10\x88\x08\x89\x08\x8a\x08\x8b\x08\x8c\x08\x8d\x08\x8e\x08\x8f\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x38\x34\x62\x35\x64\x35\x61\x39\x2d\x33\x34\x64\x66\x2d\x34\x61\x33\x37\x2d\x62\x66\x37\x64\x2d\x63\x37\x37\x61\x34\x65\x33\x34\x33\x61\x37\x64\x7d\x2f\x70\x6f\x6e\x2d\x7b\x30\x7d\x2f\x6f\x6e\x75\x2d\x7b\x32\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x80\x08\x2a\x10\x80\x08\x81\x08\x82\x08\x83\x08\x84\x08\x85\x08\x86\x08\x87\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x38\x34\x62\x35\x64\x35\x61\x39\x2d\x33\x34\x64\x66\x2d\x34\x61\x33\x37\x2d\x62\x66\x37\x64\x2d\x63\x37\x37\x61\x34\x65\x33\x34\x33\x61\x37\x64\x7d\x2f\x70\x6f\x6e\x2d\x7b\x31\x7d\x2f\x6f\x6e\x75\x2d\x7b\x31\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x80\x08\x2a\x10\x80\x08\x81\x08\x82\x08\x83\x08\x84\x08\x85\x08\x86\x08\x87\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x38\x34\x62\x35\x64\x35\x61\x39\x2d\x33\x34\x64\x66\x2d\x34\x61\x33\x37\x2d\x62\x66\x37\x64\x2d\x63\x37\x37\x61\x34\x65\x33\x34\x33\x61\x37\x64\x7d\x2f\x70\x6f\x6e\x2d\x7b\x31\x7d\x2f\x6f\x6e\x75\x2d\x7b\x32\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x81\x08\x2a\x10\x88\x08\x89\x08\x8a\x08\x8b\x08\x8c\x08\x8d\x08\x8e\x08\x8f\x08",
        b"\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x61\x61\x34\x36\x63\x62\x63\x61\x2d\x39\x31\x64\x37\x2d\x34\x36\x64\x65\x2d\x61\x61\x30\x65\x2d\x61\x32\x65\x33\x64\x32\x36\x61\x61\x66\x36\x32\x7d\x2f\x70\x6f\x6e\x2d\x7b\x30\x7d\x2f\x6f\x6e\x75\x2d\x7b\x31\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x80\x08\x2a\x10\x80\x08\x81\x08\x82\x08\x83\x08\x84\x08\x85\x08\x86\x08\x87\x08",
        "\x08\x40\x12\x07\x58\x47\x53\x2d\x50\x4f\x4e\x1a\x42\x6f\x6c\x74\x2d\x7b\x61\x61\x34\x36\x63\x62\x63\x61\x2d\x39\x31\x64\x37\x2d\x34\x36\x64\x65\x2d\x61\x61\x30\x65\x2d\x61\x32\x65\x33\x64\x32\x36\x61\x61\x66\x36\x32\x7d\x2f\x70\x6f\x6e\x2d\x7b\x30\x7d\x2f\x6f\x6e\x75\x2d\x7b\x31\x7d\x2f\x75\x6e\x69\x2d\x7b\x30\x7d\x20\x80\x08\x2a\x10\x80\x08\x81\x08\x82\x08\x83\x08\x84\x08\x85\x08\x86\x08\x87\x08",
        "\\x08\\x40\\x12\\x07\\x58\\x47\\x53\\x2d\\x50\\x4f\\x4e\\x1a\\x42\\x6f\\x6c\\x74\\x2d\\x7b\\x61\\x61\\x34\\x36\\x63\\x62\\x63\\x61\\x2d\\x39\\x31\\x64\\x37\\x2d\\x34\\x36\\x64\\x65\\x2d\\x61\\x61\\x30\\x65\\x2d\\x61\\x32\\x65\\x33\\x64\\x32\\x36\\x61\\x61\\x66\\x36\\x32\\x7d\\x2f\\x70\\x6f\\x6e\\x2d\\x7b\\x30\\x7d\\x2f\\x6f\\x6e\\x75\\x2d\\x7b\\x31\\x7d\\x2f\\x75\\x6e\\x69\\x2d\\x7b\\x30\\x7d\\x20\\x80\\x08\\x2a\\x10\\x80\\x08\\x81\\x08\\x82\\x08\\x83\\x08\\x84\\x08\\x85\\x08\\x86\\x08\\x87\\x08"
    ]
    # for message in messages:
    #     print(VolthaTools().tech_profile_decode_resource_instance(message))
