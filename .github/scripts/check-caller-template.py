"""The six-line caller (templates/camp-release.yml) is what plugin repos and
scaffolding tools (mdlcode) copy or fetch; it must stay correct when the
reusable workflow changes, and its other copies must stay identical.

Fails when:
  1. camp-workflows release.yml (fetched from main) declares a workflow_call
     input or secret without a default, i.e. one the caller would have to
     pass and does not;
  2. the caller does not grant the permissions the reusable workflow needs
     (contents: read, id-token: write), or does not call release.yml@v1;
  3. the inline copies in camp-docs AUTHORS.md and camp-workflows README.md
     differ from the template (comment lines excluded).
Runs in publish; a failure is loud twice a day until someone updates the
template and its copies together.
"""
import re
import sys
import urllib.request

import yaml

RAW = "https://raw.githubusercontent.com/camp-registry/camp-workflows/main/"


def fetch(name):
    return urllib.request.urlopen(RAW + name, timeout=20).read().decode()


def template_body(path):
    return "\n".join(l for l in open(path).read().splitlines()
                     if l.strip() and not l.lstrip().startswith("#")).strip()


def inline_block(text, must_contain="uses: camp-registry/camp-workflows"):
    blocks = re.findall(r"```yaml\n(.*?)```", text, re.S)
    hits = [b.strip() for b in blocks if must_contain in b]
    return hits[0] if len(hits) == 1 else None


def main(template_path, authors_path):
    problems = []
    canon = template_body(template_path)
    caller = yaml.safe_load(canon)
    reusable = yaml.safe_load(fetch(".github/workflows/release.yml"))

    call = (reusable.get("on") or reusable.get(True) or {}).get("workflow_call") or {}
    for kind in ("inputs", "secrets"):
        for name, spec in (call.get(kind) or {}).items():
            spec = spec or {}
            if spec.get("required") or (kind == "inputs" and "default" not in spec):
                problems.append(f"release.yml now requires {kind[:-1]} '{name}'; "
                                f"the caller template passes nothing")

    perms = caller.get("permissions") or {}
    for key, level in (("contents", "read"), ("id-token", "write")):
        if perms.get(key) != level:
            problems.append(f"caller template must grant {key}: {level}")
    uses = [j.get("uses", "") for j in (caller.get("jobs") or {}).values()]
    if uses != ["camp-registry/camp-workflows/.github/workflows/release.yml@v1"]:
        problems.append(f"caller template must call release.yml@v1, has {uses}")

    authors = inline_block(open(authors_path).read())
    if authors != canon:
        problems.append("camp-docs AUTHORS.md inline caller differs from the template")
    readme = inline_block(fetch("README.md"))
    if readme != canon:
        problems.append("camp-workflows README.md inline caller differs from the template")

    for p in problems:
        print(f"::error::caller template: {p}")
    print("caller template: ok" if not problems else
          "caller template: UPDATE templates/camp-release.yml and its copies together")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
