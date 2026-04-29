---
{
  "projection_kind": "taulib_declaration",
  "title": "rh_internal_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-bridge-tightening/rh-internal-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.BridgeTightening`.",
  "declaration_id": "TauLib.BookIII.Doors.BridgeTightening::rh_internal_check",
  "declaration_slug": "rh-internal-check",
  "kind": "def",
  "name": "rh_internal_check",
  "module_name": "TauLib.BookIII.Doors.BridgeTightening",
  "module_url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/",
  "source_line_start": 62,
  "source_line_end": 69,
  "registry_ids": [
    "III.D93"
  ],
  "related_registry_items": [
    {
      "id": "III.D93",
      "title": "RH Spectral Gap Characterization",
      "url": "/registry/object/III.D93/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L62-L69",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.BridgeTightening",
        "url": "/verify/taulib/docs/book-iii-doors-bridge-tightening/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L62-L69",
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

- Module: [TauLib.BookIII.Doors.BridgeTightening](/verify/taulib/docs/book-iii-doors-bridge-tightening/)
- Source path: [`TauLib/BookIII/Doors/BridgeTightening.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/BridgeTightening.lean#L62-L69)
- Source range: L62-L69
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D93` — RH Spectral Gap Characterization

## Immediate Comment / Docstring

```lean
/-- [III.D93] RH internal check at stage k: self-adjointness +
    eigenvalue ordering + spectral gap. All pass at finite stages. -/
```

## Source Excerpt

```lean
def rh_internal_check (k : Nat) : Bool :=
  -- Self-adjoint: eigenvalues n² are real and non-negative
  let sa := self_adjoint_check k
  -- Spectral gap: λ₁ > λ₀
  let gap := lemniscate_eigenvalue 1 > lemniscate_eigenvalue 0
  -- Eigenvalue nesting: eigenvalues at stage k are consistent
  let nest := discrete_spectrum_check k
  sa && gap && nest
```
