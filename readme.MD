Generate hash for pass:
```
tor --hash-password deeznuts
```

Locate `torrc` and edit the following:

(on Mac if installed with `brew`)
```
/usr/local/etc/tor/
```
#(create ^^ by duplicating torrc.sample if not exits)

Uncomment and fill:
```
SOCKSPort 9050
HashedControlPassword <generated hash of deeznuts>
CookieAuthentication 1
```

add to your shellrc (`.bashrc`, `.zshrc`, `.whateverrc`...)
```
export TOR_PASS=deeznuts
```

put on RaspberryPI and forget about it :)