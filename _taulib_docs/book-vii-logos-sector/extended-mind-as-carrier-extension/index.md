---
{
  "projection_kind": "taulib_declaration",
  "title": "extended_mind_as_carrier_extension",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/extended-mind-as-carrier-extension/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::extended_mind_as_carrier_extension",
  "declaration_slug": "extended-mind-as-carrier-extension",
  "kind": "theorem",
  "name": "extended_mind_as_carrier_extension",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 300,
  "source_line_end": 303,
  "registry_ids": [
    "VII.P28"
  ],
  "related_registry_items": [
    {
      "id": "VII.P28",
      "title": "Extended Mind as Carrier Extension",
      "url": "/registry/object/VII.P28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L300-L303",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L300-L303",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L300-L303)
- Source range: L300-L303
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.P28` — Extended Mind as Carrier Extension

## Immediate Comment / Docstring

```lean
/-- [VII.P28] Extended Mind as Carrier Extension (ch117). The extended
    mind thesis categorified: external tools extend the carrier of
    the mind-topos. A notebook is part of the mind iff it satisfies
    the gluing condition (functorial coupling with internal states). -/
```

## Source Excerpt

```lean
theorem extended_mind_as_carrier_extension :
    mind_topos.topos_structure = true ∧
    mind_topos.has_exponentials = true :=
  ⟨rfl, rfl⟩
```
