# Jekyll Static Website with Docker

A modern, responsive static website built with Jekyll and served using Docker containers. This project provides both development and production environments with easy setup and deployment.

## Features

- 🚀 **Fast & Lightweight**: Built with Jekyll for optimal performance
- 🐳 **Docker Ready**: Containerized for consistent environments
- 📱 **Responsive Design**: Modern design that works on all devices
- 🔧 **Easy to Customize**: Clean, semantic HTML and CSS
- 📝 **Blog Support**: Built-in blog functionality with Markdown
- 🔍 **SEO Optimized**: Built with SEO best practices

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Development Mode

To run the site in development mode with live reloading:

```bash
docker-compose up jekyll-dev
```

Visit [http://localhost:4000](http://localhost:4000) to see your site.

### Production Mode

To build and serve the production version:

```bash
docker-compose up jekyll-prod
```

Visit [http://localhost](http://localhost) to see your site.

## Project Structure

```
.
├── _layouts/          # Jekyll layout templates
├── _posts/            # Blog posts (Markdown files)
├── assets/            # Static assets (CSS, JS, images)
├── Dockerfile         # Production Docker configuration
├── Dockerfile.dev     # Development Docker configuration
├── docker-compose.yml # Docker Compose configuration
├── _config.yml        # Jekyll configuration
├── Gemfile           # Ruby dependencies
└── README.md         # This file
```

## Customization

### Site Configuration

Edit `_config.yml` to customize your site:

- Site title and description
- Author information
- URL settings
- Plugin configuration

### Styling

The main stylesheet is located at `assets/css/main.css`. It includes:

- Modern, responsive design
- Clean typography
- Mobile-first approach
- CSS Grid and Flexbox layouts

### Content

- **Pages**: Create new pages in the root directory with `.html` or `.md` extension
- **Posts**: Add blog posts to the `_posts/` directory
- **Layouts**: Customize layouts in the `_layouts/` directory

## Docker Commands

### Build the image

```bash
# Development
docker build -f Dockerfile.dev -t jekyll-dev .

# Production
docker build -t jekyll-prod .
```

### Run containers

```bash
# Development with live reload
docker run -p 4000:4000 -v $(pwd):/app jekyll-dev

# Production
docker run -p 80:80 jekyll-prod
```

### Using Docker Compose

```bash
# Start development environment
docker-compose up jekyll-dev

# Start production environment
docker-compose up jekyll-prod

# Run in background
docker-compose up -d jekyll-dev

# Stop containers
docker-compose down
```

## Development Workflow

1. **Start Development Server**:
   ```bash
   docker-compose up jekyll-dev
   ```

2. **Edit Content**: 
   - Modify pages in the root directory
   - Add posts to `_posts/`
   - Update styles in `assets/css/main.css`

3. **Live Reload**: Changes are automatically detected and the site reloads

4. **Build for Production**:
   ```bash
   docker-compose up jekyll-prod
   ```

## Deployment

### Local Production Build

```bash
docker-compose up jekyll-prod
```

### Cloud Deployment

This setup works well with various cloud platforms:

- **AWS**: Deploy to ECS or EC2
- **Google Cloud**: Deploy to Cloud Run or GKE
- **Azure**: Deploy to Container Instances or AKS
- **DigitalOcean**: Deploy to App Platform or Droplets

### Static Site Hosting

You can also extract the built site from the container and deploy to static hosting services:

```bash
# Extract the built site
docker create --name temp jekyll-prod
docker cp temp:/usr/share/nginx/html ./_site
docker rm temp

# Deploy _site/ to your preferred hosting service
```

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `docker-compose.yml`
2. **Permission errors**: Ensure Docker has proper permissions
3. **Build failures**: Check that all dependencies are properly specified

### Logs

```bash
# View development logs
docker-compose logs jekyll-dev

# View production logs
docker-compose logs jekyll-prod
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues and questions:

1. Check the [Jekyll documentation](https://jekyllrb.com/docs/)
2. Review Docker logs for errors
3. Open an issue in this repository 