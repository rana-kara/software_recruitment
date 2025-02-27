import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='reseq',
            executable='temperature_sensor',
            name='temperature_sensor',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='reseq',
            executable='temperature_logger',
            name='temperature_logger',
            output='screen'
        ),
    ])
