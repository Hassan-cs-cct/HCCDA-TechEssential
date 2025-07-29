# Lab 3: Configuring Elastic Load Balancer (ELB) and Auto Scaling on Huawei Cloud

![ELB Setup](images/S3)

## Objective
Improve the availability and scalability of your web application by configuring ELB and Auto Scaling with a custom ECS image.

---

## Step 1: Create a Load Balancer (ELB)

- Navigate to: **Service List > Networking > Elastic Load Balance**
- Click **Buy Load Balancer**
  - **Type**: Shared
  - **Network Type**: Public
  - **Region**: AP-Singapore
  - **VPC**: Select the VPC used by your ECS
  - **EIP**: Automatically assign (2 Mbps is enough)
  - **Name**: `elb-mp`
- Click **Submit**

---

## Step 2: Add Listener and Backend

- After ELB is created, go to its **Details Page**
- Add a **Listener**:
  - **Protocol**: HTTP
  - **Port**: 80
  - **Backend Group**: Add your ECS as a backend server

---

## Step 3: Create ECS Private Image

- Stop your original ECS
- Navigate to: **Compute > Image Management > Create Image**
  - **Image Type**: System Disk Image
  - **Source**: Select your configured ECS
  - **Name**: `image-mp`
- Click **Submit**

---

## Step 4: Configure Auto Scaling (AS)

- Go to: **Compute > Auto Scaling**
- Click **Create AS Configuration**
  - **Name**: `as-mp`
  - **Image**: Use the image `image-mp`
  - **Login**: Set same login password (e.g., `Huawei@123!`)
  - **Network**: Same VPC, do not assign EIP
  - **Add to Load Balancer**: Yes (select `elb-mp`)
- Save the AS configuration

---

## Step 5: Create AS Group and Policy

- Create a new **AS Group**
  - **Min Instances**: 1
  - **Max Instances**: 3
  - **Desired**: 1
  - **Health Check**: ELB
- Add **Scaling Policies**:
  - **Scale Out**: If CPU > 60% for 5 minutes → Add 1 ECS
  - **Scale In**: If CPU < 20% for 5 minutes → Remove 1 ECS

Once saved, the AS group will manage the number of ECS instances automatically based on the traffic load.

---
