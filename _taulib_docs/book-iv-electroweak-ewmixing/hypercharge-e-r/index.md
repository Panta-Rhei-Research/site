---
{
  "projection_kind": "taulib_declaration",
  "title": "hypercharge_eR",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/hypercharge-e-r/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::hypercharge_eR",
  "declaration_slug": "hypercharge-e-r",
  "kind": "def",
  "name": "hypercharge_eR",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 85,
  "source_line_end": 88,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L85-L88",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L85-L88",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L85-L88)
- Source range: L85-L88
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Right-handed electron singlet: Y = -2. -/
```

## Source Excerpt

```lean
def hypercharge_eR : Hypercharge where
  label := "e_R"
  y_numer := -2
  y_denom := 1
```
