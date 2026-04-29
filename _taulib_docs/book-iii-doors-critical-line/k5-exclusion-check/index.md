---
{
  "projection_kind": "taulib_declaration",
  "title": "k5_exclusion_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-critical-line/k5-exclusion-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.CriticalLine`.",
  "declaration_id": "TauLib.BookIII.Doors.CriticalLine::k5_exclusion_check",
  "declaration_slug": "k5-exclusion-check",
  "kind": "def",
  "name": "k5_exclusion_check",
  "module_name": "TauLib.BookIII.Doors.CriticalLine",
  "module_url": "/verify/taulib/docs/book-iii-doors-critical-line/",
  "source_line_start": 81,
  "source_line_end": 97,
  "registry_ids": [
    "III.P10"
  ],
  "related_registry_items": [
    {
      "id": "III.P10",
      "title": "K5 Off-Diagonal Exclusion",
      "url": "/registry/object/III.P10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L81-L97",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L81-L97",
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
- Source path: [`TauLib/BookIII/Doors/CriticalLine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/CriticalLine.lean#L81-L97)
- Source range: L81-L97
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P10` — K5 Off-Diagonal Exclusion

## Immediate Comment / Docstring

```lean
/-- [III.P10] K5 off-diagonal exclusion: at each primorial level k,
    the B-lobe and C-lobe eigenvalues have zero off-diagonal coupling.
    The crossing-point boundary conditions enforce real spectral flow. -/
```

## Source Excerpt

```lean
def k5_exclusion_check (bound db : TauIdx) : Bool :=
  go 1 1 ((bound + 1) * (db + 1))
where
  go (n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n > bound then true
    else if k > db then go (n + 1) 1 (fuel - 1)
    else
      -- Eigenvalue at mode n: real-valued (= n²) confirms no imaginary coupling
      let lambda := lemniscate_eigenvalue n
      let eigenval_real := lambda == n * n
      -- K5 off-diagonal exclusion: B and C sector products are coprime at depth k
      let b_prod := split_zeta_b k
      let c_prod := split_zeta_c k
      let sectors_coprime := Nat.gcd b_prod c_prod == 1
      eigenval_real && sectors_coprime && go n (k + 1) (fuel - 1)
  termination_by fuel
```
