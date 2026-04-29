---
{
  "projection_kind": "taulib_declaration",
  "title": "EmEliminability",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/em-eliminability/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.LinearityAudit`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearityAudit::EmEliminability",
  "declaration_slug": "em-eliminability",
  "kind": "structure",
  "name": "EmEliminability",
  "module_name": "TauLib.BookI.MetaLogic.LinearityAudit",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/",
  "source_line_start": 239,
  "source_line_end": 243,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L239-L243",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.LinearityAudit",
        "url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L239-L243",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.MetaLogic.LinearityAudit](/verify/taulib/docs/book-i-meta-logic-linearity-audit/)
- Source path: [`TauLib/BookI/MetaLogic/LinearityAudit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L239-L243)
- Source range: L239-L243
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The Classical.em uses in Primes.lean are both on divisibility
    predicates, which are decidable. Therefore both sites are
    eliminable: Classical.em can be replaced by decidable_em. -/
```

## Source Excerpt

```lean
structure EmEliminability where
  /-- Divisibility is decidable -/
  dvd_dec : ∀ a b : Nat, Decidable (a ∣ b)
  /-- Decidable em works without Classical.em -/
  dvd_em_constructive : ∀ a b : Nat, (a ∣ b) ∨ ¬(a ∣ b)
```
