# igrules

📅 Last change: 2025/04/18-07:32:04.

- [`ig-rules-ja-en.json`](./ig-rules-ja-en.json)

A bilingual collection of permissibility rules for Immediate Grammar

> The name "igrules" comes from "Immediate Grammar Rules"—and sounds just a little like "Ig Nobel", but it's serious!

**igrules** is a project that documents permissibility rules for Immediate Grammar in a bilingual format (Japanese and English).

## 🧭 Overview

This repository documents expression patterns that are typically considered unacceptable in phrase structure grammar (adjustive grammar), but are fully natural and functional within immediate grammar, based on real-time speech phenomena.

---

## 🔍 Intended Uses

- Japanese learners: Searching for examples of immediate and natural speech
- Linguists: Describing and organizing syntactic constraints
- Developers: Applications in rule-based natural language processing (NLP) and interpreters
- Educators: Introducing as a variation of grammar

---

## Structure

- `ig-rules-ja-en.json`:
  - The main body of the immediate grammar rules (bilingual)
  - Each rule includes:
    - `title-ja` / `title-en`: Title
    - `description-ja` / `description-en`: Explanation
    - `examples`: Example sentences in Japanese and English
    - `tags`: Classification from multiple perspectives
    - `level`: Classification such as `core`, `extended`, `stylistic` (planned)

---

## ⚖️ License

- This repository is licensed under the MIT License.
- The main body of the immediate grammar rules (`ig-rules-ja-en.json`) is licensed under CC-BY-SA 4.0.
  - https://creativecommons.org/licenses/by-sa/4.0/

---

## 🔮 Future Plans

- Expansion of the rule set
- LaTeX・Markdown format conversion script
- PHP + AJAX-based searchable web UI
- Version control and management of the rule set
- Open source and open data at GitHub and Zenodo

---

## 👤 Author

- Hilofumi Yamamoto, Ph.D., Institute of Science Tokyo

## Definitions

- **Immediate Grammar**: A type of grammar that is used in spontaneous, context-dependent utterances such as casual conversation or emotional reaction.
- **Adjustive Grammar**: A type of grammar that is used in pre-structured, composed contexts such as formal speeches, letters, or ceremonial language.
- **Tasuki-gake Effect**: [en](./tasuki-gake-effect-en.md) [ja](./tasuki-gake-effect-ja.md)A rhetorical effect that arises when immediate grammar is used in adjustment contexts or vice versa, producing expressive contrasts and heightened rhetorical impact.
