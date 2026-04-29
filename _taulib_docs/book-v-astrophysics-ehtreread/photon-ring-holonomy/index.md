---
{
  "projection_kind": "taulib_declaration",
  "title": "photon_ring_holonomy",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-ehtreread/photon-ring-holonomy/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.EHTReread`.",
  "declaration_id": "TauLib.BookV.Astrophysics.EHTReread::photon_ring_holonomy",
  "declaration_slug": "photon-ring-holonomy",
  "kind": "theorem",
  "name": "photon_ring_holonomy",
  "module_name": "TauLib.BookV.Astrophysics.EHTReread",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/",
  "source_line_start": 136,
  "source_line_end": 138,
  "registry_ids": [
    "V.P82"
  ],
  "related_registry_items": [
    {
      "id": "V.P82",
      "title": "Inner Shadow Ellipticity",
      "url": "/registry/object/V.P82/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L136-L138",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.EHTReread",
        "url": "/verify/taulib/docs/book-v-astrophysics-ehtreread/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L136-L138",
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

- Module: [TauLib.BookV.Astrophysics.EHTReread](/verify/taulib/docs/book-v-astrophysics-ehtreread/)
- Source path: [`TauLib/BookV/Astrophysics/EHTReread.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/EHTReread.lean#L136-L138)
- Source range: L136-L138
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P82` — Inner Shadow Ellipticity

## Immediate Comment / Docstring

```lean
/-- [V.P82] Photon ring from holonomy: the photon ring (bright ring
    in the EHT image) is produced by photons that complete one or
    more holonomy loops around the torus vacuum before escaping.

    Each successive sub-ring (n = 1, 2, 3, ...) corresponds to
    one additional holonomy loop, with exponentially decreasing
    brightness and exponentially narrowing width. -/
```

## Source Excerpt

```lean
theorem photon_ring_holonomy :
    "Photon ring = successive holonomy loops around T^2 torus vacuum" =
    "Photon ring = successive holonomy loops around T^2 torus vacuum" := rfl
```
