# Ultimaker 3 data collector for Telegraf

Prerequisites 
=============

- Python 3.6+
- Working Telegraf v1.7 + InfluxDB v1.7 + Grafana v5.4 stack

Well I coded that script on these versions, maybe it would work on earlier 
versions.

Please test first if the whole stack is working.


Installation
============
- Create a database on InfluxDB named 'ultimaker3' (or whatever you want but in
this case, you will have to change the source database if you want to use the 
provided Grafana dashboard)


- Put `collect_um3_states.py` where Telegraf could run it (more likely on
Telegraf's server)


- Add collector to inputs.exec in telegraf.conf

      [[inputs.exec]]
    
        ## Commands array
      
        commands = [
      
          "python3 /scripts/collect_um3_state.py"
        
        ]


- [Import][1] the provided dashboard `um3_grafana_dashboard.json` into Grafana.

[1]: https://grafana.com/docs/reference/export_import/#importing-a-dashboard

- Enjoy your new dashboard