---
{
  "projection_kind": "taulib_declaration",
  "title": "ads_cft_echo",
  "permalink": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/ads-cft-echo/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Orthodox.EmergentGeometry`.",
  "declaration_id": "TauLib.BookV.Orthodox.EmergentGeometry::ads_cft_echo",
  "declaration_slug": "ads-cft-echo",
  "kind": "theorem",
  "name": "ads_cft_echo",
  "module_name": "TauLib.BookV.Orthodox.EmergentGeometry",
  "module_url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/",
  "source_line_start": 260,
  "source_line_end": 262,
  "registry_ids": [
    "V.R274"
  ],
  "related_registry_items": [
    {
      "id": "V.R274",
      "title": "AdS/CFT as a partial echo",
      "url": "/registry/object/V.R274/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L260-L262",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Orthodox.EmergentGeometry",
        "url": "/verify/taulib/docs/book-v-orthodox-emergent-geometry/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L260-L262",
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

- Module: [TauLib.BookV.Orthodox.EmergentGeometry](/verify/taulib/docs/book-v-orthodox-emergent-geometry/)
- Source path: [`TauLib/BookV/Orthodox/EmergentGeometry.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Orthodox/EmergentGeometry.lean#L260-L262)
- Source range: L260-L262
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.R274` — AdS/CFT as a partial echo

## Immediate Comment / Docstring

```lean
/-- [V.R274] AdS/CFT as a partial echo of native holography.
    Maldacena's conjecture captures the boundary-bulk correspondence
    but requires (a) negative Lambda, (b) supersymmetry, (c) large N.
    tau's holography needs none of these. -/
```

## Source Excerpt

```lean
theorem ads_cft_echo :
    "AdS/CFT = partial echo: needs Lambda < 0, SUSY, large N; tau needs none" =
    "AdS/CFT = partial echo: needs Lambda < 0, SUSY, large N; tau needs none" := rfl
```
