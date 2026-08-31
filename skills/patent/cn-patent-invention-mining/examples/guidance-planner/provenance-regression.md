# Regression example: `feiyushaw/guidance_planner`

Purpose: test whether patent skills distinguish an applicant/user repository from inherited public technology instead of treating sophisticated upstream code as the user's invention.

## Observed repository facts

`feiyushaw/guidance_planner` is a public fork of `tud-amr/guidance_planner`. The upstream implementation is associated with published work and explicitly contains mechanisms including Visibility-PRM, topology-distinct trajectory generation, H-signature, winding-angle, and UVD topology comparison.

## Expected provenance classification

| Mechanism | Expected class | Candidate status | Reason |
|---|---|---|---|
| Visibility-PRM guidance graph | `UPSTREAM_PRIOR_ART` | `BACKGROUND_ONLY` | Explicit upstream feature |
| topology-distinct trajectory generation | `UPSTREAM_PRIOR_ART` | `BACKGROUND_ONLY` | Explicit paper/repository contribution |
| H-signature / winding-angle / UVD comparison | `THIRD_PARTY_PRIOR_ART` / `UPSTREAM_PRIOR_ART` | `BACKGROUND_ONLY` | Pre-existing/upstream mechanisms |
| ROS support / ordinary bug fixes | `COMMON_ENGINEERING` by default | `EXCLUDE` | Routine work unless a distinct mechanism is shown |
| autonomous-driving closed-loop coupling absent upstream | `USER_MODIFICATION` if implemented | `REVIEW_DELTA` | Requires actual user evidence |
| ego-action-conditioned interactive-agent response feeding replanning | `POTENTIAL_INVENTION` if implemented and not otherwise public | `CANDIDATE` | Coupling may create a technical effect |

## Regression assertions

A correct run detects the fork and upstream publications, does not claim upstream planner mechanisms as applicant inventions, does not infer inventorship from repository ownership, explicitly reports when no material user delta is found, and mines only added coupling/feedback mechanisms when a separate system supplies them.

This is a regression fixture, not evidence that the target repository implements the synthetic extension mechanisms.
