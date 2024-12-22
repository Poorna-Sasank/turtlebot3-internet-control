<a id="readme-top"></a>

<h3 align="center">TurtleBot3 internet control via MQTT protocol using ROS2 framework</h3>

  <p align="center">
    Leveraged the ROS2 framework and Gazebo simulator to modify the TurtleBot3's state over the internet using the MQTT protocol.
    <br />
    <a href="https://medium.com/@dennymech22/web-based-control-for-turtlebot3-3185eb6e22eb"><strong>Inspired from »</strong></a>
    <br />
  </p>
</div>

## Control Methodology

The end effector of the UR5e robotic arm is controlled using local optimization techniques. The control approach utilizes:

- The `scipy.minimize` library for optimization.
- A custom gradient descent algorithm based on the Jacobian transpose method.
- 
## MQTT Velocity Publisher

- This HTML page enables users to input `x` and `y` values and publish them as a JSON message to the MQTT topic `robot/cmd_vel`.  
- It utilizes the `mqtt.js` library to connect to the MQTT broker at `wss://broker.emqx.io:8084/mqtt`.  
- The connection status and any errors are logged to the browser console for monitoring.  

### Tools involved

* Mujoco (latest)
* Python - scipy.optimize and numpy libraries
* Constrained Optimization (knowledge required)

<!-- GETTING STARTED -->
## Getting Started

Steps to setup the framework in your local machine.

### Prerequisites

Install the MuJoCo and SciPy libraries using pip to ensure the code runs without errors.
* pip
  ```sh
  python3 -m pip install mujoco scipy numpy
  ```

### Installation
Considering that you have the prerequisites
1. Clone the repo
   ```sh
   git clone https://github.com/Poorna-Sasank/mujoco_ik_simulation.git
   ```
2. Navigate to optim_kinematic_control folder
   ```sh
   cd path/to/mujoco_ik_simulation/optim_kinematic_control
   ```
3. Choose your desired optimization framework and run the main code :)
   <br />
   * You can choose your optimization framework in the main code itself
   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
Should you require any further clarifications on mujoco or optimization techniques please refer to their respective documentations

_For mujoco, please refer to the [Mujoco Documentation](https://mujoco.readthedocs.io/en/stable/python.html)_
<br />
_To learn about optimization methods, there are numerous resources available; I recommend starting with [3B1B](https://youtu.be/IHZwWFHWa-w?si=o6CwgQx7aMiLjyko)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


