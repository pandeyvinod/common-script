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