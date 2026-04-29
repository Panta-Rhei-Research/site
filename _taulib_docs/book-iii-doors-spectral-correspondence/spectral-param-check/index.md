---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_param_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/spectral-param-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_param_check",
  "declaration_slug": "spectral-param-check",
  "kind": "def",
  "name": "spectral_param_check",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 45,
  "source_line_end": 60,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L45-L60",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L45-L60",
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
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L45-L60)
- Source range: L45-L60
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D29` — Spectral Parameter Λ(s)

## Immediate Comment / Docstring

```lean
/-- [III.D29] Spectral parameter check: Λ maps valid indices to valid
    eigenvalues at each level. -/
```

## Source Excerpt

```lean
def spectral_param_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (s k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if s > bound then true
    else if k > db then go (s + 1) 1 (fuel - 1)
    else
      let mode := spectral_parameter s k
      -- Mode is within the spectral window
      let ok := mode <= k
      -- Eigenvalue at this mode is well-defined
      let eigenval := lemniscate_eigenvalue mode
      let eigenval_ok := eigenval == mode * mode
      ok && eigenval_ok && go s (k + 1) (fuel - 1)
  termination_by fuel
```
