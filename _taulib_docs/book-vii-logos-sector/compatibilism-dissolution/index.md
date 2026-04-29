---
{
  "projection_kind": "taulib_declaration",
  "title": "compatibilism_dissolution",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/compatibilism-dissolution/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::compatibilism_dissolution",
  "declaration_slug": "compatibilism-dissolution",
  "kind": "theorem",
  "name": "compatibilism_dissolution",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 249,
  "source_line_end": 252,
  "registry_ids": [
    "VII.P26"
  ],
  "related_registry_items": [
    {
      "id": "VII.P26",
      "title": "Compatibilism Dissolution",
      "url": "/registry/object/VII.P26/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L249-L252",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L249-L252",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L249-L252)
- Source range: L249-L252
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P26` — Compatibilism Dissolution

## Immediate Comment / Docstring

```lean
/-- [VII.P26] Compatibilism Dissolution (ch113). The free will debate
    dissolves: at the micro scale (single address), determinism holds
    (Boolean logic); at the macro scale (multiple addresses), branching
    is real. The apparent conflict is a scale confusion. -/
```

## Source Excerpt

```lean
theorem compatibilism_dissolution :
    mind_topos.topos_structure = true ∧
    mind_topos.has_exponentials = true :=
  ⟨rfl, rfl⟩
```
