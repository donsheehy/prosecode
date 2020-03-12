# Planning

## Deal correctly with files

Eliminate all uses of string concatenation for file paths.

Move all file processing for weave to the CLI.

## Chunks

Print the raw code of a chunk into a LaTeX comment.

Allow looser syntax for code chunk parameters.
- [ ] Parse options with single quotes.
- [ ] Be okay with some extra spaces around lang

Correctly, handle generic continues in chunks.

## Tables

Correctly map tables to latex tabular environments.

## Test the Chunk code

Make sure it handles hide and output options

## Test the CLI

Integrate `pyfakefs` into CLI tests.

## Add support for other languages similar to what is done with MPE

Support for weaving other languages besides python.

Support for tangling other languages besides python.

## LaTeX Diffs
