---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_parameter",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/spectral-parameter/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_parameter",
  "declaration_slug": "spectral-parameter",
  "kind": "def",
  "name": "spectral_parameter",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 39,
  "source_line_end": 41,
  "registry_ids": [
    "III.D29"
  ],
  "related_registry_items": [
    {
      "id": "III.D29",
      "title": "Spectral Parameter Λ(s)",
      "url": "/registry/object/III.D29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L39-L41",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralCorrespondence",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L39-L41",
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

- Module: [TauLib.BookIII.Doors.SpectralCorrespondence](/verify/taulib/docs/book-iii-doors-spectral-correspondence/)
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L39-L41)
- Source range: L39-L41
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D29` — Spectral Parameter Λ(s)

## Immediate Comment / Docstring

```lean
/-- [III.D29] Spectral parameter at finite level: maps a zeta index s
    to the corresponding eigenvalue mode. At primorial level k,
    Λ(s) = s mod (k+1), the mode within the k-level spectral window. -/
```

## Source Excerpt

```lean
def spectral_parameter (s k : TauIdx) : TauIdx :=
  if k == 0 then 0
  else s % (k + 1)
```
