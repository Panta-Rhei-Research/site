---
{
  "projection_kind": "taulib_declaration",
  "title": "no_explosion_at_boundaries",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/no-explosion-at-boundaries/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::no_explosion_at_boundaries",
  "declaration_slug": "no-explosion-at-boundaries",
  "kind": "theorem",
  "name": "no_explosion_at_boundaries",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 883,
  "source_line_end": 887,
  "registry_ids": [
    "VII.T29"
  ],
  "related_registry_items": [
    {
      "id": "VII.T29",
      "title": "No-Explosion at Boundaries",
      "url": "/registry/object/VII.T29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L883-L887",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L883-L887",
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
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L883-L887)
- Source range: L883-L887
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T29` — No-Explosion at Boundaries

## Immediate Comment / Docstring

```lean
/-- [VII.T29] No-Explosion at Boundaries (ch44). At register
    boundaries, the logic is paraconsistent: φ ∧ ¬φ does not
    entail arbitrary ψ. The monodromy around the crossing point
    prevents global trivialization. -/
```

## Source Excerpt

```lean
theorem no_explosion_at_boundaries :
    paraconsistent.controlled_contradiction = true ∧
    paraconsistent.no_explosion = true ∧
    paraconsistent.crossing_point_site = true :=
  ⟨rfl, rfl, rfl⟩
```
