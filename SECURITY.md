# Reporting a security vulnerability

**Never report a vulnerability in a public issue, pull request, or forum
post.** Public disclosure before a fix exists puts every site running the
affected code at risk.

## You maintain a listed plugin and are fixing a vulnerability

Tell the registry privately, using
[private vulnerability reporting on this repository](../../security/advisories/new),
so a `CAMP-YYYY-NNNN` advisory goes out when your fix does. Report
before you tag the fix if you can; as soon as you have a release date
is ideal. Include:

- the component (for example `filter_example`);
- the affected versions and the fixed version, or the tag you plan to
  release;
- your severity rating (low, medium, high or critical), with a CVSS
  vector if you have one;
- a short description that is safe to publish at release, and fuller
  details if you want them published later;
- whether the affected versions should be revoked (removed from
  installation channels; the archived artifacts are kept);
- the reporter, and whether they agree to be credited;
- the CVE, if you have one or have requested one.

The registry prepares the advisory privately and publishes it once your
fixed release is live in the registry. Nothing about the vulnerability
is published before then. When you disclose full details, the registry
adds them, the credit and any CVE to the same advisory. If the fix is
already out, report the same way. Do not open a public issue or pull
request for an advisory: advisory IDs are assigned by the registry at
publication.

## In a plugin listed in the registry

Report it to the plugin's maintainer first, privately. Every claimed
listing on [camp-registry.org](https://camp-registry.org) publishes a
**security contact** on its plugin page — preferably the source
repository's private vulnerability reporting form. The maintainer
develops a fix under embargo (90 days by default, negotiable), releases
it, and the registry then publishes a `CAMP-YYYY-NNNN` advisory that
warns affected sites through the site, `composer audit`, and the client
plugin (RFC §5.3).

**Escalate to the registry** — using
[private vulnerability reporting on this repository](../../security/advisories/new)
— when:

- the maintainer is unresponsive or declines to fix;
- the listing is unclaimed (Tier 0) and has no security contact;
- the vulnerability is being actively exploited and coordinated
  disclosure through the maintainer alone is too slow.

The registry's security team will attempt to reach the maintainer,
coordinate the embargo, and may publish an advisory — and in severe
cases revoke affected versions from installation — with or without a
fix once the embargo expires.

## In camp itself

Vulnerabilities in the registry's own infrastructure (this index, the
tooling, the website, the client plugin) go through
[private vulnerability reporting on this repository](../../security/advisories/new)
as well.

## Out of scope

Vulnerabilities in **Moodle core** are always reported to
[Moodle HQ's security process](https://moodledev.io/general/development/process/security),
never here.

## What happens to a report

Reports are triaged by the registry security team. GitHub's private
advisory workspace is used for **intake and coordination only**: the
published artifact is always a `CAMP-YYYY-NNNN` advisory in this
repository's `advisories/` directory, and the draft GitHub advisory is
closed unpublished. Advisory IDs are assigned by the registry at
publication time. If the maintainer requests a CVE through their own
repository, the CAMP advisory records it in its `cve` field.
