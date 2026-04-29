---
{
  "projection_kind": "taulib_declaration",
  "title": "NoVacuumCatastrophe",
  "permalink": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/no-vacuum-catastrophe/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.VacuumCatastrophe`.",
  "declaration_id": "TauLib.BookIV.Strong.VacuumCatastrophe::NoVacuumCatastrophe",
  "declaration_slug": "no-vacuum-catastrophe",
  "kind": "structure",
  "name": "NoVacuumCatastrophe",
  "module_name": "TauLib.BookIV.Strong.VacuumCatastrophe",
  "module_url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/",
  "source_line_start": 182,
  "source_line_end": 195,
  "registry_ids": [
    "IV.T78"
  ],
  "related_registry_items": [
    {
      "id": "IV.T78",
      "title": "No vacuum catastrophe in τ",
      "url": "/registry/object/IV.T78/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L182-L195",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.VacuumCatastrophe",
        "url": "/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L182-L195",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Strong.VacuumCatastrophe](/verify/taulib/docs/book-iv-strong-vacuum-catastrophe/)
- Source path: [`TauLib/BookIV/Strong/VacuumCatastrophe.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/VacuumCatastrophe.lean#L182-L195)
- Source range: L182-L195
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T78` — No vacuum catastrophe in τ

## Immediate Comment / Docstring

```lean
/-- [IV.T78] No vacuum catastrophe in tau: the tau-vacuum energy density
    rho_vac^(tau) = sum over {B,A,C,D} of eval(Delta^S_omega(Vac^*_S))
    is:
    1. FINITE (a stabilized boundary invariant)
    2. PARAMETER-FREE (no additive renormalization needed)
    3. SCALE-INDEPENDENT (same element of H_partial at all regimes)

    The orthodox catastrophe (10^120 mismatch) arises from assigning
    uncountably many unearned modes and then attempting to regulate the
    resulting divergence. In tau, finiteness is built in. -/
```

## Source Excerpt

```lean
structure NoVacuumCatastrophe where
  /-- Vacuum energy is finite. -/
  finite : Bool := true
  /-- No additive renormalization needed. -/
  parameter_free : Bool := true
  /-- Scale-independent. -/
  scale_independent : Bool := true
  /-- Sum over 4 primitive sectors. -/
  num_sectors_summed : Nat := 4
  /-- Orthodox mismatch (order of magnitude in exponent). -/
  orthodox_mismatch_exponent : Nat := 120
  /-- Tau: no mismatch by construction. -/
  tau_mismatch : String := "none (finite by construction)"
  deriving Repr
```
