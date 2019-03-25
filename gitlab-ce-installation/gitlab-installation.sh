#!/usr/bin/env bash
docker run -it \
    --hostname gitlab.yourdomain.com \ #enter your custom domain here
    --env GITLAB_OMNIBUS_CONFIG="
letsencrypt['auto_renew'] = false;
letsencrypt['enable'] = true;
letsencrypt['contact_emails'] = ['youremail@gmail.com']; #enter your email id here
external_url 'https://gitlab.yourdomain.com/'; #enter your custom domain here again
registry_external_url 'https://registry.yourdomain.ca'; ##enter your custom domain here again
gitlab_rails['smtp_enable'] = true;
gitlab_rails['smtp_address'] = \"smtp.sendgrid.net\";
gitlab_rails['smtp_port'] = 587;
gitlab_rails['smtp_user_name'] = \"apikey\";
gitlab_rails['smtp_password'] = \"SG.wCsa3KhAIzaSyClzfrOzB818x55FASHvX4JuGQciR9lv7q\";
gitlab_rails['smtp_domain'] = \"smtp.sendgrid.net\";
gitlab_rails['smtp_authentication'] = \"login\";
gitlab_rails['smtp_enable_starttls_auto'] = true;
gitlab_rails['smtp_tls'] = false;" \
    --publish 443:443 --publish 80:80 --publish 22:22 \
    --name gitlab \
    --restart always \
    --volume /gitlab/config:/etc/gitlab \
    --volume /gitlab/logs:/var/log/gitlab \
    --volume /gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest
