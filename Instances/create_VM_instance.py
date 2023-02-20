import os
import googleapiclient.discovery
import google.auth

from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('/home/saksham/Downloads/industrial-problem-378404-685329678653.json')

# Set the name, project, and zone for the instance
name = "master-instance"
project = "industrial-problem-378404"
zone = "us-central1-a"

# Authenticate with Google Cloud
service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

# Get the latest Ubuntu 22.04 LTS image
image_response = service.images().getFromFamily(
    project='ubuntu-os-cloud', family='ubuntu-2204-lts').execute()
source_disk_image = image_response['selfLink']

# Set the machine type and startup script
machine_type = f"zones/{zone}/machineTypes/e2-medium"
startup_script = open(os.path.join(
    os.path.dirname(__file__), 'startup_instance.sh'), 'r').read()

# Set the configuration for the instance
config = {
    'name': name,
    'machineType': machine_type,
    'disks': [
        {
            'boot': True,
            'autoDelete': True,
            'initializeParams': {
                'sourceImage': source_disk_image,
            }
        }
    ],
    'networkInterfaces': [
        {
            'network': 'global/networks/default',
            'accessConfigs': [
                {
                    'type': 'ONE_TO_ONE_NAT',
                    'name': 'External NAT'
                }
            ]
        }
    ],
    'serviceAccounts': [
        {
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }
    ],
    'metadata': {
        'items': [
            {
                'key': 'startup-script',
                'value': startup_script
            }
        ]
    }
}

# Create the instance
request = service.instances().insert(project=project, zone=zone, body=config)
response = request.execute()
