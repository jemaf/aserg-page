---
layout: post
title: "Welcome to Jekyll"
date: 2024-01-01
categories: jekyll update
tags: [jekyll, docker, static-site]
author: Your Name
---

You'll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

## Code Examples

Jekyll also offers powerful support for code snippets:

```ruby
def print_hello_world
  puts "Hello, World!"
end
print_hello_world
```

## Lists and Links

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll's GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/

## Docker Integration

This site is built and served using Docker containers, which provides several benefits:

- **Consistent Environment**: The same build environment across all machines
- **Easy Deployment**: Simple commands to build and deploy
- **Isolation**: No conflicts with system dependencies
- **Scalability**: Easy to scale horizontally

To run this site locally, simply use:

```bash
docker-compose up jekyll-dev
```

This will start the development server with live reloading enabled. 