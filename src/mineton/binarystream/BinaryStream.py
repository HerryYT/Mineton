#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import bitstring

stream = bitstring.BitStream()


class BinaryStream:

    @staticmethod
    def append(data):
        if isinstance(data, BinaryStream):
            stream.append(data.getStream())
        else:
            stream.append(data)

    @staticmethod
    def putByte(byte):
        stream.append(f"int:8={byte}")

    @staticmethod
    def putShort(short):
        stream.append(f"int:16={short}")

    @staticmethod
    def putInt(integer):
        stream.append(f"int:32={integer}")

    @staticmethod
    def getStream():
        return stream
