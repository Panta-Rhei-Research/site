---
{
  "projection_kind": "taulib_declaration",
  "title": "relaxation_plus_stability",
  "permalink": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/relaxation-plus-stability/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.GravityField.TauSchwarzschildScale`.",
  "declaration_id": "TauLib.BookV.GravityField.TauSchwarzschildScale::relaxation_plus_stability",
  "declaration_slug": "relaxation-plus-stability",
  "kind": "theorem",
  "name": "relaxation_plus_stability",
  "module_name": "TauLib.BookV.GravityField.TauSchwarzschildScale",
  "module_url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/",
  "source_line_start": 129,
  "source_line_end": 130,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L129-L130",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.GravityField.TauSchwarzschildScale",
        "url": "/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L129-L130",
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

- Module: [TauLib.BookV.GravityField.TauSchwarzschildScale](/verify/taulib/docs/book-v-gravity-field-tau-schwarzschild-scale/)
- Source path: [`TauLib/BookV/GravityField/TauSchwarzschildScale.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/GravityField/TauSchwarzschildScale.lean#L129-L130)
- Source range: L129-L130
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 2 relaxation modes + 3 stability conditions = 5 field modes. -/
```

## Source Excerpt

```lean
theorem relaxation_plus_stability :
    2 + 3 = (5 : Nat) := by omega
```
