#!/bin/bash

# Local testing and observability script

# Function to check if a service is running
check_service() {
    if systemctl is-active --quiet $1; then
        echo "$1 is running"
    else
        echo "$1 is not running"
    fi
}

# Check HAProxy and NGINX status
check_service haproxy
check_service nginx

# Test HAProxy configuration
echo "Testing HAProxy configuration..."
haproxy -c -f /etc/haproxy/haproxy.cfg

# Test NGINX configuration
echo "Testing NGINX configuration..."
nginx -t

# Check SSL certificates
echo "Checking SSL certificates..."
openssl x509 -in /etc/ssl/certs/haproxy.pem -text -noout | grep "Subject:"
openssl x509 -in /etc/ssl/certs/nginx.crt -text -noout | grep "Subject:"

# Test mTLS connection
echo "Testing mTLS connection..."
curl --cert /path/to/client.crt --key /path/to/client.key --cacert /etc/ssl/certs/ca.pem https://example.com

# Check security policy
echo "Checking security policy..."
cat /etc/security_policy.yaml

# Monitor logs
echo "Monitoring logs (press Ctrl+C to stop)..."
tail -f /var/log/haproxy.log /var/log/nginx/access.log
