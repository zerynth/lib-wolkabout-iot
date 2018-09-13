# WolkConnect-Python-Zerynth
WolkAbout Python Connector library for connecting Zerynth enabled devices to WolkAbout IoT platform.

Supported protocol(s):
* JsonSingleReferenceProtocol


Example Usage
-------------
**Establishing connection with WolkAbout IoT platform:**
```python
# Insert your device credentials
device_key = "device_key"
device_password = "some_password"
actuator_references = ["ACTUATOR_REFERENCE_ONE", "ACTUATOR_REFERENCE_TWO"]

device = Wolk.Device(device_key, device_password, actuator_references)

# Provide implementation of a way to read actuator status
class ActuatorStatusProviderImpl(Wolk.ActuatorStatusProvider):

    def get_actuator_status(self, reference):
    if reference == "ACTUATOR_REFERENCE_ONE":
        value = digitalRead(LED4)
        if value == 1:
            return Wolk.ACTUATOR_STATE_READY, "true"
        else:
            return Wolk.ACTUATOR_STATE_READY, "false"


# Provide implementation of an actuation handler
class ActuationHandlerImpl(Wolk.ActuationHandler):

    def handle_actuation(self, reference, value):
        if reference == "ACTUATOR_REFERENCE_ONE":
            print("Setting actuator " + reference + " to value: " + value)
            current_state = digitalRead(LED4)
            if current_state == 1:
                if value == "false":
                    digitalWrite(LED4, LOW)
            else:
                if value == "true":
                    digitalWrite(LED4, HIGH)


# WolkConnect-PythonCore dependencies
wolk = Wolk.Wolk(device, ActuationHandlerImpl(), ActuatorStatusProviderImpl())

wolk.connect()
```

**Publishing sensor readings:**
```python
wolk.add_sensor_reading("T", 26.93)
```

**Publishing actuator statuses:**
```python
wolk.publish_actuator_status("ACTUATOR_REFERENCE_ONE")
```
This will call the `ActuatorStatusProvider` to read the actuator status and publish actuator status.


**Publishing events:**
```python
wolk.add_alarm("ALARM_REFERENCE", "ALARM_MESSAGE_FROM_CONNECTOR")
```

**Data publish strategy:**

Stored sensor readings and alarms, as well as current actuator statuses are pushed to WolkAbout IoT platform on demand by calling
```python
wolk.publish()
```

Whereas actuator statuses are published automatically by calling:

```python
wolk.publish_actuator_status("ACTUATOR_REFERENCE_ONE")
```

**Disconnecting from the platform:**
```python
wolk.disconnect()
```

**Data persistence:**

WolkAbout Python Connector provides a mechanism for persisting data in situations where readings can not be sent to WolkAbout IoT platform.

Persisted readings are sent to WolkAbout IoT platform once connection is established.
Data persistence mechanism used **by default** stores data in-memory.

In cases when provided in-memory persistence is suboptimal, one can use custom persistence by implementing `Wolk.OutboundMessageQueue`,
and forwarding it to the constructor in the following manner:

```python
wolk = Wolk.Wolk(device, ActuationHandlerImpl(), ActuatorStatusProviderImpl(), custom_queue)
wolk.connect()
```

For more info on persistence mechanism see `Wolk.OutboundMessageQueue` class