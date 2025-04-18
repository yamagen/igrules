# igrules

📅 Last change: 2025/04/18-15:23:54.

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

## 📜 Tools

- **JSON**: The main body of the immediate grammar rules is in JSON format.

```
$ python tools/merge.py > ig-rules-ja-en.json
$ python tools/merge.py --include-hidden > ig-rules-all.json
```

## 🗂️ Structure

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
- **Tasuki-gake Effect** [en](./tasuki-gake-effect-en.md) [ja](./tasuki-gake-effect-ja.md): A rhetorical effect that arises when immediate grammar is used in adjustment contexts or vice versa, producing expressive contrasts and heightened rhetorical impact.

---

## 🧱 Design Philosophy

The igrules project adopts a modular and layered design to ensure clarity, maintainability, and extensibility.

- Each rule is defined in its own JSON file under `json/`, containing only the core descriptive content (`title`, `description`, `examples`, etc.).
- Metadata such as `author`, `license`, and `affiliation` is defined once in `json/meta.json`.
- Rule publication status, ordering, and editorial control are handled in `json/order.json`, which defines:
  - `id`: Rule identifier
  - `visible`: Whether the rule is included in public merges
  - `status`: e.g., `draft`, `review`, `published`
- Additional review records (`reviewer`, `review-date`) and notes can be added directly within each rule file under `reviews` and `note`.

This separation of concerns enables:

- Clear version control
- Selective publishing (draft rules can be excluded)
- Structured collaboration and editorial workflows
- Future extensions like categorization, dependency graphs, and rule groupings

This design reflects not only the linguistic nature of immediate grammar but also a practical approach to knowledge organization.
