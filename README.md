## APosTel-team

## Modifying the website

All the website contents are stored in the folder `docs`. 
After each push, github will rerun the jekyll static website generator and update the contents of the site.
This typically takes less than a minute.

### Updating existing content

All the html pages are generated from markdown files.
To update/edit some content, simply find the appropriate markdown file in the `docs` folder and make a pull request.

To change the title or subtitle, you can change values for the appropriate tags in `_config.yml`.

### Adding a new page

To make a new page, simply make a new markdown file in the `docs` folder.
Any new pages will be automatically added to the navagation bar.
You can write github-flavored markdown including code blocks with syntax highlighting.
The only special consideration for these markdown files are the YAML headers which have jekyll specific tags.

Lets walk through this example YAML header:

```text
---
title: Software Tools
layout: default
nav: true
---
```

- `title:` Will be used as the display name in the navagation side bar.
- `layout:`  This should always be set to `default`, as we have only implemented 1 style of layout.
- `nav:`  When `true`, this will allow the page to be listed in the navagation bar.
Set to `false` to hide it from there.

## License

This website is a modified version of the [jekyll-theme-slate](https://github.com/pages-themes/slate) which was distributed under the *Creative Commons Zero v1.0 Universal* license.
