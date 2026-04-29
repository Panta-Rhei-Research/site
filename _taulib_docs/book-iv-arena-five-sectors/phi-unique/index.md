---
{
  "projection_kind": "taulib_declaration",
  "title": "phi_unique",
  "permalink": "/verify/taulib/docs/book-iv-arena-five-sectors/phi-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Arena.FiveSectors`.",
  "declaration_id": "TauLib.BookIV.Arena.FiveSectors::phi_unique",
  "declaration_slug": "phi-unique",
  "kind": "theorem",
  "name": "phi_unique",
  "module_name": "TauLib.BookIV.Arena.FiveSectors",
  "module_url": "/verify/taulib/docs/book-iv-arena-five-sectors/",
  "source_line_start": 48,
  "source_line_end": 52,
  "registry_ids": [
    "IV.T98"
  ],
  "related_registry_items": [
    {
      "id": "IV.T98",
      "title": "Uniqueness of Phi",
      "url": "/registry/object/IV.T98/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L48-L52",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Arena.FiveSectors",
        "url": "/verify/taulib/docs/book-iv-arena-five-sectors/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L48-L52",
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

- Module: [TauLib.BookIV.Arena.FiveSectors](/verify/taulib/docs/book-iv-arena-five-sectors/)
- Source path: [`TauLib/BookIV/Arena/FiveSectors.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Arena/FiveSectors.lean#L48-L52)
- Source range: L48-L52
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T98` — Uniqueness of Phi

## Immediate Comment / Docstring

```lean
/-- [IV.T98] Φ is the unique polarity-preserving, depth-respecting assignment.
    Wraps assignment_unique from CoherenceKernel. -/
```

## Source Excerpt

```lean
theorem phi_unique (Psi : Generator → Sector)
    (h_pol : ∀ g, (sector_physics (Psi g)).polarity = gen_polarity g)
    (h_dep : ∀ g, (sector_physics (Psi g)).depth = gen_depth g) :
    ∀ g, Psi g = gen_sector_corr g :=
  assignment_unique Psi h_pol h_dep
```
