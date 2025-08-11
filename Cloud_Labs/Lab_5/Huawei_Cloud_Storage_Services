# Lab: Huawei Cloud Storage Services — OBS, EVS, and SFS

![Storage Services](images/S6)

## Objective
- **OBS**: Create an Object Storage Service bucket, set lifecycle rules, and configure permissions.
- **EVS**: Create an Elastic Volume Service disk, attach it to an ECS, and perform read/write operations.
- **SFS**: (Optional) Brief overview for file sharing service.

---

## Part 1: OBS (Object Storage Service)

### Step 1: Create an OBS Bucket
1. Navigate to: **Service List > Storage > Object Storage Service**
2. Click **Create Bucket**.
   - **Bucket Name**: `obs-lab-bucket`
   - **Region**: Same as your ECS for performance.
   - **Storage Class**: Standard
   - **Default Storage**: Keep as-is.
3. Click **Create Now**.

---

### Step 2: Configure Lifecycle Rule
1. Go to your bucket → **Lifecycle Rules**.
2. Click **Create Rule**:
   - **Name**: `rule-expire-30days`
   - **Prefix**: `/` (root)
   - **Transition**: After 30 days, move to **Infrequent Access**.
   - **Expiration**: After 60 days, delete the objects.
3. Save the rule.

---

### Step 3: Set Permission Policy
1. Go to bucket → **Permissions**.
2. Add a **Custom Policy** to allow public read (optional):
   ```json
   {
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": [
           "obs:GetObject"
         ],
         "Resource": [
           "obs:bucket:obs-lab-bucket/*"
         ]
       }
     ]
   }
