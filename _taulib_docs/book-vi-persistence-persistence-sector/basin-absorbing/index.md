---
{
  "projection_kind": "taulib_declaration",
  "title": "BasinAbsorbing",
  "permalink": "/verify/taulib/docs/book-vi-persistence-persistence-sector/basin-absorbing/",
  "summary_short": "`structure` declaration in `TauLib.BookVI.Persistence.PersistenceSector`.",
  "declaration_id": "TauLib.BookVI.Persistence.PersistenceSector::BasinAbsorbing",
  "declaration_slug": "basin-absorbing",
  "kind": "structure",
  "name": "BasinAbsorbing",
  "module_name": "TauLib.BookVI.Persistence.PersistenceSector",
  "module_url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/",
  "source_line_start": 333,
  "source_line_end": 342,
  "registry_ids": [
    "VI.L16"
  ],
  "related_registry_items": [
    {
      "id": "VI.L16",
      "title": "Basin Is Absorbing",
      "url": "/registry/object/VI.L16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L333-L342",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Persistence.PersistenceSector",
        "url": "/verify/taulib/docs/book-vi-persistence-persistence-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L333-L342",
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

- Module: [TauLib.BookVI.Persistence.PersistenceSector](/verify/taulib/docs/book-vi-persistence-persistence-sector/)
- Source path: [`TauLib/BookVI/Persistence/PersistenceSector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Persistence/PersistenceSector.lean#L333-L342)
- Source range: L333-L342
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VI.L16` — Basin Is Absorbing

## Immediate Comment / Docstring

```lean
/-- [VI.L16] Basin Is Absorbing Lemma: once entered, the system stays.
    SelfDesc closure (VI.T03) provides an internal evaluator that actively
    reconstructs the distinction after perturbation, making the basin absorbing.
    Proof: SelfDesc evaluator reads code and returns system to basin (VI.T03). -/
```

## Source Excerpt

```lean
structure BasinAbsorbing where
  /-- SelfDesc closure guarantees return. -/
  selfdesc_closure : Bool := true
  /-- Basin is absorbing (no escape under bounded perturbation). -/
  absorbing : Bool := true
  /-- Derived from VI.T03. -/
  derived_from_selfdesc : Bool := true
  /-- Scope: τ-effective. -/
  scope : String := "tau_effective"
  deriving Repr
```
