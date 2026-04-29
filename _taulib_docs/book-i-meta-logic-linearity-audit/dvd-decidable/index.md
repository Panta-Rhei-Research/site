---
{
  "projection_kind": "taulib_declaration",
  "title": "dvd_decidable",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/dvd-decidable/",
  "summary_short": "`def` declaration in `TauLib.BookI.MetaLogic.LinearityAudit`.",
  "declaration_id": "TauLib.BookI.MetaLogic.LinearityAudit::dvd_decidable",
  "declaration_slug": "dvd-decidable",
  "kind": "def",
  "name": "dvd_decidable",
  "module_name": "TauLib.BookI.MetaLogic.LinearityAudit",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-linearity-audit/",
  "source_line_start": 209,
  "source_line_end": 210,
  "registry_ids": [
    "I.P38"
  ],
  "related_registry_items": [
    {
      "id": "I.P38",
      "title": "Classical.em Eliminability",
      "url": "/registry/object/I.P38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L209-L210",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L209-L210",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookI/MetaLogic/LinearityAudit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/LinearityAudit.lean#L209-L210)
- Source range: L209-L210
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.P38` — Classical.em Eliminability

## Immediate Comment / Docstring

```lean
/-- [I.P38] The Classical.em sites in Primes.lean are applied to
    decidable predicates on Nat. Since Nat divisibility is decidable,
    these uses are eliminable: they can be replaced by `Decidable.em`.

    Proof that divisibility is decidable: -/
```

## Source Excerpt

```lean
def dvd_decidable (a b : Nat) : Decidable (a ∣ b) :=
  inferInstance
```
