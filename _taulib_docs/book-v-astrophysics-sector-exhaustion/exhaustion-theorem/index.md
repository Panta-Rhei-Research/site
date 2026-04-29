---
{
  "projection_kind": "taulib_declaration",
  "title": "exhaustion_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/exhaustion-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::exhaustion_theorem",
  "declaration_slug": "exhaustion-theorem",
  "kind": "theorem",
  "name": "exhaustion_theorem",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 158,
  "source_line_end": 160,
  "registry_ids": [
    "V.T99"
  ],
  "related_registry_items": [
    {
      "id": "V.T99",
      "title": "Sector Exhaustion Theorem",
      "url": "/registry/object/V.T99/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L158-L160",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L158-L160",
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L158-L160)
- Source range: L158-L160
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T99` — Sector Exhaustion Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T99] Exhaustion theorem: every astrophysical phenomenon in
    the catalog has a non-empty sector assignment.

    The 12-element catalog covers all known astrophysical phenomena.
    Each is assigned to one or more of the 5 sectors. No phenomenon
    is unassigned ("orphan"). -/
```

## Source Excerpt

```lean
theorem exhaustion_theorem :
    ∀ p : AstroPhenomenon, (primarySectors p).length > 0 :=
  sector_assignment
```
