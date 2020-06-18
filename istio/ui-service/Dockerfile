FROM nginx
COPY index.html /var/www/index.html
COPY static /var/www/static
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf