import subprocess
import os
import yaml

# HAProxy configuration
def configure_haproxy():
    haproxy_config = """
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000

frontend https_front
    bind *:443 ssl crt /etc/ssl/certs/haproxy.pem ca-file /etc/ssl/certs/ca.pem verify required
    mode http
    option forwardfor
    http-request set-header X-Forwarded-Proto https
    default_backend nginx_backend

backend nginx_backend
    mode http
    balance roundrobin
    option httpchk
    server nginx1 127.0.0.1:8080 check ssl verify required ca-file /etc/ssl/certs/ca.pem
    """
    
    with open('/etc/haproxy/haproxy.cfg', 'w') as f:
        f.write(haproxy_config)

# NGINX configuration
def configure_nginx():
    nginx_config = """
http {
    server {
        listen 8080 ssl;
        server_name example.com;

        ssl_certificate /etc/ssl/certs/nginx.crt;
        ssl_certificate_key /etc/ssl/certs/nginx.key;
        ssl_client_certificate /etc/ssl/certs/ca.pem;
        ssl_verify_client on;

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
    """
    
    with open('/etc/nginx/nginx.conf', 'w') as f:
        f.write(nginx_config)

# Security policy implementation
def implement_security_policy():
    security_policy = {
        'allowed_ips': ['192.168.1.0/24', '10.0.0.0/8'],
        'max_requests_per_second': 100,
        'enable_waf': True,
        'ssl_protocols': ['TLSv1.2', 'TLSv1.3'],
        'ssl_ciphers': ['ECDHE-ECDSA-AES256-GCM-SHA384', 'ECDHE-RSA-AES256-GCM-SHA384']
    }
    
    with open('/etc/security_policy.yaml', 'w') as f:
        yaml.dump(security_policy, f)

# Main function to set up the environment
def setup_environment():
    configure_haproxy()
    configure_nginx()
    implement_security_policy()
    print("Environment setup completed.")

if __name__ == "__main__":
    setup_environment()
