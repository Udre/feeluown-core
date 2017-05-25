#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import time
import random

from fuocore.backends import MpvPlayer
from fuocore.engine import set_backend, get_backend
from fuocore.source import Source

from fuocore.third_party.netease import NeteaseProvider


player = MpvPlayer()
set_backend(player)
player = get_backend()
player.initialize()
source = Source()

netease_pvd = NeteaseProvider()
source.add_provider(netease_pvd)

songs = source.search(u'周杰伦 - 我很忙')
for song in songs:
    try:
        song_ = netease_pvd.get_song(song.identifier)
        player.playlist.add(song_)
        if len(player.playlist) > 2:
            break
    except:
        print()

player.play_song(player.playlist[1])

event_loop = asyncio.get_event_loop()
event_loop.run_forever()
