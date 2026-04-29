---
{
  "projection_kind": "taulib_declaration",
  "title": "self_recognition_e3",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/self-recognition-e3/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::self_recognition_e3",
  "declaration_slug": "self-recognition-e3",
  "kind": "theorem",
  "name": "self_recognition_e3",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 223,
  "source_line_end": 226,
  "registry_ids": [
    "VII.T42"
  ],
  "related_registry_items": [
    {
      "id": "VII.T42",
      "title": "Self-Recognition as E₃ Operator",
      "url": "/registry/object/VII.T42/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L223-L226",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L223-L226",
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
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L223-L226)
- Source range: L223-L226
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T42` — Self-Recognition as E₃ Operator

## Immediate Comment / Docstring

```lean
/-- [VII.T42] Self-Recognition as E₃ Operator (ch112). Self-recognition
    = the MetaDecode operator applied reflexively: the system recognizes
    itself as the system that recognizes. This is SelfDesc² at the
    phenomenological level. -/
```

## Source Excerpt

```lean
theorem self_recognition_e3 :
    mind_topos.topos_structure = true ∧
    mind_topos.has_internal_logic = true :=
  ⟨rfl, rfl⟩
```
