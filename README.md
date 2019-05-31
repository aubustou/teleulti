# Ultimaker 3 data collector for Telegraf

Add a collector for Ultimaker 3 in order to gather data into Grafana stack.

This works with only one Ultimaker 3 (or S5, I guess it's the same API). I only
have one currently so...

Code could be easily improved in order to manage several Ultimaker printers.



Prerequisites 
=============

- Python 3.6+ with requests 2.22.0 library
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