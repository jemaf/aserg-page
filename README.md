# ASERG Page

This repository contains the source code and resources for the ASERG (Advanced Software Engineering Research Group) webpage. 
The ASERG page provides information about our research projects, publications, team members, and upcoming events.

- [Adding a Publication](templates/publication_template.md)
- [Adding a Thesis/Dissertation](templates/thesis_template.md)

## Running Locally

Requires [Docker](https://www.docker.com/). From the repository root:

```bash
# Build the development image
docker build -f Dockerfile.dev -t aserg-page-dev .

# Run it, exposing the Jekyll server (4000) and LiveReload (35729) ports,
# and mounting the source folder so edits are reloaded automatically
docker run --rm -p 4000:4000 -p 35729:35729 -v "$(pwd)":/app aserg-page-dev
```

Then open <http://localhost:4000>. The page reloads on every change to the source files.

