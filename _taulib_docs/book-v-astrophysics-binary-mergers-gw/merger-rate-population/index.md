---
{
  "projection_kind": "taulib_declaration",
  "title": "merger_rate_population",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/merger-rate-population/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::merger_rate_population",
  "declaration_slug": "merger-rate-population",
  "kind": "theorem",
  "name": "merger_rate_population",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 231,
  "source_line_end": 233,
  "registry_ids": [
    "V.P81"
  ],
  "related_registry_items": [
    {
      "id": "V.P81",
      "title": "Merger Graviton Count",
      "url": "/registry/object/V.P81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L231-L233",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L231-L233",
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
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L231-L233)
- Source range: L231-L233
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P81` — Merger Graviton Count

## Immediate Comment / Docstring

```lean
/-- [V.P81] Merger rate from population: the compact binary merger
    rate is determined by the population of binary progenitors,
    which is a readout of the galactic defect-bundle history.

    Current estimates (LIGO O3):
    - BH-BH: ~24 Gpc⁻³ yr⁻¹
    - NS-NS: ~13-1900 Gpc⁻³ yr⁻¹
    - BH-NS: ~8-140 Gpc⁻³ yr⁻¹ -/
```

## Source Excerpt

```lean
theorem merger_rate_population :
    "Merger rate = f(binary population) = galactic defect-bundle history readout" =
    "Merger rate = f(binary population) = galactic defect-bundle history readout" := rfl
```
