# Profile design and live statistics

This repository powers the public profile at [github.com/vigorlee](https://github.com/vigorlee).

- `assets/header.svg`: a lightweight animated perception–memory–reasoning–action loop. It respects `prefers-reduced-motion` and remains readable without animation.
- Project cards link to their corresponding repositories; the native `<details>` sections open and close on click or keyboard activation.
- Total Stars uses `https://img.shields.io/github/stars/vigorlee?affiliations=OWNER`. The number is fetched by Shields from GitHub; it is not written into this repository.
- Shields currently sums the top 200 repositories by stars; all 19 public repositories at setup are covered. [Service implementation](https://github.com/badges/shields/blob/master/services/github/github-total-star.service.js).
- The scope is stars **received by repositories owned by vigorlee**, not the account's starred-repository list. Repository-specific star badges update independently.
- The profile is a rendered document, not a continuously running web app. Badge service caching and GitHub's image proxy can delay visible updates; `cacheSeconds=300` requests a cache duration but does not guarantee a five-minute refresh or second-by-second updates. Reloading the page may still show a cached image.
- No access token is embedded in the README, SVGs or badge URLs. No scheduled write workflow is needed for these statistics.

All research descriptions are based on the existing profile and public repositories. The WAVE-Go image links to a fixed, verified result commit so later README changes do not silently replace the illustrated experiment.
