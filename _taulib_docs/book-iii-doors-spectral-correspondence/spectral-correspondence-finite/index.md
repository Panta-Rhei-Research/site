---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_correspondence_finite",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/spectral-correspondence-finite/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_correspondence_finite",
  "declaration_slug": "spectral-correspondence-finite",
  "kind": "def",
  "name": "spectral_correspondence_finite",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 85,
  "source_line_end": 95,
  "registry_ids": [
    "III.T18"
  ],
  "related_registry_items": [
    {
      "id": "III.T18",
      "title": "Spectral Correspondence Theorem",
      "url": "/registry/object/III.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L85-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L85-L95",
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
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L85-L95)
- Source range: L85-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T18` — Spectral Correspondence Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T18] Finite-level spectral correspondence: at level k,
    each zeta index s maps to a mode whose eigenvalue is consistent
    with the spectral structure of H_{≤k}. -/
```

## Source Excerpt

```lean
def spectral_correspondence_finite (k : TauIdx) : Bool :=
  go 0 (k + 1)
where
  go (s fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if s > k then true
    else
      let mode := spectral_parameter s k
      let eigenval := lemniscate_eigenvalue mode
      mode <= k && eigenval == mode * mode && go (s + 1) (fuel - 1)
  termination_by fuel
```
