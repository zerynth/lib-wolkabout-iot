#   Copyright 2018 WolkAbout Technology s.r.o.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


"""
    Provide implementation of ConfigurationHandler to pass configuration commands from the platform to your device.
"""


class ConfigurationHandler:
    """
        Configuration Handler Interface
    """

    def handle_configuration(self, configuration):
        """
        When the configuration command is given from the platform, it will be delivered to this method.
        This method should update device configuration with received configuration values.
        Must be implemented as non blocking.
        Must be implemented as thread safe.

        :param configuration: Holds the command and a dictionary of configuration key/value pairs
        :type configuration: ConfigurationCommand
        """
        pass
