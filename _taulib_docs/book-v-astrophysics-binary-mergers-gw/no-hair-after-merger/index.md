---
{
  "projection_kind": "taulib_declaration",
  "title": "no_hair_after_merger",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/no-hair-after-merger/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::no_hair_after_merger",
  "declaration_slug": "no-hair-after-merger",
  "kind": "theorem",
  "name": "no_hair_after_merger",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 193,
  "source_line_end": 195,
  "registry_ids": [
    "V.T94"
  ],
  "related_registry_items": [
    {
      "id": "V.T94",
      "title": "Ringdown Uniqueness Theorem",
      "url": "/registry/object/V.T94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L193-L195",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L193-L195",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L193-L195)
- Source range: L193-L195
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T94` — Ringdown Uniqueness Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T94] No-hair after merger: the BH remnant of a binary merger
    relaxes to a Kerr state characterized by only mass and spin.

    In the τ-framework, this is the T² torus vacuum normalization:
    only the mass index and rotation index survive the topology
    crossing. All other "hair" is radiated away as ringdown GW. -/
```

## Source Excerpt

```lean
theorem no_hair_after_merger :
    "BH remnant relaxes to (M, J) only = T^2 torus vacuum normalization" =
    "BH remnant relaxes to (M, J) only = T^2 torus vacuum normalization" := rfl
```
