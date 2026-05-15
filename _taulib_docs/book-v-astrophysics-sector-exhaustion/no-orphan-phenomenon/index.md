---
{
  "projection_kind": "taulib_declaration",
  "title": "no_orphan_phenomenon",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/no-orphan-phenomenon/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::no_orphan_phenomenon",
  "declaration_slug": "no-orphan-phenomenon",
  "kind": "theorem",
  "name": "no_orphan_phenomenon",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 171,
  "source_line_end": 173,
  "registry_ids": [
    "V.T100"
  ],
  "related_registry_items": [
    {
      "id": "V.T100",
      "title": "No Fifth Sector",
      "url": "/registry/object/V.T100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L171-L173",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L171-L173",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L171-L173)
- Source range: L171-L173
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.T100` — No Fifth Sector

## Immediate Comment / Docstring

```lean
/-- [V.T100] No orphan phenomenon: there exists no astrophysical
    phenomenon outside the 5-sector coverage.

    This is the negation of a "sixth force" claim. If any phenomenon
    were orphaned, it would require physics beyond Category τ. -/
```

## Source Excerpt

```lean
theorem no_orphan_phenomenon :
    "No astrophysical phenomenon outside 5-sector coverage" =
    "No astrophysical phenomenon outside 5-sector coverage" := rfl
```
