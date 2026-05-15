---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_extension_c",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-thinness/crt-extension-c/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.Thinness`.",
  "declaration_id": "TauLib.BookI.Holomorphy.Thinness::crt_extension_c",
  "declaration_slug": "crt-extension-c",
  "kind": "theorem",
  "name": "crt_extension_c",
  "module_name": "TauLib.BookI.Holomorphy.Thinness",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-thinness/",
  "source_line_start": 93,
  "source_line_end": 96,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L93-L96",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.Thinness",
        "url": "/corpus/taulib/docs/book-i-holomorphy-thinness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L93-L96",
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

- Module: [TauLib.BookI.Holomorphy.Thinness](/corpus/taulib/docs/book-i-holomorphy-thinness/)
- Source path: [`TauLib/BookI/Holomorphy/Thinness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/Thinness.lean#L93-L96)
- Source range: L93-L96
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT extension for C-sector. -/
```

## Source Excerpt

```lean
theorem crt_extension_c (f : StageFun) (hcoh : TowerCoherent f)
    (n k l : TauIdx) (hkl : k ≤ l) :
    reduce (f.c_fun n l) k = f.c_fun n k :=
  hcoh.2 n k l hkl
```
