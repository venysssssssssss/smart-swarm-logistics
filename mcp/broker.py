import paho.mqtt.client as mqtt
from typing import Callable, Any

class MCPBroker:
    """
    Model-Context Protocol broker for agent communication.
    """
    def __init__(self, broker_address: str = "localhost", port: int = 1883):
        self.broker_address = broker_address
        self.port = port
        self.client = mqtt.Client()

    def connect(self) -> None:
        """Connect to the MQTT broker."""
        self.client.connect(self.broker_address, self.port)

    def publish(self, topic: str, message: str) -> None:
        """Publish a message to a topic."""
        self.client.publish(topic, message)

    def subscribe(self, topic: str, callback: Callable[[str, Any], None]) -> None:
        """Subscribe to a topic with a callback."""
        self.client.subscribe(topic)
        self.client.on_message = lambda client, userdata, msg: callback(msg.topic, msg.payload.decode())

    def start_loop(self) -> None:
        """Start the MQTT loop."""
        self.client.loop_start()

    def stop_loop(self) -> None:
        """Stop the MQTT loop."""
        self.client.loop_stop()