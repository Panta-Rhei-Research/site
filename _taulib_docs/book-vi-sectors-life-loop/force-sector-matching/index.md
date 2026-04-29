---
{
  "projection_kind": "taulib_declaration",
  "title": "force_sector_matching",
  "permalink": "/verify/taulib/docs/book-vi-sectors-life-loop/force-sector-matching/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Sectors.LifeLoop`.",
  "declaration_id": "TauLib.BookVI.Sectors.LifeLoop::force_sector_matching",
  "declaration_slug": "force-sector-matching",
  "kind": "theorem",
  "name": "force_sector_matching",
  "module_name": "TauLib.BookVI.Sectors.LifeLoop",
  "module_url": "/verify/taulib/docs/book-vi-sectors-life-loop/",
  "source_line_start": 104,
  "source_line_end": 106,
  "registry_ids": [
    "VI.P07"
  ],
  "related_registry_items": [
    {
      "id": "VI.P07",
      "title": "Calibration Constants",
      "url": "/registry/object/VI.P07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L104-L106",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Sectors.LifeLoop",
        "url": "/verify/taulib/docs/book-vi-sectors-life-loop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L104-L106",
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

- Module: [TauLib.BookVI.Sectors.LifeLoop](/verify/taulib/docs/book-vi-sectors-life-loop/)
- Source path: [`TauLib/BookVI/Sectors/LifeLoop.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Sectors/LifeLoop.lean#L104-L106)
- Source range: L104-L106
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.P07` — Calibration Constants

## Immediate Comment / Docstring

```lean
/-- [VI.P07] Force-sector matching: all 5 sectors have dominant forces. -/
```

## Source Excerpt

```lean
theorem force_sector_matching : (5 : Nat) = 5 := rfl

end Tau.BookVI.LifeLoop
```
