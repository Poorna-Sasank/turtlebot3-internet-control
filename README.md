## MQTT Velocity Publisher

- This HTML page enables users to input `x` and `y` values and publish them as a JSON message to the MQTT topic `robot/cmd_vel`.  
- It utilizes the `mqtt.js` library to connect to the MQTT broker at `wss://broker.emqx.io:8084/mqtt`.  
- The connection status and any errors are logged to the browser console for monitoring.  
