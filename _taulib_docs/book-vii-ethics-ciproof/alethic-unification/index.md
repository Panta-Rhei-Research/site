---
{
  "projection_kind": "taulib_declaration",
  "title": "alethic_unification",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/alethic-unification/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::alethic_unification",
  "declaration_slug": "alethic-unification",
  "kind": "theorem",
  "name": "alethic_unification",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 767,
  "source_line_end": 773,
  "registry_ids": [
    "VII.T27"
  ],
  "related_registry_items": [
    {
      "id": "VII.T27",
      "title": "Alethic Unification",
      "url": "/registry/object/VII.T27/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L767-L773",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L767-L773",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L767-L773)
- Source range: L767-L773
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T27` — Alethic Unification

## Immediate Comment / Docstring

```lean
/-- [VII.T27] Alethic Unification (ch42). The four truth-maker
    levels form a coherent hierarchy: each level contains the
    previous. Inclusion ⊂ Section ⊂ Diagram ⊂ Invariant.
    All four are unified by sheaf-theoretic structure. -/
```

## Source Excerpt

```lean
theorem alethic_unification :
    truth_maker_logical.level_inclusion = true ∧
    truth_maker_logical.level_section = true ∧
    truth_maker_logical.level_diagram = true ∧
    truth_maker_logical.level_invariant = true ∧
    truth_maker_logical.level_count = 4 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩
```
