---
{
  "projection_kind": "taulib_declaration",
  "title": "projector_idempotent_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-decomp/projector-idempotent-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.SpectralDecomp`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralDecomp::projector_idempotent_check",
  "declaration_slug": "projector-idempotent-check",
  "kind": "def",
  "name": "projector_idempotent_check",
  "module_name": "TauLib.BookIII.Doors.SpectralDecomp",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-decomp/",
  "source_line_start": 63,
  "source_line_end": 82,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L63-L82",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L63-L82",
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
- Source path: [`TauLib/BookIII/Doors/SpectralDecomp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralDecomp.lean#L63-L82)
- Source range: L63-L82
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D80` — q-Expansion Coefficients

## Immediate Comment / Docstring

```lean
/-- [III.D80] Check projector is idempotent: P_n² = P_n. -/
```

## Source Excerpt

```lean
def projector_idempotent_check (N : Nat) : Bool :=
  go_n 0 N N
where
  go_n (n bound fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if n >= bound then true
    else
      let f : Nat → Int := fun x => if x == n then 1 else 0
      -- P_n(P_n(f)) should equal P_n(f)
      let pf : Nat → Int := spectral_projector n f bound
      go_x n 0 bound bound pf f && go_n (n + 1) bound (fuel - 1)
  termination_by fuel
  go_x (n x bound fuel : Nat) (pf f : Nat → Int) : Bool :=
    if fuel = 0 then true
    else if x >= bound then true
    else
      let ppf := spectral_projector n pf bound x
      let pf_val := spectral_projector n f bound x
      (ppf == pf_val) && go_x n (x + 1) bound (fuel - 1) pf f
  termination_by fuel
```
