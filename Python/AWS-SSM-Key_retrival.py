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