# Install Gitlab Community edition on any Ubuntu/Debian systems

This script installs self-hosted Gitlab Community edition platform on any Ubuntu/Debian systems. This script is tested on Ubuntu 18.04.2 Bionic Beaver.

https://gitlab.com/gitlab-org/gitlab-ce/

# Usage

1) Clone the repository or download the script

2) Search for the following lines and include your domain names. Make sure gitlab and registry subdomains are available.

   --hostname gitlab.yourdomain.com 
   
   letsencrypt['contact_emails'] = ['youremail@gmail.com'] 
   
   external_url 'https://gitlab.yourdomain.com/'; 
   
   registry_external_url 'https://registry.yourdomain.com'; 
   
3) Modify username and password in 

   gitlab_rails['smtp_user_name'] = \"yourusername\"; example \"apikey\";
   
   gitlab_rails['smtp_password'] = \"yourpassword\"; # example \"SG.wCsa3KhAIzaSyClzfrOzB818x55FASHvX4JuGQciR9lv7q\";
   
 4) chmod +x ./gitlab-installation.sh
 
 5) ./gitlab-installation.sh
 
 # Updates
 
 Source : https://about.gitlab.com/update/
 
 To update to the latest version
 
 1) Backup your repositories first,
 
 docker exec -t <container name> gitlab-rake gitlab:backup:create
 
 You backups will be saved to /var/opt/gitlab/backups by default
 
 2) Update
 
 sudo apt-get update && sudo apt-get install gitlab-ce
 
 3) Check version
 
 https://gitlab.yourdomain.com/help 
 
 # SSL certificates for HTTPS
 
 This script uses Letsencrypt(https://letsencrypt.org/) free, automated, and open Certificate Authority. But you can choose a different CA.
 
 The Letsencrypt certificates are valid for 90 days. But the script is set to automatically renew before expiry.
 
 
