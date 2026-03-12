# MikroTik traffic monitor example
# This script logs interface traffic counters in a simple format
# for collection by remote syslog / Graylog

:foreach i in=[/interface find] do={

    :local name [/interface get $i name]
    :local rx [/interface get $i rx-byte]
    :local tx [/interface get $i tx-byte]

    :log info ("MTTRAFFIC if=" . $name . " rx=" . $rx . " tx=" . $tx)
}
