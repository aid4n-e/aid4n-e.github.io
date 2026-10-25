# Portfolio site

A Jekyll site for GitHub Pages.

## Edit your content

1. `_config.yml`: your name, email, GitHub and LinkedIn usernames, and site URL.
2. `about.md`: your bio, skills and résumé link (put the PDF at `assets/resume.pdf`).
3. `_projects/*.md`: one file per project. Copy an existing file to add a new one. Delete the yellow "Placeholder" boxes once you've written real content.
4. Images go in `assets/img/`.

## Preview locally (optional)

```
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Publish on GitHub Pages

1. Create a repo named `yourusername.github.io` and push these files to it.
2. In the repo, go to Settings, then Pages, and set the source to deploy from the `main` branch.
3. Your site will appear at `https://yourusername.github.io` after a minute or two.

If you use a differently named repo, set `baseurl: "/repo-name"` in `_config.yml`.
