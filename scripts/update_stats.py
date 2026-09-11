"""Generate a public, paginated GitHub star snapshot; never publish partial results."""
import json
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
USER = 'vigorlee'


def fetch_repos():
    repos = []
    page = 1
    while True:
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'vigorlee-profile'}
        if os.environ.get('GITHUB_TOKEN'):
            headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
        request = Request(f'https://api.github.com/users/{USER}/repos?type=owner&per_page=100&page={page}', headers=headers)
        with urlopen(request, timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError('Expected repository list')
        repos.extend(r for r in batch if not r['private'] and r['owner']['login'].lower() == USER)
        if len(batch) < 100:
            break
        page += 1
    return repos


def render(repos, updated):
    total = sum(r['stargazers_count'] for r in repos)
    ranked = sorted(repos, key=lambda r: (-r['stargazers_count'], r['name']))
    top = [r for r in ranked if r['stargazers_count']][:4]
    parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360" role="img" aria-labelledby="title desc">
<title id="title">{total:,} total stars across {len(repos)} public repositories</title>
<desc id="desc">Current stars received, including owned forks. Updated {escape(updated)}. Snapshot; see the live badge for independently updated statistics.</desc>
<defs><linearGradient id="bg"><stop stop-color="#0b1728"/><stop offset="1" stop-color="#102d37"/></linearGradient></defs>
<style>text{{font-family:Segoe UI,Arial,sans-serif}}.beacon{{animation:blink 3s ease-in-out infinite}}@keyframes blink{{50%{{opacity:.35}}}}@media(prefers-reduced-motion:reduce){{.beacon{{animation:none}}}}</style>
<rect width="1200" height="360" rx="22" fill="url(#bg)"/>
<circle class="beacon" cx="48" cy="43" r="5" fill="#5eead4"/>
<text x="64" y="48" font-size="13" letter-spacing="2" fill="#9db9cb">OPEN SOURCE / STAR SNAPSHOT</text>
<text x="42" y="170" font-size="104" font-weight="700" fill="#f0f7fc">{total:,}</text>
<text x="48" y="207" font-size="20" fill="#5eead4">STARS RECEIVED</text>
<text x="48" y="244" font-size="16" fill="#9db9cb">{len(repos)} public repos · {sum(not r['fork'] for r in repos)} original repos</text>
<path d="M460 78V268" stroke="#31546c"/>
<text x="508" y="88" font-size="12" letter-spacing="2" fill="#9db9cb">WHERE THE STARS LAND</text>''']
    colors = ['#38bdf8', '#5eead4', '#c4b5fd', '#f6bd75']
    for index, repo in enumerate(top):
        y = 124 + index * 43
        stars = repo['stargazers_count']
        share = stars / total if total else 0
        parts.append(f'<text x="508" y="{y}" font-size="15" fill="#e5f0f7">{escape(repo["name"])}</text><rect x="805" y="{y-11}" width="220" height="8" rx="4" fill="#24424f"/><rect x="805" y="{y-11}" width="{220*share:.2f}" height="8" rx="4" fill="{colors[index]}"/><text x="1148" y="{y}" text-anchor="end" font-size="15" fill="{colors[index]}">{stars} / {share:.0%}</text>')
    parts.append(f'<path d="M44 294H1156" stroke="#31546c"/><text x="48" y="328" fill="#9db9cb" font-size="13">UPDATED {escape(updated)} · SNAPSHOT · LIVE TOTAL AVAILABLE IN THE BADGE ABOVE</text></svg>')
    return '\n'.join(parts), {'total_stars': total, 'public_repositories': len(repos), 'updated_at': updated, 'scope': 'Current stars on all public repositories owned by vigorlee, including forks; not historical lifetime stars.', 'repositories': [{'name': r['name'], 'stars': r['stargazers_count'], 'fork': r['fork']} for r in ranked]}


def main():
    repos = fetch_repos()
    updated = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    svg, data = render(repos, updated)
    (ROOT / 'assets/stars.svg').write_text(svg, encoding='utf-8')
    (ROOT / 'assets/stars.json').write_text(json.dumps(data, indent=2) + '\n', encoding='utf-8')
    print(f"Updated {data['total_stars']} stars across {len(repos)} repositories")


if __name__ == '__main__':
    main()
