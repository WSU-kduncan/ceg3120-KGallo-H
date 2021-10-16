# Part 1  
1.    

![VPC creation](/Project3/images/VPCcreation.png)  
    - A VPC enables you to launch AWS resources into a virtual network that you've defined

2.   
 ![Subnet creation](/Project3/images/SubnetCreation.png)  
    - A subnet is the range of IP addresses that can be used by devices. Subnets can also lets define routes as well as firewalls. Public subnets are used for resources connected to the internet and Private subnets are for resources that are not.

3.    
![Creation of a gateway and attachment](/Project3/images/GatewayCreationAndAttachment.png)  
    - A gateway is a node that serves as the forwarding host to other networks when no other route specification matches the destination IP address of a packet.

4.    
![Route Table Gateway connection](/Project3/images/RouteTableGateway.png)  
![Route Table Subnet Association](/Project3/images/RouteTableSubnet.png)  
    - Routing tables defines where packets go based on their destination address.

5.    
![Created security group](/Project3/images/CreatedSecurityGroup.png)
    ![Security group Inbound Rules](/Project3/images/InboundRules.png)
    -Security groups allow you to filter traffic in and out of a VPC based on protocols, port numbers, and IP addresses.


# Part 2
1.  The name of the AMI type I selected was Ubuntu Server 20.04 LTS (HVM), SSD Volume Type. The name of the instance type I selected was t2.micro
  

2. I attached my VPC by changing the Network dropdown menu from its default to the name of my VPC

3. The IPv4 address should not be auto assigned because the auto assigned IP can be taken and given back to you by Amazon at any time.

4. In the `add storage` section of the instance creation menu, I chose General Purpose SSD as my volume type.  

5. In the `Tags` section of instance creation, I added a new tag, specified it was a name tag, then gave it a name.  

6. In the `configure security group` section I selected the `select an existing security group` prompt and then chose my security group from the list.  

7. In the Elastic IP section of EC2, I hit the `Allocate Elastic IP address button`, then created a name tag and named it Weeks-EIP. To associate it with my instance I clicked on the `Actions` menu then clicked `Associate Elastic IP address`. In that menu I choose the name of my instance and hit `Associate`.  

8.   
![Instance info](/Project3/images/InstanceDetails.png)  

9. To ssh in I used the command `ssh -i ceg3120F21-aws.pem ubuntu@54.157.151.87`, then I used the command `sudo hostname Weeks-AMI`.  
    ![New hostname](/Project3/images/NewHostName.png)
