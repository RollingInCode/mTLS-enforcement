# HAProxy and NGINX Setup with mTLS and Security Policy Implementation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Security Policy](#security-policy)
8. [Local Testing and Observability](#local-testing-and-observability)
9. [Troubleshooting](#troubleshooting)
10. [Maintenance](#maintenance)
11. [Contributing](#contributing)
12. [License](#license)

## Introduction

This project provides a robust setup for HAProxy and NGINX with mutual TLS (mTLS) enforcement and security policy implementation. It uses Python for configuration management and a shell script for local testing and observability. This setup is designed to enhance the security and performance of web applications by implementing reverse proxy, load balancing, and strict security measures.

## Features

- **HAProxy Configuration**: Advanced load balancing and SSL termination
- **NGINX Configuration**: Secure web server setup with mTLS
- **mTLS Enforcement**: Ensures secure communication between clients and servers
- **Security Policy Implementation**: YAML-based security policy for fine-grained control
- **Local Testing**: Shell script for comprehensive local testing and observability
- **Python-based Configuration Management**: Easy-to-maintain configuration scripts

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6+
- HAProxy
- NGINX
- OpenSSL
- PyYAML (`pip install PyYAML`)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/haproxy-nginx-mtls-setup.git
   cd haproxy-nginx-mtls-setup
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Ensure HAProxy and NGINX are installed on your system.

## Configuration

### HAProxy Configuration

The HAProxy configuration is managed by the `configure_haproxy()` function in the Python script. It sets up:
- SSL termination
- Frontend for HTTPS traffic
- Backend for NGINX servers
- mTLS verification

### NGINX Configuration

The NGINX configuration is handled by the `configure_nginx()` function. It configures:
- SSL/TLS settings
- Server block for the application
- mTLS client verification

### Security Policy

The security policy is defined in YAML format and includes:
- Allowed IP ranges
- Rate limiting
- Web Application Firewall (WAF) settings
- SSL/TLS protocols and ciphers

## Usage

1. Run the Python script to set up the environment:
   ```
   sudo python3 setup_environment.py
   ```

2. Make the shell script executable:
   ```
   chmod +x local_test.sh
   ```

3. Run the local testing script:
   ```
   ./local_test.sh
   ```

## Security Policy

The security policy is implemented in the `implement_security_policy()` function. It creates a YAML file with the following structure:

```yaml
allowed_ips:
  - 192.168.1.0/24
  - 10.0.0.0/8
max_requests_per_second: 100
enable_waf: true
ssl_protocols:
  - TLSv1.2
  - TLSv1.3
ssl_ciphers:
  - ECDHE-ECDSA-AES256-GCM-SHA384
  - ECDHE-RSA-AES256-GCM-SHA384
```

Modify this policy as needed for your specific security requirements.

## Local Testing and Observability

The `local_test.sh` script provides comprehensive testing and observability features:

- Service status checks for HAProxy and NGINX
- Configuration syntax validation
- SSL certificate verification
- mTLS connection testing
- Security policy verification
- Log monitoring

Run this script regularly to ensure the health and security of your setup.

## Troubleshooting

Common issues and their solutions:

1. **HAProxy fails to start**: 
   - Check the HAProxy configuration for syntax errors
   - Ensure SSL certificates are correctly placed and have proper permissions

2. **NGINX fails to start**: 
   - Verify the NGINX configuration
   - Check SSL certificate paths and permissions

3. **mTLS connection fails**: 
   - Ensure client certificates are properly configured
   - Verify the CA certificate is correctly set up in both HAProxy and NGINX

4. **Security policy not applied**: 
   - Check if the YAML file is correctly formatted
   - Ensure the policy file is in the correct location and readable

## Maintenance

Regular maintenance tasks:

1. Keep HAProxy and NGINX updated to the latest stable versions
2. Regularly update SSL certificates before they expire
3. Review and update the security policy as needed
4. Monitor logs for any suspicious activities
5. Perform regular security audits

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This README.md provides a comprehensive overview of the HAProxy and NGINX setup with mTLS enforcement and security policy implementation. It covers all aspects of the project, from installation to maintenance, and provides guidance for troubleshooting and contributing to the project. You can further customize this README to include specific details about your implementation or any additional features you may add to the project.
