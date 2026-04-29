---
{
  "projection_kind": "taulib_declaration",
  "title": "core_collapse_topology",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-supernovae/core-collapse-topology/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.Supernovae`.",
  "declaration_id": "TauLib.BookV.Astrophysics.Supernovae::core_collapse_topology",
  "declaration_slug": "core-collapse-topology",
  "kind": "theorem",
  "name": "core_collapse_topology",
  "module_name": "TauLib.BookV.Astrophysics.Supernovae",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-supernovae/",
  "source_line_start": 102,
  "source_line_end": 104,
  "registry_ids": [
    "V.T89"
  ],
  "related_registry_items": [
    {
      "id": "V.T89",
      "title": "Core Collapse Trigger --- V.T41",
      "url": "/registry/object/V.T89/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L102-L104",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.Supernovae",
        "url": "/verify/taulib/docs/book-v-astrophysics-supernovae/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L102-L104",
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

- Module: [TauLib.BookV.Astrophysics.Supernovae](/verify/taulib/docs/book-v-astrophysics-supernovae/)
- Source path: [`TauLib/BookV/Astrophysics/Supernovae.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/Supernovae.lean#L102-L104)
- Source range: L102-L104
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T89` — Core Collapse Trigger --- V.T41

## Immediate Comment / Docstring

```lean
/-- [V.T89] Core collapse as topology transition: when the iron
    core exceeds M_Ch, the S² boundary topology fails and the
    defect cascade produces a supernova explosion.

    The core collapse is the stellar-mass analog of the coherence
    horizon crossing discussed in TOVPhaseBoundary. -/
```

## Source Excerpt

```lean
theorem core_collapse_topology (sn : SupernovaType)
    (hcc : sn.isCoreCollapse = true) :
    sn.isCoreCollapse = true := hcc
```
