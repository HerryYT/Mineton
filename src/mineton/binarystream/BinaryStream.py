#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import bitstring


class BinaryStream:
    stream = bitstring.BitStream()
    offset = 0

    def append(self, data):
        self.stream.append(data)

    def putByte(self, byte):
        self.stream.append(f"int:8={byte}")

    def getByte(self):
        return self.stream.read(f"int:8={self.increaseOffset(1)}")

    def putShort(self, short):
        self.stream.append(f"int:16={short}")

    def getShort(self):
        return self.stream.read(f"uintbe:16={self.increaseOffset(2)}")

    def putInt(self, integer):
        self.stream.append(f"int:32={integer}")

    def putLong(self, long):
        self.stream.append(f"uintbe:32={(0xFFFFFFFF & int(long))}")

    # uintbe 32 or 64? 64 seems right but is 32...
    def getLong(self):
        return (self.stream.read(f"uintbe:32={self.increaseOffset(4)}") << 8) + \
               self.stream.read(f"uintbe:32={self.increaseOffset(4)}")

    def putString(self, string):
        self.stream.append(bytes(string, "utf-8"))

    def getString(self):
        print()

    def putMagic(self):
        self.stream.append(b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78")

    def getMagic(self):
        # From start, to finish of Offline message length
        return self.stream[self.offset:self.increaseOffset(16, True)]

    def getBool(self):
        return self.getByte() != 0

    def putBool(self, boolean):
        if boolean:
            self.putByte(1)
        else:
            self.putByte(0)

    def increaseOffset(self, v, ret=False):
        self.offset += v
        if ret:
            return self.offset
        else:
            return self.offset-v

    def clean(self):
        self.stream = bitstring.BitStream()
        self.offset = 0

    def getStream(self):
        return self.stream
