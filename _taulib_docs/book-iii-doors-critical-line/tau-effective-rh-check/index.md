---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_effective_rh_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/tau-effective-rh-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::tau_effective_rh_check",
  "declaration_slug": "tau-effective-rh-check",
  "kind": "def",
  "name": "tau_effective_rh_check",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 106,
  "source_line_end": 120,
  "registry_ids": [
    "III.D30"
  ],
  "related_registry_items": [
    {
      "id": "III.D30",
      "title": "τ-Effective RH Statement",
      "url": "/registry/object/III.D30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L106-L120",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L106-L120",
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
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L106-L120)
- Source range: L106-L120
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D30` — τ-Effective RH Statement

## Immediate Comment / Docstring

```lean
/-- [III.D30] τ-Effective RH: for each primorial depth k, the finite-cutoff
    operator H_{≤k} has only real eigenvalues, and the finite zeta
    has the correct zero structure. A computable predicate. -/
```

## Source Excerpt

```lean
def tau_effective_rh_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      -- Step 1: eigenvalues are real (n² for all modes ≤ k)
      let eigenvalues_real := self_adjoint_check k
      -- Step 2: spectral correspondence holds at this level
      let corr_ok := spectral_correspondence_finite k
      -- Step 3: Euler product factorization is consistent
      let euler_ok := split_zeta_check k
      eigenvalues_real && corr_ok && euler_ok && go (k + 1) (fuel - 1)
  termination_by fuel
```
