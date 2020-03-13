# prosecode Planning

## Deal correctly with files

- [x] Move all file processing for weave to the CLI.
- [ ] Eliminate all uses of string concatenation for file paths.

## Chunks

- [x] Print the raw code of a chunk into a LaTeX comment.

- [ ] Allow looser syntax for code chunk parameters.
  - [ ] Parse options with single quotes.
  - [ ] Be okay with some extra spaces around lang

- [ ] Correctly, handle generic continues in chunks.

## Tables

- [ ] Correctly map tables to latex tabular environments.

## Testing

- [ ] Test that Chunk processing handles `hide` and `output` options.
- [x] Test the CLI without touching files.
- [ ] Test the html and latex escape corner cases.

## Add support for other languages similar to what is done with MPE

- [ ] Support for weaving other languages besides python.
  - [ ] Test it with node and python to js book

- [ ] Support for tangling other languages besides python.

## LaTeX Diffs

- [ ] Do an experiment to see how it works.

## Log errors

- [ ] Unexpected errors are written to stderr
- [ ] Unexpected errors are logged

## code coverage

- [ ] The total code coverage is calculated and reported.

## Integrated pytest testing

- [ ] Working examples of pytest tests inline.

## Produce nice HTML

- [ ] add a format option to weave to produce html instead
- [ ] Add the prettify script to HTML.
  - `<script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>`
- [ ] Mark code as `<code class="prettyprint lang-python">` or just `<code class="prettyprint">`
