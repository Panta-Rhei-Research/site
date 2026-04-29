---
{
  "projection_kind": "taulib_declaration",
  "title": "bipolar_channel_independence",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/bipolar-channel-independence/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::bipolar_channel_independence",
  "declaration_slug": "bipolar-channel-independence",
  "kind": "def",
  "name": "bipolar_channel_independence",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 233,
  "source_line_end": 250,
  "registry_ids": [
    "II.P08"
  ],
  "related_registry_items": [
    {
      "id": "II.P08",
      "title": "Projection Formula",
      "url": "/registry/object/II.P08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L233-L250",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L233-L250",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L233-L250)
- Source range: L233-L250
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P08` — Projection Formula

## Immediate Comment / Docstring

```lean
/-- [II.P08] Bipolar channel independence under BndLift.

    The B-component and C-component of the lifted value are independent:
    varying B (exponent) while fixing C (tetration) produces independent
    effects on the lifted value, and vice versa.

    Evidence: for pairs of τ-admissible points that differ ONLY in B
    (or only in C), the lifted ABCD charts show independent variation
    in the corresponding sector.

    We test this by examining how the ABCD decomposition of the lifted
    value responds to B-only and C-only changes in the input. -/
```

## Source Excerpt

```lean
def bipolar_channel_independence (bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else
      let p := from_tau_idx x
      let bp := interior_bipolar p
      -- e₊-projection depends only on B
      let proj_plus := SectorPair.mul e_plus_sector bp
      -- e₋-projection depends only on C
      let proj_minus := SectorPair.mul e_minus_sector bp
      -- Independence: proj_plus has zero C-sector, proj_minus has zero B-sector
      (proj_plus.c_sector == 0) &&
      (proj_minus.b_sector == 0) &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```
