<a id="readme-top"></a>

<h3 align="center">TurtleBot3 internet control via MQTT protocol using ROS2 framework</h3>

  <p align="center">
    Leveraged the ROS2 framework and Gazebo simulator to modify the TurtleBot3's state over the internet using the MQTT protocol.
    <br />
    <a href="https://medium.com/@dennymech22/web-based-control-for-turtlebot3-3185eb6e22eb"><strong>Inspired from »</strong></a>
    <br />
  </p>
</div>
## FYI

Make sure `TURTLEBOT3_MODEL` is set to `waffle` in your bashrc file
```sh
TURTLEBOT3_MODEL=waffle
```
and 
```sh
GZ_VERSION=HARMONIC
```

## Control Methodology

The state (linear and angular velocities) of the TurtleBot3 is modified over the internet via the MQTT protocol from a custom webpage (remote messages), which is developed using HTML and JavaScript for simplicity.

- A ros2 node is created to unpack the remote messages from the custom webpage and publish them to `/Twist` topic to modify the turtlebot3's state.
  
## MQTT Velocity Publisher

- The HTML page enables users to input `(x) linear velocity` and `(y) angular velocity` values and publish them as a JSON message to the MQTT topic `robot/cmd_vel`.  
- It utilizes the `mqtt.js` library to connect to the MQTT broker at `wss://broker.emqx.io:8084/mqtt`.  
- The connection status and any errors are logged to the browser console for monitoring.  

### Tools

* Ubuntu 22.04 LTS
* ROS2 Humble Hawksbill
* Python, XML, HTML, JS 

<!-- USAGE EXAMPLES -->
## Usage
Refer to the docs for better understanding of the terms and functionalities.
<br />
_[ROS2 Documentation](https://docs.ros.org/en/humble/index.html)_


<p align="right">(<a href="#readme-top">back to top</a>)</p>


