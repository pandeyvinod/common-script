# Case1 

#!/usr/bin/python3

import boto3

ssm = boto3.client('ssm', '<your region>')

parameter_name = '<parameter name>'

try:
  response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)

  api_key = response['Parameter']['Value']

  print(f"Retrived API Key: {api_key}")

except ssm.exceptions.ParameterNotfound as e:
  print(f"Parameter {parameter_name} not found: {e}")
except Exception as e:
  print(f"Error retrieving parameter: {e}")


#####################################

# in case you have use case where you need to use key at \ 
# at multiple location then you can cache that global variable

#!/usr/bin/python3

import boto3

ssm = boto3.client('ssm', '<your region>')

parameter_name = '<parameter name>'

global cached_api_key

if 'cached_api_key' not in globals():
  try:
    response = ssm.get_parameter(Name=parameter_name, WithDecryption=True)
    cached_api_key = response['Parameter']['Value']
  except ssm.exceptions.ParameterNotFound as e:
    print(f"Parameter {parameter_name} not found: {e}")
  except Exception as e:
    print(f"Error retrieving Parameter: {e}")
else:
  cached_api_key = globals()['cached_api_key']

print(f"Retrived API Key: {cached_api_key}")



#case 3 - avoid API calls multiple times. once you get the value then next run of the script should not make API call again. 

#!/usr/bin/python3
import os
import boto3
import json

# but this require Assumed role or role permission to get the value
def get_ssm_param():
    session = boto3.Session()
    ssm_client = session.client('ssm', 'us-east-1')

    api_key = ssm_client.get_parameter(Name='name give')['Parameter']['Value']
    endpoint_url = ssm_client.get_parameter(Name='End name')['Parameter']['Value']

    return api_key, endpoint_url

api_key, endpoint_url = get_ssm_param()
print("FROM SSM", api_key,endpoint_url)

def write_config_to_file(api_key, endpoint_url):
    data = {
        'NEWRELIC_API_KEY': api_key,
        'ENDPOINT_URL': endpoint_url
    }

    with open('config.json','w') as file:
        json.dump(data,file)

write_config_to_file()
print('config.json')


if not os.path.exists('config.json'):
    api_key, endpoint_url = get_ssm_param()
    write_config_to_file(api_key, endpoint_url)
else:
    with open('config.json', 'r') as file:
        data = json.load(file)
        api_key = data['API_KEY']
        endpoint_url = data['ENDPOINT_URL']

print("API Key:", api_key)
print("Endpoint URL:", endpoint_url)

