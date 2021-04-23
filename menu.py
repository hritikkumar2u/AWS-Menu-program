import os
print("\t\t\t\t\t\t AWS")
print("\t\t\t\t\t\t ---------------------")
print("Press 1:  To show date")
print("Press 2:  To create a Key pair in AWS Cloud")
print("Press 3:  To create a security group in AWS Cloud")
print("Press 4:  To create a EBS volume in AWS")
print("Press 5:  To launch AWS instance")
print("Press 6:  To attach EBS volume to AWS instance")
print("Press 7:  To configure Web server")
print("Press 8:  To start a HTTPD Service")
print("Press 9:  To check status of HTTPD service")
print("Press 10: To create a Partition")
print("Press 11: To format a partition")
print("Press 12: To mount a partition in /var/www/html/")
print("Press 13: To stop a AWS instance")
print("Press 14: To start a AWS instance")
print("Press 15: To create a s3 bucket in AWS")
print("Press 16: To make S3 bucket public")
print("Press 17: To know the list of  s3 bucket in AWS")
print("Press 18: To Upload a image to the s3 bucket")
print("Press 19: To make s3 object public")
print("Press 20: To login to the instance using AWS CLI")
print("Press 21: To create a cloudfront Distribution service")
while True:
	x=int(input("Press number:"))
	if x == 1:
		os.system("date")
	elif x == 2:
		y = input("Enter key name:")
		os.system("aws ec2 create-key-pair {} {}".format("--key-name",y))
	elif x == 3:
		a=input("Enter group name:")
		b=input("Enter description:")
		os.system("aws ec2 create-security-group {} {} {} {}".format("--group-name",a,"--description",b))
	elif x == 4:
		c=input("Enter availability zone:")
		os.system("aws ec2 create-volume {} {} {} {} {} {}".format("--volume-type","gp2","--size",2,"--availability-zone",c))
	elif x == 5:
		os.system("aws ec2 run-instances {} {} {} {} {} {} {} {} {} {}".format("--image-id","ami-098f16afa9edf40be","--instance-type","t2.micro","--count",1,"--security-group-ids","sg-04869634b75ecc256","--key-name","hk1"))
	elif x == 6:
		f=input("Enter Instance Id:")
		g=input("Enter Volume Id:")
		h=input("Enter device name:")
		os.system("aws ec2 attach-volume {} {} {} {} {} {}".format("--instance-id",f,"--volume-id",g,"--device",h))
	elif x == 7:
		i = input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {} {} {} {}".format(i, "-i", "hk1.pem","sudo","yum","install","httpd","-y"))
	elif x == 8:
		j = input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {} {} {} {} {}".format (j,"-i","hk1.pem","sudo","systemctl","start","httpd"))
	elif x == 9:
		k = input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {} {} {} {} {}".format (k,"-i","hk1.pem","sudo","systemctl","status","httpd"))
	elif x == 10:
		l=input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {} {} {} {}".format(l,"-i","hk1.pem","sudo","fdisk","/dev/xvdf"))
	elif x == 11:
		m = input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {} {} {} {}".format(m, "-i", "hk1.pem", "sudo", "mkfs.ext4", "/dev/xvdf"))
	elif x == 12:
		n = input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {} {} {} {} {}".format(n, "-i", "hk1.pem", "sudo", "mount", "/dev/xvdf","/var/www/html"))
	elif x == 13:
		os.system("aws ec2 stop-instances {} {}".format("--instance-ids","i-07f23f9880c2cbdcc"))
	elif x == 14:
		os.system("aws ec2 start-instances {} {}".format("--instance-ids","i-07f23f9880c2cbdcc"))
	elif x == 15:
		os.system("aws s3 mb {} {} {}".format("s3://my34568","--region","us-east-1"))
	elif x == 16:
		os.system("aws s3api put-bucket-acl {} {} {} {}".format("--acl","public-read","--bucket","my34568"))
	elif x == 17:
		os.system("aws s3 ls")
	elif x == 18:
		os.system("aws s3 cp {} {}".format("car.jpg","s3://my34568"))
	elif x == 19:
		os.system("aws s3api put-object-acl {} {} {} {} {} {}".format("--bucket","my34568","--key","car.jpg","--grant-read","uri=http://acs.amazonaws.com/groups/global/AllUsers"))
	elif x == 20:
		p=input("Enter IP address:")
		os.system("ssh -l ec2-user {} {} {}".format(p,"-i","hk1.pem"))
	elif x == 21:
		os.system("aws cloudfront create-distribution {} {} {} {}".format("--origin-domain-name","my34568.s3.amazonaws.com","--default-root-object","car.jpg"))
	elif x == 22:
		break
