
1. In the /etc/hosts folder in each instance the private Ip address of the instance is listed along with the name it will be called.

2. To SSH between instances using their private IPs each instance will need a copy of the private key you used to SSH in, as they only have copies of the public key.

3. To install HAProxy use the command `sudo apt-get install -y haproxy`, this will make a haproxy directory in the /etc directory. In the haproxy directory `sudo vim` the haproxy.cfg file and make changes to the timeout times on the connect, client, and server as well as binding IP's to port 80 `(bind*:80)` and setting the balance to roundrobin. Add your servers with their name and their private IPs and bind them to port 80. To restart haproxy use the command `sudo systemctl restart haproxy.service`.  
- Resources used: https://www.digitalocean.com/community/tutorials/how-to-use-haproxy-to-set-up-http-load-balancing-on-an-ubuntu-vps

4. To install apache onto your instance run the command `sudo apt-get install -y apache2`. Then use `sudo systemctl status apache2` to ensure that apache2 is running. Use the command `sudo mkdir /var/www/your_domain` to create a domain directory, then assign ownership with `sudo chown -R $USER:USER /var/www/you_domain`. Change permissions with `sudo chmod -R 755 /var/www/your_domain`. To create the page that will have your content use `sudo nano /var/www/your_domain/index.html` and then add what you want to display. Edit the config file with `sudo nano /etc/apache2/sites-available/your_domain.conf` and then add this block  
![Domain config](/Project5/DomainConf.png)  

- Enable the file with `sudo a2ensite your_domain.conf`  

- Disable the default site with `sudo a2dissite 000-default.conf`  

- Test for configuration errors with `sudo apache2ctl configtest`  

- Restart with `sudo systemctl restart apache2`  

- Resources used: https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

5.  
![Web Server 1 page](/Project5/WebServ1.png)  
![Web Server 2 page](/Project5/WebServ2.png)  


















