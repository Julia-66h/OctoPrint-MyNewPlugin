# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
			octoprint.plugin.OctoPrintPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World!")

    def change_temperature(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        global temp
        if gcode and gcode == "M104":
            cmd = "M104 S210"
        return cmd
        
__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = HelloWorldPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.sent": __plugin_implementation__.change_temperature 
    }

