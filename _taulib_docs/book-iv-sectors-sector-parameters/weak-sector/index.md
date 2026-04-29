---
{
  "projection_kind": "taulib_declaration",
  "title": "weak_sector",
  "permalink": "/verify/taulib/docs/book-iv-sectors-sector-parameters/weak-sector/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Sectors.SectorParameters`.",
  "declaration_id": "TauLib.BookIV.Sectors.SectorParameters::weak_sector",
  "declaration_slug": "weak-sector",
  "kind": "def",
  "name": "weak_sector",
  "module_name": "TauLib.BookIV.Sectors.SectorParameters",
  "module_url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/",
  "source_line_start": 186,
  "source_line_end": 193,
  "registry_ids": [
    "IV.D06"
  ],
  "related_registry_items": [
    {
      "id": "IV.D06",
      "title": "Weak Sector at E₁",
      "url": "/registry/object/IV.D06/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L186-L193",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Sectors.SectorParameters",
        "url": "/verify/taulib/docs/book-iv-sectors-sector-parameters/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L186-L193",
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

- Module: [TauLib.BookIV.Sectors.SectorParameters](/verify/taulib/docs/book-iv-sectors-sector-parameters/)
- Source path: [`TauLib/BookIV/Sectors/SectorParameters.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Sectors/SectorParameters.lean#L186-L193)
- Source range: L186-L193
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D06` — Weak Sector at E₁

## Immediate Comment / Docstring

```lean
/-- [IV.D06] **Weak Sector (A)**: π-generator, weak force.
    Self-coupling κ(A;1) = ι_τ.
    Polarity: balanced (unique sector with pol = 1).
    Depth: 1 (first primorial level).
    Physical: temporal arrow, parity violation, beta decay.
    The master constant ι_τ itself IS the weak self-coupling. -/
```

## Source Excerpt

```lean
def weak_sector : SectorPhysics where
  sector := .A
  generator := .pi
  depth := 1
  polarity := .Balanced
  coupling_numer := iota                      -- ι_τ numerator = 341304
  coupling_denom := iotaD                     -- denominator = 10⁶
  denom_pos := by simp [iotaD, iota_tau_denom]
```
