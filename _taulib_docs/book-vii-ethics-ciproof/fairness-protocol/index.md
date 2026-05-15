---
{
  "projection_kind": "taulib_declaration",
  "title": "FairnessProtocol",
  "permalink": "/corpus/taulib/docs/book-vii-ethics-ciproof/fairness-protocol/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::FairnessProtocol",
  "declaration_slug": "fairness-protocol",
  "kind": "structure",
  "name": "FairnessProtocol",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/corpus/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 567,
  "source_line_end": 573,
  "registry_ids": [
    "VII.D67"
  ],
  "related_registry_items": [
    {
      "id": "VII.D67",
      "title": "Fairness Protocol",
      "url": "/registry/object/VII.D67/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L567-L573",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/corpus/taulib/docs/book-vii-ethics-ciproof/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L567-L573",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookVII.Ethics.CIProof](/corpus/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L567-L573)
- Source range: L567-L573
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `VII.D67` — Fairness Protocol

## Immediate Comment / Docstring

```lean
/-- [VII.D67] Fairness Protocol (ch80). 5-step procedure:
    (1) Boundary identification (affected persons, actions)
    (2) Structural filtering (label-independent criteria)
    (3) Dignity check (factors through L_dig)
    (4) Residual tie-breaking (uniform lottery 1/n)
    (5) Execution (no conditioning on contingent labels) -/
```

## Source Excerpt

```lean
structure FairnessProtocol where
  step_count : Nat := 5
  /-- Label-independent throughout. -/
  label_independent : Bool := true
  /-- Dignity-preserving throughout. -/
  dignity_preserving : Bool := true
  deriving Repr
```
