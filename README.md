# bucket-o-slop

Integration test fixture repository for [slop-mop](https://github.com/ScienceIsNeato/slop-mop).

This repo has three branches, each representing a different quality state:

| Branch | Behaviour |
|--------|-----------|
| `main` | Happy path — all gates pass |
| `all-fail` | Every gate is uniquely broken |
| `mixed` | Mixture of passes, failures, and edge cases |

The slop-mop integration tests check out each branch inside a Docker container,
`pip install slopmop`, run `sm init --non-interactive`, then run `sm validate commit`
and assert the expected outcome.
