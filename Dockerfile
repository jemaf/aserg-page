# Multi-stage build for Jekyll site
FROM ruby:3.2-alpine AS builder

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    gcc \
    g++ \
    make \
    libc-dev \
    libffi-dev \
    zlib-dev \
    libxml2-dev \
    libxslt-dev \
    readline-dev \
    yaml-dev \
    zlib-dev

# Set working directory
WORKDIR /app

# Copy Gemfile and Gemfile.lock and install dependencies
COPY Gemfile ./
COPY Gemfile.lock ./
RUN bundle config set --local build.nokogiri --use-system-libraries
RUN bundle install --jobs 4 --retry 3

# Copy source code
COPY . .

# Build the site
RUN bundle exec jekyll build --destination /app/_site

# Production stage with nginx
FROM nginx:alpine

# Copy built site to nginx
COPY --from=builder /app/_site /usr/share/nginx/html

# Copy custom nginx configuration (optional)
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"] 