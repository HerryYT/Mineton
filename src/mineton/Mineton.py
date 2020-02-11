#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from loguru import logger
from mineton.binarystream.BinaryStream import BinaryStream
import sys
import socket

# Used to recognize software version

BUILD = "0.1B1"


# Mineton main file, used to initialize the software
class Mineton:

    def __init__(self):
        # Start all features
        self.bootstrap()

        # Socket listener
        self.socket_listen(19132)

    # Function used to setup all software properties
    def bootstrap(self):
        # Logger init
        logger.remove()
        logger.add(
            sys.stderr,
            colorize=True,
            format="<blue>{time:HH:mm:ss}</blue> :: <level>{message}</level>"
        )
        logger.info("Bootstrapping Mineton v{build}...", build=BUILD)

    def socket_listen(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("localhost", port))
        logger.info("Mineton bound on localhost:{port}!", port=port)

        while True:
            data, addr = sock.recvfrom(1024)
            self.offline_data_handler(data=data, addr=addr)
            # logger.debug("Received {data} from {addr}", data=data, addr=addr)

    def offline_data_handler(self, data, addr):
        pid = data[0]
        logger.debug("Received packet {pid} from {addr}", pid=hex(data[0]), addr=addr)

        if pid == 1:
            logger.info("Got unconnected ping")
            stream = BinaryStream()
            stream.clean()
            stream.append(data)
            logger.info(stream.getStream())
            stream.getByte()
            logger.info(stream.getLong())
            logger.info(stream.getMagic())


if __name__ == "__main__":
    Mineton()
