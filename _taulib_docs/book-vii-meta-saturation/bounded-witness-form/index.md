---
{
  "projection_kind": "taulib_declaration",
  "title": "BoundedWitnessForm",
  "permalink": "/verify/taulib/docs/book-vii-meta-saturation/bounded-witness-form/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::BoundedWitnessForm",
  "declaration_slug": "bounded-witness-form",
  "kind": "structure",
  "name": "BoundedWitnessForm",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/verify/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 372,
  "source_line_end": 379,
  "registry_ids": [
    "VII.D15"
  ],
  "related_registry_items": [
    {
      "id": "VII.D15",
      "title": "Bounded Witness Form",
      "url": "/registry/object/VII.D15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L372-L379",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/verify/taulib/docs/book-vii-meta-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L372-L379",
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

- Module: [TauLib.BookVII.Meta.Saturation](/verify/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L372-L379)
- Source range: L372-L379
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D15` — Bounded Witness Form

## Immediate Comment / Docstring

```lean
/-- [VII.D15] Bounded Witness Form (BWF): claim φ has a finite τ-finite witness w
    with NF-address, certifying φ, terminating in finitely many kernel-axiom steps.
    Key constraint: excludes unbounded quantification. -/
```

## Source Excerpt

```lean
structure BoundedWitnessForm where
  /-- Witness is τ-finite. -/
  tau_finite : Bool := true
  /-- Witness has NF-address. -/
  nf_addressed : Bool := true
  /-- Terminates in finitely many steps. -/
  finitely_terminating : Bool := true
  deriving Repr
```
