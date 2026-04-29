---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_fun_independent",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/sector-fun-independent/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DHolomorphic::sector_fun_independent",
  "declaration_slug": "sector-fun-independent",
  "kind": "theorem",
  "name": "sector_fun_independent",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/",
  "source_line_start": 72,
  "source_line_end": 78,
  "registry_ids": [
    "I.P22"
  ],
  "related_registry_items": [
    {
      "id": "I.P22",
      "title": "Sector Independence",
      "url": "/registry/object/I.P22/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L72-L78",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-dholomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L72-L78",
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

- Module: [TauLib.BookI.Holomorphy.DHolomorphic](/verify/taulib/docs/book-i-holomorphy-dholomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L72-L78)
- Source range: L72-L78
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P22` — Sector Independence

## Immediate Comment / Docstring

```lean
/-- [I.P22] Every SectorFun is sector-independent by construction. -/
```

## Source Excerpt

```lean
theorem sector_fun_independent (sf : SectorFun) :
    is_sector_independent sf.apply := by
  intro s₁ s₂
  simp only [SectorFun.apply]
  constructor
  · intro hb; exact congrArg sf.g hb
  · intro hc; exact congrArg sf.h hc
```
