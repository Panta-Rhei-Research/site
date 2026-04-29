---
{
  "projection_kind": "taulib_declaration",
  "title": "critical_line_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/critical-line-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::critical_line_check",
  "declaration_slug": "critical-line-check",
  "kind": "def",
  "name": "critical_line_check",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 47,
  "source_line_end": 61,
  "registry_ids": [
    "III.T19"
  ],
  "related_registry_items": [
    {
      "id": "III.T19",
      "title": "Critical Line Theorem",
      "url": "/registry/object/III.T19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L47-L61",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.CriticalLine",
        "url": "/verify/taulib/docs/book-iii-doors-critical-line/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L47-L61",
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

- Module: [TauLib.BookIII.Doors.CriticalLine](/verify/taulib/docs/book-iii-doors-critical-line/)
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L47-L61)
- Source range: L47-L61
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T19` — Critical Line Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T19] Critical line check at level k: all spectral modes have
    real eigenvalues (= natural numbers) and the spectral correspondence
    maps them consistently. Combines self-adjointness + O3. -/
```

## Source Excerpt

```lean
def critical_line_check (k : TauIdx) : Bool :=
  go 0 (k + 1)
where
  go (n fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > k then true
    else
      -- Self-adjointness: eigenvalue is real (n², always real for Nat)
      let lambda := lemniscate_eigenvalue n
      let is_real := lambda == n * n
      -- Spectral correspondence: mode maps within window
      let mode := spectral_parameter n k
      let in_window := mode <= k
      is_real && in_window && go (n + 1) (fuel - 1)
  termination_by fuel
```
