## Prerequisites:
- Need to check whether billing account was linked with my project.
- Need to create service accounts based on each services with active keys.

### Linux Terminal Commands:
``` bash
- cd #Change directory
- cd .. # To go back.
- ls
- ls -a
- ls -la # List hidden files
- rm -rf <folderName>
- rm -r <foldername>*  # Recursive deletion on all subfiles and folders.
- touch <fileName>
- vi <fileName> #after vi, press "i" to insert the contents and to save press "esc" :wq (write and quit)
- vim <filename>
- nano <filename>
- cat <fileName>
```

### Commands:
#### For Container Registry:
```bash
- gcloud auth login
- gcloud projects list
- gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE
- gcloud auth configure-docker
- docker push gcr.io/ml-project-382217/flask-app:red
- docker pull gcr.io/ml-project-382217/flask-app:red
- gcloud config set project <project-id>
- gcloud config set run/region us-central1
- gcloud builds submit --tag gcr.io/ml-project-382217/flask-app:red .  # [Build image and push on cloud]
- gcloud run deploy --image gcr.io/ml-project-382217/flask-app:red  # [Deploy on Cloud Run]
```
#### For Artifact Registry:
``` bash
- gcloud auth configure-docker asia-south1-docker.pkg.dev  # [To Configure Docker]
- gcloud builds submit --tag asia-south1-docker.pkg.dev/ml-project-382217/images/flask-app:red .
- gcloud run deploy --image asia-south1-docker.pkg.dev/ml-project-382217/images/flask-app:red  # [Deploy on Cloud Run]
```

### For Azure Container Registry:
```bash
- docker build -t <resgroup>.azurecr.io/<imagename>:latest .
- docker login <resgroup>.azurecr.io
- docker push <resgroup>.azurecr.io/<imagename>:latest
```


### For running Docker images on local from Container registry:
- Upload the necessary files in GCP Cloudshell and build the image.
- Now tag the image based on gcr.io
- Push the image in Container registry.
- Pull the image from local with 'gcloud auth login'.
- Run the image in local for testing.


### For GithubActions: [Service-name: github-actions]
- Need to create only one service account based on 'Storage Admin' role with active keys.
- For Container registry:
    - Add grant access on 'Cloud Storage' service using 'github-actions' service name.
- For Artifact registry:
    - Need to create a repository name as 'images'
    - Add principal name as 'github-actions' based on 'Artifact registry writer' role
