---
{
  "projection_kind": "taulib_declaration",
  "title": "c_covers_nuclear",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/c-covers-nuclear/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::c_covers_nuclear",
  "declaration_slug": "c-covers-nuclear",
  "kind": "theorem",
  "name": "c_covers_nuclear",
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 190,
  "source_line_end": 192,
  "registry_ids": [
    "V.C16"
  ],
  "related_registry_items": [
    {
      "id": "V.C16",
      "title": "No Fifth Force",
      "url": "/registry/object/V.C16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L190-L192",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L190-L192",
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
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L190-L192)
- Source range: L190-L192
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `V.C16` — No Fifth Force

## Immediate Comment / Docstring

```lean
/-- [V.C16] C-sector covers all nuclear phenomena. -/
```

## Source Excerpt

```lean
theorem c_covers_nuclear :
    SectorLabel.C ∈ primarySectors .NuclearReactions := by
  simp [primarySectors]
```
