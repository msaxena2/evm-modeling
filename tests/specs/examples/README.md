Verification Instructions for KEVM
==================================

If you're trying to analyze Solidity smart contracts with symbolic execution, check out our guide for Kontrol at [docs.runtimeverification.com/kontrol].

This folder contains instructions for kompiling and running claims using KEVM to help you start proving.

Example: Sum to N
-----------------

Have a look at the [sum-to-n-spec.k] file.
It has two modules:

  - `VERIFICATION` - containing the EVM program and a few `simplification` rules.
  - `SUM-TO-N-SPEC` - containing the claims which will be executed.

The first step is kompiling the `.k` file with the below command.

```sh
kevm kompile-spec sum-to-n-spec.k --target haskell --syntax-module VERIFICATION --main-module VERIFICATION --output-definition sum-to-n-spec/haskell
```

In this example, the arguments used are:

  - `--target haskell`: specify which symbolic backend to use for reasoning.
  - `--syntax-module VERIFICATION`: explicitly state the syntax module.
  - `--main-module VERIFICATION`: explicitly state the main module.
  - `--output-definition sum-to-n-spec/haskell`: the path where the kompiled definition is stored.

Next, run the prover with:

```sh
kevm prove sum-to-n-spec.k --definition sum-to-n-spec/haskell
```

The expected output is `#Top` which represents that all the claims have been proven.

Debugging a proof
-----------------

For `kevm prove`, you can use `kevm show-kcfg ...` or `kevm view-kcfg ...` to get a visualization.

`kevm view-kcfg [spec_file] [--save-directory save_directory] [--claim claim_label] ...` command takes the same basic arguments as `kevm prove ...` does, including:
  - `spec_file` is the file to look in for specifications.
  This is the same file that is used for `kevm prove …`.
  - `--save-directory` must be passed as where the KCFGs have been saved (by a previous call to `kevm prove --save-directory save_directory ...`)
  - `--claim claim_label` lets you select an individual claim out of the `spec_file`.
If the flag is omitted, it’s assumed that only one claim is present.
If the flag is omitted and more than one claim is present in the `spec_file` then an error will be raised.
  - `--spec-module spec_module` is also an inherited option.

The interactive KCFG (`view-kcfg`) puts your terminal in *application mode*.
To select text in this mode, hold the modifier key provided by your terminal emulator (typically SHIFT or OPTION) while clicking and dragging.
Refer to the [Textualize documentation](https://github.com/Textualize/textual/blob/main/docs/FAQ.md#how-can-i-select-and-copy-text-in-a-textual-app) for more information.

`kevm show-kcfg [spec_file] [--save-directory save_directory] [--claim claim_label] ...` command is pretty similar, but prints out the K Control Flow Graph to `stdout` instead.

A running example (starting from the root of the repository):

```sh
mkdir kcfgs
kevm kompile-spec tests/specs/benchmarks/verification.k --output-definition tests/specs/benchmarks/verification/haskell --main-module VERIFICATION --syntax-module VERIFICATION
kevm prove tests/specs/benchmarks/address00-spec.k --definition tests/specs/benchmarks/verification/haskell --verbose --save-directory kcfgs
kevm view-kcfg tests/specs/benchmarks/address00-spec.k --save-directory kcfgs --definition tests/specs/benchmarks/verification/haskell
```

[sum-to-n-spec.k]: <./sum-to-n-spec.k>
[K tutorial]: <https://github.com/runtimeverification/k/tree/master/k-distribution/k-tutorial>
[more about it here]: <https://github.com/runtimeverification/k/tree/master/k-distribution/k-tutorial/1_basic/20_backends#k-backends>
[docs.runtimeverification.com/kontrol]: <https://docs.runtimeverification.com/kontrol/>
