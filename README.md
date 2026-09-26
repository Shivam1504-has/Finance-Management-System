# 💰 Finance Management System

![CI](https://github.com/Shivam1504-has/Finance-Management-System/actions/workflows/ci.yml/badge.svg)
![Flutter](https://img.shields.io/badge/Flutter-3.10%2B-02569B?logo=flutter)
![Firebase](https://img.shields.io/badge/Firebase-Auth%20%2B%20Firestore-FFCA28?logo=firebase)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A **cross-platform Financial Management System** with role-based access control —
built with **Flutter** (Android, iOS, Web, Desktop) and **Firebase**
(Authentication + Cloud Firestore).

It serves three user roles in one codebase:

| Role | Can do |
|------|--------|
| 👑 **Authority** | Manage employees, projects, tasks, generate payslips |
| 🧑‍💼 **Employee** | View tasks, payslips, profile |
| 👤 **Regular user** | Track income/expenses, budgets, transactions |

> 🚀 **New here?** Read [`ROADMAP.md`](ROADMAP.md) for the 30-day build plan and
> [`CONTRIBUTING.md`](CONTRIBUTING.md) to make your first contribution.

---

## ✨ Features

- 🔐 Email/password + Google Sign-In (Firebase Auth)
- 👥 Role-based dashboards & route guards (`go_router`)
- 📊 Expense charts (`fl_chart`), budgets, transaction history
- 🧾 Payslip generation for employees
- 📴 Offline-first caching with Hive
- 🌙 AMOLED-black Material 3 theme
- ✅ CI: Flutter analyze + tests, Python project tests, JS syntax checks

## 🏗️ Repo structure

```
.
├── flutter_app/   # Main Flutter app (all roles, all platforms)
├── firebase/      # Firestore rules + setup / seed scripts (Node.js)
├── webapp/        # (Planned) Web companion — see ROADMAP.md
├── projects/      # Daily mini-projects: small, tested, documented tools
├── docs/          # Playbooks: profile growth, Arena+C.Lastopilot workflow
└── .github/       # Issue/PR templates + CI workflows
```

## 🚀 Quickstart

### 1. Flutter app

```bash
cd flutter_app
flutter pub get
flutter run
```

Requirements: Flutter SDK `>=3.10`, Dart `^3.10.0`.
Configure Firebase for your platforms (see [`firebase/README.md`](firebase/README.md)).

### 2. Firebase backend

```bash
cd firebase
npm install
npm run create-admin   # create first authority user
npm run seed           # optional: load demo data
```

### 3. Mini-projects

Each folder in [`projects/`](projects/) is self-contained with its own README + tests:

```bash
cd projects/day-01-csv-expense-parser
pip install pytest
pytest -q
```

## 🗺️ Roadmap

We build in public, a little every day. See **[`ROADMAP.md`](ROADMAP.md)** for the
30-day plan: repo hygiene → app features → mini-projects → first open-source release.

## 🤝 Contributing

Contributions are welcome! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and our
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Good first issues are labeled
[`good first issue`](https://github.com/Shivam1504-has/Finance-Management-System/labels/good%20first%20issue).

## 🔒 Security

Found a vulnerability? Please **do not** open a public issue — see [`SECURITY.md`](SECURITY.md).

## 📄 License

MIT © 2026 Shivam1504-has — see [`LICENSE`](LICENSE).
