# Ultimaker 3 data collector for Telegraf

1. Prerequisites 

- Python 3.6+
- Working Telegraf v1.7 + InfluxDB v1.7 + Grafana v5.4 stack

Well I coded that script on these versions, maybe it would work on earlier 
versions.


2. Installation

- Put collect_um3_states.py where Telegraf could run it (more likely on the same
server as Telegraf)


- Add collector to inputs.exec in telegraf.conf

[[inputs.exec]]
  ## Commands array
  commands = [
    "python3 /scripts/collect_um3_state.py"
  ]


