# PyRemoteExec and PyMultiRemoteExec

PyRemoteExec and PyMultiRemoteExec are Python-based remote command execution tools that allow you to run commands on remote client machines from a central server. While PyRemoteExec is designed for single-client scenarios, PyMultiRemoteExec extends the functionality to handle multiple client connections concurrently. Both tools provide interactive command execution and response handling.

## Directory Structure

- `Single Client`: Contains the PyRemoteExec tool for single-client scenarios.
- `Multiclient`: Contains the PyMultiRemoteExec tool for handling multiple client connections concurrently.

## How They Work

Both tools consist of two scripts: a server script and a client script.

### PyRemoteExec

- The server script listens on a specific port, waiting for incoming connections from a single client.
- The client script connects to the server using the server's IP address and port number.
- Once the connection is established, the server can send commands to the client, and the client will execute those commands and return the output to the server.

### PyMultiRemoteExec

- The server script can handle multiple client connections simultaneously, providing an interactive command execution environment.
- It maintains a list of connected clients, allowing you to manage and interact with each of them independently.

## Features

- Remote command execution on one or multiple client machines.
- Basic file system navigation using the 'cd' command.
- Graceful handling of connection termination.
- Interactive command execution and response handling.

## Prerequisites

- Python 3.x installed on both the server and client machines.

## Usage

### PyRemoteExec (Single Client)

1. Navigate to the `Single Client` directory.
2. Follow the instructions in the README located in the `Single Client` directory to set up and use PyRemoteExec.

### PyMultiRemoteExec (Multi-Client)

1. Navigate to the `Multiclient` directory.
2. Follow the instructions in the README located in the `Multiclient` directory to set up and use PyMultiRemoteExec.

## Security Considerations

**Warning:** These tools are intended for educational purposes and should not be used on untrusted networks or systems. Be cautious and responsible when using them, and ensure that you have permission to execute commands on the remote client machines.

## Disclaimer

These tools are provided "as is" without any warranty. The authors are not responsible for any misuse or damage caused by using these tools. Use them responsibly and in compliance with applicable laws and regulations.

## License

These tools are released under the [MIT License](LICENSE).

## Feedback and Contributions

We welcome feedback and contributions to improve these tools. Feel free to submit issues, feature requests, or pull requests on the respective GitHub repository for [Reverse_Shell](https://github.com/AbinMadathil/Reverse_Shell). Your feedback is valuable for us to make these tools better.
