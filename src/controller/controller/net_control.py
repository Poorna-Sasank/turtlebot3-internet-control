import paho.mqtt.client as mqtt
import json

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MqttToRobot(Node):

    def __init__(self):
        super().__init__('mqtt_to_robot')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message

        self.mqtt_client.connect("broker.emqx.io", 1883, 60)
        self.mqtt_client.loop_start()
    
    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            self.get_logger().info('Connected to MQTT Broker!')
            client.subscribe('robot/cmd_vel')
        else:
            self.get_logger().error(f'Failed to connect, return code {reason_code}')
    
    def on_message(self, client, userdata, msg):
        data = json.loads(msg.payload.decode())
        x = float(data['x'])
        y = float(data['y'])
        self.get_logger().info(f'Received x: {x}, y: {y}')

        move = Twist()
        move.linear.x = x
        move.angular.z = y
        self.publisher_.publish(move)

def main(args=None):
    rclpy.init(args=args)
    node = MqttToRobot()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down node.')
    finally:
        node.mqtt_client.loop_stop()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
    
