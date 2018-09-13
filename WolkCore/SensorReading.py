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
    Sensor as defined in the device manifest
"""


class SensorReading:
    """
        Sensor Reading Class
    """

    def __init__(self, reference, value, timestamp=None):
        """
        :param reference: The reference of the sensor
        :type reference: str
        :param value: The value of the reading
        :type value: int, float, str
        :param timestamp: (optional) Unix timestamp - if not provided, platform will assign one upon reception
        :type timestamp: int
        """
        self.reference = reference
        self.value = value
        self.timestamp = timestamp
