import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureLogger(Node):
    def __init__(self, filename: str):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(
            Float32,
            '/temperature',
            self.temperature_callback,
            10
        )
        self.log_file = filename
        self.get_logger().info("Temperature Logger Node has started.")

    def temperature_callback(self, msg: Float32):
        temperature = msg.data
        self.get_logger().info(f"Received Temperature: {temperature}°C")

        if temperature > 50:
            with open(self.log_file, "a") as file:
                file.write(f"{temperature}\n")
            self.get_logger().info(f"Logged temperature: {temperature}°C")


def main(args=None):
    rclpy.init(args=args)
    logger = TemperatureLogger("log.txt")

    try:
        rclpy.spin(logger)
    except KeyboardInterrupt:
        pass
    finally:
        logger.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()