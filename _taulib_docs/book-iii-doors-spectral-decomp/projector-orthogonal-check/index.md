---
{
  "projection_kind": "taulib_declaration",
  "title": "projector_orthogonal_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-decomp/projector-orthogonal-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::projector_orthogonal_check",
  "declaration_slug": "projector-orthogonal-check",
  "kind": "def",
  "name": "projector_orthogonal_check",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 85,
  "source_line_end": 108,
  "registry_ids": [
    "III.D80"
  ],
  "related_registry_items": [
    {
      "id": "III.D80",
      "title": "q-Expansion Coefficients",
      "url": "/registry/object/III.D80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L85-L108",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralDecomp",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L85-L108",
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

- Module: [TauLib.BookIII.Doors.SpectralDecomp](/verify/taulib/docs/book-iii-doors-spectral-decomp/)
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L85-L108)
- Source range: L85-L108
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] Check projectors are orthogonal: P_n · P_m = 0 for n ≠ m. -/
```

## Source Excerpt

```lean
def projector_orthogonal_check (N : Nat) : Bool :=
  go_n 0 N N
where
  go_n (n bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n >= bound then true
    else go_m n 0 bound bound && go_n (n + 1) bound (fuel - 1)
  termination_by fuel
  go_m (n m bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m >= bound then true
    else if n == m then go_m n (m + 1) bound (fuel - 1)
    else
      -- P_m applied to e_n should give 0
      let en : Nat → Int := fun x => if x == n then 1 else 0
      let pm_en := spectral_projector m en bound
      -- Check all values are 0
      go_x 0 bound bound pm_en && go_m n (m + 1) bound (fuel - 1)
  termination_by fuel
  go_x (x bound fuel : Nat) (result : Nat → Int) : Bool :=
    if fuel = 0 then true
    else if x >= bound then true
    else (result x == 0) && go_x (x + 1) bound (fuel - 1) result
  termination_by fuel
```
