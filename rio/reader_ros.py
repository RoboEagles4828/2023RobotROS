import rclpy
from rclpy.node import Node
from rclpy import qos
from sensor_msgs.msg import Joy

class OrinSubscriber(Node):
    
    def __init__(self):
        super().__init__('orin_subscriber')

        qos_profile = qos.QoSProfile(depth=1,reliability=qos.ReliabilityPolicy.BEST_EFFORT, durability=qos.DurabilityPolicy.VOLATILE)

        self.subscription = self.create_subscription(Joy, ' rt/joystick_data', self.listener_callback, qos_profile)

    def listener_callback(self, msg):
        self.get_logger().info('Recieved: "%s"' % msg.data)

def main(args=None):
    print('Init')
    context = rclpy.get_default_context().init()
    rclpy.init(args=args, domain_id=1)

    orin_subscriber = OrinSubscriber()

    rclpy.spin(orin_subscriber)

    orin_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()