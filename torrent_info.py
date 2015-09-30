import libtorrent
info = libtorrent.torrent_info('[rutracker.org].t5015459.torrent')
print(info)
for f in info.files():
    print ("%s - %s" % (f.path, f.size))
