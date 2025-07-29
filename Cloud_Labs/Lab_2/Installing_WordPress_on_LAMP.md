# Lab 2: Installing WordPress on LAMP (Linux, Apache, MySQL, PHP)

![WordPress Install](images/S2)

## Objective
Install and configure WordPress on a CentOS ECS using the LAMP stack and RDS MySQL as the backend database.

---

## Step 1: Install LAMP Stack on ECS

Connect to your ECS using a remote SSH tool, then run:

```bash
`yum install -y httpd php php-fpm php-mysql mysql`

### Start and enable the services:

`systemctl start httpd`
`systemctl enable httpd`
`systemctl start php-fpm`
`systemctl enable php-fpm`

## Step 2: Configure Apache
Edit the Apache config file:

`vim /etc/httpd/conf/httpd.conf`

### At the bottom of the file, add:

`ServerName localhost:80`

### Then restart Apache:

`systemctl restart httpd`

## Step 3: Download & Extract WordPress

Download WordPress:

`wget -c https://koolabsfiles.obs.ap-southeast-3.myhuaweicloud.com:443/20220731/wordpress-4.9.10.tar.gz`

Extract it into the web root directory:

`tar -zxvf wordpress-4.9.10.tar.gz -C /var/www/html`
`chmod -R 777 /var/www/html`

## Step 4: Create WordPress Database in RDS

Go to RDS Console > SQL Query, and run:

`CREATE DATABASE wordpress;`

Make sure your ECS security group allows MySQL access to RDS (port 3306).

## Step 5: Configure WordPress via Web

In your browser, go to:

`http://<ECS_Public_IP>/wordpress`

### Set up the database connection:

- Database Name: wordpress

- Username: root

- Password: Huawei!@#$

- Database Host: <RDS_Floating_IP>

### Click Submit and finish the installation steps.
