---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_idempotent_supported",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/spectral-idempotent-supported/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.CentralTheorem.CentralTheorem`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.CentralTheorem::spectral_idempotent_supported",
  "declaration_slug": "spectral-idempotent-supported",
  "kind": "theorem",
  "name": "spectral_idempotent_supported",
  "module_name": "TauLib.BookII.CentralTheorem.CentralTheorem",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/",
  "source_line_start": 413,
  "source_line_end": 419,
  "registry_ids": [
    "II.D60"
  ],
  "related_registry_items": [
    {
      "id": "II.D60",
      "title": "Spectral Algebra",
      "url": "/registry/object/II.D60/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L413-L419",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.CentralTheorem",
        "url": "/verify/taulib/docs/book-ii-central-theorem-central-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L413-L419",
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

- Module: [TauLib.BookII.CentralTheorem.CentralTheorem](/verify/taulib/docs/book-ii-central-theorem-central-theorem/)
- Source path: [`TauLib/BookII/CentralTheorem/CentralTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/CentralTheorem.lean#L413-L419)
- Source range: L413-L419
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.D60` — Spectral Algebra

## Immediate Comment / Docstring

```lean
/-- [II.D60] Spectral algebra elements are always idempotent-supported.
    This is decompose_recovery applied pointwise. -/
```

## Source Excerpt

```lean
theorem spectral_idempotent_supported (sa : SpectralAlgebraElement) (x k : TauIdx) :
    let bp := sa.eval x k
    SectorPair.add
      (SectorPair.mul e_plus_sector bp)
      (SectorPair.mul e_minus_sector bp) = bp := by
  simp [SpectralAlgebraElement.eval, SectorPair.add, SectorPair.mul,
        e_plus_sector, e_minus_sector]
```
