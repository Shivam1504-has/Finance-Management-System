# Security Policy

## Supported versions

| Version | Supported |
| ------- | --------- |
| `main` (latest) | ✅ |
| Anything else | ❌ |

## Reporting a vulnerability

**Please do not open a public issue for security bugs.**

Instead, report privately:

1. Go to the repo's **Security → Advisories → Report a vulnerability**, or
2. Message the maintainer directly via their GitHub profile.

Include: description, steps to reproduce, and impact. Expect an initial
response within 72 hours. Thanks for keeping this project safe! 🙏

## Secrets hygiene

- Never commit `.env`, `serviceAccountKey.json`, `google-services.json`,
  or API keys. CI and `.gitignore` are configured to help, but stay vigilant.
- Rotate any credential that was ever committed, then purge it from history.
