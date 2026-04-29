---
{
  "projection_kind": "taulib_declaration",
  "title": "eigenvalue_nesting_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/eigenvalue-nesting-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::eigenvalue_nesting_check",
  "declaration_slug": "eigenvalue-nesting-check",
  "kind": "def",
  "name": "eigenvalue_nesting_check",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 65,
  "source_line_end": 76,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L65-L76",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L65-L76",
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
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L65-L76)
- Source range: L65-L76
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D29` — Spectral Parameter Λ(s)

## Immediate Comment / Docstring

```lean
/-- [III.D29] Eigenvalue tower nesting: eigenvalues at depth k are a
    subset of eigenvalues at depth k+1 (the n² sequence is independent
    of depth, so the spectrum at level k is included in level k+1). -/
```

## Source Excerpt

```lean
def eigenvalue_nesting_check (db : TauIdx) : Bool :=
  go 0 1 ((db + 1) * (db + 1))
where
  go (n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else if n > k then go 0 (k + 1) (fuel - 1)
    else
      -- Eigenvalue at mode n matches definition (n² independent of depth)
      let same := lemniscate_eigenvalue n == n * n
      same && go (n + 1) k (fuel - 1)
  termination_by fuel
```
