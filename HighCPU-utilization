###################################################################
#
#  Author : RENUGA
#
###################################################################

import sys
import subprocess
import json
import os, traceback
import ConfigParser

def HighUtilizationEC2instances():
	aws_cmd = "aws support describe-trusted-advisor-check-result --language en --check-id ZRxQlPsb6c --region us-east-1 --query 'result.sort_by(flaggedResources[?status!=`ok`],&metadata[2])[].{Region:metadata[0],InstanceId:metadata[1],InstanceName:metadata[2],InstanceType:metadata[3],NumberofDays_CPU_Utilization:metadata[19],Status:status}' --output json"
	proc = subprocess.Popen([aws_cmd], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	data = json.loads(out)
        if not data:
                print "CPU Utilization of Amazon EC2 instances are normal. There is no critical/warning instances"
        else:
		print out
		send_mail(data)

def send_mail(data):
	message_dict = {"Subject":{"Data": "[Trusted Advisor] Performance: High Utilization Amazon EC2 Instances", "Charset": "UTF-8"},"Body": {"Html": {"Data":"message comes here","Charset": "UTF-8"}}}
	table_of_instnces = ""
	for iter in data:
		stat = iter.get("Status")
                reg = iter.get("Region")
                instance_id = iter.get("InstanceId")
                instance_name = iter.get("InstanceName")
                instance_type = iter.get("InstanceType")
                noof_days = iter.get("NumberofDays_CPU_Utilization")
                table_of_instnces = table_of_instnces+"<tr><td>"+ str(instance_id) +"</td><td>"+ str(instance_name) +"</td><td>"+ str(instance_type) +"</td><td>"+ str(noof_days) +"</td><td>"+ str(reg) +"</td><td>"+ str(stat) +"</td></tr>"
	mail_content = "Dear Amazon EC2 Customer,<br/><br/>Checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days and alerts you if the daily CPU utilization was more than 90% on 4 or more days. Consistent high utilization can indicate optimized, steady performance, but it can also indicate that an application does not have enough resources.<br/><br/><table border=\"1\"><th>Instance Id</th><th>Instance Name</th><th>Instance Type</th><th>Number of Days over 90% CPU Utilization</th><th>Region</th><th>Status</th>" + table_of_instnces+"</table><br/><br/>Sincerely,<br/>Wipro TechOps Team"
	message_dict["Body"]["Html"]["Data"] = mail_content
	with open('/home/xdeploy/PyScripts/Renuga/msg.json', 'w') as outfile:
	       	json.dump(message_dict, outfile)
	aws_cmd_to_exec = "aws ses send-email --region us-east-1 --from 'Wipro Techops <sangeetha_venugopal@cable.comcast.com>' --destination file:///home/xdeploy/PyScripts/Renuga/dest.json --message file:///home/xdeploy/PyScripts/Renuga/msg.json"
	proc = subprocess.Popen([aws_cmd_to_exec], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	if "MessageId" in out:
	       	print "SUCCESS: Mail sent"
	else:
	       	print "FAILURE"
	print out

def main():
	HighUtilizationEC2instances()

if __name__ == '__main__':
        try:
                main()
        except Exception, e:
                print str(e)
                traceback.print_exc()
                os._exit(1)
