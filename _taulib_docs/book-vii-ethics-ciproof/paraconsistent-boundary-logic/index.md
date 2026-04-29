---
{
  "projection_kind": "taulib_declaration",
  "title": "ParaconsistentBoundaryLogic",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/paraconsistent-boundary-logic/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::ParaconsistentBoundaryLogic",
  "declaration_slug": "paraconsistent-boundary-logic",
  "kind": "structure",
  "name": "ParaconsistentBoundaryLogic",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 864,
  "source_line_end": 871,
  "registry_ids": [
    "VII.D64"
  ],
  "related_registry_items": [
    {
      "id": "VII.D64",
      "title": "Paraconsistent Boundary Logic",
      "url": "/registry/object/VII.D64/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L864-L871",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L864-L871",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L864-L871)
- Source range: L864-L871
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D64` — Paraconsistent Boundary Logic

## Immediate Comment / Docstring

```lean
/-- [VII.D64] Paraconsistent Boundary Logic (ch44). At register
    boundaries (sector crossings), controlled contradiction is
    possible: φ ∧ ¬φ can hold locally without global explosion.
    The lemniscate crossing point p₀ is the canonical site. -/
```

## Source Excerpt

```lean
structure ParaconsistentBoundaryLogic where
  /-- Controlled contradiction at boundaries. -/
  controlled_contradiction : Bool := true
  /-- No global explosion. -/
  no_explosion : Bool := true
  /-- Canonical site: crossing point p₀. -/
  crossing_point_site : Bool := true
  deriving Repr
```
