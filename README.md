# Human in the Loop

Quarto documentation project for human-in-the-loop content.

## Project Structure

```
.
├── source/          # Source Quarto documents
│   ├── assets/      # Images and templates
│   ├── faq.md
│   ├── presentation.md
│   └── references.md
└── docs/            # Rendered output for GitHub Pages
```

## Workflow

1. Edit source files in `source/`
2. Render documents locally to `docs/` folder
3. Commit and push both source and rendered output
4. GitHub Pages serves content from `docs/` folder

## Requirements

- [Quarto](https://quarto.org/)

## Usage

Render the documents:

```bash
quarto render source/
```

## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

[![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
