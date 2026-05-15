---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_gap_check",
  "permalink": "/corpus/taulib/docs/book-iii-doors-lemniscate-operator/spectral-gap-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::spectral_gap_check",
  "declaration_slug": "spectral-gap-check",
  "kind": "def",
  "name": "spectral_gap_check",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/corpus/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 134,
  "source_line_end": 135,
  "registry_ids": [
    "III.P09"
  ],
  "related_registry_items": [
    {
      "id": "III.P09",
      "title": "Discrete Spectrum of H_L",
      "url": "/registry/object/III.P09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L134-L135",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.LemniscateOperator",
        "url": "/corpus/taulib/docs/book-iii-doors-lemniscate-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L134-L135",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/corpus/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L134-L135)
- Source range: L134-L135
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.P09` — Discrete Spectrum of H_L

## Immediate Comment / Docstring

```lean
/-- [III.P09] Spectral gap: λ₁ > 0 (first nonzero eigenvalue). -/
```

## Source Excerpt

```lean
def spectral_gap_check : Bool :=
  lemniscate_eigenvalue 1 > lemniscate_eigenvalue 0
```
