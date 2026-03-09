# bucket-o-slop 🪣

**Test fixture repository for [slop-mop](https://github.com/ScienceIsNeato/slop-mop) integration tests.**

> Do not use this repo as a template for real projects — it is intentionally broken in places.
> The broken states exist to verify that slop-mop catches them.

---

## What this is

`bucket-o-slop` is a minimal Python project that exists solely so slop-mop's integration tests
have something real to run against. It contains three git branches, each representing a
different quality state:

| Branch     | Purpose                                 | Expected slop-mop outcome          |
| ---------- | --------------------------------------- | ---------------------------------- |
| `main`     | Clean, well-written code                | All gates **pass** → exit 0        |
| `all-fail` | Every supported gate is uniquely broken | All gates **fail** → exit non-zero |
| `mixed`    | Some gates fail, one gate disabled      | Mixed results → exit non-zero      |

The integration tests in slop-mop ([`tests/integration/`](https://github.com/ScienceIsNeato/slop-mop/tree/main/tests/integration))
check out each branch inside a Docker container, run `sm validate commit`, and assert on
the exit code and output.

---

## Branch details

### `main` — happy path

All gates enabled and passing:

- `src/calculator.py` and `src/utils.py` — clean, typed, no dead code, no secrets
- `tests/` — full coverage, no bogus tests
- `.sb_config.json` — all gates enabled with standard thresholds

### `all-fail` — every gate uniquely broken

Each file deliberately trips a different gate:

| File                                      | Gate triggered       | How                                                     |
| ----------------------------------------- | -------------------- | ------------------------------------------------------- |
| `src/calculator.py`                       | `py-lint`            | unused import (`import os`)                             |
| `src/calculator.py`                       | `security:local`     | hardcoded credential (`DB_PASSWORD`)                    |
| `src/calculator.py`                       | `dead-code`          | unused function `_internal_helper_nobody_calls()`       |
| `src/calculator.py`                       | `py-lint`            | format drift (missing spaces around `:`)                |
| `src/utils.py`                            | `string-duplication` | same error message string defined 3×                    |
| `src/utils.py`                            | `complexity`         | `classify_input()` has 16+ branches                     |
| `src/utils.py` + `src/duplicate_block.py` | `source-duplication` | verbatim copied function body                           |
| `src/utils.py`                            | `loc-lock`           | `bloated_function()` is ~120 lines                      |
| `tests/test_calculator.py`                | `py-tests`           | `test_add_wrong_expectation()` asserts `add(2,2) == 99` |
| `tests/test_utils.py`                     | `bogus-tests`        | tautological asserts (`assert True`, `assert x == x`)   |
| `tests/test_utils.py`                     | `py-coverage`        | coverage drops below 80% threshold                      |

### `mixed` — partial failures + disabled gate

Realistic mid-development state:

- **Fails:** `security:local` (hardcoded API key), `dead-code` (`_experimental_feature`), `bogus-tests` (tautology in test)
- **Passes:** `py-lint`, `py-tests`, `py-coverage`, `complexity`, `loc-lock`, `string-duplication`
- **Skipped:** `source-duplication` — disabled in `.sb_config.json` to exercise the skip path

---

## Project structure

```
bucket-o-slop/
├── src/
│   ├── __init__.py
│   ├── calculator.py       # arithmetic functions
│   ├── utils.py            # string utilities
│   └── duplicate_block.py  # (all-fail only) source-duplication target
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_utils.py
├── .sb_config.json         # slop-mop gate configuration
├── pyproject.toml
└── README.md
```

---

## Running slop-mop against this repo manually

```bash
# Clone both repos as siblings
git clone https://github.com/ScienceIsNeato/slop-mop.git
git clone https://github.com/ScienceIsNeato/bucket-o-slop.git

# Build the integration test image (run from inside slop-mop/)
cd slop-mop
docker build -t slop-mop-integration-test -f tests/integration/Dockerfile .

# Drop into the container interactively to explore
docker run --rm -it \
  -v "$(pwd):/slopmop-src:ro" \
  -v "$(cd ../bucket-o-slop && pwd):/test-repo" \
  --workdir /test-repo \
  slop-mop-integration-test bash

# Inside the container:
#   git checkout main && sm validate commit    # → should exit 0
#   git checkout all-fail && sm validate commit # → should exit 1
#   git checkout mixed && sm validate commit    # → should exit 1

# Run the full pytest integration suite
BUCKET_O_SLOP_PATH="$(cd ../bucket-o-slop && pwd)" \
  pytest tests/integration/ -m integration -v
```

---

## ⚠️ Not for production use

This repo is maintained as a test fixture. Its `all-fail` branch contains intentional
security issues, dead code, and broken tests. **Do not copy code from this repo.**
