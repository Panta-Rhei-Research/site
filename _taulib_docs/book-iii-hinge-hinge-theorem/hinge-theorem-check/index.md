---
{
  "projection_kind": "taulib_declaration",
  "title": "hinge_theorem_check",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/hinge-theorem-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::hinge_theorem_check",
  "declaration_slug": "hinge-theorem-check",
  "kind": "def",
  "name": "hinge_theorem_check",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 175,
  "source_line_end": 183,
  "registry_ids": [
    "III.T41"
  ],
  "related_registry_items": [
    {
      "id": "III.T41",
      "title": "Hinge Theorem",
      "url": "/registry/object/III.T41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L175-L183",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L175-L183",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L175-L183)
- Source range: L175-L183
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T41` — Hinge Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T41] Hinge theorem check: sector instantiation + level coherence +
    enrichment determines sectors + dependency chain valid. -/
```

## Source Excerpt

```lean
def hinge_theorem_check (bound db : TauIdx) : Bool :=
  -- The dependency chain is valid
  dependency_chain_check bound db &&
  -- Sector instantiation at each level
  sector_instantiation_check bound db &&
  -- Level coherence across depths
  level_coherence_check db &&
  -- Enrichment determines sector assignments
  enrichment_determines_sectors bound db
```
