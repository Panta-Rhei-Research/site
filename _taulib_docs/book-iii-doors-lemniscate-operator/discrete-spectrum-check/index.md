---
{
  "projection_kind": "taulib_declaration",
  "title": "discrete_spectrum_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/discrete-spectrum-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.LemniscateOperator`.",
  "declaration_id": "TauLib.BookIII.Doors.LemniscateOperator::discrete_spectrum_check",
  "declaration_slug": "discrete-spectrum-check",
  "kind": "def",
  "name": "discrete_spectrum_check",
  "module_name": "TauLib.BookIII.Doors.LemniscateOperator",
  "module_url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/",
  "source_line_start": 121,
  "source_line_end": 131,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L121-L131",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.LemniscateOperator",
        "url": "/verify/taulib/docs/book-iii-doors-lemniscate-operator/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L121-L131",
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

- Module: [TauLib.BookIII.Doors.LemniscateOperator](/verify/taulib/docs/book-iii-doors-lemniscate-operator/)
- Source path: [`TauLib/BookIII/Doors/LemniscateOperator.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/LemniscateOperator.lean#L121-L131)
- Source range: L121-L131
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P09` — Discrete Spectrum of H_L

## Immediate Comment / Docstring

```lean
/-- [III.P09] Discrete spectrum: eigenvalues form a strictly increasing
    unbounded sequence. -/
```

## Source Excerpt

```lean
def discrete_spectrum_check (bound : TauIdx) : Bool :=
  go 1 bound
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n >= bound then true
    else
      let increasing := lemniscate_eigenvalue (n + 1) > lemniscate_eigenvalue n
      let unbounded := lemniscate_eigenvalue n >= n * n
      increasing && unbounded && go (n + 1) (fuel - 1)
  termination_by fuel
```
