---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_measure",
  "permalink": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/spectral-measure/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::spectral_measure",
  "declaration_slug": "spectral-measure",
  "kind": "def",
  "name": "spectral_measure",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 120,
  "source_line_end": 122,
  "registry_ids": [
    "III.D81"
  ],
  "related_registry_items": [
    {
      "id": "III.D81",
      "title": "Spectral Projector",
      "url": "/registry/object/III.D81/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L120-L122",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/corpus/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L120-L122",
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/corpus/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L120-L122)
- Source range: L120-L122
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `III.D81` — Spectral Projector

## Immediate Comment / Docstring

```lean
/-- [III.D81] Spectral measure: weight of eigenvalue λ_n = n² is 1/N.
    Total measure = N · (1/N) = 1. -/
```

## Source Excerpt

```lean
def spectral_measure (N : Nat) (n : Nat) : Bool :=
  -- Each mode has equal weight in the counting measure
  n < N
```
